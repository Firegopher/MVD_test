from .base_page import BasePage

class NewsPage(BasePage):
    def should_be_news_url(self):
            assert "news" in self.browser.current_url, 'В url страницы отсутствует "news"'