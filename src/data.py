from locators.order_page_locators import OrderPageScooterLocators
from locators.home_page_locators import HomePageScooterLocators


class Data:
    # набор №1 тестовых данных для заказа самоката
    ORDER_1 = {'allure_step': 'Кликаем на кнопку "Заказать" в хедере главной страницы',
               'order_button': HomePageScooterLocators.order_button_header,
               'name': 'Анна',
               'surname': 'Иванова',
               'address': 'Москва, бульвар Маршала Рокоссовского, 1',
               'metro_station': OrderPageScooterLocators.metro_station_choice_1,
               'phone': '+77777777777',
               'date': OrderPageScooterLocators.date_choice_1,
               'rental_period': OrderPageScooterLocators.rental_period_choice_1,
               'color': OrderPageScooterLocators.color_black,
               'comment': 'заранее позвонить'
               }

    # набор №2 тестовых данных для заказа самоката
    ORDER_2 = {'allure_step': 'Кликаем на кнопку "Заказать" внизу главной страницы',
               'order_button': HomePageScooterLocators.order_button_down,
               'name': 'Иван',
               'surname': 'Иванов',
               'address': 'Москва, улица Большая Черкизовская, 1',
               'metro_station': OrderPageScooterLocators.metro_station_choice_2,
               'phone': '+78888888888',
               'date': OrderPageScooterLocators.date_choice_2,
               'rental_period': OrderPageScooterLocators.rental_period_choice_2,
               'color': OrderPageScooterLocators.color_gray,
               'comment': 'номер домофона 111'
               }

    # наборы элемент_вопрос-текст_ответа в разделе "Вопросы о важном"
    FAQ_1 = {'question': HomePageScooterLocators.question_1,
             'question_text': 'Сколько это стоит? И как оплатить?',
             'answer_text': 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
             }

    FAQ_2 = {'question': HomePageScooterLocators.question_2,
             'question_text': 'Хочу сразу несколько самокатов! Так можно?',
             'answer_text': 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, '
                            'можете просто сделать несколько заказов — один за другим.'
             }

    FAQ_3 = {'question': HomePageScooterLocators.question_3,
             'question_text': 'Как рассчитывается время аренды?',
             'answer_text': 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт '
                            'времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли '
                            'самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
             }

    FAQ_4 = {'question': HomePageScooterLocators.question_4,
             'question_text': 'Можно ли заказать самокат прямо на сегодня?',
             'answer_text': 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
             }

    FAQ_5 = {'question': HomePageScooterLocators.question_5,
             'question_text': 'Можно ли продлить заказ или вернуть самокат раньше?',
             'answer_text': 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому '
                            'номеру 1010.'
             }

    FAQ_6 = {'question': HomePageScooterLocators.question_6,
             'question_text': 'Вы привозите зарядку вместе с самокатом?',
             'answer_text': 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если '
                            'будете кататься без передышек и во сне. Зарядка не понадобится.'
             }

    FAQ_7 = {'question': HomePageScooterLocators.question_7,
             'question_text': 'Можно ли отменить заказ?',
             'answer_text': 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. '
                            'Все же свои.'
             }

    FAQ_8 = {'question': HomePageScooterLocators.question_8,
             'question_text': 'Я жизу за МКАДом, привезёте?',
             'answer_text': 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
             }
