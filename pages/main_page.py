from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Locators:
    USERS_BUTTON = (By.XPATH, '//*[@id="basic-nav-dropdown"]')
    READ_ALL_BUTTON = (By.XPATH, '//*[@id="basic-navbar-nav"]/div/div[1]/div/a[1]')


class MainPage(BasePage):
    def click_on_the_users_button(self):
        return self.find_element(Locators.USERS_BUTTON, time=100).click()

    def click_on_the_read_all_button(self):
        return self.find_element(Locators.READ_ALL_BUTTON, time=100).click()

    def get_text(self):
        return self.find_element(Locators.READ_ALL_BUTTON, time=100).text
