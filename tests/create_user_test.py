import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from constants import *
from models import Person
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
    time.sleep(2)
    page.input(FIRST_NAME, LAST_NAME, AGE, MONEY)
    page.click_on_the_push_button()
    time.sleep(2)
    browser.get_screenshot_as_file('res_create.png')

    assert browser.current_url == 'http://77.50.236.203:4881/#/create/user'

    # получаем id созданного юзера из формы об успешном создании:
    new_user_id_in_web = page.find_new_id()  # -> 'New user ID: 153784'
    new_user_id = new_user_id_in_web.replace('New user ID: ', '')  # удаляем ненужные символы

    # получаем id последнего созданного юзера в БД:
    user_obj = Person.select().order_by(Person.id.desc()).limit(1)
    user_in_db = [user.id for user in user_obj]
    user_in_db = int(''.join(map(str, user_in_db)))

    assert user_in_db == new_user_id
