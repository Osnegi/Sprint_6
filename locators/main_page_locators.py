from selenium.webdriver.common.by import By

class MainPageLocators:

    ACCEPT_COOKIES_BUTTON = [By.XPATH, '//button[@id="rcc-confirm-button"]']
    ORDER_TOP_BUTTON = (By.XPATH, '//button[@class = "Button_Button__ra12g"]')
    ORDER_BOTTOM_BUTTON = (By.XPATH, '//button[@class = "Button_Button__ra12g Button_Middle__1CSJM"]')

    YANDEX_LOGO = (By.XPATH, '//*[@href="//yandex.ru" and contains(@class, "Header_LogoYandex")]')
    DZEN_TITLE = (By.XPATH, '//title[contains(text(), "Дзен")]')
    SAMOKAT_LOGO = (By.XPATH, '//*[contains(@class, "Header_LogoScooter")]')
    MAIN_PAGE_HEAD = (By.XPATH, '//*[contains(@class, "Home_Header") and text() = "Самокат "]')

    QUESTION_0 = (By.XPATH, '// *[ @ id = "accordion__heading-0"]')
    QUESTION_1 = (By.XPATH, '// *[ @ id = "accordion__heading-1"]')
    QUESTION_2 = (By.XPATH, '// *[ @ id = "accordion__heading-2"]')
    QUESTION_3 = (By.XPATH, '// *[ @ id = "accordion__heading-3"]')
    QUESTION_4 = (By.XPATH, '// *[ @ id = "accordion__heading-4"]')
    QUESTION_5 = (By.XPATH, '// *[ @ id = "accordion__heading-5"]')
    QUESTION_6 = (By.XPATH, '// *[ @ id = "accordion__heading-6"]')
    QUESTION_7 = (By.XPATH, '// *[ @ id = "accordion__heading-7"]')

    ANSWER_0 = (By.XPATH, '// *[ @ id = "accordion__panel-0"] / p')
    ANSWER_1 = (By.XPATH, '// *[ @ id = "accordion__panel-1"] / p')
    ANSWER_2 = (By.XPATH, '// *[ @ id = "accordion__panel-2"] / p')
    ANSWER_3 = (By.XPATH, '// *[ @ id = "accordion__panel-3"] / p')
    ANSWER_4 = (By.XPATH, '// *[ @ id = "accordion__panel-4"] / p')
    ANSWER_5 = (By.XPATH, '// *[ @ id = "accordion__panel-5"] / p')
    ANSWER_6 = (By.XPATH, '// *[ @ id = "accordion__panel-6"] / p')
    ANSWER_7 = (By.XPATH, '// *[ @ id = "accordion__panel-7"] / p')