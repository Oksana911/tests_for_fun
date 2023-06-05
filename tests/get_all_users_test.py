import time
import collections
from selenium.webdriver.common.by import By
from pages.main_page import MainPage


def test_get_all_users(browser, db_cursor):
    """Тест открытия страницы списка всех пользователей без логина"""
    page = MainPage(browser)
    page.go_to_site()
    assert browser.title == 'PFLB Test-API'

    page.click_on_the_users_button()
    page.click_on_the_read_all_button()
    assert browser.title == 'PFLB Test-API'
    assert browser.current_url == 'http://77.50.236.203:4881/#/read/users'

    time.sleep(2)
    browser.get_screenshot_as_file('result.png')

    db_cursor.execute("SELECT id, first_name, second_name, age, sex"
                      " FROM person LIMIT 1")
    first_user_in_db = db_cursor.fetchone()

    first_user_in_db = [str(i) for i in first_user_in_db]
    first_user_in_db = list(map(lambda x: x.replace('True', 'MALE'), first_user_in_db))

    first_user_in_web_str = browser.find_element(By.XPATH,
                                                 '//*[@id="root"]/div/section/div/table/tbody/tr[1]').text  # '4 Peter Form 25 MALE 26061'
    first_user_in_web = first_user_in_web_str.split(' ')
    first_user_in_web.pop(-1)

    assert collections.Counter(first_user_in_db) == collections.Counter(first_user_in_web)
