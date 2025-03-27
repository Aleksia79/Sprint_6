from allure import step

from selenium.common import TimeoutException

from locators.home_page_locators import HomePageScooterLocators
from pages.base_page import BasePage


class HomePageScooter(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @step('Ожидаем загрузку главной страницы Яндекс.Самокат')
    # метод ожидания загрузки главной страницы
    def wait_for_load_home_page(self):
        self.find_element(HomePageScooterLocators.HOME_PAGE_TEXT)

    @step('Принимаем куки')
    def accept_cookies(self):
        try:
            self.find_element(HomePageScooterLocators.BUTTON_COOKIE_OK, 1)
        except TimeoutException:
            pass
        else:
            self.click_element(HomePageScooterLocators.BUTTON_COOKIE_OK)
        finally:
            self.wait_for_element_invisible(HomePageScooterLocators.BUTTON_COOKIE_OK)

    @step('Скроллим до раздела "Вопросы о важном"')
    # скролл до раздела "Вопросы о важном"
    def scroll(self):
        self.scroll_to_element(HomePageScooterLocators.QUESTIONS_SECTION)

    @step('Ожидаем загрузку главной страницы Самокаты, принимаем куки и скроллим до раздела "Вопросы о важном"')
    # ожидаем загрузку главной страницы, принимаем куки и скроллим до раздела "Вопросы о важном"
    def wait_for_load_home_page_accept_cookies_and_scroll(self):
        self.wait_for_load_home_page()
        self.accept_cookies()
        self.scroll()

    @step('Кликаем на вопрос в разделе "Вопросы о важном"')
    # клик на вопрос в разделе "Вопросы о важном" (для параметризации)
    def click_question_in_questions_section_all_purpose(self, question):
        self.click_element(question)

    @step('Получаем текст ответа на вопрос')
    # метод для получения соответствующего ответа на каждый вопрос
    def get_answer_in_questions_section(self):
        elements = self.find_elements(HomePageScooterLocators.ANSWER)
        for item in elements:
            if item.text != '':
                return item.text

    @step('Скроллим до кнопки Заказать и кликаем на нее')
    # скролл и клик на кнопку "Заказать"
    def scroll_and_click_on_button_order(self, order_button):
        self.scroll_to_element(order_button)
        self.click_element(order_button)
