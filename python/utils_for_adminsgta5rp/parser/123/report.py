from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from datetime import *
import math
import random
import codecs
import numpy as np

chrome_options = Options()
chrome_options.add_argument("--user-data-dir=C:\\Users\\vlada\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 2")
# chrome_options.add_argument("headless")
driver = webdriver.Chrome(options=chrome_options)



today = datetime.now()
yesterday = today - timedelta(days=1)
day_before_yesterday = yesterday - timedelta(days=2)
date = yesterday.strftime('%d %m %Y')
day_week = yesterday.isoweekday()


months = [0, "Янв", "Фев", "Мар", "Апр", "Май", "Июн", "Июл", "Авг", "Сен", "Окт", "Ноя", "Дек"]
for i in range(1, 13):
    dateS = date.split()
    a = int(dateS[1])
    if a == i:
        for k in range(1, 10):
            if dateS[0] == '0'+ str(k): dateS[0] = str(k)
        date = dateS[0] + " " + months[i] + " " + dateS[2]
        break

day = []

for i in range(1, 40):
    driver.get(f'https://forum.gta5rp.com/forums/zhaloby-na-igrokov.1515/page-{i}')
    day_report = driver.find_elements(By.CLASS_NAME, value = 'structItem-cell--main')
    for i in range(0, len(day_report)):
        day.append(day_report[i].get_attribute('outerHTML'))


all_reports = []
for i in day:
    if date in i and "Рассмотрено" not in i and "Отказано" not in i and "На рассмотрении" not in i:
        report1 = i.split()
        for a in report1:
            if 'threads' in a:
                all_reports.append("https://forum.gta5rp.com/" + a[6:-1])
                break

driver.quit()

# def func_chunks_num(lst, c_num):
#     n = math.ceil(len(lst) / c_num)

#     for x in range(0, len(lst), n):
#         e_c = lst[x : n + x]

#         if len(e_c) < n:
#             e_c = e_c + [None for y in range(n - len(e_c))]
#         yield e_c


Mo = ['GreyAbsolute','ForzeMikasa','RudyUntouchable','NoaDay', 'JeanOwl']
Tu = ['NeonNeurotic', 'JettSportik','ViVien','RickMeow','ScroogeLuccheze', 'BlackStar', 'EmilioRintaro']
We = ['NoahWennetti',  'ErnestoBaldini', 'MilkyWay', 'BenjaminFranklim', 'PacoAdams', 'RodjerMesh', 'AyatoKillstation']
Th = ['ChoppaHurtz','TenshiKato','ForzeMikasa','RudyUntouchable','GreyAbsolute', 'LovvMode', 'AeshKa']
Fr = ['NoaDay', 'ChoppaHurtz', 'BlackStar', 'JeanOwl', 'EmilioRintaro']
Sa = ['ErnestoBaldini','MilkyWay', 'TenshiKato','NeonNeurotic', 'LovvMode', 'AyatoKillstation', 'AeshKa']
Su = ['NoahWennetti', 'JettSportik','ViVien','RickMeow','ScroogeLuccheze', 'BenjaminFranklim', 'PacoAdams']

days_of_week = [0, Mo, Tu, We, Th, Fr, Sa, Su]
random.shuffle(days_of_week[day_week])

listR = np.array_split(all_reports, len(days_of_week[day_week]))
# listR = list(func_chunks_num(all_reports, c_num=len(days_of_week[day_week])))

with codecs.open("reports.txt", "w", "utf-8") as rep:
    rep.write(f"{len(listR[0])} жалоб\n{days_of_week[day_week][0]}\n")
    for i in listR[0]:
        rep.write(i + "\n")
    rep.write(f"{days_of_week[day_week][1]}\n")
    for i in listR[1]:
        rep.write(i + "\n")
    rep.write(f"{days_of_week[day_week][2]}\n")
    for i in listR[2]:
        rep.write(i + "\n")
    rep.write(f"{days_of_week[day_week][3]}\n")
    for i in listR[3]:
        rep.write(i + "\n")
    rep.write(f"{days_of_week[day_week][4]}\n")
    for i in listR[4]:
        rep.write(str(i) + "\n")
    if len(days_of_week[day_week]) >= 6:
        rep.write(f"{days_of_week[day_week][5]}\n")
        for i in listR[5]:
            rep.write(str(i) + "\n")
    if len(days_of_week[day_week]) >= 7:
        rep.write(f"{days_of_week[day_week][6]}\n")
        for i in listR[6]:
            rep.write(str(i) + "\n")
    if len(days_of_week[day_week]) >= 8:
        rep.write(f"{days_of_week[day_week][7]}\n")
        for i in listR[7]:
            rep.write(str(i) + "\n")
    if len(days_of_week[day_week]) >= 9:
        rep.write(f"{days_of_week[day_week][8]}\n")
        for i in listR[8]:
            rep.write(str(i) + "\n")
