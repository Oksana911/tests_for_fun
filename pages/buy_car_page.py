from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class Locators:
    USER_ID_BUTTON = (By.XPATH, '//*[@id="id_send"]')
    CAR_ID_BUTTON = (By.XPATH, '//*[@id="car_send"]')
    PUSH_BUTTON = (By.XPATH, '//*[@id="root"]/div/section/div/div/button[1]')


class BuyCarPage(BasePage):
    base_url = 'http://77.50.236.203:4881/#/update/users/buyCar'

    def enter_user_id(self, user_id: int):
        id_field = self.find_element(Locators.USER_ID_BUTTON)
        id_field.click()
        id_field.send_keys(user_id)
        return user_id

    def enter_car_id(self, car_id: int):
        car_id_field = self.find_element(Locators.CAR_ID_BUTTON)
        car_id_field.click()
        car_id_field.send_keys(car_id)
        return car_id

    def click_on_the_push_button(self):
        return self.find_element(Locators.PUSH_BUTTON).click()
