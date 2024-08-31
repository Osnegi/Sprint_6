from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import allure

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Дождаться отображения элемента на странице и получить элемент')
    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    @allure.step('Нажать элемент на странице')
    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Нажать элемент JavaScript на странице - стрелка вниз')
    def click_element_JS(self, locator):
        self.wait_and_find_element(locator)
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Открыть веб-страницу в браузере')
    def open_page(self, url):
        self.driver.get(url)

    @allure.step('Заполнить поле ввода')
    def input_data(self, locator, data):
        element = self.wait_and_find_element(locator)
        element.send_keys(data)


    @allure.step('Получить титул страницы')
    def get_page_title(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located(locator))
        return self.driver.title

    @allure.step('Проверить наличие элемента')
    def check_element_display(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    @allure.step('Переключение на другую вкладку')
    def switch_next_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])



