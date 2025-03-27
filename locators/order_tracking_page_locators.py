from selenium.webdriver.common.by import By


class OrderTrackingPageScooterLocators:

    # Кнопка "Отменить заказ" для проверки перехода на страницу отслеживания заказа
    ORDER_CANCEL_BUTTON = [By.XPATH, './/button[text()="Отменить заказ"]']

    # Логотип "Самокат"
    LOGO_SCOOTER = [By.CLASS_NAME, 'Header_LogoScooter__3lsAR']

    # Логотип "Яндекс"
    LOGO_YANDEX = [By.CLASS_NAME, 'Header_LogoYandex__3TSOI']

    # Логотип "Дзен" на главной странице "Дзена"
    LOGO_DZEN = [By.ID, 'stella_logo_3464--react']
