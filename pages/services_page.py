from .base_page import BasePage

class ServicesPage(BasePage):
    def should_be_services_url(self):
            assert "%D1%81%D0%B5%D1%80%D0%B2%D0%B8%D1%81%D1%8B" in self.browser.current_url, 'В url страницы отсутствует "сервисы"'