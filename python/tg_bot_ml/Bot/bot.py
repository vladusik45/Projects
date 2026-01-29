
import json
import random
import re
import sqlite3
from datetime import datetime, timedelta
from pathlib import Path
import pickle
import nltk
from sklearn.svm import LinearSVC
from sklearn.feature_extraction.text import TfidfVectorizer
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    ConversationHandler, ContextTypes, filters
)

# -----------------------
# Конфигурация
# -----------------------
with open("token.txt", "r") as file:
    TELEGRAM_TOKEN = file.read().strip()
MODEL_DIR = Path("model")
INTENTS_FILE = "intents.json"
DIALOGUES_FILE = "dialogues.txt"
TICKETS_FILE = "tickets.json"
DB_FILE = "bookings.db"

CHOOSING_ROUTE, CHOOSING_DATE, CHOOSING_CLASS, CONFIRM_BOOK = range(4)

# -----------------------
# Утилиты
# -----------------------
def clear_phrase(phrase: str) -> str:
    phrase = phrase.lower()
    phrase = re.sub(r'[^а-яё0-9\s\-]', ' ', phrase)
    phrase = re.sub(r'\s+', ' ', phrase)
    return phrase.strip()


# -----------------------
# Загрузка данных
# -----------------------
with open(INTENTS_FILE, encoding="utf-8") as f:
    INTENTS = json.load(f)

if Path(DIALOGUES_FILE).exists():
    with open(DIALOGUES_FILE, encoding="utf-8") as f:
        DIALOGUES_SRC = f.read().split("\n\n")
else:
    DIALOGUES_SRC = []

with open(TICKETS_FILE, encoding="utf-8") as f:
    TICKETS = json.load(f)

# -----------------------
# ML-модель для NLU
# -----------------------
MODEL_DIR.mkdir(exist_ok=True)
VEC_FILE = MODEL_DIR / "vectorizer.pkl"
CLF_FILE = MODEL_DIR / "clf.pkl"

def train_or_load_nlu():
    X_text, y = [], []
    for intent, data in INTENTS["intents"].items():
        for ex in data.get("examples", []):
            X_text.append(clear_phrase(ex))
            y.append(intent)
    vectorizer = TfidfVectorizer(analyzer="char", ngram_range=(3, 3))
    X = vectorizer.fit_transform(X_text)
    clf = LinearSVC()
    clf.fit(X, y)
    with open(VEC_FILE, "wb") as f:
        pickle.dump(vectorizer, f)
    with open(CLF_FILE, "wb") as f:
        pickle.dump(clf, f)
    return vectorizer, clf

def load_nlu():
    if VEC_FILE.exists() and CLF_FILE.exists():
        with open(VEC_FILE, "rb") as f:
            vec = pickle.load(f)
        with open(CLF_FILE, "rb") as f:
            clf = pickle.load(f)
    else:
        vec, clf = train_or_load_nlu()
    return vec, clf

def predict_intent(text, vectorizer, clf):
    if not text.strip():
        return None
    try:
        X = vectorizer.transform([text])
        intent = clf.predict(X)[0]
        return intent
    except Exception as e:
        print(f"Ошибка при классификации: {e}")
        return None

vectorizer, clf = load_nlu()

def classify_intent(text: str):
    text_c = clear_phrase(text)
    if not text_c:
        return None
    try:
        intent = clf.predict(vectorizer.transform([text_c]))[0]
        return intent
    except Exception:
        return None


# -----------------------
# Поиск ответа в dialogues.txt
# -----------------------
def search_dialogue_answer(replica: str):
    r = clear_phrase(replica)
    best = None
    best_score = 1.0
    for block in DIALOGUES_SRC:
        lines = block.splitlines()
        if not lines:
            continue
        q = clear_phrase(lines[0])
        if not q:
            continue
        dist = nltk.edit_distance(r, q) / max(1, len(q))
        if dist < best_score:
            best_score = dist
            best = lines[1] if len(lines) > 1 else None
    if best and best_score < 0.25:
        return best
    return None


# -----------------------
# База данных
# -----------------------
def init_db():
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS bookings(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            user_name TEXT,
            route_id TEXT,
            route_desc TEXT,
            travel_date TEXT,
            cls TEXT,
            price REAL,
            created_at TEXT
        )
    """)
    conn.commit()
    conn.close()

def save_booking(user_id, user_name, route_id, route_desc, travel_date, cls, price):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO bookings(user_id, user_name, route_id, route_desc, travel_date, cls, price, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (user_id, user_name, route_id, route_desc, travel_date, cls, price, datetime.utcnow().isoformat()))
    conn.commit()
    conn.close()


# -----------------------
# Вспомогательные функции
# -----------------------
def list_routes_text():
    lines = []
    for r in TICKETS:
        lines.append(f"{r['id']}: {r['from']} → {r['to']} | {r['depart_time']} | классы: {', '.join(r['classes'].keys())}")
    return "\n".join(lines)

def find_route_by_id(rid):
    for r in TICKETS:
        if str(r["id"]) == str(rid):
            return r
    return None


# -----------------------
# Обработчики команд
# -----------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "Привет! Я бот для поиска и бронирования ЖД билетов.\n"
        "Скажите, что вы хотите: посмотреть рейсы, найти по направлению или забронировать билет.\n"
        "Команды: /routes /mybookings /help"
    )
    kb = [["Показать рейсы", "Поиск по направлению"], ["Забронировать билет", "Спецпредложения"]]
    await update.message.reply_text(text, reply_markup=ReplyKeyboardMarkup(kb, one_time_keyboard=True))

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Используйте /routes чтобы увидеть список рейсов. Напишите 'забронировать' чтобы начать бронирование.")

async def routes_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Доступные рейсы:\n\n" + list_routes_text())

async def mybookings_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute("SELECT id, route_desc, travel_date, cls, price, created_at FROM bookings WHERE user_id=?", (update.message.from_user.id,))
    rows = cur.fetchall()
    conn.close()
    if not rows:
        await update.message.reply_text("У вас пока нет бронирований.")
    else:
        txt = "Ваши брони:\n"
        for r in rows:
            txt += f"#{r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} ₽ | {r[5]}\n"
        await update.message.reply_text(txt)


# -----------------------
# Сценарий бронирования
# -----------------------
async def booking_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text.strip().lower()

    # Если пользователь прямо указал номер рейса (например "2", "рейс 3", "хочу третий")
    m_digit = re.search(r"\b(\d{1,3})\b", user_text)
    if m_digit:
        rid = m_digit.group(1)
        r = find_route_by_id(rid)
        if r:
            # сразу переходим к выбору даты
            context.user_data["route"] = r
            await update.message.reply_text(
                f"Вы выбрали: {r['from']} → {r['to']} | {r['depart_time']}\n"
                "Введите дату поездки в формате YYYY-MM-DD (например 2025-10-20)."
            )
            return CHOOSING_DATE

    # поддержка порядковых слов: "первый/второй/третий"
    ord_map = {"перв": "1", "втор": "2", "трет": "3", "четв": "4", "пят": "5"}
    for k, v in ord_map.items():
        if k in user_text:
            r = find_route_by_id(v)
            if r:
                context.user_data["route"] = r
                await update.message.reply_text(
                    f"Вы выбрали: {r['from']} → {r['to']} | {r['depart_time']}\n"
                    "Введите дату поездки в формате YYYY-MM-DD (например 2025-10-20)."
                )
                return CHOOSING_DATE

    # Попытка извлечь город 
    known_cities = {r["from"].lower() for r in TICKETS} | {r["to"].lower() for r in TICKETS}
    # ищем слова в тексте и сопоставляем с известными городами
    words = re.findall(r"[а-яёА-ЯЁ\-]+", user_text)
    found_city = None
    for w in words:
        for city in known_cities:
            # частичное совпадение
            if city in w or w.startswith(city[:4]):
                found_city = city
                break
        if found_city:
            break

    # если найден город из расписания — показываем только подходящие рейсы
    if found_city:
        matching_routes = [
            r for r in TICKETS
            if found_city in r["from"].lower() or found_city in r["to"].lower()
        ]
        if matching_routes:
            routes_text = "\n".join([
                f"{r['id']}: {r['from']} → {r['to']} | {r['depart_time']} | классы: {', '.join(r['classes'].keys())}"
                for r in matching_routes
            ])
            await update.message.reply_text(
                f"Нашлись рейсы, связанные с «{found_city.capitalize()}»:\n\n{routes_text}\n\n"
                "Введите номер рейса, который хотите выбрать."
            )
            context.user_data["matching_routes"] = matching_routes
            context.user_data["found_city"] = found_city
            return CHOOSING_ROUTE

        else:
            # найден город, но для него нет рейсов
            await update.message.reply_text(
                f"К сожалению, рейсов в направлении «{found_city.capitalize()}» пока нет.\n"
                "Хотите посмотреть список доступных маршрутов?"
            )
            return ConversationHandler.END

    # Если текст короткий и явно команда билет/забронировать/хочу билет — показываем весь список и переходим в CHOOSING_ROUTE
    simple_booking_triggers = ["билет", "хочу билет", "забронировать", "хочу забронировать", "купить билет", "хочу билет", "бронировать"]
    if any(trigger in user_text for trigger in simple_booking_triggers) or user_text.strip() in ("билет", "бронировать", "забронировать"):
        # показываем весь каталог и переходим в выбор
        await update.message.reply_text("Выберите рейс из списка:\n\n" + list_routes_text())
        return CHOOSING_ROUTE

    # Если ничего не распознано — пусть NLU/общий обработчик решит
    await update.message.reply_text(
        "Понял, давайте начнём. Напишите 'хочу билет' или укажите город/номер рейса (например, 'в Москву' или '2')."
    )
    return ConversationHandler.END


async def choosing_route(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text.strip().lower()

    # Фразы для выхода из сценария
    cancel_phrases = [
        "нет", "отмена", "отменить", "не хочу", 
        "у меня другой вопрос", "другой вопрос",
        "вернуться", "покажи меню", "назад"
    ]
    if any(p in user_text for p in cancel_phrases):
        await update.message.reply_text(
            "Хорошо, вы можете задать другой вопрос или посмотреть поезда позже.",
            reply_markup=ReplyKeyboardRemove()
        )
        return ConversationHandler.END 

    # Проверяем id (число)
    if user_text.isdigit():
        r = find_route_by_id(user_text)
        if r:
            context.user_data["route"] = r
            await update.message.reply_text(
                f"Вы выбрали: {r['from']} → {r['to']} | {r['depart_time']}\n"
                "Введите дату поездки в формате YYYY-MM-DD (например 2025-10-20)."
            )
            return CHOOSING_DATE
        else:
            await update.message.reply_text("Такого рейса нет. Введите id поезда из списка.")
            return CHOOSING_ROUTE

    # Проверяем совпадение по названию маршрута
    matched = None
    for route in TICKETS:
        route_text = f"{route['from']} {route['to']}".lower()
        if route['from'].lower() in user_text or route['to'].lower() in user_text or user_text in route_text:
            matched = route
            break

    if matched:
        context.user_data["route"] = matched
        await update.message.reply_text(
            f"Вы выбрали: {matched['from']} → {matched['to']} | {matched['depart_time']}\n"
            "Введите дату поездки в формате YYYY-MM-DD (например 2025-10-20)."
        )
        return CHOOSING_DATE

    # Проверяем “первый / второй / третий”
    mapping = {"перв": "1", "втор": "2", "трет": "3"}
    for key, val in mapping.items():
        if key in user_text:
            r = find_route_by_id(val)
            if r:
                context.user_data["route"] = r
                await update.message.reply_text(
                    f"Вы выбрали: {r['from']} → {r['to']} | {r['depart_time']}\n"
                    "Введите дату поездки в формате YYYY-MM-DD (например 2025-10-20)."
                )
                return CHOOSING_DATE

    # Если ничего не подошло
    await update.message.reply_text(
        "Не могу определить, какой рейс вы имели в виду. "
        "Введите id (например 1) или название города (например «в Сочи»). "
        "Если хотите выйти, напишите «отмена» или «у меня другой вопрос»."
    )
    return CHOOSING_ROUTE

async def choosing_date(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text.strip().lower()

    # Фразы для выхода из сценария
    cancel_phrases = [
        "нет", "отмена", "отменить", "не хочу",
        "у меня другой вопрос", "другой вопрос",
        "вернуться", "покажи меню", "назад"
    ]
    if any(p in user_text for p in cancel_phrases):
        await update.message.reply_text(
            "Хорошо, бронирование отменено. Вы можете задать другой вопрос или начать заново.",
            reply_markup=ReplyKeyboardRemove()
        )
        return ConversationHandler.END

    # Обработка естественных дат
    today = datetime.today()
    date = None

    if "завтра" in user_text:
        date = today + timedelta(days=1)
    elif "послезавтра" in user_text:
        date = today + timedelta(days=2)
    elif "через" in user_text:
        match = re.search(r"через\s+(\d+)\s*(дн|дня|день|недел)", user_text)
        if match:
            num = int(match.group(1))
            if "недел" in match.group(2):
                date = today + timedelta(days=num * 7)
            else:
                date = today + timedelta(days=num)

    # Если пользователь ввёл дату вручную
    if date is None:
        try:
            date = datetime.strptime(user_text, "%Y-%m-%d")
        except ValueError:
            await update.message.reply_text(
                "Не удалось определить дату. Введите в формате YYYY-MM-DD "
                "или попробуйте сказать, например, «завтра» или «через 3 дня». "
                "Для выхода напишите «отмена»."
            )
            return CHOOSING_DATE

    # Сохраняем дату и переходим к выбору класса
    context.user_data["date"] = date.strftime("%Y-%m-%d")
    classes = list(context.user_data["route"]["classes"].keys())
    kb = [[c] for c in classes]
    await update.message.reply_text(
        f"Поездка запланирована на {context.user_data['date']}.\nВыберите класс:",
        reply_markup=ReplyKeyboardMarkup(kb, one_time_keyboard=True)
    )
    return CHOOSING_CLASS

async def choosing_class(update: Update, context: ContextTypes.DEFAULT_TYPE):
    cls = update.message.text.strip()
    r = context.user_data["route"]
    if cls not in r["classes"]:
        await update.message.reply_text("Неверный класс. Выберите один из предложенных.")
        return CHOOSING_CLASS
    context.user_data["class"] = cls
    price = r["classes"][cls]
    context.user_data["price"] = price
    await update.message.reply_text(f"Итого: {price} ₽. Подтвердите бронирование (Да/Нет).", reply_markup=ReplyKeyboardMarkup([["Да", "Нет"]], one_time_keyboard=True))
    return CONFIRM_BOOK

async def confirm_book(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ans = update.message.text.strip().lower()
    if ans not in ("да", "yes", "y"):
        await update.message.reply_text("Бронирование отменено.", reply_markup=ReplyKeyboardRemove())
        return ConversationHandler.END
    r = context.user_data["route"]
    save_booking(update.message.from_user.id, update.message.from_user.full_name,
                 r["id"], f"{r['from']}→{r['to']} {r['depart_time']}",
                 context.user_data["date"], context.user_data["class"], context.user_data["price"])
    await update.message.reply_text("Бронирование успешно сохранено! Спасибо.", reply_markup=ReplyKeyboardRemove())
    return ConversationHandler.END


# -----------------------
# Обработка обычных сообщений
# -----------------------
async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text.strip().lower()

    # Приветствие
    greetings = ["привет", "здравствуй", "здравствуйте", "добрый день", "добрый вечер", "ку", "хай", "hello", "hi"]
    if any(g in user_text for g in greetings):
        await update.message.reply_text("Здравствуйте! Я помогу подобрать железнодорожный билет. Куда хотите поехать?")
        return

    # Проверяем, упомянут ли известный город
    known_cities = {r["from"].lower() for r in TICKETS} | {r["to"].lower() for r in TICKETS}
    found_city = None

    # Извлекаем возможные слова (в т.ч. из фраз "в крым", "поезд до москвы")
    words = re.findall(r"[а-яёА-ЯЁ]+", user_text)
    for w in words:
        for city in known_cities:
            if city in w or w.startswith(city[:4]):
                found_city = city
                break
        if found_city:
            break

    # Если нашли город из списка маршрутов
    if found_city:
        matching_routes = [
            r for r in TICKETS
            if found_city in r["from"].lower() or found_city in r["to"].lower()
        ]

        if matching_routes:
            routes_text = "\n".join([
                f"{r['id']}: {r['from']} → {r['to']} | {r['depart_time']} | классы: {', '.join(r['classes'].keys())}"
                for r in matching_routes
            ])

            await update.message.reply_text(
                f"Нашлись рейсы, связанные с «{found_city.capitalize()}»:\n\n{routes_text}\n\n"
                "Введите номер рейса, который хотите выбрать."
            )

            context.user_data["matching_routes"] = matching_routes
            context.user_data["found_city"] = found_city

            return CHOOSING_ROUTE



    # Проверяем неизвестные города после предлогов
    match = re.search(r"(в|до|из)\s+([а-яёА-ЯЁ\-]+)", user_text)
    if match:
        guessed_city = match.group(2).capitalize()
        await update.message.reply_text(
            f"К сожалению, рейсов в направлении «{guessed_city}» пока нет.\n"
            "Хотите посмотреть список доступных маршрутов?"
        )
        return

    # Обработка интентов через NLU
    intent = predict_intent(user_text, vectorizer, clf)

    if intent:
        if intent == "ask_routes":
            await update.message.reply_text(
                "Доступные рейсы:\n\n" + list_routes_text()
            )
            return

        resp = random.choice(INTENTS["intents"][intent].get("responses", []))
        # Убираем лишние приветствия
        resp = resp.replace("Здравствуйте! ", "").replace("Привет! ", "").strip()
        await update.message.reply_text(resp)
        return

    # Если ничего не поняли
    await update.message.reply_text(
        "Извини, я не понял запрос. Попробуй написать, например, 'показать рейсы' или 'хочу в Москву'."
    )

# -----------------------
# Запуск
# -----------------------
def main():
    nltk.download("punkt", quiet=True)
    init_db()

    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    conv = ConversationHandler(
        entry_points=[MessageHandler(filters.Regex("(?i)забронировать|билет|купить"), booking_start)],
        states={
            CHOOSING_ROUTE: [MessageHandler(filters.TEXT & ~filters.COMMAND, choosing_route)],
            CHOOSING_DATE: [MessageHandler(filters.TEXT & ~filters.COMMAND, choosing_date)],
            CHOOSING_CLASS: [MessageHandler(filters.TEXT & ~filters.COMMAND, choosing_class)],
            CONFIRM_BOOK: [MessageHandler(filters.Regex("(?i)да|нет"), confirm_book)],
        },
        fallbacks=[],
    )

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("routes", routes_cmd))
    app.add_handler(CommandHandler("mybookings", mybookings_cmd))
    app.add_handler(conv)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

    print("Bot started...")
    app.run_polling()

if __name__ == "__main__":
    main()
