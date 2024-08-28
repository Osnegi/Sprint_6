from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Дождаться отображение элемента на странице')
    def wait_and_find_element(self, locator) -> WebElement:
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Кликнуть на элемент на странице')
    def click_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Открыть веб-страницу в браузере')
    def open_page(self, url):
        self.driver.get(url)