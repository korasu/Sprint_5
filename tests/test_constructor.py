from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_constructor_stay_at_rolls():
    driver = webdriver.Chrome()

    driver.get("https://stellarburgers.nomoreparties.site")

    driver.find_element(By.XPATH, ".//span[text() = 'Соусы']").click()
    driver.find_element(By.XPATH, ".//span[text() = 'Булки']").click()

    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//span[text() = "
                                                                                          "'Булки']")))

    element = driver.find_element(By.XPATH, ".//div[@style = 'display: flex;']/div[1]").get_attribute('class')

    assert 'current' in element

    driver.quit()


def test_constructor_stay_at_sauces():
    driver = webdriver.Chrome()

    driver.get("https://stellarburgers.nomoreparties.site")

    driver.find_element(By.XPATH, ".//span[text() = 'Соусы']").click()

    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//span[text() = "
                                                                                          "'Соусы']")))

    element = driver.find_element(By.XPATH, ".//div[@style = 'display: flex;']/div[2]").get_attribute('class')

    assert 'current' in element

    driver.quit()


def test_constructor_stay_at_fillings():
    driver = webdriver.Chrome()

    driver.get("https://stellarburgers.nomoreparties.site")

    driver.find_element(By.XPATH, ".//span[text() = 'Начинки']").click()

    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//span[text() = "
                                                                                          "'Начинки']")))

    element = driver.find_element(By.XPATH, ".//div[@style = 'display: flex;']/div[3]").get_attribute('class')

    assert 'current' in element

    driver.quit()
