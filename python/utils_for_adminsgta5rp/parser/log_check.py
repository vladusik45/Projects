from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import codecs
from datetime import datetime, timedelta
from tkinter import *
from tkinter import ttk

# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--user-data-dir=C:\\Users\\User\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")
# chrome_options.add_argument("headless")
# driver = webdriver.Chrome(options=chrome_options)
# driver.get('https://gta5rp.com/logs?act=auth')
# clear_punish = open('Наказания.txt', 'w')

# date_to = driver.find_element(by=By.XPATH, value='//*[@id="auth_logs_time_to"]')
# date_from = driver.find_element(by=By.XPATH, value='//*[@id="auth_logs_time_from"]')
# IDplayer = driver.find_element(by=By.XPATH, value='//*[@id="auth_logs_game_id"]')
# search = driver.find_element(by=By.XPATH, value='/html/body/div[2]/main/div[1]/div[2]/div/div[1]/div/div[2]/div[4]/div/button')
# sleep(1)

# def searching(dateText, timeText, IDplayerText):
#     date_to_report = datetime.strptime(dateText, '%d.%m.%Y')
#     ReportTime = dateText + ', ' + timeText
#     ReportDate = datetime.strptime(ReportTime, '%d.%m.%Y, %H:%M')
#     temp_date = date_to_report - timedelta(days=1)
#     date_from_report = temp_date.strftime('%d-%m-%Y')

#     hueta = driver.find_element(by=By.XPATH, value='/html/body/div[2]/main/div[1]/div[2]/div/div[1]/div/div[1]/div[1]/label')

#     date_to.clear()
#     date_to.send_keys(dateText)
#     date_from.clear()
#     date_from.send_keys(date_from_report)
#     hueta.click()
#     IDplayer.clear()
#     IDplayer.click()
#     IDplayer.send_keys(IDplayerText)
#     search.click()
#     sleep(2)

#     countStrings = driver.find_element(by=By.XPATH, value='//*[@id="logs_total_cnt"]').text

#     for i in range(1, int(countStrings)+1):
#         elements = driver.find_element(by=By.XPATH, value='//*[@id="logs_table"]/tr[' + str(i) + ']').text
#         element = elements.split(' ')
#         time = elements[-20:-3]
#         time_log = datetime.strptime(time, '%d.%m.%Y, %H:%M')
#         a = 0
#         if ReportDate > time_log:
#             full_pers = str(element[2]) + ' ' + str(element[6])
#             global statick
#             statick = element[6]
#             result_text.insert("1.0", full_pers)
#             result_text.insert(END, '\n'+time)
#             button = driver.find_element(by=By.XPATH, value = '/html/body/div[2]/main/div[2]/div/table/tbody/tr[' + str(i) + ']/td[3]/a[1]')
#             button.click()
#             sleep(1)
#             character_count = driver.find_element(by=By.XPATH, value='/html/body/div[2]/div[3]/div/div/div[2]/p').text
#             if character_count[-6] == '1':
#                 characters = 1
#             elif character_count[-6] == '2':
#                 characters = 2
#             else: characters = 3
#             if characters == 2 or characters == 3:
#                 for pers in range(1, characters):
#                     b = 0
#                     id = driver.find_element(by=By.XPATH, value ='/html/body/div[2]/div[3]/div/div/div[2]/div/div['+ str(pers) + ']/ul/li[1]').text
#                     if id[4:] == element[6]:
#                         faction = driver.find_element(by= By.XPATH, value = '/html/body/div[2]/div[3]/div/div/div[2]/div/div['+ str(pers) + ']/ul/li[3]').text
#                         result_text.insert(END, '\n'+faction)
#                         button_close = driver.find_element(by= By.CLASS_NAME, value = 'close')
#                         button_close.click()
#                         b = 1
#                     if b == 1: break     
#             else:
#                 character = driver.find_element(by=By.CLASS_NAME, value = 'card')
#                 faction = driver.find_element(by= By.XPATH, value = '/html/body/div[2]/div[3]/div/div/div[2]/div/div/ul/li[3]').text
#                 result_text.insert(END, '\n'+faction)
#                 button_close = driver.find_element(by= By.CLASS_NAME, value = 'close')
#                 button_close.click()
#             a = 1
#         if a == 1: break

def button_click():
    result_text.delete("1.0", END)
    dateText = entry_date.get()
    IDplayerText = entry_id.get()
    timeText = entry_time.get()
    # searching(dateText, timeText, IDplayerText)

def prison_click():
    a = 1
    # with open('Наказания.txt', 'a') as punish_text:
    #     punish_text.write('offprison ' + statick + ' ' + str(punish_entry.get()) + ' Жалоба №' + report_num_enrty.get() + ' \\ by Way\n')

def warn_click():
    a = 1
    # with open('Наказания.txt', 'a') as punish_text:
    #     punish_text.write('offwarn ' + statick + ' Жалоба №' + report_num_enrty.get() + ' \\ by Way\n')

def mute_click():
    a = 1
    # with open('Наказания.txt', 'a') as punish_text:
    #     punish_text.write('offmute ' + statick + ' ' + str(punish_entry.get()) + ' Жалоба №' + report_num_enrty.get() + ' \\ by Way\n')

def ban_click():
    a = 1
    # with open('Наказания.txt', 'a') as punish_text:
    #     punish_text.write('offban ' + statick + ' ' + str(punish_entry.get()) + ' Жалоба №' + report_num_enrty.get() + ' \\ by Way\n')

# root = Tk()
# root.geometry("500x200")
# root.overrideredirect(1)
# root.attributes("-topmost",True)
# x = 0
# y = 800
# root.wm_geometry("+%d+%d" % (x, y))
# root.configure(bg='midnight blue')

# entry_date = Entry(font=30, bg = 'grey47')
# entry_date.place(x=10, y=35, width=85)

# label_date = Label(text= 'Дата', font=30, bg = 'grey33')
# label_date.place(x=10, y=10)

# entry_time = Entry(font=30, bg = 'grey47')
# entry_time.place(x=105, y=35, width=50)

# label_time = Label(text='Время',font=30, bg = 'grey33')
# label_time.place(x=100, y=10)

# entry_id = Entry(font=30, bg = 'grey47')
# entry_id.place(x=165, y=35, width=50)

# label_id = Label(text= 'ID',font=30, bg = 'grey33')
# label_id.place(x=165, y=10)

# punish_label = Label(text='Наказание',font=30, bg = 'grey33')
# punish_label.place(x=220, y=10)

# report_num_enrty = Entry(font=30, bg = 'grey47')
# report_num_enrty.place(x=300, y=35, width=50)

# report_num_label = Label(text= 'Жалоба',font=30, bg = 'grey33')
# report_num_label.place(x=300, y=10)

# punish_entry = Entry(font=30, bg = 'grey47')
# punish_entry.place(x=225, y=35, width=50)

# result_button = Button(text='Результат', font=30, command=button_click)
# result_button.place(x=400, y=20)

# result_text = Text()
# result_text.place(x=10, y=70, width=180, height=120)

# prison_button = Button(text='Prison', font=30, command=prison_click)
# prison_button.place(x=200, y = 70, width=50, height=20)

# mute_button = Button(text='Mute', font=30, command=mute_click)
# mute_button.place(x=200, y = 100, width=50, height=20)

# warn_button = Button(text='Warn', font=30, command=warn_click)
# warn_button.place(x=200, y = 130, width=50, height=20)

# ban_button = Button(text='Ban', font=30, command=ban_click)
# ban_button.place(x=200, y = 160, width=50, height=20)

# root.mainloop()

root = Tk()
root.geometry("120x420")
root.overrideredirect(1)
root.attributes("-topmost",True)
x = 0
y = 620
root.wm_geometry("+%d+%d" % (x, y))
root.configure(bg='LavenderBlush4')

entry_date = Entry(font=30, bg = 'grey67')
entry_date.place(x=10, y=30, width=85)

label_date = Label(text= 'Дата', font=30, bg = 'grey33', fg = 'GhostWhite')
label_date.place(x=10, y=5)


entry_time = Entry(font=30, bg = 'grey67')
entry_time.place(x=10, y=80, width=50)

label_time = Label(text='Время',font=30, bg = 'grey33', fg = 'GhostWhite')
label_time.place(x=10, y=55)


entry_id = Entry(font=30, bg = 'grey67')
entry_id.place(x=10, y=130, width=50)

label_id = Label(text= 'ID',font=30, bg = 'grey33', fg = 'GhostWhite')
label_id.place(x=10, y=105)


punish_label = Label(text='Наказание',font=30, bg = 'grey33', fg = 'GhostWhite')
punish_label.place(x=10, y=155)

punish_entry = Entry(font=30, bg = 'grey67')
punish_entry.place(x=10, y=180, width=50)


report_num_enrty = Entry(font=30, bg = 'grey67')
report_num_enrty.place(x=10, y=230, width=50)

report_num_label = Label(text= 'Жалоба',font=30, bg = 'grey33', fg = 'GhostWhite')
report_num_label.place(x=10, y=205)


result_button = Button(text='Результат', font=30, command=button_click, fg = 'GhostWhite')
result_button.place(x=400, y=20)

result_text = Text(weight = 'bold')
result_text.place(x=10, y=300, width=180, height=120)


prison_button = Button(text='Prison', font=30, command=prison_click, fg = 'GhostWhite')
prison_button.place(x=200, y = 70, width=50, height=20)

mute_button = Button(text='Mute', font=30, command=mute_click, fg = 'GhostWhite')
mute_button.place(x=200, y = 100, width=50, height=20)

warn_button = Button(text='Warn', font=30, command=warn_click, fg = 'GhostWhite')
warn_button.place(x=200, y = 130, width=50, height=20)

ban_button = Button(text='Ban', font=30, command=ban_click, fg = 'GhostWhite')
ban_button.place(x=200, y = 160, width=50, height=20)

root.mainloop()