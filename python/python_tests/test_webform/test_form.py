from pages.form_page import ContactPage
import time


def test_positive_form_submission(driver):
    page = ContactPage(driver)
    page.open()

    page.fill_form(
        name="V",
        last_name="VV",
        email="vvv@test.com",
        gender="male",
        mobile="8899773388",
        current_addr="Moscow"
    )

    page.submit_form()

    time.sleep(2)

    assert page.is_success_displayed()

def test_negative_empty_email(driver):
    page = ContactPage(driver)
    page.open()

    page.fill_form(
        name="V",
        last_name="VV",
        email="vvv@test.com",
        gender="",
        mobile="",
        current_addr="Moscow"
    )
    time.sleep(3)

    page.submit_form()

    assert page.is_email_invalid()