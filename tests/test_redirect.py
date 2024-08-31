from pages.main_page import MainPage
from data import Data
import allure

class TestLogoRedirect:

    @allure.title('По логотипу Яндекса выполнить переход (редирект) на главную страницу "ЯндексДзен" в новой вкладке ')
    @allure.step('Переход на главную страницу "ЯндексДзен" в новой вкладке')
    def test_yandex_logo_redirect_dzen(self, driver):
        page = MainPage(driver)
        page.yandex_logo_redirect_dzen()
        assert page.get_page_title_dzen() == Data.DZEN_TITLE

    @allure.title('По логотипу Самоката выполнить переход (редирект) на главную страницу "ЯндексСамокат" ')
    @allure.step('Переход на главную страницу "ЯндексСамокат" ')
    def test_samokat_logo_redirect_main_page_samokat(self, driver):
        page = MainPage(driver)
        page.samokat_logo_redirect_main_page()
        assert page.check_main_page_head_display()