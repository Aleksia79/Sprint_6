from selenium.webdriver.common.by import By


class OrderTrackingPageScooterLocators:

    # Кнопка "Отменить заказ" для проверки перехода на страницу отслеживания заказа
    order_cancel_button = [By.XPATH, './/button[text()="Отменить заказ"]']

    # Логотип "Самокат"
    logo_scooter = [By.CLASS_NAME, 'Header_LogoScooter__3lsAR']

    # Логотип "Яндекс"
    logo_Yandex = [By.CLASS_NAME, 'Header_LogoYandex__3TSOI']

    # Логотип "Дзен" на главной странице "Дзена"
    logo_dzen = [By.ID, 'stella_logo_3464--react']
