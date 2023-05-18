import pytest
from pages.main_page import MainPage


def test_get_all_users(browser):
    """Тест открытия страницы списка всех пользователей без логина"""
    page = MainPage(browser)
    page.go_to_site()
    assert browser.title == 'PFLB Test-API'

    page.click_on_the_users_button()
    page.click_on_the_read_all_button()
    assert browser.title == 'PFLB Test-API'

    browser.get_screenshot_as_file('result.png')  # TODO

    assert browser.current_url == 'http://77.50.236.203:4881/#/read/users'
    # text = page.get_text()  # TODO assert полученных пользователей в БД