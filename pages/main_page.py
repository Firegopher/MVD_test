from .base_page import BasePage
from .locators import MainPageLocators

class MainPage(BasePage):
    
    def should_be_news_section(self):
        assert self.is_element_present(*MainPageLocators.NEWS_SECTION), "Отсутствует секция новостей"
        assert self.is_element_present(*MainPageLocators.NEWSLINE), "Отсутствует новостная лента"
        assert self.is_element_present(*MainPageLocators.ALL_NEWS_LINK), "Отсутствует ссылка на все новости"
        self.browser.find_element(*MainPageLocators.ALL_NEWS_LINK).click()

    def should_be_public_opinion_section(self):
        assert self.is_element_present(*MainPageLocators.PUBLIC_OPINION_SECTION), "Отсутствует секция общественного мнения"
        self.browser.find_element(*MainPageLocators.ALL_QUIZ_LINK).click()

    def should_be_mass_media_about_section(self):
        assert self.is_element_present(*MainPageLocators.MASS_MEDIA_ABOUT_US_SECTION), 'Отсутствует секция "СМИ о нас"'
        self.browser.find_element(*MainPageLocators.MASS_MEDIA_ABOUT_US_LINK).click()

    def should_be_quiz_section(self):
        assert self.is_element_present(*MainPageLocators.QUIZ_SECTION), "Отсутствует секция опросов"

    def should_be_speach_section(self):
        assert self.is_element_present(*MainPageLocators.SPEACH_SECTION), "Отсутствует секция с прямой речью"



    
        
