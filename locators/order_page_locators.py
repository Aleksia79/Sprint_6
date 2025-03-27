from selenium.webdriver.common.by import By


class OrderPageScooterLocators:

    # форма заказа "Для кого самокат"
    FORM_TITLE_1 = [By.XPATH, './/div[text()="Для кого самокат"]']
    NAME = [By.CSS_SELECTOR, 'input[placeholder="* Имя"]']
    SURNAME = [By.CSS_SELECTOR, 'input[placeholder="* Фамилия"]']
    ADDRESS = [By.CSS_SELECTOR, ' input[placeholder="* Адрес: куда привезти заказ"]']
    METRO_STATION = [By.CSS_SELECTOR, 'input[placeholder="* Станция метро"]']
    METRO_STATION_CHOICE_1 = [By.XPATH, './/div[text()="Бульвар Рокоссовского"]']
    METRO_STATION_CHOICE_2 = [By.XPATH, './/div[text()="Черкизовская"]']
    PHONE = [By.CSS_SELECTOR, 'input[placeholder="* Телефон: на него позвонит курьер"]']
    NEXT_BUTTON = [By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]']

    # форма заказа "Про аренду"
    FORM_TITLE_2 = [By.XPATH, './/div[text()="Про аренду"]']
    DATE = [By.CSS_SELECTOR, 'input[placeholder="* Когда привезти самокат"]']
    DATE_CHOICE_1 = [By.CSS_SELECTOR, '[aria-label="Choose пятница, 28-е марта 2025 г."]']
    DATE_CHOICE_2 = [By.CSS_SELECTOR, '[aria-label="Choose суббота, 29-е марта 2025 г."]']
    RENTAL_PERIOD = [By.XPATH, './/div[text()="* Срок аренды"]']
    RENTAL_PERIOD_CHOICE_1 = [By.XPATH, './/div[text()="сутки"]']
    RENTAL_PERIOD_CHOICE_2 = [By.XPATH, './/div[text()="двое суток"]']
    COLOR = [By.XPATH, './/div[text()="Цвет самоката"]']
    COLOR_BLACK = [By.ID, 'black']
    COLOR_GRAY = [By.ID, 'grey']
    COMMENT = [By.CSS_SELECTOR, 'input[placeholder="Комментарий для курьера"]']
    ORDER_BUTTON = [By.XPATH, './/div[@class="Order_Buttons__1xGrp"]/button[text()="Заказать"]']

    # окно подтверждения заказа
    MESSAGE_QUESTION = [By.XPATH, './/div[text()="Хотите оформить заказ?"]']
    BUTTON_YES = [By.XPATH, './/button[text()="Да"]']

    # окно с сообщением об успешном создании заказа
    MESSAGE_OK = [By.XPATH, './/div[text()="Заказ оформлен"]']
    VIEW_STATUS_BUTTON = [By.XPATH, './/button[text()="Посмотреть статус"]']

    # раздел "Вопросы о важном"
    QUESTION_SECTION = [By.XPATH, './/div[text()="Вопросы о важном"]']
