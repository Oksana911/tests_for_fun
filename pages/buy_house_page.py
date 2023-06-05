from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class Locators:
    USER_ID_BUTTON = (By.XPATH, '//*[@id="id_send"]')
    HOUSE_ID_BUTTON = (By.XPATH, '//*[@id="house_send"]')
    SETTLE_RADIO = (By.XPATH, '//*[@id="settleOrEvict"]')
    PUSH_BUTTON = (By.XPATH, '//*[@id="root"]/div/section/div/div/button[1]')


class BuyHousePage(BasePage):
    base_url = 'http://77.50.236.203:4881/#/update/houseAndUser'

    def enter_user_id(self, user_id: int):
        id_field = self.find_element(Locators.USER_ID_BUTTON)
        id_field.click()
        id_field.send_keys(user_id)
        return user_id

    def enter_house_id(self, house_id: int):
        house_id_field = self.find_element(Locators.HOUSE_ID_BUTTON)
        house_id_field.click()
        house_id_field.send_keys(house_id)
        return house_id

    def choose_settle(self):
        return self.find_element(Locators.SETTLE_RADIO).click()

    def click_on_the_push_button(self):
        return self.find_element(Locators.PUSH_BUTTON).click()
