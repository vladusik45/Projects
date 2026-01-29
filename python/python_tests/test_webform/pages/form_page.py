from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ContactPage(BasePage):
    URL = "https://demoqa.com/automation-practice-form"

    NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    EMAIL = (By.ID, "userEmail")
    GENDER_MALE = (By.CSS_SELECTOR, "label[for='gender-radio-1']")
    GENDER_FEMALE = (By.CSS_SELECTOR, "label[for='gender-radio-2']")
    MOBILE=(By.ID, "userNumber")
    CURRENT_ADDRESS = (By.ID, "currentAddress") 
    SUBMIT = (By.ID, "submit")

    OUTPUT = (By.ID, "example-modal-sizes-title-lg")
    EMAIL_FIELD = (By.ID, "userEmail")

    def open(self):
        self.driver.get(self.URL)

    def fill_form(self, name, last_name, email, gender, mobile, current_addr):
        self.type(self.NAME, name)
        self.type(self.LAST_NAME, last_name)
        self.type(self.EMAIL, email)
        if (gender == "male"):
            self.click(self.GENDER_MALE)
        elif (gender == "female"):
            self.click(self.GENDER_FEMALE)
        self.type(self.MOBILE, mobile)
        self.type(self.CURRENT_ADDRESS, current_addr)

    def submit_form(self):
        self.click(self.SUBMIT)

    def is_success_displayed(self):
        try:
            modal = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located(self.OUTPUT)
            )
            return modal.is_displayed()
        except:
            return False

    def is_email_invalid(self):
        return "field-error" in self.driver.find_element(*self.EMAIL_FIELD).get_attribute("class")
