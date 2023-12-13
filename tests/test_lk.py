import locator
import helpers
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLK:
    def test_open_lk_page(self, driver_option):
        driver_option = helpers.authorized(driver_option)

        driver_option.find_element(*locator.Locator.lk_in_header).click()

        WebDriverWait(driver_option, 3).until(
            expected_conditions.visibility_of_element_located(locator.Locator.link_for_setting_profile))

        assert driver_option.current_url == "https://stellarburgers.nomoreparties.site/account/profile"

    def test_switch_lk_to_construct_with_click_to_logo(self, driver_option):
        driver_option = helpers.authorized(driver_option)

        driver_option.find_element(*locator.Locator.lk_in_header).click()

        WebDriverWait(driver_option, 3).until(
            expected_conditions.visibility_of_element_located(locator.Locator.link_for_setting_profile))

        driver_option.find_element(*locator.Locator.logo_in_header).click()

        WebDriverWait(driver_option, 5).until(expected_conditions.visibility_of_element_located(
            locator.Locator.constructr_block))

        assert driver_option.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_switch_lk_to_construct_with_click_to_constructor_button(self, driver_option):
        driver_option = helpers.authorized(driver_option)

        driver_option.find_element(*locator.Locator.lk_in_header).click()

        WebDriverWait(driver_option, 3).until(
            expected_conditions.visibility_of_element_located(locator.Locator.link_for_setting_profile))

        driver_option.find_element(*locator.Locator.constructor_in_header).click()

        WebDriverWait(driver_option, 5).until(expected_conditions.visibility_of_element_located(
            locator.Locator.constructr_block))

        assert driver_option.current_url == "https://stellarburgers.nomoreparties.site/"

    def test_exit_from_lk(self, driver_option):
        driver_option = helpers.authorized(driver_option)

        driver_option.find_element(*locator.Locator.lk_in_header).click()

        WebDriverWait(driver_option, 3).until(
            expected_conditions.visibility_of_element_located(locator.Locator.link_for_setting_profile))

        driver_option.find_element(*locator.Locator.logout_button).click()

        WebDriverWait(driver_option, 3).until(expected_conditions.visibility_of_element_located(
            locator.Locator.button_login))

        assert driver_option.current_url == "https://stellarburgers.nomoreparties.site/login"
