from .base_page import BasePage

class MinisterPage(BasePage):
    def should_be_minister_url(self):
            assert "%D0%BC%D0%B8%D0%BD%D0%B8%D1%81%D1%82%D1%80" in self.browser.current_url, 'В url страницы отсутствует "министр"'