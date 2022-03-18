from .base_page import BasePage

class QuizPage(BasePage):
    def should_be_quiz_url(self):
        self.switch_to_new_window()
        assert "%D0%BE%D0%BF%D1%80%D0%BE%D1%81%D1%8B" in self.browser.current_url, 'В url страницы отсутствует "опросы"'