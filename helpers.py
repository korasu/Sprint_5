import random

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

import locator


def create_login():
    email = ''

    for nick in range(8):
        email += random.choice(list('abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))

    email += f'3{random.randint(100, 999)}@example.com'

    return email


def create_password():
    password = ''

    for i in range(random.randint(6, 12)):
        password += random.choice(list('0123456789abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))

    return password


def create_incorrect_password():
    password = ''

    for i in range(random.randint(1, 5)):
        password += random.choice(list('0123456789abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))

    return password


def create_name():
    name = ''

    for i in range(random.randint(1, 15)):
        name += random.choice(list('abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))

    if name[0].isupper():
        name = name[0] + name[1:len(name)].lower()
    else:
        name = name[0].upper() + name[1:len(name)].lower()

    return name


def create_account(driver_option):
    name = create_name()
    email = create_login()
    password = create_password()

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


def authorized(driver_option):
    registration = create_account(driver_option)
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

    return driver_option
