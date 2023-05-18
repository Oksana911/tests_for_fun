import pytest
from selenium.webdriver import Chrome
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from constants import *


# Инициализация webdriver
@pytest.fixture(scope='session')
def browser():
    driver = Chrome(executable_path='../chromedriver')
    # driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def db_cursor():
    # Подключение к базе данных
    with psycopg2.connect(dbname=DB_NAME,
                          user=DB_USER,
                          password=DB_PASSWORD,
                          host=DB_HOST,
                          port=DB_PORT) as connection:
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        # Курсор для выполнения операций с базой данных
        cursor = connection.cursor()
        return cursor
