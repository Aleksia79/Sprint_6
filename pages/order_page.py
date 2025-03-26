import allure

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.order_page_locators import OrderPageScooterLocators
from locators.home_page_locators import HomePageScooterLocators
from locators.order_tracking_page_locators import OrderTrackingPageScooterLocators

from src.config import Config


class OrderPageScooter:

    def __init__(self, driver):
        self.driver = driver

    @allure.step(f'ожидаем загрузку экрана заказа "Для кого самокат" на странице {Config.URL}/order')
    # метод ожидания загрузки экрана заказа "Для кого самокат"
    def wait_for_load_order_form_1(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(OrderPageScooterLocators.form_title_1))

    @allure.step(f'ожидаем загрузку экрана "Про аренду" на странице {Config.URL}/order')
    # метод ожидания загрузки экрана заказа "Про аренду"
    def wait_for_load_order_form_2(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(OrderPageScooterLocators.form_title_2))

    @allure.step('Заполняем поле "Имя"')
    # заполняем поле Имя
    def set_name(self, name):
        self.driver.find_element(*OrderPageScooterLocators.name).send_keys(name)

    @allure.step('Заполняем поле "Фамилия"')
    # заполняем поле Фамилия
    def set_surname(self, surname):
        self.driver.find_element(*OrderPageScooterLocators.surname).send_keys(surname)

    @allure.step('Заполняем поле "Адрес"')
    # заполняем поле Адрес
    def set_address(self, address):
        self.driver.find_element(*OrderPageScooterLocators.address).send_keys(address)

    @allure.step('Кликаем на поле "Станция метро" и в выпадающем списке выбираем станцию')
    # заполняем поле Метро
    def set_metro_station(self, metro_station):
        self.driver.find_element(*OrderPageScooterLocators.metro_station).click()
        self.driver.find_element(*metro_station).click()

    @allure.step('Заполняем поле "Телефон: на него позвонит курьер"')
    # заполняем поле Телефон
    def set_phone(self, phone):
        self.driver.find_element(*OrderPageScooterLocators.phone).send_keys(phone)

    @allure.step('Кликаем на кнопку "Далее"')
    # клик на кнопку "Далее" в форме "Для кого самокат"
    def click_on_next_button(self):
        self.driver.find_element(*OrderPageScooterLocators.next_button).click()

    @allure.step('Кликаем на поле "Когда привезти самокат" и в выпадающем календаре выбираем дату не ранее завтрашней')
    # заполняем поле Когда привезти самокат
    def set_date(self, date):
        self.driver.find_element(*OrderPageScooterLocators.date).click()
        self.driver.find_element(*date).click()

    @allure.step('Кликаем на поле "Срок аренды" и выбираем значение из выпадающего списка')
    # выбираем Срок аренды
    def set_rental_period(self, rental_period):
        self.driver.find_element(*OrderPageScooterLocators.rental_period).click()
        self.driver.find_element(*rental_period).click()

    @allure.step('В поле "Цвет самоката" ставим галочку в чек-боксе')
    # выбираем Цвет самоката
    def set_color(self, color):
        self.driver.find_element(*color).click()

    @allure.step('Заполняем поле "Комментарий лля курьера"')
    # заполняем поле Комментарий для курьера
    def set_comment(self, comment):
        self.driver.find_element(*OrderPageScooterLocators.comment).send_keys(comment)

    @allure.step('Кликаем на кнопку "Заказать" в форме "Про аренду"')
    # клик на кнопку "Заказать" в форме "Про аренду"
    def click_order_button(self):
        self.driver.find_element(*OrderPageScooterLocators.order_button).click()

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

    @allure.step('Ожидаем всплывающее окно с текстом "Хотите оформить заказ"')
    # ожидание всплывающего окна для подтверждения заказа
    def wait_for_order_confirmation_window(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(OrderPageScooterLocators.message_question))

    @allure.step('Кликаем на кнопку "Да" во всплывающем окне с вопросом о подтверждении заказа"')
    # клик на кнопку "Да" для подтверждения заказа
    def click_on_button_yes_in_order_confirmation_window(self):
        self.driver.find_element(*OrderPageScooterLocators.button_yes).click()

    @allure.step('Ожидаем всплывающее окно с сообщением об успешном создании заказа')
    # ожидание всплывающего окна с сообщением об успешном создании заказа
    def wait_for_successful_order_creation_window(self):
        wait = WebDriverWait(self.driver, 5)
        try:
            wait.until(EC.visibility_of_element_located(OrderPageScooterLocators.message_ok))
            return True
        except TimeoutException:
            return False

    @allure.step('Кликаем на кнопку "Посмотреть статус" во всплывающем окне с сообщением об успешном создании заказа')
    # клик на кнопку "Посмотреть статус"
    def click_view_status_button(self):
        self.driver.find_element(*OrderPageScooterLocators.view_status_button).click()

    @allure.step('Ожидаем загрузку страницы отслеживания заказа')
    # ожидание загрузки страницы отслеживания заказа
    def wait_for_order_tracking_page(self):
        WebDriverWait(self.driver, 5).until(
            EC.visibility_of_element_located(OrderTrackingPageScooterLocators.order_cancel_button))

    @allure.step(f'Кликаем на логотип Самокат в хедере страницы и ожидаем перехода на {Config.URL}')
    # переход на главную страницу по клику на логотип Самокат
    def transition_by_clicking_logo_scooter(self):
        self.driver.find_element(*OrderTrackingPageScooterLocators.logo_scooter).click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(HomePageScooterLocators.home_page_text))
        return self.driver.current_url

    @allure.step(f'Кликаем на логотип Яндекс в хедере страницы и ожидаем открытия через ридирект {Config.URL_DZEN}')
    # переход через редирект в новое окно с главной страницей Дзена по клику на логотип Яндекс
    def redirect_by_clicking_logo_yandex(self):
        self.driver.find_element(*OrderTrackingPageScooterLocators.logo_Yandex).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(OrderTrackingPageScooterLocators.logo_dzen))
        current_url = self.driver.current_url
        return current_url

    @allure.step('Закрываем текущую вкладку и возвращаемся на предыдущую вкладку')
    # закрытие текущей вкладки и возврат на предыдущую вкладку
    def close_tab_and_return_to_previous_tab(self):
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])
