from selenium.webdriver.common.by import By


class HomePageScooterLocators:

    # раздел Вопросы о важном
    questions_section = [By.XPATH, './/div[text()="Вопросы о важном"]']
    question_1 = [By.ID, 'accordion__heading-0']
    question_2 = [By.ID, 'accordion__heading-1']
    question_3 = [By.ID, 'accordion__heading-2']
    question_4 = [By.ID, 'accordion__heading-3']
    question_5 = [By.ID, 'accordion__heading-4']
    question_6 = [By.ID, 'accordion__heading-5']
    question_7 = [By.ID, 'accordion__heading-6']
    question_8 = [By.ID, 'accordion__heading-7']
    answer = [By.XPATH, './/div[@class="accordion"]//..//p']

    # Кнопка "принять куки"
    button_cookie_ok = [By.ID, 'rcc-confirm-button']

    # Кнопка "Заказать" в шапке страницы
    order_button_header = [By.XPATH, './/div[@class="Header_Nav__AGCXC"]/button[text()="Заказать"]']

    # Кнопка "Заказать" внизу страницы
    order_button_down = [By.XPATH, './/div[@class="Home_FinishButton__1_cWm"]/button[text()="Заказать"]']

    # текст на главной странице для wait
    home_page_text = [By.XPATH, './/div[text()= "Привезём его прямо к вашей двери,"]']
