from selenium.webdriver.common.by import By


class HomePageScooterLocators:

    # раздел Вопросы о важном
    QUESTIONS_SECTION = [By.XPATH, './/div[text()="Вопросы о важном"]']
    QUESTION_1 = [By.ID, 'accordion__heading-0']
    QUESTION_2 = [By.ID, 'accordion__heading-1']
    QUESTION_3 = [By.ID, 'accordion__heading-2']
    QUESTION_4 = [By.ID, 'accordion__heading-3']
    QUESTION_5 = [By.ID, 'accordion__heading-4']
    QUESTION_6 = [By.ID, 'accordion__heading-5']
    QUESTION_7 = [By.ID, 'accordion__heading-6']
    QUESTION_8 = [By.ID, 'accordion__heading-7']
    ANSWER = [By.XPATH, './/div[@class="accordion"]//..//p']

    # Кнопка "принять куки"
    BUTTON_COOKIE_OK = [By.ID, 'rcc-confirm-button']

    # Кнопка "Заказать" в шапке страницы
    ORDER_BUTTON_HEADER = [By.XPATH, './/div[@class="Header_Nav__AGCXC"]/button[text()="Заказать"]']

    # Кнопка "Заказать" внизу страницы
    ORDER_BUTTON_DOWN = [By.XPATH, './/div[@class="Home_FinishButton__1_cWm"]/button[text()="Заказать"]']

    # текст на главной странице для wait
    HOME_PAGE_TEXT = [By.XPATH, './/div[text()= "Привезём его прямо к вашей двери,"]']
