from selenium.webdriver.common.by import By
from pages.main_page import MainPage


class Locators:
    USER_ID_BUTTON = (By.XPATH, '//*[@id="id_send"]')
    MONEY_BUTTON = (By.XPATH, '//*[@id="money_send"]')
    PUSH_BUTTON = (By.XPATH, '//*[@id="root"]/div/section/div/div/button[1]')


class AddMoneyPage(MainPage):
    base_url = 'http://77.50.236.203:4881/#/update/users/plusMoney'

    def enter_user_id(self, user_id: int):
        id_field = self.find_element(Locators.USER_ID_BUTTON)
        id_field.click()
        id_field.send_keys(user_id)
        return user_id

    def enter_money(self, money: int):
        money_field = self.find_element(Locators.MONEY_BUTTON)
        money_field.click()
        money_field.send_keys(money)
        return money

    def click_on_the_push_button(self):
        return self.find_element(Locators.PUSH_BUTTON).click()
