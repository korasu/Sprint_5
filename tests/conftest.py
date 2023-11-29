import random
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def create_login():
    email = ''

    for nick in range(8):
        email += random.choice(list('abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))

    email += f'3{random.randint(100, 999)}@example.com'

    return email


@pytest.fixture
def create_password():
    password = ''

    for i in range(random.randint(6, 12)):
        password += random.choice(list('0123456789abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))

    return password


@pytest.fixture
def create_incorrect_password():
    password = ''

    for i in range(random.randint(1, 5)):
        password += random.choice(list('0123456789abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))

    return password


@pytest.fixture
def create_name():
    name = ''

    for i in range(random.randint(1, 15)):
        name += random.choice(list('abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))

    if name[0].isupper():
        name = name[0] + name[1:len(name)].lower()
    else:
        name = name[0].upper() + name[1:len(name)].lower()

    return name


@pytest.fixture
def create_account(create_name, create_login, create_password):
    login = create_login
    password = create_password

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome(options=options)

    driver.get("https://stellarburgers.nomoreparties.site")
    driver.find_element(By.CSS_SELECTOR, ".button_button__33qZ0").click()
    driver.find_element(By.CLASS_NAME, "Auth_link__1fOlj").click()

    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".Auth_login__3hAey")))

    driver.find_element(By.XPATH, "(//input)[1]").send_keys(create_name)
    driver.find_element(By.XPATH, "(//input)[2]").send_keys(login)
    driver.find_element(By.XPATH, "(//input)[3]").send_keys(password)

    driver.find_element(By.XPATH, ".//button[text() = 'Зарегистрироваться']").click()

    driver.quit()
    return login, password


@pytest.fixture
def authorized(create_account):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    driver = webdriver.Chrome()

    driver.get("https://stellarburgers.nomoreparties.site")
    driver.find_element(By.CSS_SELECTOR, ".button_button__33qZ0").click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".App_App__aOmNj")))

    driver.find_element(By.XPATH, "(//input)[1]").send_keys(create_account[0])
    driver.find_element(By.XPATH, "(//input)[2]").send_keys(create_account[1])

    driver.find_element(By.XPATH, ".//button[text() = 'Войти']").click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.CLASS_NAME, "BurgerIngredients_ingredients__1N8v2")))

    return driver
