import allure
import pytest

from selenium import webdriver
from src.config import Config


# фикстура для создания драйвера на Firefox
@pytest.fixture(scope='class')
@allure.title(f'Запускаем браузер Firefox, открываем {Config.URL}')
def driver():
    firefox = webdriver.Firefox()
    firefox.get(Config.URL)
    yield firefox
    firefox.quit()
