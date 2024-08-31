from data import Data, OrderData, Urls
from pages.order_page import OrderPage
import allure
import pytest

class TestOrder:

    @allure.title(
        'Проверка перехода в форму оформления заказа через нижнюю кнопку "Заказать" - в середине главной страницы')
    @allure.description(
        'Нажать нижнюю кнопку "Заказать" в середине главной страницы и перейти в форму оформления заказа с заголовком "Для кого самокат"')
    def test_click_order_bottom_button(self, driver):
        page = OrderPage(driver)
        page.open_page(Urls.MAIN_PAGE)
        page.click_accept_cookies_button()

        assert page.click_order_bottom_button() == Data.ORDER_PAGE_HEAD

    @allure.title('Проверка заказа самоката через верхнюю кнопку "Заказать"(позитивный сценарий)')
    @allure.description('Проверить успешное оформление заказа самоката с двумя наборами тестовых данных через верхнюю кнопку "Заказать" (вверху главной страницы) - позитивные сценарии')
    @pytest.mark.parametrize('name, surname, address, phone, comment',
    [
        [OrderData.NAME, OrderData.SURNAME, OrderData.ADDRESS, OrderData.PHONE, OrderData.COMMENT],
        [OrderData.NAME_1, OrderData.SURNAME_1, OrderData.ADDRESS_1, OrderData.PHONE_1, OrderData.COMMENT_1]
    ])
    def test_order_page(self, driver, name, surname, address, phone, comment):

        form_order = OrderPage(driver)
        form_order.open_page(Urls.MAIN_PAGE)
        form_order.click_accept_cookies_button()
        form_order.click_order_top_button()

        form_order.fill_in_customer_data(name, surname, address, phone)
        form_order.wait_and_click_next_button()

        form_order.fill_in_rent_data(comment)
        form_order.wait_and_click_make_order_button()
        form_order.wait_and_click_confirm_order_button()

        assert Data.ORDER_CONFIRMATION_HEAD in form_order.get_order_confirmation_head()
