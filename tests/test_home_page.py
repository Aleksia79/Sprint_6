import allure
import pytest

from src.data import Data
from src.config import Config
from pages.home_page import HomePageScooter


class TestHomePageScooter:
    faq = [
        Data.FAQ_1,
        Data.FAQ_2,
        Data.FAQ_3,
        Data.FAQ_4,
        Data.FAQ_5,
        Data.FAQ_6,
        Data.FAQ_7,
        Data.FAQ_8
    ]

    @allure.title(f'Проверка соответствующего выпадающего текста при клике на каждый вопрос в разделе "Разговоры о '
                  f'важном" на {Config.URL}')
    # проверка соответствующего выпадающего текста при клике на вопрос в разделе "Разговоры о важном"
    @pytest.mark.parametrize('questions_section', faq)
    def test_check_faq(self, questions_section, driver):
        home_page = HomePageScooter(driver)
        home_page.wait_for_load_home_page_and_scroll()
        home_page.click_question_in_questions_section_all_purpose(questions_section.get('question'))
        answer = home_page.get_answer_in_questions_section()
        with allure.step(f'Проверяем, что текст ответа после клика на вопрос '
                         f'"{questions_section.get('question_text')}": "{questions_section.get('answer_text')}" '):
            assert answer == questions_section.get('answer_text')

    @allure.title(f'Проверка выпадающего ответа на вопрос "Сколько это стоит? И как оплатить?" в разделе "Вопросы о '
                  f'важном" на {Config.URL}')
    @allure.description('В разделе "Вопросы о важном" проверяем, что при клике на вопрос "Сколько это стоит? И как '
                        'оплатить?" открывается текст "Сутки — 400 рублей. Оплата курьеру — наличными или картой."')
    # проверка выпадающего текста на вопрос об оплате
    def test_check_faq_payment_true(self, driver):
        home_page = HomePageScooter(driver)
        home_page.wait_for_load_home_page_and_scroll()
        home_page.click_question_about_payment()
        answer = home_page.get_answer_in_questions_section()
        assert answer == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

    @allure.title(f'Проверка выпадающего ответа на вопрос "Хочу сразу несколько самокатов! Так можно?" в разделе '
                  f'"Вопросы о важном" на {Config.URL}')
    @allure.description('В разделе "Вопросы о важном" проверяем, что при клике на вопрос "Хочу сразу несколько '
                        'самокатов! Так можно?" открывается текст "Пока что у нас так: один заказ — один самокат. '
                        'Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."')
    # проверка выпадающего текста на вопрос о количестве
    def test_check_faq_quantity_true(self, driver):
        home_page = HomePageScooter(driver)
        home_page.wait_for_load_home_page_and_scroll()
        home_page.click_question_about_quantity()
        answer = home_page.get_answer_in_questions_section()
        assert answer == ('Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, '
                          'можете просто сделать несколько заказов — один за другим.')

    @allure.title('Проверка выпадающего ответа на вопрос "Как рассчитывается время аренды?" в разделе "Вопросы о '
                  f'важном на {Config.URL}')
    @allure.description('В разделе "Вопросы о важном" проверяем, что при клике на вопрос "Как рассчитывается время '
                        'аренды?" открывается текст "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 '
                        'мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ '
                        'курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."')
    # проверка выпадающего текста на вопрос о времени аренды
    def test_check_faq_rental_time_true(self, driver):
        home_page = HomePageScooter(driver)
        home_page.wait_for_load_home_page_and_scroll()
        home_page.click_question_about_rental_time()
        answer = home_page.get_answer_in_questions_section()
        assert answer == ('Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт '
                          'времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли '
                          'самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.')

    @allure.title('Проверка выпадающего ответа на вопрос "Можно ли заказать самокат прямо на сегодня?" в разделе '
                  f'"Вопросы о важном" на {Config.URL}')
    @allure.description('В разделе "Вопросы о важном" проверяем, что при клике на вопрос "Можно ли заказать самокат '
                        'прямо на сегодня?" открывается текст "Только начиная с завтрашнего дня. Но скоро станем '
                        'расторопнее."')
    # проверка выпадающего текста на вопрос о заказе на сегодня
    def test_check_faq_ordering_today_true(self, driver):
        home_page = HomePageScooter(driver)
        home_page.wait_for_load_home_page_and_scroll()
        home_page.click_question_about_ordering_today()
        answer = home_page.get_answer_in_questions_section()
        assert answer == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

    @allure.title('Проверка выпадающего ответа на вопрос "Можно ли продлить заказ или вернуть самокат раньше?" в '
                  f'разделе "Вопросы о важном" на {Config.URL}')
    @allure.description('В разделе "Вопросы о важном" проверяем, что при клике на вопрос "Можно ли продлить заказ '
                        'или вернуть самокат раньше?" открывается текст "Пока что нет! Но если что-то срочное — '
                        'всегда можно позвонить в поддержку по красивому номеру 1010."')
    # проверка выпадающего текста на вопрос об изменении срока аренды
    def test_check_faq_changing_the_deadline_true(self, driver):
        home_page = HomePageScooter(driver)
        home_page.wait_for_load_home_page_and_scroll()
        home_page.click_question_about_changing_the_deadline()
        answer = home_page.get_answer_in_questions_section()
        assert answer == ('Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому '
                          'номеру 1010.')

    @allure.title('Проверка выпадающего ответа на вопрос "Вы привозите зарядку вместе с самокатом?" в разделе '
                  f'"Вопросы о важном" на {Config.URL}')
    @allure.description('В разделе "Вопросы о важном" проверяем, что при клике на вопрос "Вы привозите зарядку '
                        'вместе с самокатом?" открывается текст "Самокат приезжает к вам с полной зарядкой. Этого '
                        'хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не '
                        'понадобится."')
    # проверка выпадающего текста на вопрос о зарядке
    def test_check_faq_charger_true(self, driver):
        home_page = HomePageScooter(driver)
        home_page.wait_for_load_home_page_and_scroll()
        home_page.click_question_about_charger()
        answer = home_page.get_answer_in_questions_section()
        assert answer == ('Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если '
                          'будете кататься без передышек и во сне. Зарядка не понадобится.')

    @allure.title('Проверка выпадающего ответа на вопрос "Можно ли отменить заказ?" в разделе "Вопросы о важном" на '
                  f'{Config.URL}')
    @allure.description('В разделе "Вопросы о важном" проверяем, что при клике на вопрос "Можно ли отменить заказ?" '
                        'открывается текст "Да, пока самокат не привезли. Штрафа не будет, объяснительной '
                        'записки тоже не попросим. Все же свои."')
    # проверка выпадающего текста на вопрос об отмене заказа
    def test_check_faq_order_cancellation_true(self, driver):
        home_page = HomePageScooter(driver)
        home_page.wait_for_load_home_page_and_scroll()
        home_page.click_question_about_order_cancellation()
        answer = home_page.get_answer_in_questions_section()
        assert answer == ('Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. '
                          'Все же свои.')

    @allure.title('Проверка выпадающего ответа на вопрос "Я жизу за МКАДом, привезёте?" в разделе "Вопросы о важном" '
                  f'на {Config.URL}')
    @allure.description('В разделе "Вопросы о важном" проверяем, что при клике на вопрос "Я жизу за МКАДом, '
                        'привезёте?" открывается текст "Да, обязательно. Всем самокатов! И Москве, и Московской '
                        'области."')
    # проверка выпадающего текста на вопрос о доставке за МКАД --ОПЕЧАТКА В ТЕКСТЕ ВОПРОСА--
    def test_check_faq_for_moscow_region_true(self, driver):
        home_page = HomePageScooter(driver)
        home_page.wait_for_load_home_page_and_scroll()
        home_page.click_question_for_moscow_region()
        answer = home_page.get_answer_in_questions_section()
        assert answer == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
