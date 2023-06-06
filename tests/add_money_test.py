import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import EMAIL, PASSWORD
from models import Person
from pages.add_money_page import AddMoneyPage
from pages.main_page import MainPage


def test_add_money(browser):
    """Тест добавления денег последнему созданному пользователю"""

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
    page.click_on_the_add_money_button()

    page = AddMoneyPage(browser)
    time.sleep(3)

    # получаем id последнего созданного юзера в БД:
    user_obj = Person.select().order_by(Person.id.desc()).limit(1)
    user_id = [user.id for user in user_obj]
    user_id = int(''.join(map(str, user_id)))

    user_money = [user.money for user in user_obj]
    user_money = float(''.join(map(str, user_money)))

    page.enter_user_id(user_id)
    page.enter_money(100)
    page.click_on_the_push_button()

    # для проверки наличия денег в БД:
    money_in_db = Person.get(Person.id == user_id).money
    assert money_in_db > 100
    assert money_in_db == user_money + 100
