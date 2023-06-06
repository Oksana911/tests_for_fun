import pytest
from selenium.webdriver import Chrome


# Инициализация webdriver
@pytest.fixture(scope='session')
def browser():
    driver = Chrome(executable_path='../chromedriver')
    # driver.implicitly_wait(10)
    yield driver
    driver.quit()
