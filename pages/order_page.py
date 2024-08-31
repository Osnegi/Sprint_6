from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
import allure

class OrderPage(BasePage):

    @allure.step('Нажать верхнюю кнопку "Заказать" - вверху главной страницы')
    def click_order_top_button(self):
        self.click_element(OrderPageLocators.ORDER_TOP_BUTTON)

    @allure.step('Заполнить поля ввода на первой странице формы заказа самоката (Для кого самокат)')
    def fill_in_customer_data(self, name, surname, address, phone):
        self.wait_and_find_element(OrderPageLocators.NAME_INPUT)
        self.input_data(OrderPageLocators.NAME_INPUT, name)

        self.wait_and_find_element(OrderPageLocators.SURNAME_INPUT)
        self.input_data(OrderPageLocators.SURNAME_INPUT, surname)

        self.wait_and_find_element(OrderPageLocators.ADDRESS_INPUT)
        self.input_data(OrderPageLocators.ADDRESS_INPUT, address)

        self.wait_and_find_element(OrderPageLocators.METRO_INPUT)
        self.click_element(OrderPageLocators.METRO_INPUT)
        self.wait_and_find_element(OrderPageLocators.METRO_LIST_OPEN)
        self.click_element(OrderPageLocators.METRO_SELECT)

        self.wait_and_find_element(OrderPageLocators.PHONE_INPUT)
        self.input_data(OrderPageLocators.PHONE_INPUT, phone)

    @allure.step('Нажать кнопку "Далее"')
    def click_next_button(self):
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Заполнить поля ввода на второй странице формы заказа самоката (Про аренду)')
    def fill_in_rent_data(self, comment):
        self.wait_and_find_element(OrderPageLocators.DELIVERY_DATE_INPUT)
        self.click_element(OrderPageLocators.DELIVERY_DATE_INPUT)
        self.wait_and_find_element(OrderPageLocators.CALENDAR_INPUT)
        self.click_element(OrderPageLocators.CALENDAR_DAY_SELECT)

        self.wait_and_find_element(OrderPageLocators.RENT_TIME_OPEN)
        self.click_element(OrderPageLocators.RENT_TIME_OPEN)
        self.wait_and_find_element(OrderPageLocators.RENT_TIME_SELECT)
        self.click_element(OrderPageLocators.RENT_TIME_SELECT)

        self.click_element(OrderPageLocators.COLOR_SELECT)

        self.wait_and_find_element(OrderPageLocators.COMMENT_INPUT)
        self.input_data(OrderPageLocators.COMMENT_INPUT, comment)

        #self.click_element(OrderPageLocators.MAKE_ORDER_BUTTON)
        #self.wait_and_find_element(OrderPageLocators.ORDER_CONFIRMATION_BUTTON)
        #self.click_element(OrderPageLocators.ORDER_CONFIRMATION_BUTTON)

    @allure.step('Убедиться, что кнопка "Далее" стала кликабельной (все поля заполнены корректно) и нажать на нее')
    def wait_and_click_next_button(self):
        self.wait_and_find_element(OrderPageLocators.NEXT_BUTTON)
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Убедиться, что кнопка "Заказать" на странице "Про аренду" стала кликабельной (все поля заполнены корректно), нажать на нее')
    def wait_and_click_make_order_button(self):
        self.wait_and_find_element(OrderPageLocators.MAKE_ORDER_BUTTON)
        self.click_element(OrderPageLocators.MAKE_ORDER_BUTTON)

    @allure.step('Убедиться, что кнопка "Да" на странице "Хотите оформить заказ?" стала кликабельной, нажать на нее')
    def wait_and_click_confirm_order_button(self):
        self.wait_and_find_element(OrderPageLocators.ORDER_CONFIRMATION_BUTTON)
        self.click_element(OrderPageLocators.ORDER_CONFIRMATION_BUTTON)

    @allure.step('Получить заголовок всплываюшего окна подтверждения заказа - "Заказ оформлен")')
    def get_order_confirmation_head(self):
        return self.wait_and_find_element(OrderPageLocators.ORDER_CONFIRMATION_HEAD).text

    @allure.step('Нажать кнопку согласия на использование cookies')
    def click_accept_cookies_button(self):
        self.wait_and_find_element(OrderPageLocators.ACCEPT_COOKIES_BUTTON).click()

    @allure.step('Нажать нижнюю кнопку "Заказать" (в середине главной страницы) и получить заголовок формы заказа')
    def click_order_bottom_button(self):
        self.wait_and_find_element(OrderPageLocators.ORDER_BOTTOM_BUTTON)
        self.click_element(OrderPageLocators.ORDER_BOTTOM_BUTTON)
        return self.wait_and_find_element(OrderPageLocators.ORDER_PAGE_HEAD).text

