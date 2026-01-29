from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from datetime import *

date_from_text = input("Введите дату (ОТ). Пример: 03.01.2024\n")
date_to_text = input("Введите дату (ДО). Пример: 03.01.2024\n")

chrome_options = Options()
chrome_options.add_argument("--user-data-dir=C:\\Users\\User\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 2")
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://forum.gta5rp.com/forums/zhaloby-na-igrokov.1515/')
sleep(3)


dateFrom = driver.find_element(by=By.XPATH, value='//*[@id="faction_logs_time_from"]')
dateTo = driver.find_element(by=By.XPATH, value='//*[@id="faction_logs_time_to"]')
action = driver.find_element(by=By.XPATH, value='//*[@id="faction_logs_text"]')
search = driver.find_element(by=By.XPATH, value='/html/body/div[2]/main/div[1]/div[2]/div/div[1]/div/div[2]/div[3]/div/button')
sleep(1)
dropdown = driver.find_element(By.XPATH, value = "/html/body/div[2]/main/div[1]/div[2]/div/div[1]/div/div[1]/div[3]/div/div/button")
dropdown.click()
sleep(1)
buttonNull = driver.find_element(by=By.XPATH, value='/html/body/div[2]/main/div[1]/div[2]/div/div[1]/div/div[1]/div[3]/div/div/div/div/ul/li[1]/a')
buttonNull.click()


dateFrom.clear()
dateFrom.send_keys(dateFromText)
dateTo.clear()
dateTo.send_keys(dateToText)
action.clear()
action.send_keys(actionText)
action.click()
sleep(2)
search.click()
sleep(2)

table = []
logsFile = open("logsFile.txt", "w")
def TableElem(count):
    for i in range(1, int(count)+1):
        element = driver.find_element(by=By.XPATH, value='//*[@id="logs_table"]/tr[' + str(i) + ']/td[1]').text + "\t" + driver.find_element(by=By.XPATH, value='//*[@id="logs_table"]/tr[' + str(i) + ']/td[2]').text + "\t" + driver.find_element(by=By.XPATH, value='//*[@id="logs_table"]/tr[' + str(i) + ']/td[3]').text + "\t" + driver.find_element(by=By.XPATH, value='//*[@id="logs_table"]/tr[' + str(i) + ']/td[4]').text + "\t" + driver.find_element(by=By.XPATH, value='//*[@id="logs_table"]/tr[' + str(i) + ']/td[5]').text
        logsFile.write(element + "\n")
        print(element)

countStrings = driver.find_element(by=By.XPATH, value='/html/body/div[2]/main/div[1]/div[2]/div/div[3]/b[1]').text
if int(countStrings) > 3000:
    countPages = int(countStrings) // 3000
    countTemp = int(countStrings)
    for i in range(countPages + 1):
        sleep(3)
        if countTemp > 3000:
            TableElem(3000)
        else:
            TableElem(countTemp)
        countTemp -= 3000
        if i <= countPages:
            strelka = driver.find_element(by=By.XPATH, value='/html/body/div[2]/main/div[1]/div[2]/div/div[2]/ul/li[5]')
            strelka.click()
else:
    TableElem(countStrings)

driver.quit()

