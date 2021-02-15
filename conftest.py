from selenium import webdriver
import pytest


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture()
def db_connection():
    pass