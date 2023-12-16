import locator
import helpers
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestRegistrationPage:
    def test_success_registration(self, driver_option):
        name = helpers.create_name()
        email = helpers.create_login()
        password = helpers.create_password()

        driver_option.get("https://stellarburgers.nomoreparties.site")
        driver_option.find_element(*locator.Locator.account_entry).click()
        driver_option.find_element(*locator.Locator.register).click()

        WebDriverWait(driver_option, 3).until(
            expected_conditions.visibility_of_element_located(locator.Locator.form_login))

        driver_option.find_element(*locator.Locator.name).send_keys(name)
        driver_option.find_element(*locator.Locator.login).send_keys(email)
        driver_option.find_element(*locator.Locator.password).send_keys(password)

        driver_option.find_element(*locator.Locator.button_registration).click()

        WebDriverWait(driver_option, 10).until(
            expected_conditions.visibility_of_element_located(locator.Locator.button_login))

        assert driver_option.current_url == 'https://stellarburgers.nomoreparties.site/login'


    def test_failed_registration_incorrect_password(self, driver_option):
        name = helpers.create_name()
        email = helpers.create_login()
        password = helpers.create_incorrect_password()

        driver_option.get("https://stellarburgers.nomoreparties.site")
        driver_option.find_element(*locator.Locator.account_entry).click()
        driver_option.find_element(*locator.Locator.register).click()

        WebDriverWait(driver_option, 3).until(
            expected_conditions.visibility_of_element_located(locator.Locator.form_login))

        driver_option.find_element(*locator.Locator.name).send_keys(name)
        driver_option.find_element(*locator.Locator.login).send_keys(email)
        driver_option.find_element(*locator.Locator.password).send_keys(password)

        driver_option.find_element(*locator.Locator.button_registration).click()
        WebDriverWait(driver_option, 3).until(
            expected_conditions.visibility_of_element_located(locator.Locator.error))

        assert driver_option.find_element(*locator.Locator.error).text == 'Некорректный пароль'
