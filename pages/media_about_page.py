from .base_page import BasePage

class MediaAboutPage(BasePage):
    def should_be_media_about_url(self):
            assert "media_digest" in self.browser.current_url, 'В url страницы отсутствует "media_digest"'