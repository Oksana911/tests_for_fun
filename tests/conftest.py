import pytest
from selenium.webdriver import Chrome


# Инициализация webdriver
@pytest.fixture(scope='session')
def browser():
    driver = Chrome(executable_path='../chromedriver')
    yield driver
    driver.quit()
