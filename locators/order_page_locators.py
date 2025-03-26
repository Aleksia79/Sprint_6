from selenium.webdriver.common.by import By


class OrderPageScooterLocators:

    # форма заказа "Для кого самокат"
    form_title_1 = [By.XPATH, './/div[text()="Для кого самокат"]']
    name = [By.CSS_SELECTOR, 'input[placeholder="* Имя"]']
    surname = [By.CSS_SELECTOR, 'input[placeholder="* Фамилия"]']
    address = [By.CSS_SELECTOR, ' input[placeholder="* Адрес: куда привезти заказ"]']
    metro_station = [By.CSS_SELECTOR, 'input[placeholder="* Станция метро"]']
    metro_station_choice_1 = [By.XPATH, './/div[text()="Бульвар Рокоссовского"]']
    metro_station_choice_2 = [By.XPATH, './/div[text()="Черкизовская"]']
    phone = [By.CSS_SELECTOR, 'input[placeholder="* Телефон: на него позвонит курьер"]']
    next_button = [By.XPATH, '//button[@class="Button_Button__ra12g Button_Middle__1CSJM"]']

    # форма заказа "Про аренду"
    form_title_2 = [By.XPATH, './/div[text()="Про аренду"]']
    date = [By.CSS_SELECTOR, 'input[placeholder="* Когда привезти самокат"]']
    date_choice_1 = [By.CSS_SELECTOR, '[aria-label="Choose пятница, 28-е марта 2025 г."]']
    date_choice_2 = [By.CSS_SELECTOR, '[aria-label="Choose суббота, 29-е марта 2025 г."]']
    rental_period = [By.XPATH, './/div[text()="* Срок аренды"]']
    rental_period_choice_1 = [By.XPATH, './/div[text()="сутки"]']
    rental_period_choice_2 = [By.XPATH, './/div[text()="двое суток"]']
    color = [By.XPATH, './/div[text()="Цвет самоката"]']
    color_black = [By.ID, 'black']
    color_gray = [By.ID, 'grey']
    comment = [By.CSS_SELECTOR, 'input[placeholder="Комментарий для курьера"]']
    order_button = [By.XPATH, './/div[@class="Order_Buttons__1xGrp"]/button[text()="Заказать"]']

    # окно подтверждения заказа
    message_question = [By.XPATH, './/div[text()="Хотите оформить заказ?"]']
    button_yes = [By.XPATH, './/button[text()="Да"]']

    # окно с сообщением об успешном создании заказа
    message_ok = [By.XPATH, './/div[text()="Заказ оформлен"]']
    view_status_button = [By.XPATH, './/button[text()="Посмотреть статус"]']

    # раздел "Вопросы о важном"
    questions_section = [By.XPATH, './/div[text()="Вопросы о важном"]']
