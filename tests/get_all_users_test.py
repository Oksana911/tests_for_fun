import pytest
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

    browser.get_screenshot_as_file('result.png')  # TODO

    db_cursor.execute("SELECT * FROM person LIMIT 1")
    first_user_in_db = db_cursor.fetchall()  # [(4, 25, 'Peter', Decimal('26061.00'), 'Form', True, 1)]
    first_user_in_web_str = browser.find_element(By.XPATH,
                                                 '//*[@id="root"]/div/section/div/table/tbody/tr[1]').text  # '4 Peter Form 25 MALE 26061'

    # convert string to tuple
    first_user_in_web_tuple = tuple(map(str, first_user_in_web_str.split(', ')))

    assert first_user_in_db == first_user_in_web_tuple
