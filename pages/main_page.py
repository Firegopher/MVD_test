from .base_page import BasePage
from .locators import MainPageLocators
import time

class MainPage(BasePage):
    def should_be_header(self):
        assert self.is_element_present(*MainPageLocators.HEADER), "На странице не отображается хэдер"
        assert self.is_element_present(*MainPageLocators.SITE_LOGO_TITLE), "В хэдере не отображается заголовок сайта"

    def should_be_main_menu(self):
        self.browser.find_element(*MainPageLocators.MAIN_MENU).click()
        assert self.is_element_present(*MainPageLocators.MAIN_MENU_OPENED), "Главное меню не открывается"

    def should_be_news_section(self):
        assert self.is_element_present(*MainPageLocators.NEWS_SECTION), "Отсутствует секция новостей"
        assert self.is_element_present(*MainPageLocators.NEWSLINE), "Отсутствует новостная лента"
        assert self.is_element_present(*MainPageLocators.ALL_NEWS_LINK), "Отсутствует ссылка на все новости"

    def should_be_services_section(self):
        assert self.is_element_present(*MainPageLocators.SERVICES_SECTION), "Отсутствует секция сервисов"
        assert self.is_element_present(*MainPageLocators.SERVICE_LINK), "В секции сервисов отсутствуют сервисы"

    def should_be_public_opinion_section(self):
        assert self.is_element_present(*MainPageLocators.PUBLIC_OPINION_SECTION), "Отсутствует секция общественного мнения"

    def should_be_mass_media_about_section(self):
        assert self.is_element_present(*MainPageLocators.MASS_MEDIA_ABOUT_US_SECTION), 'Отсутствует секция "СМИ о нас"'

    def should_be_quiz_section(self):
        assert self.is_element_present(*MainPageLocators.QUIZ_SECTION), "Отсутствует секция опросов"

    def should_be_speach_section(self)
