from selenium.webdriver.common.by import By

class OrderPageLocators:

    ORDER_PAGE_HEAD = [By.XPATH, './/*[text() = "Для кого самокат"]']  #Первая страница формы оформления заказа для ввода данных клиента

    NAME_INPUT = [By.XPATH, './/input[@placeholder = "* Имя"]']
    SURNAME_INPUT = [By.XPATH, '//input[@placeholder = "* Фамилия"]']
    ADDRESS_INPUT = [By.XPATH, '//input[@placeholder = "* Адрес: куда привезти заказ"]']

    METRO_INPUT = [By.XPATH, '//input[@class = "select-search__input"]']
    METRO_LIST_OPEN = [By.XPATH, '//div[@class = "select-search__select"]']
    METRO_SELECT = [By.XPATH, '//button[@value = "15"]']

    PHONE_INPUT = [By.XPATH, '//input[@placeholder = "* Телефон: на него позвонит курьер"]']

    NEXT_BUTTON = [By.XPATH, '//button[text() = "Далее"]'] #Переход на вторую страницу формы оформления заказа для ввода данных об аренде самоката

    RENT_PAGE_HEAD = [By.XPATH, '//*[text() = "Про аренду")]']  #Вторая страница формы оформления заказа для ввода данных об аренде самоката

    DELIVERY_DATE_INPUT = [By.XPATH, '//input[@placeholder = "* Когда привезти самокат"]']
    CALENDAR_INPUT = [By.XPATH, '//*[@class = "react-datepicker-popper"]']
    CALENDAR_DAY_SELECT = [By.XPATH, '//*[contains(@class, "day--012")]']

    RENT_TIME_OPEN = [By.XPATH, '//*[text() = "* Срок аренды"]']
    RENT_TIME_SELECT = [By.XPATH, '//*[text()= "трое суток"]']

    COLOR_SELECT = [By.XPATH, '//input[@id = "black"]']
    COMMENT_INPUT = [By.XPATH, '//input[@placeholder = "Комментарий для курьера"]']

    MAKE_ORDER_BUTTON = [By.XPATH, '//*[contains(@class, "Order_Buttons")]/button[text() = "Заказать"]']
    ORDER_CONFIRMATION_BUTTON = [By.XPATH, '//button[text() = "Да"]']
    ORDER_CONFIRMATION_HEAD = [By.XPATH, '//*[contains(text(), "Заказ оформлен")]']

    ACCEPT_COOKIES_BUTTON = [By.XPATH, '//button[@id="rcc-confirm-button"]']
    ORDER_TOP_BUTTON = (By.XPATH, '//button[@class = "Button_Button__ra12g"]')
    ORDER_BOTTOM_BUTTON = (By.XPATH, '//button[@class = "Button_Button__ra12g Button_Middle__1CSJM"]')