import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_open_lk_page(authorized):
    driver = authorized

    driver.find_element(By.XPATH, ".//a[@href = '/account']").click()

    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, ".//a[@href = '/account/profile']")))

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile"

    driver.quit()


def test_switch_lk_to_construct_with_click_to_logo(authorized):
    driver = authorized

    driver.find_element(By.XPATH, ".//a[@href = '/account']").click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, ".//a[@href = '/account/profile']")))

    driver.find_element(By.CLASS_NAME, "AppHeader_header__logo__2D0X2").click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        (By.CLASS_NAME, "BurgerIngredients_ingredients__1N8v2")))

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    driver.quit()


def test_switch_lk_to_construct_with_click_to_constructor_button(authorized):
    driver = authorized

    driver.find_element(By.XPATH, ".//a[@href = '/account']").click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        (By.XPATH, ".//a[@href = '/account/profile']")))

    driver.find_element(By.CLASS_NAME, "AppHeader_header__linkText__3q_va").click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
        (By.CLASS_NAME, "BurgerIngredients_ingredients__1N8v2")))

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/"

    driver.quit()


def test_exit_from_lk(authorized):
    driver = authorized

    driver.find_element(By.XPATH, ".//a[@href = '/account']").click()

    driver.find_element(By.XPATH, ".//li[@class = 'Account_listItem__35dAP'][3]/button").click()

    WebDriverWait(driver, 3).until(
        expected_conditions.element_to_be_clickable((By.XPATH, ".//li[@class = 'Account_listItem__35dAP'][3]/button")))

    assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"

    driver.quit()
