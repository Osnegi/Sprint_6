from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    def get_answer(self, answer_locator):
        answer = self.wait_and_find_element(*answer_locator)
        return answer.text

    @allure.step('Получить текст ответа из вопроса о важном')
    def get_answer(self, question_locator, answer_locator):
        self.click_element(question_locator)
        self.wait_and_find_element(answer_locator)
        return self.get_answer(answer_locator)

