import time
from selenium.webdriver.common.by import By
from models import Person
from pages.main_page import MainPage


def test_get_all_users(browser):
    """Тест открытия страницы списка всех пользователей без логина"""

    page = MainPage(browser)
    page.go_to_site()
    assert browser.title == 'PFLB Test-API'

    page.click_on_the_users_button()
    page.click_on_the_read_all_button()
    time.sleep(2)
    page.click_on_the_sort_button()
    assert browser.title == 'PFLB Test-API'
    assert browser.current_url == 'http://77.50.236.203:4881/#/read/users'

    time.sleep(2)
    browser.get_screenshot_as_file('result.png')

    # получаем юзера с первой строчки таблицы на web-странице
    first_user_in_web_str = browser.find_element(By.XPATH,
                                                 '//*[@id="root"]/div/section/div/table/tbody/tr[1]').text  # '4 Peter Form 25 MALE 26061'
    first_user_in_web = first_user_in_web_str.split(' ')

    # получаем из БД первого по id юзера
    user_obj = Person.select().order_by(Person.id).limit(1).dicts()
    # перекладываем данные из словаря в список строк
    first_user_list = []
    for row in user_obj:
        first_user_list.append(str(row['id']))
        first_user_list.append(row['first_name'])
        first_user_list.append(row['second_name'])
        first_user_list.append(str(row['age']))
        first_user_list.append(str(row['sex']))
        first_user_list.append(str(row['money']))

        first_user_list = list(map(lambda x: x.replace('True', 'MALE'), first_user_list))

        assert first_user_list == first_user_in_web
