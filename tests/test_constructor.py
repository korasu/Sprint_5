import locator
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestConstructor:
    def test_constructor_stay_at_rolls(self, driver_option):
        driver_option.get("https://stellarburgers.nomoreparties.site")

        driver_option.find_element(*locator.Locator.button_sauces).click()
        driver_option.find_element(*locator.Locator.button_buns).click()

        WebDriverWait(driver_option, 3).until(expected_conditions.element_to_be_clickable(locator.Locator.button_buns))

        assert driver_option.find_element(*locator.Locator.constructor_page_buns_proof_element).text == 'Краторная булка N-200i'

    def test_constructor_stay_at_sauces(self, driver_option):
        driver_option.get("https://stellarburgers.nomoreparties.site")

        driver_option.find_element(*locator.Locator.button_sauces).click()

        WebDriverWait(driver_option, 3).until(expected_conditions.element_to_be_clickable(locator.Locator.button_sauces))

        assert driver_option.find_element(*locator.Locator.constructor_page_sauces_proof_element).text == 'Соус с шипами Антарианского плоскоходца'

    def test_constructor_stay_at_fillings(self, driver_option):
        driver_option.get("https://stellarburgers.nomoreparties.site")

        driver_option.find_element(*locator.Locator.button_fillers).click()

        WebDriverWait(driver_option, 3).until(expected_conditions.element_to_be_clickable(locator.Locator.button_fillers))

        assert driver_option.find_element(*locator.Locator.constructor_page_fillers_proof_element).text == 'Говяжий метеорит (отбивная)'
