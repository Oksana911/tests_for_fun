import time
from peewee import fn
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import EMAIL, PASSWORD
from models import Person, Car
from pages.buy_car_page import BuyCarPage
from pages.main_page import MainPage


def test_buy_car(browser):
    """
    Тест покупки машины пользователю с достаточным количеством денег, предварительно найденному в БД
    """
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

    # выбираем рандомное свободное (ничье)  авто из БД:
    car_obj = Car.select().where(Car.person_id is None).order_by(fn.Random()).limit(1).dicts()

    # получаем id и стоимость авто в инт:
    for car in car_obj:
        car_id = car['id']
        car_price = car['price']

        # выбираем id пользователя из БД с достаточным количеством денег:
        user = Person.select().where(Person.money > car_price).limit(1)
        user_id = [user.id for user in user]
        user_id = int(''.join(map(str, user_id)))

        # покупаем авто:
        page = BuyCarPage(browser)
        time.sleep(3)

        page.enter_user_id(user_id)
        page.enter_car_id(car_id)
        page.choose_buy()
        time.sleep(3)
        page.click_on_the_push_button()

        # проверяем добавился ли авто юзеру в БД:
        test_car = Car.get_by_id(car_id)

        assert test_car.person_id is not None
