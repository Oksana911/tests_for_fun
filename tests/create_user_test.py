from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from constants import *
from pages.create_page import CreatePage
from pages.main_page import MainPage


def test_create_user(browser):
    """Тест создания нового пользователя"""
    page = MainPage(browser)
    page.go_to_site()
    assert browser.title == 'PFLB Test-API'

    page.login(EMAIL, PASSWORD)

    # подтверждаем всплывающее окно:
    WebDriverWait(browser, 3).until(EC.alert_is_present(),
                                    'Timed out waiting for PA creation ' +
                                    'confirmation popup to appear.')
    alert = browser.switch_to.alert
    assert alert.text == 'Successful authorization'
    alert.accept()
    ###
    page.click_on_the_users_button()
    page.click_on_the_create_button()

    page = CreatePage(browser)
    page.input(FIRST_NAME, LAST_NAME, AGE, MONEY)
    page.click_on_the_push_button()

    browser.get_screenshot_as_file('res_create.png')

    assert browser.current_url == 'http://77.50.236.203:4881/#/create/user'

    #  TODO:
    # assert '//*[@id="root"]/div/section/div/div/button[3]' - New user ID:000000
