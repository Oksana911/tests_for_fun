from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Locators:
    FIRST_NAME = (By.XPATH, '//*[@id="first_name_send"]')
    LAST_NAME = (By.XPATH, '//*[@id="last_name_send"]')
    AGE = (By.XPATH, '//*[@id="age_send"]')
    MALE_SEX = (By.XPATH, '//*[@id="sex_send"]')
    MONEY = (By.XPATH, '//*[@id="money_send"]')
    PUSH_TO_API_BUTTON = (By.XPATH, '//*[@id="root"]/div/section/div/div/button[1]')
    NEW_USER_ID = (By.XPATH, '//*[@id="root"]/div/section/div/div/button[3]')


class CreatePage(BasePage):
    base_url = 'http://77.50.236.203:4881/#/create/user'

    def enter_first_name(self, first_name: str):
        first_name_field = self.find_element(Locators.FIRST_NAME)
        first_name_field.click()
        first_name_field.send_keys(first_name)
        return first_name

    def enter_last_name(self, last_name: str):
        last_name_field = self.find_element(Locators.LAST_NAME)
        last_name_field.click()
        last_name_field.send_keys(last_name)
        return last_name

    def enter_age(self, age: int):
        age_field = self.find_element(Locators.AGE)
        age_field.click()
        age_field.send_keys(age)
        return age

    def choose_male_sex(self):
        return self.find_element(Locators.MALE_SEX).click()

    def enter_money(self, money: int):
        money_field = self.find_element(Locators.MONEY)
        money_field.click()
        money_field.send_keys(money)
        return money

    def input(self, first_name, last_name, age, money):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_age(age)
        self.choose_male_sex()
        self.enter_money(money)

    def click_on_the_push_button(self):
        return self.find_element(Locators.PUSH_TO_API_BUTTON).click()

    def find_new_id(self):
        return self.find_element(Locators.NEW_USER_ID).text
