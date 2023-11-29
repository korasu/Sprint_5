from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_success_login_with_click_button_entry_in_account(create_account):
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

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    driver.quit()


def test_success_login_with_click_button_lk(create_account):
    driver = webdriver.Chrome()

    driver.get("https://stellarburgers.nomoreparties.site")
    driver.find_element(By.XPATH, ".//a[@href = '/account']").click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".App_App__aOmNj")))

    driver.find_element(By.XPATH, "(//input)[1]").send_keys(create_account[0])
    driver.find_element(By.XPATH, "(//input)[2]").send_keys(create_account[1])

    driver.find_element(By.XPATH, ".//button[text() = 'Войти']").click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.CLASS_NAME, "BurgerIngredients_ingredients__1N8v2")))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    driver.quit()


def test_success_login_across_registration_page(create_account):
    driver = webdriver.Chrome()

    driver.get("https://stellarburgers.nomoreparties.site")
    driver.find_element(By.CSS_SELECTOR, ".button_button__33qZ0").click()
    driver.find_element(By.CLASS_NAME, "Auth_link__1fOlj").click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".Auth_login__3hAey")))

    driver.find_element(By.CLASS_NAME, "Auth_link__1fOlj").click()

    driver.find_element(By.XPATH, "(//input)[1]").send_keys(create_account[0])
    driver.find_element(By.XPATH, "(//input)[2]").send_keys(create_account[1])

    driver.find_element(By.XPATH, ".//button[text() = 'Войти']").click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.CLASS_NAME, "BurgerIngredients_ingredients__1N8v2")))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    driver.quit()


def test_success_login_across_recovery_password_page(create_account):
    driver = webdriver.Chrome()

    driver.get("https://stellarburgers.nomoreparties.site")

    driver.find_element(By.CSS_SELECTOR, ".button_button__33qZ0").click()
    driver.find_element(By.XPATH, ".//a[@href = '/account']").click()
    driver.find_element(By.XPATH, ".//a[@href = '/forgot-password']").click()
    driver.find_element(By.XPATH, ".//a[@href = '/login']").click()

    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".Auth_login__3hAey")))

    driver.find_element(By.XPATH, "(//input)[1]").send_keys(create_account[0])
    driver.find_element(By.XPATH, "(//input)[2]").send_keys(create_account[1])

    driver.find_element(By.XPATH, ".//button[text() = 'Войти']").click()
    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.CLASS_NAME, "BurgerIngredients_ingredients__1N8v2")))

    assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    driver.quit()
