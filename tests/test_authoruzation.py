import locator
import helpers
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestAuthorization:
    def test_success_login_with_click_button_entry_in_account(self, driver_option):
        registration = helpers.create_account(driver_option)
        email = registration[0]
        password = registration[1]

        driver_option.get("https://stellarburgers.nomoreparties.site")
        driver_option.find_element(*locator.Locator.account_entry).click()
        WebDriverWait(driver_option, 3).until(
            expected_conditions.visibility_of_element_located(locator.Locator.button_login))

        driver_option.find_element(*locator.Locator.login_email).send_keys(email)
        driver_option.find_element(*locator.Locator.login_password).send_keys(password)

        driver_option.find_element(*locator.Locator.button_login).click()
        WebDriverWait(driver_option, 3).until(
            expected_conditions.visibility_of_element_located(locator.Locator.constructr_block))

        assert driver_option.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_success_login_with_click_button_lk(self, driver_option):
        registration = helpers.create_account(driver_option)
        email = registration[0]
        password = registration[1]

        driver_option.get("https://stellarburgers.nomoreparties.site")
        driver_option.find_element(*locator.Locator.lk_in_header).click()
        WebDriverWait(driver_option, 3).until(
            expected_conditions.visibility_of_element_located(locator.Locator.button_login))

        driver_option.find_element(*locator.Locator.login_email).send_keys(email)
        driver_option.find_element(*locator.Locator.login_password).send_keys(password)

        driver_option.find_element(*locator.Locator.button_login).click()
        WebDriverWait(driver_option, 3).until(
            expected_conditions.visibility_of_element_located(locator.Locator.constructr_block))

        assert driver_option.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_success_login_across_registration_page(self, driver_option):
        registration = helpers.create_account(driver_option)
        email = registration[0]
        password = registration[1]

        driver_option.get("https://stellarburgers.nomoreparties.site")
        driver_option.find_element(*locator.Locator.account_entry).click()
        driver_option.find_element(*locator.Locator.register).click()
        WebDriverWait(driver_option, 3).until(
            expected_conditions.visibility_of_element_located(locator.Locator.form_login))

        driver_option.find_element(*locator.Locator.login_page_from_registration).click()

        driver_option.find_element(*locator.Locator.login_email).send_keys(email)
        driver_option.find_element(*locator.Locator.login_password).send_keys(password)

        driver_option.find_element(*locator.Locator.button_login).click()
        WebDriverWait(driver_option, 3).until(
            expected_conditions.visibility_of_element_located(locator.Locator.constructr_block))

        assert driver_option.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_success_login_across_recovery_password_page(self, driver_option):
        registration = helpers.create_account(driver_option)
        email = registration[0]
        password = registration[1]

        driver_option.get("https://stellarburgers.nomoreparties.site")

        driver_option.find_element(*locator.Locator.account_entry).click()
        driver_option.find_element(*locator.Locator.link_for_recovery_password).click()
        driver_option.find_element(*locator.Locator.login_page_from_registration).click()

        WebDriverWait(driver_option, 3).until(
            expected_conditions.visibility_of_element_located(locator.Locator.button_login))

        driver_option.find_element(*locator.Locator.login_email).send_keys(email)
        driver_option.find_element(*locator.Locator.login_password).send_keys(password)

        driver_option.find_element(*locator.Locator.button_login).click()
        WebDriverWait(driver_option, 3).until(
            expected_conditions.visibility_of_element_located(locator.Locator.constructr_block))

        assert driver_option.current_url == 'https://stellarburgers.nomoreparties.site/'
