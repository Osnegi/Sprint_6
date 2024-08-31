import pytest
import allure
from data import QuestionData, Urls
from locators.main_page_locators import MainPageLocators
from pages.main_page import MainPage


class TestQuestion:

    @allure.title('Проверка соответствия текста ответа открытому вопросу')
    @allure.description('Тест проверяет, что текст ответов в разделе "Вопросы о важном" оторбражается корректно')
    @pytest.mark.parametrize('question_locator, answer_locator, expected_answer',
    [
        [MainPageLocators.QUESTION_0, MainPageLocators.ANSWER_0, QuestionData.ANSWER_0_TEXT],
        [MainPageLocators.QUESTION_1, MainPageLocators.ANSWER_1, QuestionData.ANSWER_1_TEXT],
        [MainPageLocators.QUESTION_2, MainPageLocators.ANSWER_2, QuestionData.ANSWER_2_TEXT],
        [MainPageLocators.QUESTION_3, MainPageLocators.ANSWER_3, QuestionData.ANSWER_3_TEXT],
        [MainPageLocators.QUESTION_4, MainPageLocators.ANSWER_4, QuestionData.ANSWER_4_TEXT],
        [MainPageLocators.QUESTION_5, MainPageLocators.ANSWER_5, QuestionData.ANSWER_5_TEXT],
        [MainPageLocators.QUESTION_6, MainPageLocators.ANSWER_6, QuestionData.ANSWER_6_TEXT],
        [MainPageLocators.QUESTION_7, MainPageLocators.ANSWER_7, QuestionData.ANSWER_7_TEXT]
    ])
    def test_question(self, driver, question_locator, answer_locator, expected_answer):
        page = MainPage(driver)
        page.open_page(Urls.MAIN_PAGE)
        page.click_accept_cookies_button()
        assert page.get_answer(question_locator, answer_locator) == expected_answer



