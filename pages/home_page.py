import allure

from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators.home_page_locators import HomePageScooterLocators


class HomePageScooter:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Ожидаем загрузку главной страницы Самокаты')
    # метод ожидания загрузки главной страницы
    def wait_for_load_home_page(self):
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(HomePageScooterLocators.home_page_text))

    @allure.step('Принимаем куки')
    def accept_cookies(self):
        try:
            self.driver.find_element(*HomePageScooterLocators.button_cookie_ok)
        except NoSuchElementException:
            pass
        else:
            self.driver.find_element(*HomePageScooterLocators.button_cookie_ok).click()
        finally:
            WebDriverWait(self.driver, 5).until(EC.invisibility_of_element_located(HomePageScooterLocators.button_cookie_ok))

    @allure.step('Скроллим до раздела "Вопросы о важном"')
    # скролл до раздела "Вопросы о важном"
    def scroll(self):
        questions_section = self.driver.find_element(*HomePageScooterLocators.questions_section)
        self.driver.execute_script("arguments[0].scrollIntoView();", questions_section)

    @allure.step('Ожидаем загрузку главной страницы Самокаты и скроллим до раздела "Вопросы о важном"')
    # ожидаем загрузку главной страницы и скроллим до раздела "Вопросы о важном"
    def wait_for_load_home_page_and_scroll(self):
        self.wait_for_load_home_page()
        self.scroll()

    @allure.step('Кликаем на вопрос "Сколько это стоит? И как оплатить?"')
    # клик на вопрос "Сколько это стоит? И как оплатить?"
    def click_question_about_payment(self):
        self.driver.find_element(*HomePageScooterLocators.question_1).click()

    @allure.step('Кликаем на вопрос "Хочу сразу несколько самокатов! Так можно?"')
    # клик на вопрос "Хочу сразу несколько самокатов! Так можно?"
    def click_question_about_quantity(self):
        self.driver.find_element(*HomePageScooterLocators.question_2).click()

    @allure.step('Кликаем на вопрос "Как рассчитывается время аренды?"')
    # клик на вопрос "Как рассчитывается время аренды?"
    def click_question_about_rental_time(self):
        self.driver.find_element(*HomePageScooterLocators.question_3).click()

    @allure.step('Кликаем на вопрос "Можно ли заказать самокат прямо на сегодня?"')
    # клик на вопрос "Можно ли заказать самокат прямо на сегодня?"
    def click_question_about_ordering_today(self):
        self.driver.find_element(*HomePageScooterLocators.question_4).click()

    @allure.step('Кликаем на вопрос "Можно ли продлить заказ или вернуть самокат раньше?"')
    # клик на вопрос "Можно ли продлить заказ или вернуть самокат раньше?"
    def click_question_about_changing_the_deadline(self):
        self.driver.find_element(*HomePageScooterLocators.question_5).click()

    @allure.step('Кликаем на вопрос "Вы привозите зарядку вместе с самокатом?"')
    # клик на вопрос "Вы привозите зарядку вместе с самокатом?"
    def click_question_about_charger(self):
        self.driver.find_element(*HomePageScooterLocators.question_6).click()

    @allure.step('Кликаем на вопрос "Можно ли отменить заказ?"')
    # клик на вопрос "Можно ли отменить заказ?"
    def click_question_about_order_cancellation(self):
        self.driver.find_element(*HomePageScooterLocators.question_7).click()

    @allure.step('Кликаем на вопрос "Я жизу за МКАДом, привезёте?"')
    # клик на вопрос "Я жизу за МКАДом, привезёте?"
    def click_question_for_moscow_region(self):
        self.driver.find_element(*HomePageScooterLocators.question_8).click()

    @allure.step(f'Кликаем на вопрос в разделе "Вопросы о важном"')
    # клик на вопрос в разделе "Вопросы о важном" (для параметризации)
    def click_question_in_questions_section_all_purpose(self, question):
        self.driver.find_element(*question).click()

    @allure.step('Получаем текст ответа на вопрос')
    # метод для получения соответствующего ответа на каждый вопрос
    def get_answer_in_questions_section(self):
        elements = self.driver.find_elements(*HomePageScooterLocators.answer)
        for item in elements:
            if item.text != '':
                return item.text

    @allure.step('Скроллим до кнопки Заказать и кликаем на нее')
    # скролл и клик на кнопку "Заказать"
    def scroll_and_click_on_button_order(self, order_button):
        scroll_order_button = self.driver.find_element(*order_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", scroll_order_button)
        self.driver.find_element(*order_button).click()
