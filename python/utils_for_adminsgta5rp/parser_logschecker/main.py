from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Открыть браузер и перейти на нужную страницу
browser = webdriver.Chrome()
browser.get("https://gta5rp.com/mi?act=faction_members&faction=F_ARMENIAMAFIA&sid=15")
time.sleep(60) # 60 sec wait

# Найти элементы строки и извлечь Имя и Фамилию
rows = browser.find_elements(By.XPATH("//table/tbody/tr"))
for row in rows:
    name = row.find_elements(By.XPATH("./td[1]"))

    # Нажать на кнопку и дождаться появления модального окна
    button = row.find_element(By.XPATH(".//a[text()='ч']"))
    button.click()
    modal = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".modal-content")))

    # Собрать информацию из модального окна и сохранить в файл
    info = modal.find_element(By.ID, 'modal-content').text
    with open(f"{name}.txt", "w") as file:
        file.write(info)

    # Закрыть модальное окно и перейти к следующей строке
    close_button = modal.find_element(By.CLASS_NAME, 'btn btn-default')
    close_button.click()

# Закрыть браузер
browser.quit()