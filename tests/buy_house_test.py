import time
from decimal import Decimal

from peewee import fn
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import EMAIL, PASSWORD
from models import House, Person
from pages.buy_house_page import BuyHousePage
from pages.main_page import MainPage


def test_buy_house(browser):
    """
    Тест покупки дома пользователю с достаточным количеством денег, предварительно найденному в БД
    """
    # логин:
    main_page = MainPage(browser)
    main_page.go_to_site()
    assert browser.title == 'PFLB Test-API'
    main_page.login(EMAIL, PASSWORD)

    # подтверждаем всплывающее окно:
    WebDriverWait(browser, 3).until(EC.alert_is_present(),
                                    'Timed out waiting for PA creation ' +
                                    'confirmation popup to appear.')
    alert = browser.switch_to.alert
    assert alert.text == 'Successful authorization'
    alert.accept()
    main_page.click_on_the_users_button()
    main_page.click_on_the_settle_to_house_button()

    # выбираем рандомный дом из БД:
    house_obj = House.select().order_by(fn.Random()).limit(1)

    # получаем id и стоимость дома в инт:
    house_id = [house.id for house in house_obj]
    house_id = int(''.join(map(str, house_id)))

    house_price = [house.price for house in house_obj]
    if house_price == [None]:
        house_price = 0
    else:
        house_price = float(''.join(map(str, house_price)))

    # выбираем из БД id пользователя без дома и с достаточным количеством денег:
    user_obj = Person.select().where((Person.money > house_price) & (Person.house_id.is_null())).limit(1)
    user_id = [user.id for user in user_obj]
    user_id = int(''.join(map(str, user_id)))
    user_money = [user.money for user in user_obj]
    user_money = float(''.join(map(str, user_money)))

    # заселяем юзера в дом:
    page = BuyHousePage(browser)
    time.sleep(2)

    page.enter_user_id(user_id)
    page.enter_house_id(house_id)
    page.choose_settle()
    page.click_on_the_push_button()
    time.sleep(5)

    # проверяем все ли ок в БД:

    test_user_house_id = Person.get(Person.id == user_id).house_id
    assert test_user_house_id == house_id

    # вычитаем потраченную сумму из денег юзера в БД и проверяем
    Person.update(Person.money - house_price).where(Person.id == user_id)
    money_befor = Decimal(user_money)
    money_after = Person.get(Person.id == user_id).money
    assert money_befor == money_after + Decimal(house_price)
