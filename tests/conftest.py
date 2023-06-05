import pytest
from peewee import PostgresqlDatabase
from selenium.webdriver import Chrome
from constants import *


# Инициализация webdriver
@pytest.fixture(scope='session')
def browser():
    driver = Chrome(executable_path='../chromedriver')
    # driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def db():
    # Подключение к базе данных
    db = PostgresqlDatabase(DB_NAME,
                            user=DB_USER,
                            password=DB_PASSWORD,
                            host=DB_HOST,
                            port=DB_PORT)
    connection = db.connection()
    return connection


@pytest.fixture(scope='session')
def db_cursor(db):
    # Курсор для выполнения операций с базой данных
    cursor = db.cursor()
    return cursor
