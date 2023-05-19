from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class Locators:
    USERS_BUTTON = (By.XPATH, '//*[@id="basic-nav-dropdown"]')
    READ_ALL_BUTTON = (By.XPATH, '//*[@id="basic-navbar-nav"]/div/div[1]/div/a[1]')

    EMAIL = (By.NAME, 'email')
    PASSWORD = (By.NAME, 'password')
    GO_BUTTON = (By.XPATH, '//*[@id="root"]/div/section/div/div/div/div/div/button[1]')

    CREATE_NEW_BUTTON = (By.XPATH, '//*[@id="basic-navbar-nav"]/div/div[1]/div/a[3]')
    ADD_MONEY_BUTTON = (By.XPATH, '//*[@id="basic-navbar-nav"]/div/div[1]/div/a[4]')
    BUY_CAR_BUTTON = (By.XPATH, '//*[@id="basic-navbar-nav"]/div/div[1]/div/a[5]')


class MainPage(BasePage):
    def click_on_the_users_button(self):
        return self.find_element(Locators.USERS_BUTTON).click()

    def click_on_the_read_all_button(self):
        return self.find_element(Locators.READ_ALL_BUTTON).click()

    # def get_text(self):
    #     return self.find_element(Locators.READ_ALL_BUTTON, time=100).text

    def click_on_the_create_button(self):
        return self.find_element(Locators.CREATE_NEW_BUTTON).click()

    def enter_email(self, email: str):
        email_field = self.find_element(Locators.EMAIL)
        email_field.click()
        email_field.send_keys(email)
        return email_field

    def enter_password(self, password: str):
        password_field = self.find_element(Locators.PASSWORD)
        password_field.click()
        password_field.send_keys(password)
        return password_field

    def click_on_the_go_button(self):
        return self.find_element(Locators.GO_BUTTON).click()

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_on_the_go_button()

    def click_on_the_add_money_button(self):
        return self.find_element(Locators.ADD_MONEY_BUTTON).click()

    def click_on_the_buy_car_button(self):
        return self.find_element(Locators.BUY_CAR_BUTTON).click()
