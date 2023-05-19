import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import EMAIL, PASSWORD
from pages.buy_car_page import BuyCarPage
from pages.main_page import MainPage


def test_buy_car(browser, db_cursor):
    """
    Тест покупки машины пользователю с достаточным количеством денег, предварительно найденному в БД
    """

    # выбираем рандомное авто из БД:
    db_cursor.execute("SELECT id, price FROM car "
                      "ORDER BY RANDOM() "
                      "LIMIT 1")

    car = db_cursor.fetchone()  # (66, Decimal('70000.00'))

    # получаем id и стоимость авто в инт:
    car_id, car_price = car

    # выбираем id пользователя из БД с достаточным количеством денег:
    db_cursor.execute("SELECT id FROM person "
                      "WHERE money > 2138339713"  #TODO использовать car_price 
                      "LIMIT 1")
    user_id = db_cursor.fetchone()

    # получаем id пользователя в инт:
    user_id = int(''.join(map(str, user_id)))

    # логин:
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
    page.click_on_the_users_button()
    page.click_on_the_buy_car_button()

    # покупаем авто:
    page = BuyCarPage(browser)
    time.sleep(3)

    page.enter_user_id(user_id)
    page.enter_car_id(car_id)
    page.click_on_the_push_button()

    # проверяем добавился ли авто юзеру в БД:
    # assert
