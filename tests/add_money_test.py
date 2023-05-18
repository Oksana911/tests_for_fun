import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import EMAIL, PASSWORD
from pages.add_money_page import AddMoneyPage
from pages.main_page import MainPage


def test_add_money(browser, db_cursor):
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
    db_cursor.execute("SELECT MAX(id) FROM person LIMIT 1")
    id_in_db = db_cursor.fetchone()  # (111111,)
    id_in_db = int(''.join([str(value) for value in id_in_db]))

    page.enter_user_id(id_in_db)
    page.enter_money(100)

    page.click_on_the_push_button()

    # для проверки наличия денег в БД:
    db_cursor.execute("SELECT money FROM person "
                      "ORDER BY id DESC ")
    money_in_db = db_cursor.fetchone() # (112.00,)
    money_in_db = float(''.join([str(value) for value in money_in_db])) # приводим кортеж к float

    assert money_in_db > 100


