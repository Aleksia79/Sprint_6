from allure import step

from selenium.common.exceptions import TimeoutException

from locators.order_page_locators import OrderPageScooterLocators
from locators.home_page_locators import HomePageScooterLocators
from locators.order_tracking_page_locators import OrderTrackingPageScooterLocators
from pages.base_page import BasePage

from src.config import Config


class OrderPageScooter(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @step(f'ожидаем загрузку экрана заказа "Для кого самокат" на странице {Config.URL}/order')
    # метод ожидания загрузки экрана заказа "Для кого самокат"
    def wait_for_load_order_form_1(self):
        self.wait_for_element_visible(OrderPageScooterLocators.FORM_TITLE_1)

    @step(f'ожидаем загрузку экрана "Про аренду" на странице {Config.URL}/order')
    # метод ожидания загрузки экрана заказа "Про аренду"
    def wait_for_load_order_form_2(self):
        self.wait_for_element_visible(OrderPageScooterLocators.FORM_TITLE_2)

    @step('Заполняем поле "Имя"')
    # заполняем поле Имя
    def set_name(self, name):
        self.enter_text(OrderPageScooterLocators.NAME, name)

    @step('Заполняем поле "Фамилия"')
    # заполняем поле Фамилия
    def set_surname(self, surname):
        self.enter_text(OrderPageScooterLocators.SURNAME, surname)

    @step('Заполняем поле "Адрес"')
    # заполняем поле Адрес
    def set_address(self, address):
        self.enter_text(OrderPageScooterLocators.ADDRESS, address)

    @step('Кликаем на поле "Станция метро" и в выпадающем списке выбираем станцию')
    # заполняем поле Метро
    def set_metro_station(self, metro_station):
        self.click_element(OrderPageScooterLocators.METRO_STATION)
        self.click_element(metro_station)

    @step('Заполняем поле "Телефон: на него позвонит курьер"')
    # заполняем поле Телефон
    def set_phone(self, phone):
        self.enter_text(OrderPageScooterLocators.PHONE, phone)

    @step('Кликаем на кнопку "Далее"')
    # клик на кнопку "Далее" в форме "Для кого самокат"
    def click_on_next_button(self):
        self.click_element(OrderPageScooterLocators.NEXT_BUTTON)

    @step('Кликаем на поле "Когда привезти самокат" и в выпадающем календаре выбираем дату не ранее завтрашней')
    # заполняем поле Когда привезти самокат
    def set_date(self, date):
        self.click_element(OrderPageScooterLocators.DATE)
        self.click_element(date)

    @step('Кликаем на поле "Срок аренды" и выбираем значение из выпадающего списка')
    # выбираем Срок аренды
    def set_rental_period(self, rental_period):
        self.click_element(OrderPageScooterLocators.RENTAL_PERIOD)
        self.click_element(rental_period)

    @step('В поле "Цвет самоката" ставим галочку в чек-боксе')
    # выбираем Цвет самоката
    def set_color(self, color):
        self.click_element(color)

    @step('Заполняем поле "Комментарий лля курьера"')
    # заполняем поле Комментарий для курьера
    def set_comment(self, comment):
        self.enter_text(OrderPageScooterLocators.COMMENT, comment)

    @step('Кликаем на кнопку "Заказать" в форме "Про аренду"')
    # клик на кнопку "Заказать" в форме "Про аренду"
    def click_order_button(self):
        self.click_element(OrderPageScooterLocators.ORDER_BUTTON)

    # метод оформления заказа в двух экранах "Для кого самокат" и "Про аренду"
    def order(self, name, surname, address, metro_station, phone, date, rental_period, color, comment):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_metro_station(metro_station)
        self.set_phone(phone)
        self.click_on_next_button()
        self.wait_for_load_order_form_2()
        self.set_date(date)
        self.set_rental_period(rental_period)
        self.set_color(color)
        self.set_comment(comment)
        self.click_order_button()

    @step('Ожидаем всплывающее окно с текстом "Хотите оформить заказ"')
    # ожидание всплывающего окна для подтверждения заказа
    def wait_for_order_confirmation_window(self):
        self.wait_for_element_visible(OrderPageScooterLocators.MESSAGE_QUESTION)

    @step('Кликаем на кнопку "Да" во всплывающем окне с вопросом о подтверждении заказа"')
    # клик на кнопку "Да" для подтверждения заказа
    def click_on_button_yes_in_order_confirmation_window(self):
        self.click_element(OrderPageScooterLocators.BUTTON_YES)

    @step('Ожидаем всплывающее окно с сообщением об успешном создании заказа')
    # ожидание всплывающего окна с сообщением об успешном создании заказа
    def wait_for_successful_order_creation_window(self):
        try:
            self.wait_for_element_visible(OrderPageScooterLocators.MESSAGE_OK)
            return True
        except TimeoutException:
            return False

    @step('Кликаем на кнопку "Посмотреть статус" во всплывающем окне с сообщением об успешном создании заказа')
    # клик на кнопку "Посмотреть статус"
    def click_view_status_button(self):
        self.click_element(OrderPageScooterLocators.VIEW_STATUS_BUTTON)

    @step('Ожидаем загрузку страницы отслеживания заказа')
    # ожидание загрузки страницы отслеживания заказа
    def wait_for_order_tracking_page(self):
        self.wait_for_element_visible(OrderTrackingPageScooterLocators.ORDER_CANCEL_BUTTON)

    @step(f'Кликаем на логотип Самокат в хедере страницы и ожидаем перехода на {Config.URL}')
    # переход на главную страницу по клику на логотип Самокат
    def transition_by_clicking_logo_scooter(self):
        self.click_element(OrderTrackingPageScooterLocators.LOGO_SCOOTER)
        self.wait_for_element_visible(HomePageScooterLocators.HOME_PAGE_TEXT)
        return self.driver.current_url

    @step(f'Кликаем на логотип Яндекс в хедере страницы и ожидаем перехода через рeдирект на новую вкладку '
          f' {Config.URL_DZEN}')
    # переход через редирект в новое окно с главной страницей Дзена по клику на логотип Яндекс
    def redirect_by_clicking_logo_yandex(self):
        self.click_element(OrderTrackingPageScooterLocators.LOGO_YANDEX)
        self.transition_to_next_tab()
        self.find_element(OrderTrackingPageScooterLocators.LOGO_DZEN)
        current_url = self.driver.current_url
        return current_url

    @step('Закрываем текущую вкладку и возвращаемся на предыдущую вкладку')
    # закрытие текущей вкладки и возврат на предыдущую вкладку
    def close_tab_and_return_to_previous_tab(self):
        self.driver.close()
        self.transition_to_previous_tab()
