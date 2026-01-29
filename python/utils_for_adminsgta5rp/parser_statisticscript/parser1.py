from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
import codecs

# faction = input('Выберите фракцию: ')
# action_text = input('Выберите действие: ')
# filename = input('Выберите название файла: ')
# clear = input('Нужно ли очистить файл?(y|n): ')


def parser(faction:str, filename:str, action_text:str, clear:bool, date_from_text=None, date_to_text=None, enter_exit=None):
    filename = filename
    if isinstance(enter_exit, bool):
        if not enter_exit:
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--user-data-dir=C:\\Users\\vlada\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")
            chrome_options.add_argument("headless")
            global driver
            driver = webdriver.Chrome(options=chrome_options)
            driver.get('https://gta5rp.com/logs?act=faction&page=3')
    sleep(5)
    dateFrom =driver.find_element(by=By.XPATH, value='//*[@id="faction_logs_time_from"]')
    dateTo = driver.find_element(by=By.XPATH, value='//*[@id="faction_logs_time_to"]')
    player = driver.find_element(by=By.XPATH, value='//*[@id="faction_logs_char"]')
    player.clear()
    action = driver.find_element(by=By.XPATH, value='//*[@id="faction_logs_text"]')
    action.clear()
    search = driver.find_element(by=By.XPATH, value='/html/body/div[2]/main/div[1]/div[2]/div/div[1]/div/div[2]/div[3]/div/button')
    sleep(1)
    dropdown = driver.find_element(By.XPATH, value = "/html/body/div[2]/main/div[1]/div[2]/div/div[1]/div/div[1]/div[3]/div/div/button")
    dropdown.click()
    sleep(1)
    buttonNull = driver.find_element(by=By.XPATH, value='/html/body/div[2]/main/div[1]/div[2]/div/div[1]/div/div[1]/div[3]/div/div/div/div/ul/li[1]/a')
    buttonNull.click()
    hueta = driver.find_element(by=By.XPATH,value='/html/body/div[2]/main/div[1]/div[2]/div/div[1]/div/div[1]/div[1]/label')

    def select_faction(faction):
        if faction == 'AM':
            faction = '/html/body/div[2]/main/div[1]/div[2]/div/div[1]/div/div[1]/div[3]/div/div/div/div/ul/li[2]/a'
        if faction == 'EMS':
            faction = '/html/body/div[2]/main/div[1]/div[2]/div/div[1]/div/div[1]/div[3]/div/div/div/div/ul/li[3]/a'
        if faction == 'FIB':
            faction = '/html/body/div[2]/main/div[1]/div[2]/div/div[1]/div/div[1]/div[3]/div/div/div/div/ul/li[4]/a'
        if faction == 'ESB':
            faction = '/html/body/div[2]/main/div[1]/div[2]/div/div[1]/div/div[1]/div[3]/div/div/div/div/ul/li[5]/a'
        if faction == 'BSG':
            faction = '/html/body/div[2]/main/div[1]/div[2]/div/div[1]/div/div[1]/div[3]/div/div/div/div/ul/li[6]/a'
        if faction == 'FAM':
            faction = '/html/body/div[2]/main/div[1]/div[2]/div/div[1]/div/div[1]/div[3]/div/div/div/div/ul/li[7]/a'
        if faction == 'MG':
            faction = '/html/body/div[2]/main/div[1]/div[2]/div/div[1]/div/div[1]/div[3]/div/div/div/div/ul/li[8]/a'
        if faction == 'LSV':
            faction = '/html/body/div[2]/main/div[1]/div[2]/div/div[1]/div/div[1]/div[3]/div/div/div/div/ul/li[9]/a'
        if faction == 'LCN':
            faction = '/html/body/div[2]/main/div[1]/div[2]/div/div[1]/div/div[1]/div[3]/div/div/div/div/ul/li[10]/a'
        if faction == 'ARMY':
            faction = '/html/body/div[2]/main/div[1]/div[2]/div/div[1]/div/div[1]/div[3]/div/div/div/div/ul/li[11]/a'
        if faction == 'GOV':
            faction = '/html/body/div[2]/main/div[1]/div[2]/div/div[1]/div/div[1]/div[3]/div/div/div/div/ul/li[12]/a'
        if faction == 'LSPD':
            faction = '/html/body/div[2]/main/div[1]/div[2]/div/div[1]/div/div[1]/div[3]/div/div/div/div/ul/li[13]/a'
        if faction == 'LSSD':
            faction = '/html/body/div[2]/main/div[1]/div[2]/div/div[1]/div/div[1]/div[3]/div/div/div/div/ul/li[14]/a'
        if faction == 'MM':
            faction = '/html/body/div[2]/main/div[1]/div[2]/div/div[1]/div/div[1]/div[3]/div/div/div/div/ul/li[15]/a'
        if faction == 'WN':
            faction = '/html/body/div[2]/main/div[1]/div[2]/div/div[1]/div/div[1]/div[3]/div/div/div/div/ul/li[16]/a'
        if faction == 'SASPA':
            faction = '/html/body/div[2]/main/div[1]/div[2]/div/div[1]/div/div[1]/div[3]/div/div/div/div/ul/li[17]/a'
        if faction == 'RM':
            faction = '/html/body/div[2]/main/div[1]/div[2]/div/div[1]/div/div[1]/div[3]/div/div/div/div/ul/li[18]/a'
        if faction == 'YAK':
            faction = '/html/body/div[2]/main/div[1]/div[2]/div/div[1]/div/div[1]/div[3]/div/div/div/div/ul/li[19]/a'
    
        faction1 = driver.find_element(by=By.XPATH, value=faction)
        dropdown.click()
        faction1.click()

    def Table_elem():
        with codecs.open(f'{filename}.txt', 'a', "utf-8") as file_logi:
            table = driver.find_element(by=By.XPATH, value='/html/body/div[2]/main/div[2]/div/table').text
            # string_log = driver.find_element(by=By.XPATH,value=f'/html/body/div[2]/main/div[2]/div/table/tbody/tr[{string}]').text
            table = table.replace('Ид Персонаж Фракция Текст Время', '')
            file_logi.write(f'{table}')

    def Change_Pages():
        count_strings = driver.find_element(by=By.XPATH, value='/html/body/div[2]/main/div[1]/div[2]/div/div[3]/b[1]').text
        if int(count_strings) > 3000:
            count_pages = int(count_strings) // 3000
            for i in range(count_pages + 1):
                sleep(3)
                Table_elem()
                if i <= count_pages:
                    strelka = driver.find_elements(by=By.CLASS_NAME, value='page-item')
                    strelka[len(strelka)-1].click()
        else: Table_elem()

    if clear :
        a = open(f'{filename}.txt', 'w')
        a.close()
    if isinstance(date_from_text, str):
        date_from_text = date_from_text
    else:
        date_from_text = input('Выберите начальную дату: ')
    if isinstance(date_to_text, str):
        date_to_text = date_to_text
    else:
        date_to_text = input('Выберите конечную дату: ')
    dateFrom.clear()
    dateFrom.send_keys(date_from_text)
    dateTo.clear()
    dateTo.send_keys(date_to_text)
    hueta.click()
    if faction != 'null':
        select_faction(faction)
    action.clear()
    action.send_keys(action_text)
    search.click()
    sleep(2)
    Change_Pages()
    if isinstance(enter_exit, bool):
        if enter_exit:
            driver.quit()