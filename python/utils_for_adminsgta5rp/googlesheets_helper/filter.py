import codecs
from datetime import datetime
from datetime import timedelta
from gsheet import *
# def Sorter(date_from, date_to):
def Sorter():
    # Чтение файла
    file_AllLogs = codecs.open("AllLogs.txt", "r", "utf-8")
    all_logs = file_AllLogs.readlines()
    file_AllLogs.close()
    logsFZ = []

    date_from = '22.01.2024'
    date_to = '01.02.2024'
    # date_from = input("Введите дату (ОТ) в формате 11.11.1111: ")
    # date_to = input("Введите дату (ДО) в формате 11.11.1111: ")

    date_from = datetime.strptime(date_from, '%d.%m.%Y')
    date_to = datetime.strptime(date_to, '%d.%m.%Y')
    date_from_text = date_from.strftime('%d.%m')
    date_to_text = date_to.strftime('%d.%m')

    num_days = (date_to - date_from).days + 1

    factions = [["Marabunta Grande", "Marabunta"], ["The Families", "Families"], ["Los Santos Vagos", "Los"], ["Bloods", "Bloods"], ["The Ballas Gang", "Ballas"], 
                ["Русская Мафия", "Русская"], ["Армянская Мафия", "Армянская"], ["Мексиканская Мафия", "Мексиканская"], ["Итальянская Мафия", "Итальянская"], ["Японская Мафия", "Японская"], 
                ["LSPD", ""], ["LSSD", ""], ["FIB", ""], ["LS Army", ""], ["Федеральная тюрьма", ""], ["Мэрия ЛС", ""], ["Medical Services", ""]]

    # Очистка файлов
    for faction in factions:
        fileName = "factions\\" + faction[0] + ".txt"
        fileFaction = codecs.open(fileName, "w", "utf-8")
        fileFaction.close()

    # Сортировка и разделение логов разгрузки ФЗ
    for logFZ in all_logs:
        if "Загрузил" in logFZ:
            stringFZ = logFZ.split("\t")
            stringFZ1 = stringFZ[3].split()
            timeFz = stringFZ[-1][12:14]
            dateFz = stringFZ[-1][0:5]
            for log in all_logs:
                log1 = log.split("\t")
                if "Разгружает" in log:
                    timeNg = log1[-1][12:14]
                    dateNg = log1[-1][0:5]
                    if stringFZ1[1] in log and stringFZ1[-1] in log and (timeFz == timeNg or int(timeFz) == int(timeNg) + 1) and dateNg == dateFz:
                        barak = [logFZ, log]
                        logsFZ.append(barak)
                        all_logs.remove(log)
        else:
            break

    # Класс, на основе которого создаются объекты дней
    class Day:
        def __init__(self, i):
            self.i = i
            self.army_supply = [[0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []]]
            self.ems_supply = [[0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []]]
            # 0 - количество матовозок, 1 - количество материалов/аптек
            self.contr_supply = [[0, 0, 0, []], [0, 0, 0, []], [0, 0, 0, []], [0, 0, 0, []], [0, 0, 0, []], [0, 0, 0, []], [0, 0, 0, []], [0, 0, 0, []], [0, 0, 0, []], [0, 0, 0, []], [0, 0, 0, []], [0, 0, 0, []], [0, 0, 0, []], [0, 0, 0, []], [0, 0, 0, []], [0, 0, 0, []], [0, 0, 0, []]]
            # 0 - количество матовозок, 1 - количество таблеток, 2 - покупка контракта
            self.train = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
            # 0 - победа, 1 - покупка контракта
            self.airdrop = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            self.ammunation = [[0, 0, 0, []], [0, 0, 0, []], [0, 0, 0, []], [0, 0, 0, []], [0, 0, 0, []], [0, 0, 0, []], [0, 0, 0, []], [0, 0, 0, []], [0, 0, 0, []], [0, 0, 0, []], [0, 0, 0, []], [0, 0, 0, []], [0, 0, 0, []], [0, 0, 0, []], [0, 0, 0, []], [0, 0, 0, []], [0, 0, 0, []]]
            # 0 - победа, 1 - количество матов, 2 - покупка контракта
            self.hammers = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            self.flag = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
            self.cargo_escort = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
            # 0 - победа, 1 - поражение, 2 - неявка
            self.fz = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
            # 0 - ЭМИ, 1 - количество матовозок
            self.ft = [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]]
            # 0 - ЭМИ, 1 - количество заключенных
            self.graffiti_war = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        
        def WriteLogs(self, date, i):
            add_text_cell(i+3, 2, f'{self.army_supply[0][0]} ({self.army_supply[0][2]})')
            for num in range(0, 10):
                add_header(num)
                temp = 0
                name = "factions\\" + factions[num][0] + ".txt"
                with codecs.open(name, "a", "utf-8") as fileFaction:
                    fileFaction.write("```ansi\n")
                    fileFaction.write(f"---{date}---" + "\n")
                    fileFaction.write(f"Поставки NG.\tМатовозки армии: {self.army_supply[num][0]}\tКол-во матов: {self.army_supply[num][1]}\n")
                    for strink in self.army_supply[num][2]:
                        temp = 1
                        fileFaction.write('[2;34m' + strink + '[0m')
                    if temp == 1:
                        fileFaction.write('\n')
                    fileFaction.write(f"Поставки EMS.\tКареты аптек: {self.ems_supply[num][0]}\tКол-во аптек: {self.ems_supply[num][1]}\n")
                    for strink in self.ems_supply[num][2]:
                        temp = 2
                        fileFaction.write('[2;34m' + strink + '[0m')
                    if temp == 2:
                        fileFaction.write('\n')
                    fileFaction.write(f"Контрабанда.\tМашины таблеток: {self.contr_supply[num][0]}\tКол-во таблеток: {self.contr_supply[num][1]}\tПокупки контракта: {self.contr_supply[num][2]}\n")
                    for strink in self.contr_supply[num][3]:
                        temp = 3
                        fileFaction.write('[2;34m' + strink + '[0m')
                    if temp == 3:
                        fileFaction.write('\n')
                    fileFaction.write(f"Поезд.\tХуманки: {self.train[num][0]}\tПокупки контракта: {self.train[num][1]}\n")
                    fileFaction.write(f"Аирдропы: {self.airdrop[num]}\n")
                    if num<10:
                        fileFaction.write(f"Ганшоп.\tХуманки: {self.ammunation[num][0]}\tКол-во матов: {self.ammunation[num][1]}\tПокупки контракта: {self.ammunation[num][2]}\n")
                        for strink in self.ammunation[num][3]:
                            temp = 4
                            fileFaction.write('[2;34m' + strink + '[0m')
                        if temp == 4:
                            fileFaction.write('\n')
                        fileFaction.write(f"Хаммеры: {self.hammers[num]}\n")
                        fileFaction.write(f"Захват флага.\tПобеды: {self.flag[num][0]}\tПоражения: {self.flag[num][1]}\tНеявки: {self.flag[num][2]}\n")
                        fileFaction.write(f"Сопровождение.\tПобеды: {self.cargo_escort[num][0]}\tПоражения: {self.cargo_escort[num][1]}\tНеявки: {self.cargo_escort[num][2]}\n")
                        fileFaction.write(f"Нападения ФЗ.\tЭМИ на ФЗ: {self.fz[num][0]}\tБараки: {self.fz[num][1]}\n")
                        fileFaction.write(f"Нападения ФТ.\tЭМИ на ФТ: {self.ft[num][0]}\tСпасение заключенных: {self.ft[num][1]}\n")
                        fileFaction.write(f"Победы GW: {self.graffiti_war[num]}\n\n")
                    else: fileFaction.write("\n")
                    fileFaction.write("```\n")
        
        # def WriteLogs(self, date):
        #     for num in range(0, 17):
        #         name = "factions\\" + factions[num][0] + ".txt"
        #         with codecs.open(name, "a", "utf-8") as fileFaction:
        #             fileFaction.write(f"---{date}---" + "\n")
        #             fileFaction.write(f"Поставки NG.\tМатовозки армии: {self.army_supply[num][0]}\tКол-во матов: {self.army_supply[num][1]}\n")
        #             fileFaction.write(f"Поставки EMS.\tКареты аптек: {self.ems_supply[num][0]}\tКол-во аптек: {self.ems_supply[num][1]}\n")
        #             fileFaction.write(f"Контрабанда.\tМашины таблеток: {self.contr_supply[num][0]}\tКол-во таблеток: {self.contr_supply[num][1]}\tПокупки контракта: {self.contr_supply[num][2]}\n")
        #             fileFaction.write(f"Поезд.\tХуманки: {self.train[num][0]}\tПокупки контракта: {self.train[num][1]}\n")
        #             fileFaction.write(f"Аирдропы: {self.airdrop[num]}\n")
        #             if num<10:
        #                 fileFaction.write(f"Ганшоп.\tХуманки: {self.ammunation[num][0]}\tКол-во матов: {self.ammunation[num][1]}\tПокупки контракта: {self.ammunation[num][2]}\n")
        #                 fileFaction.write(f"Хаммеры: {self.hammers[num]}\n")
        #                 fileFaction.write(f"Захват флага.\tПобеды: {self.flag[num][0]}\tПоражения: {self.flag[num][1]}\tНеявки: {self.flag[num][2]}\n")
        #                 fileFaction.write(f"Сопровождение.\tПобеды: {self.cargo_escort[num][0]}\tПоражения: {self.cargo_escort[num][1]}\tНеявки: {self.cargo_escort[num][2]}\n")
        #                 fileFaction.write(f"Нападения ФЗ.\tЭМИ на ФЗ: {self.fz[num][0]}\tБараки: {self.fz[num][1]}\n")
        #                 fileFaction.write(f"Нападения ФТ.\tЭМИ на ФТ: {self.ft[num][0]}\tСпасение заключенных: {self.ft[num][1]}\n")
        #                 fileFaction.write(f"Победы GW: {self.graffiti_war[num]}\n\n")
        #             else: fileFaction.write("\n")

        def SortLogs(self, log):
            logT = log.split("\t")
            log_action = logT[3].split()
            for num in range(0, 17):
                if logT[2] == factions[num][0]:
                    # Разгрузки
                    if "Разгру" in logT[3]:
                        if log_action[4] == "армейского":
                            self.army_supply[num][0] += 1
                            self.army_supply[num][1] += int(log_action[1])
                            self.army_supply[num][2].append(log[-9:-1])
                        if log_action[2] == "аптек":
                            self.ems_supply[num][0] += 1
                            self.ems_supply[num][1] += int(log_action[1])
                            self.ems_supply[num][2].append(log[-9:-1])
                        if log_action[2] == "таблеток":
                            self.contr_supply[num][0] += 1
                            self.contr_supply[num][1] += int(log_action[1])
                            self.contr_supply[num][3].append(log[-9:-1])
                        if log_action[4] == "Хаммера":
                            self.hammers[num] += 1
                        if log_action[4] == "оружейного":
                            self.ammunation[num][0] += 1
                            self.ammunation[num][1] += int(log_action[1])
                            self.ammunation[num][3].append(log[-9:-1])
                    # Аирдроп
                    if "припасы из выпавшего армейского груза" in logT[3]:
                        self.airdrop[num] += 1
                    # Покупка контрактов
                    if "Покупает контракт \"Ограбление поезда\"" in logT[3]:
                        self.train[num][1] +=1
                    if "Покупает контракт \"Ограбление магазина оружия\"" in logT[3]:
                        self.ammunation[num][2] += 1
                    # Заказ анальгетика
                    if "Заказывает поставку" in logT[3]:
                        self.contr_supply[num][2] +=1
                    # Поезд
                    if "грузовик с украденным" in logT[3]:
                        self.train[num][0] +=1
                    # ФТ
                    if "ЭМИ на тюрьме" in logT[3]:
                        self.ft[num][0] +=1
                    if "сбежать из тюрьмы" in logT[3]:
                        self.ft[num][1] +=1
                    # ФЗ ЭМИ
                    if "ЭМИ на Форте Занкудо" in logT[3]:
                        self.fz[num][0] +=1
                    # Флаг и вагонетка
                    if "в режиме" in logT[3]:
                        if log_action[-6] == "флага":
                            self.flag[num][0] += 1
                            for num1 in range(0, 10):
                                if log_action[4] == factions[num1][1] or log_action[5] == factions[num1][1]:
                                    self.flag[num1][1] +=1
                        if log_action[-1] == "флага.":
                            self.flag[num][2] += 1
                        if log_action[-6] == "Сопровождение":
                            self.cargo_escort[num][0] += 1
                            for num1 in range(0, 10):
                                if log_action[4] == factions[num1][1] or log_action[5] == factions[num1][1]:
                                    self.cargo_escort[num1][1] +=1
                        if log_action[-1] == "Сопровождение.":
                            self.cargo_escort[num][2] += 1
                    # Граффити
                    if "победу в GRAFFITI WAR" in logT[3]:
                        self.graffiti_war[num] += 1
                    # ФЗ бараки отдельно

        def AppendFZ(self, log):
            logT = log.split("\t")
            for num in range(0, 17):
                if logT[2] == factions[num][0]:
                    self.fz[num][1] += 1

    # Список объектов дней
    Days = [Day(i) for i in range(0, num_days)]
    # Объект для суммы всех показателей дней
    All_days = Day(100)

    for i in range(0, num_days):
        date = date_from + timedelta(days= i)
        date_text = date.strftime('%d.%m')
        for logFZ in logsFZ:
            if date_text in logFZ[1]:
                Days[i].AppendFZ(logFZ[1])
        for log in all_logs:
            if date_text in log:
                Days[i].SortLogs(log)
        Days[i].WriteLogs(date_text, i)

    for i in range(0, num_days):
        for num in range(0, 17):
            All_days.army_supply[num][0] += Days[i].army_supply[num][0]
            All_days.army_supply[num][1] += Days[i].army_supply[num][1]
            All_days.ems_supply[num][0] += Days[i].ems_supply[num][0]
            All_days.ems_supply[num][1] += Days[i].ems_supply[num][1]
            All_days.contr_supply[num][0] += Days[i].contr_supply[num][0]
            All_days.contr_supply[num][1] += Days[i].contr_supply[num][1]
            All_days.contr_supply[num][2] += Days[i].contr_supply[num][2]
            All_days.train[num][0] += Days[i].train[num][0]
            All_days.train[num][1] += Days[i].train[num][1]
            All_days.airdrop[num] += Days[i].airdrop[num]
            All_days.ammunation[num][0] += Days[i].ammunation[num][0]
            All_days.ammunation[num][1] += Days[i].ammunation[num][1]
            All_days.ammunation[num][2] += Days[i].ammunation[num][2]
            All_days.hammers[num] += Days[i].hammers[num]
            All_days.flag[num][0] += Days[i].flag[num][0]
            All_days.flag[num][1] += Days[i].flag[num][1]
            All_days.flag[num][2] += Days[i].flag[num][2]
            All_days.cargo_escort[num][0] += Days[i].cargo_escort[num][0]
            All_days.cargo_escort[num][1] += Days[i].cargo_escort[num][1]
            All_days.cargo_escort[num][2] += Days[i].cargo_escort[num][2]
            All_days.fz[num][0] += Days[i].fz[num][0]
            All_days.fz[num][1] += Days[i].fz[num][1]
            All_days.ft[num][0] += Days[i].ft[num][0]
            All_days.ft[num][1] += Days[i].ft[num][1]
            All_days.graffiti_war[num] += Days[i].graffiti_war[num]
    All_days.WriteLogs("Весь период", i)

    materials_gos = 0
    materials_crime = 0
    apt_gos = 0
    apt_crime = 0
    contr_gos = 0
    contr_crime = 0
    for i in range(0, 10):
        materials_crime += All_days.army_supply[i][1]
        apt_crime += All_days.ems_supply[i][1]
        contr_crime += All_days.contr_supply[i][1]
    for n in range(10, 17):
        materials_gos += All_days.army_supply[n][1]
        apt_gos += All_days.ems_supply[n][1]
        contr_gos += All_days.contr_supply[n][1]

    with codecs.open("factions\\-Statistic.txt", "w", "utf-8") as file_stat:
        file_stat.write(f"--- {date_from_text}-{date_to_text} ---\n")
        file_stat.write(f"Всего материалов гос - {materials_gos}\n")
        file_stat.write(f"Все аптечек гос - {apt_gos}\n")
        file_stat.write(f"Всего контрабанды гос - {contr_gos}\n")
        file_stat.write(f"Всего материалов крайм - {materials_crime}\n")
        file_stat.write(f"Все аптечек крайм - {apt_crime}\n")
        file_stat.write(f"Всего контрабанды крайм - {contr_crime}\n")

    print("Завершение работы программы.")

Sorter()