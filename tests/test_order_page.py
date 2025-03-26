import pytest
import allure

import time

from src.config import Config
from pages.home_page import HomePageScooter
from pages.order_page import OrderPageScooter
from src.data import Data


class TestOrderPageScooter:

    @allure.title('Позитивная проверка заказа самоката с двумя наборами тестовых данных и кликов на лого "Самокат" и '
                  '"Яндекс"')
    @allure.description('1. Проверяем, что после корректного заполнения полей в форме заказа на двух экранах "Для кого '
                        'самокат" и "Про аренду", клика на кнопку "Заказать" и подтверждения заказа появляется '
                        'всплывающее окно об успешном создании заказа'
                        f'2. Проверяем переход на {Config.URL} после клика на логотип "Самокат" в хедере страницы'
                        f'3. Проверяем открытие через редирект {Config.URL_DZEN} после клика на логотип Яндекса в '
                        f'хедере страницы')
    @pytest.mark.parametrize('order', [Data.ORDER_1, Data.ORDER_2])
    def test_positive_order_creation_and_click_on_logos_true(self, order, driver):
        home_page = HomePageScooter(driver)
        home_page.wait_for_load_home_page()
        home_page.accept_cookies()
        with allure.step(order.get('allure_step')):
            home_page.scroll_and_click_on_button_order(order.get('order_button'))
        order_page = OrderPageScooter(driver)
        order_page.wait_for_load_order_form_1()
        name = order.get('name')
        surname = order.get('surname')
        address = order.get('address')
        metro_station = order.get('metro_station')
        phone = order.get('phone')
        date = order.get('date')
        rental_period = order.get('rental_period')
        color = order.get('color')
        comment = order.get('comment')
        order_page.order(name, surname, address, metro_station, phone, date, rental_period, color, comment)
        order_page.wait_for_order_confirmation_window()
        order_page.click_on_button_yes_in_order_confirmation_window()
        successful_order_creation = order_page.wait_for_successful_order_creation_window()
        order_page.click_view_status_button()
        order_page.wait_for_order_tracking_page()
        home_page_scooter_url = order_page.transition_by_clicking_logo_scooter()
        home_page_dzen_url = order_page.redirect_by_clicking_logo_yandex()
        order_page.close_tab_and_return_to_previous_tab()
        assert (home_page_scooter_url == Config.URL and home_page_dzen_url == Config.URL_DZEN and
                successful_order_creation)
