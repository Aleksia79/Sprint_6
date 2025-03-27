from allure import title, step
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

    @title(f'Проверка соответствующего выпадающего текста при клике на каждый вопрос в разделе "Разговоры о '
           f'важном" на {Config.URL}')
    # проверка соответствующего выпадающего текста при клике на вопрос в разделе "Разговоры о важном"
    @pytest.mark.parametrize('questions_section', faq)
    def test_check_faq(self, questions_section, driver):
        home_page = HomePageScooter(driver)
        home_page.wait_for_load_home_page_accept_cookies_and_scroll()
        home_page.click_question_in_questions_section_all_purpose(questions_section['question'])
        answer = home_page.get_answer_in_questions_section()
        with step(f'Проверяем, что текст ответа после клика на вопрос '
                  f'"{questions_section['question_text']}": "{questions_section['answer_text']}" '):
            assert answer == questions_section['answer_text']
