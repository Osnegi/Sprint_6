from data import Urls
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
import allure

class MainPage(BasePage):

    @allure.step('Получить текст ответа из вопроса о важном')
    def get_answer(self, question_locator, answer_locator):
        self.click_element_JS(question_locator)
        return self.wait_and_find_element(answer_locator).text

    @allure.step('Нажать кнопку согласия на использование cookies')
    def click_accept_cookies_button(self):
        self.wait_and_find_element(MainPageLocators.ACCEPT_COOKIES_BUTTON).click()

    @allure.step('Редирект на дзен')
    def yandex_logo_redirect_dzen(self):
        self.open_page(Urls.MAIN_PAGE)
        self.click_accept_cookies_button()

        self.click_element(MainPageLocators.ORDER_TOP_BUTTON)
        self.wait_and_find_element(MainPageLocators.YANDEX_LOGO)
        self.click_element(MainPageLocators.YANDEX_LOGO)
        self.switch_next_tab()

    @allure.step('Редирект на домашнюю страницу')
    def samokat_logo_redirect_main_page(self):
        self.open_page(Urls.MAIN_PAGE)
        self.click_accept_cookies_button()

        self.click_element(MainPageLocators.ORDER_TOP_BUTTON)
        self.wait_and_find_element(MainPageLocators.SAMOKAT_LOGO)
        self.click_element(MainPageLocators.SAMOKAT_LOGO)
        #self.wait_and_find_element(MainPageLocators.MAIN_PAGE_HEAD)

    @allure.step('Получить титул главной страницы Дзена')
    def get_page_title_dzen(self):
        return self.get_page_title(MainPageLocators.DZEN_TITLE)

    @allure.step('Проверить заголовок главной страницы Самоката')
    def check_main_page_head_display(self):
            return self.check_element_display(MainPageLocators.MAIN_PAGE_HEAD)

