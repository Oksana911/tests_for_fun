import pytest
from selenium.webdriver import Chrome


# инициализация webdriver
@pytest.fixture(scope='session')
def browser():
    driver = Chrome(executable_path='../chromedriver')
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
