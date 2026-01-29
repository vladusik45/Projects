import codecs
from datetime import datetime
from datetime import timedelta
from gsheet import append_faction_logs
from gsheet import append_empty_row
from parser1 import parser

date_from = input("Введите дату (ОТ) в формате 11.11.1111: ")
date_to = input("Введите дату (ДО) в формате 11.11.1111: ")

# parser('null', 'AllLogs', 'из армейского склада ', True, date_from_text=date_from, date_to_text=date_to, enter_exit = False)
# parser('null', 'AllLogs', 'Применил ', False, date_from_text=date_from, date_to_text=date_to)
# parser('null', 'AllLogs', 'сбежать из тюрьмы', False, date_from_text=date_from, date_to_text=date_to)
# parser('null', 'AllLogs', 'разгру', False, date_from_text=date_from, date_to_text=date_to)
# parser('null', 'AllLogs', 'припасы из выпавшего армейского груза', False, date_from_text=date_from, date_to_text=date_to)
# parser('null', 'AllLogs', 'в режиме', False, date_from_text=date_from, date_to_text=date_to)
# parser('null', 'AllLogs', 'анальгетиков', False, date_from_text=date_from, date_to_text=date_to)
# parser('null', 'AllLogs', 'покупает контракт', False, date_from_text=date_from, date_to_text=date_to)
# parser('null', 'AllLogs', 'победу в GRAFFITI WAR', False, date_from_text=date_from, date_to_text=date_to)
# parser('null', 'AllLogs', 'из поезда грузом', False, date_from_text=date_from, date_to_text=date_to, enter_exit = True)

def Sorter(date_from, date_to):
# def Sorter():
    # Чтение файла
    file_AllLogs = codecs.open("AllLogs.txt", "r", "utf-8")
    all_logs = file_AllLogs.readlines()
    file_AllLogs.close()
    logsFZ = []
    file_capts = codecs.open("win_capt.txt", "r", "utf-8")
    capt = file_capts.read().splitlines()

    date_from = datetime.strptime(date_from, '%d.%m.%Y')
    date_to = datetime.strptime(date_to, '%d.%m.%Y')
    date_from_text = date_from.strftime('%d.%m')
    date_to_text = date_to.strftime('%d.%m')

    num_days = (date_to - date_from).days + 1

    factions = [["Marabunta Grande", "Marabunta"], ["The Families", "Families"], ["Los Santos Vagos", "Los"], ["Bloods", "Bloods"], ["The Ballas Gang", "Ballas"], 
                ["Русская Мафия", "Русская"], ["Армянская Мафия", "Армянская"], ["Мексиканская Мафия", "Мексиканская"], ["Итальянская Мафия", "Итальянская"], ["Японская Мафия", "Японская"], 
                ["LSPD", "LSPD"], ["LSSD", "LSSD"], ["FIB", "FIB"], ["LS Army", "Army"], ["Федеральная тюрьма", "тюрьма"], ["Мэрия ЛС", "Мэрия"], ["Medical Services", "Medical"]]

    # Очистка файлов
    for faction in factions:
        fileName = "factions\\" + faction[0] + ".txt"
        fileFaction = codecs.open(fileName, "w", "utf-8")
        fileFaction.close()

    # Сортировка и разделение логов разгрузки ФЗ
    for logFZ in all_logs:
        if '\n' == logFZ or 'Ничего не найдено\n' == logFZ:
            continue
        else:
            if "Загрузил" in logFZ:
                stringFZ = logFZ.split("Загрузил")[1].split()[:-2]
                timeFz = logFZ.split()[-1][:2]
                dateFz = logFZ.split()[-2][:2]
                for log in all_logs:
                    if "Разгружает" in log:
                        log1 = log.split('Разгру')[1]
                        timeNg = log1.split()[-1][:2]
                        dateNg = log1.split()[-2][:2]
                        if stringFZ[0] in log and stringFZ[-1] in log and (timeFz == timeNg or int(timeFz) == int(timeNg) + 1) and dateNg == dateFz:
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
            self.train = [[0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []]]
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
            self.capt_biz = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        
        def WriteLogs(self, date):
            for num in range(0, 17):
                temp = 0
                name = "factions\\" + factions[num][0] + ".txt"
                with codecs.open(name, "a", "utf-8") as fileFaction:
                    fileFaction.write(f"---{date}---" + "\n")
                    fileFaction.write(f"Поставки NG.\tМатовозки армии: {self.army_supply[num][0]}\tКол-во матов: {self.army_supply[num][1]}\n")
                    for strink in self.army_supply[num][2]:
                        temp = 1
                        fileFaction.write(strink + '\n')
                    if temp == 1:
                        fileFaction.write('\n')
                    fileFaction.write(f"Поставки EMS.\tКареты аптек: {self.ems_supply[num][0]}\tКол-во аптек: {self.ems_supply[num][1]}\n")
                    for strink in self.ems_supply[num][2]:
                        temp = 2
                        fileFaction.write(strink + '\n')
                    if temp == 2:
                        fileFaction.write('\n')
                    fileFaction.write(f"Контрабанда.\tМашины таблеток: {self.contr_supply[num][0]}\tКол-во таблеток: {self.contr_supply[num][1]}\tПокупки контракта: {self.contr_supply[num][2]}\n")
                    for strink in self.contr_supply[num][3]:
                        temp = 3
                        fileFaction.write(strink + '\n')
                    if temp == 3:
                        fileFaction.write('\n')
                    fileFaction.write(f"Поезд.\tХуманки: {self.train[num][0]}\tПокупки контракта: {self.train[num][1]}\n")
                    fileFaction.write(f"Аирдропы: {self.airdrop[num]}\n")
                    if num<10:
                        fileFaction.write(f"Ганшоп.\tХуманки: {self.ammunation[num][0]}\tКол-во матов: {self.ammunation[num][1]}\tПокупки контракта: {self.ammunation[num][2]}\n")
                        for strink in self.ammunation[num][3]:
                            temp = 4
                            fileFaction.write(strink + '\n')
                        if temp == 4:
                            fileFaction.write('\n')
                        fileFaction.write(f"Хаммеры: {self.hammers[num]}\n")
                        fileFaction.write(f"Захват флага.\tПобеды: {self.flag[num][0]}\tПоражения: {self.flag[num][1]}\tНеявки: {self.flag[num][2]}\n")
                        fileFaction.write(f"Сопровождение.\tПобеды: {self.cargo_escort[num][0]}\tПоражения: {self.cargo_escort[num][1]}\tНеявки: {self.cargo_escort[num][2]}\n")
                        fileFaction.write(f"Нападения ФЗ.\tЭМИ на ФЗ: {self.fz[num][0]}\tБараки: {self.fz[num][1]}\n")
                        fileFaction.write(f"Нападения ФТ.\tЭМИ на ФТ: {self.ft[num][0]}\tСпасение заключенных: {self.ft[num][1]}\n")
                        fileFaction.write(f"Победы GW: {self.graffiti_war[num]}\n\n")
                    else: fileFaction.write("\n")
        
        def SortCaptures(self, date, log):
            if len(log) != 10:
                log_split = log.split('_')
                if date == log_split[0]:
                    for num in range(0, 10):
                        if log_split[2] == factions[num][0]:
                            self.capt_biz[num] +=1
                            print(date + ' ' + log + ' ' + str(self.capt_biz[num]))

        def append_log(self, list_table, date, faction):
            army_supplys = ''
            ems_supplys = ''
            ammunations = ''
            trains = ''
            if len(self.army_supply[faction][2]) != 0:
                for s in self.army_supply[faction][2]:
                    army_supplys += s + '\n'
            if len(self.ems_supply[faction][2]) != 0:
                for s in self.ems_supply[faction][2]:
                    ems_supplys += s + '\n'
            if len(self.ammunation[faction][3]) != 0:
                for s in self.ammunation[faction][3]:
                    ammunations += s + '\n'
            if len(self.train[faction][2]) !=0:
                for s in self.train[faction][2]:
                    trains += s
            append_faction_logs(list_table, date, self.army_supply[faction][0], army_supplys, self.ems_supply[faction][0], ems_supplys, 
                                self.fz[faction][0], self.fz[faction][1], self.ft[faction][0], self.ft[faction][1], self.ammunation[faction][0], self.ammunation[faction][2], 
                                ammunations, self.graffiti_war[faction], self.train[faction][0], self.train[faction][1], trains, self.hammers[faction], self.capt_biz[faction], 
                                f'{self.flag[faction][0]}\t| {self.flag[faction][1]}\t| {self.flag[faction][2]}', 
                                f'{self.cargo_escort[faction][0]} | {self.cargo_escort[faction][1]} | {self.cargo_escort[faction][2]}', self.airdrop[faction])


        def SortLogs(self, log):
            logT = log.split()
            for num in range(0, 17):
                if logT[2] == factions[num][1] or logT[3] == factions[num][1]:
                    # Разгрузки
                    if "Разгру" in log:
                        log_action = log.split('Разгру')[1]
                        if "армейского" in log_action:
                            self.army_supply[num][0] += 1
                            self.army_supply[num][1] += int(log_action.split()[1])
                            self.army_supply[num][2].append(log_action.split()[1] + ' матов ' + log_action.split()[-2] + ' ' + log_action.split()[-1])
                        if "аптек" in log_action:
                            self.ems_supply[num][0] += 1
                            self.ems_supply[num][1] += int(log_action.split()[1])
                            self.ems_supply[num][2].append(log_action.split()[1] + ' аптек ' + log_action.split()[-2] + ' ' + log_action.split()[-1])
                        if "таблеток" in log_action:
                            self.contr_supply[num][0] += 1
                            self.contr_supply[num][1] += int(log_action.split()[1])
                            self.contr_supply[num][3].append(log_action.split()[1] + ' таблеток ' + log_action.split()[-2] + ' ' + log_action.split()[-1])
                        if "Хаммера" in log_action:
                            self.hammers[num] += 1
                        if "оружейного" in log_action:
                            self.ammunation[num][0] += 1
                            self.ammunation[num][1] += int(log_action.split()[1])
                            self.ammunation[num][3].append(log_action.split()[1] + ' матов ' + log_action.split()[-2] + ' ' + log_action.split()[-1])
                    # Аирдроп
                    if "припасы из выпавшего армейского груза" in log:
                        self.airdrop[num] += 1
                    # Покупка контрактов
                    if "Покупает контракт \"Ограбление поезда\"" in log:
                        self.train[num][1] +=1
                    if "Покупает контракт \"Ограбление магазина оружия\"" in log:
                        self.ammunation[num][2] += 1
                    # Заказ анальгетика
                    if "Заказывает поставку" in log and 'анальгетиков' in log:
                        self.contr_supply[num][2] +=1
                    # Поезд
                    if "грузовик с украденным" in log:
                        self.train[num][0] +=1
                        temp = log.split('грузом ')[1]
                        self.train[num][2].append(temp)
                        print(temp)
                    # ФТ
                    if "ЭМИ на тюрьме" in log:
                        self.ft[num][0] +=1
                    if "сбежать из тюрьмы" in log:
                        self.ft[num][1] +=1
                    # ФЗ ЭМИ
                    if "ЭМИ на Форте Занкудо" in log:
                        self.fz[num][0] +=1
                    # Флаг и вагонетка
                    if "в режиме" in log and ('лаг' in log or 'опровождение' in log):
                        log_action = log.split('.')[0].split()[2:]
                        if log_action[-6] == "флага":
                            self.flag[num][0] += 1
                            for num1 in range(0, 10):
                                if log_action[-10] == factions[num1][1] or log_action[-11] == factions[num1][1]:
                                    self.flag[num1][1] +=1
                        if log_action[-1] == "флага":
                            self.flag[num][2] += 1
                        if log_action[-6] == "Сопровождение":
                            self.cargo_escort[num][0] += 1
                            for num1 in range(0, 10):
                                if log_action[-10] == factions[num1][1] or log_action[-11] == factions[num1][1]:
                                    self.cargo_escort[num1][1] +=1
                        if log_action[-1] == "Сопровождение":
                            self.cargo_escort[num][2] += 1
                    # Граффити
                    if "победу в GRAFFITI WAR" in log:
                        self.graffiti_war[num] += 1
                    # ФЗ бараки отдельно

        def AppendFZ(self, log):
            logT = log.split(" Разгру")[0].split()[1:]
            for num in range(0, 17):
                if logT[1] == factions[num][1]:
                    self.fz[num][1] += 1
                    break
                if len(logT) > 2:
                    if logT[2] == factions[num][1]:
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
        for log in capt:
            Days[i].SortCaptures(date_text, log)
        Days[i].WriteLogs(date_text)

    for i in range(0, num_days):
        date = date_from + timedelta(days= i)
        date_text = date.strftime('%d.%m')
        for num in range(0, 5):
            if factions[num][0] == 'Marabunta Grande': faction_name = 'MG'
            if factions[num][0] == 'The Families': faction_name = 'FAM'
            if factions[num][0] == 'Los Santos Vagos': faction_name = 'LSV'
            if factions[num][0] == 'Bloods': faction_name = 'BSG'
            if factions[num][0] == 'The Ballas Gang': faction_name = 'ESB'
            Days[i].append_log(list_table=faction_name, date=date_text, faction=num)

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
    All_days.WriteLogs("Весь период")

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

    append_empty_row('MG')
    append_empty_row('BSG')
    append_empty_row('ESB')
    append_empty_row('LSV')
    append_empty_row('FAM')
    print("Завершение работы программы.")

Sorter(date_from, date_to)

a = 1
# Sorter()