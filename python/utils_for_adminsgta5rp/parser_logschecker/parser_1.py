from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep

websites = {
    "LSV": "https://gta5rp.com/-----F_GANG_VAGOS&sid=18",
    "MARA": "https://gta5rp.com/-----F_GANG_MARABUNTA&sid=18",
    "FAM": "https://gta5rp.com/-----F_GANG_GROVE&sid=18",
    "BLLS": "https://gta5rp.com/-----F_GANG_BALLAS&sid=18",
    "BSG": "https://gta5rp.com/-----F_GANG_BLOODS&sid=18",
    # "RM": "https://gta5rp.com/-----F_RUSSIANMAFIA&sid=18",
    # "AM": "https://gta5rp.com/-----F_ARMENIAMAFIA&sid=18",
    # "YAK": "https://gta5rp.com/-----F_YAKUZA&sid=18",
    # "LCN": "https://gta5rp.com/-----F_ITALYMAFIA&sid=18",
    # "MM": "https://gta5rp.com/-----F_MEXICOMAFIA&sid=18",
}

chrome_options = Options()
chrome_options.add_argument("--user-data-dir=C:\\Users\\vlada\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 1")
driver = webdriver.Chrome(options=chrome_options)

for name, site in websites.items():
    # Создать имя файла на основе имени сайта
    filename = f"{name}.txt"

    driver.get(site)
    sleep(5)

    buttons = driver.find_elements(By.XPATH, "//table//tbody//a[contains(text(), '(ч)')]")
    with open(filename, 'a') as file:
        counter = 1
        for i in range(len(buttons)):
            button = driver.find_elements(By.XPATH, "//table//tbody//a[contains(text(), '(ч)')]")[i]
            driver.execute_script("arguments[0].click();", button)
            sleep(0.75)

            modal_window = driver.find_element(By.XPATH, "//*[@id='set_user_modal']")
            information = modal_window.find_element(By.CLASS_NAME,"form-horizontal").text
            file.write(f"\nACC: {counter}\n{information}")
            counter +=1
            print("Записал:", name)
            print(information)

            close_button = driver.find_element(By.XPATH, "//button[@class='btn btn-default']")
            close_button.click()
            sleep(0.75)
        else:
            print(f"Завершено на сайте {name}")

driver.quit()