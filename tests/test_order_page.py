import pytest
from allure import title, description, step

from src.config import Config
from pages.home_page import HomePageScooter
from pages.order_page import OrderPageScooter
from src.data import Data


class TestOrderPageScooter:

    @title('Позитивная проверка заказа самоката с двумя наборами тестовых данных и кликов на лого "Самокат" и '
           '"Яндекс"')
    @description('1. Проверяем, что после корректного заполнения полей в форме заказа на двух экранах "Для кого '
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
        with step(order['allure_step']):
            home_page.scroll_and_click_on_button_order(order['order_button'])
        order_page = OrderPageScooter(driver)
        order_page.wait_for_load_order_form_1()
        order_page.order(order['name'], order['surname'], order['address'], order['metro_station'], order['phone'],
                         order['date'], order['rental_period'], order['color'], order['comment'])
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
