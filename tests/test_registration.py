from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Locator:
    def __init__(self):
        self.account_entry = ".button_button__33qZ0"  # локатор для кнопки "Войти в аккаунт"
        self.register = ".//a[@href = '/register']"  # локатор для кнопки перехода к форме регистрации
        self.form_login = ".Auth_login__3hAey"  # локатор страницы логина
        self.name = "(//input)[1]"  # локатор ввода имени пользователя
        self.login = "(//input)[2]"  # локатор ввода email пользователя
        self.password = "(//input)[3]"  # локатор ввода пароля пользователя
        self.button_registration = ".//button[text() = 'Зарегистрироваться']"  # локатор кнопки "Зарегистрироваться"
        self.error = ".//p[@class = 'input__error text_type_main-default']"  # локатор текста ошибки при неверном пароля


def test_success_registration(create_login, create_name, create_password):
    driver = webdriver.Chrome()
    locator = Locator()

    driver.get("https://stellarburgers.nomoreparties.site")
    driver.find_element(By.CSS_SELECTOR, locator.account_entry).click()
    driver.find_element(By.XPATH, locator.register).click()

    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, locator.form_login)))

    driver.find_element(By.XPATH, locator.name).send_keys(create_name)
    driver.find_element(By.XPATH, locator.login).send_keys(create_login)
    driver.find_element(By.XPATH, locator.password).send_keys(create_password)

    driver.find_element(By.XPATH, locator.button_registration).click()

    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable((By.XPATH, locator.button_registration)))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    driver.quit()


def test_failed_registration_incorrect_password(create_login, create_name, create_incorrect_password):
    driver = webdriver.Chrome()
    locator = Locator()

    driver.get("https://stellarburgers.nomoreparties.site")
    driver.find_element(By.CSS_SELECTOR, locator.account_entry).click()
    driver.find_element(By.XPATH, locator.register).click()

    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, locator.form_login)))

    driver.find_element(By.XPATH, locator.name).send_keys(create_name)
    driver.find_element(By.XPATH, locator.login).send_keys(create_login)
    driver.find_element(By.XPATH, locator.password).send_keys(create_incorrect_password)

    driver.find_element(By.XPATH, locator.button_registration).click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, locator.error)))

    assert driver.find_element(By.XPATH, locator.error).text == 'Некорректный пароль'

    driver.quit()
