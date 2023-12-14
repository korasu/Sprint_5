import pytest
import locator
import helpers
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def driver_option():
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def create_account(driver_option):
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

    return email, password


@pytest.fixture
def authorized(driver_option, create_account):
    driver_option.get("https://stellarburgers.nomoreparties.site")
    driver_option.find_element(*locator.Locator.lk_in_header).click()
    WebDriverWait(driver_option, 3).until(
        expected_conditions.visibility_of_element_located(locator.Locator.button_login))

    driver_option.find_element(*locator.Locator.login_email).send_keys(create_account[0])
    driver_option.find_element(*locator.Locator.login_password).send_keys(create_account[1])

    driver_option.find_element(*locator.Locator.button_login).click()
    WebDriverWait(driver_option, 3).until(
        expected_conditions.visibility_of_element_located(locator.Locator.constructr_block))

    return driver_option
