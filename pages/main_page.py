from .base_page import BasePage
from .locators import MainPageLocators
from .locators import MainMenuLocators
import time

class MainPage(BasePage):
    def should_be_header(self):
        assert self.is_element_present(*MainPageLocators.HEADER), "На странице не отображается хэдер"
        assert self.is_element_present(*MainPageLocators.SITE_LOGO_TITLE), "В хэдере не отображается заголовок сайта"

    def should_be_main_menu(self):
        self.browser.find_element(*MainPageLocators.MAIN_MENU_MVD).click()
        assert self.is_element_present(*MainMenuLocators.MAIN_MENU_OPENED), "Главное меню не открывается"
        self.browser.find_element(*MainMenuLocators.MAIN_MENU_MINISTER_LINK).click()

    def should_be_news_section(self):
        assert self.is_element_present(*MainPageLocators.NEWS_SECTION), "Отсутствует секция новостей"
        assert self.is_element_present(*MainPageLocators.NEWSLINE), "Отсутствует новостная лента"
        assert self.is_element_present(*MainPageLocators.ALL_NEWS_LINK), "Отсутствует ссылка на все новости"
        self.browser.find_element(*MainPageLocators.ALL_NEWS_LINK).click()

    def should_be_services_section(self):
        assert self.is_element_present(*MainPageLocators.SERVICES_SECTION), "Отсутствует секция сервисов"
        assert self.is_element_present(*MainPageLocators.SERVICE_LINK), "В секции сервисов отсутствуют сервисы"
        self.browser.find_element(*MainPageLocators.MAIN_MENU_SERVICES).click()
        self.browser.find_element(*MainMenuLocators.MAIN_MENU_ALL_SERVICE_LINK).click()

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

    def shoul_be_state_authorities_sites_section(self):
        assert self.is_element_present(*MainPageLocators.STATE_AUTHORITIES_SITES_SECTION), "Отсутствует секция с ссылками на сайты органов государственной власти"
        self.browser.find_element(*MainPageLocators.PRESIDENT_LINK).click()
        self.switch_to_new_window()
        assert "http://kremlin.ru/" in self.browser.current_url, "Не работает ссылка на сайт Президента"

    def should_be_resources_section(self):
        assert self.is_element_present(*MainPageLocators.RESOURCES_SECTION), "Отсутствует секция с полезными ресурсами"
        self.browser.find_element(*MainPageLocators.RESOURCE_BUTTON).click()
        assert self.is_element_present(*MainPageLocators.RESOURCE_SECTION_OPEN), "Не открывается секций полезных ресурсов"

    def should_be_footer(self):
        assert self.is_element_present(*MainPageLocators.FOOTER), "Отсутствует футер"
        self.browser.find_element(*MainPageLocators.SITE_MAP_LINK).click()
        assert self.is_element_present(*MainPageLocators.SITE_MAP_OPEN), "Не открывается карта сайта"

    
        
