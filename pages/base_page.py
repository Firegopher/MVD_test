from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import MainPageLocators
from .locators import MainMenuLocators

class BasePage():
    def __init__(self, browser, url, timeout=3):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True  

    def switch_to_new_window(self):
        new_window = self.browser.window_handles[1]
        self.browser.switch_to.window(new_window)
    
    def should_be_header(self):
        assert self.is_element_present(*MainPageLocators.HEADER), "На странице не отображается хэдер"
        assert self.is_element_present(*MainPageLocators.SITE_LOGO_TITLE), "В хэдере не отображается заголовок сайта"

    def should_be_main_menu(self):
        self.browser.find_element(*MainPageLocators.MAIN_MENU_MVD).click()
        assert self.is_element_present(*MainMenuLocators.MAIN_MENU_OPENED), "Главное меню не открывается"
        self.browser.find_element(*MainMenuLocators.MAIN_MENU_MINISTER_LINK).click()

    def should_be_services_section(self):
        assert self.is_element_present(*MainPageLocators.SERVICES_SECTION), "Отсутствует секция сервисов"
        assert self.is_element_present(*MainPageLocators.SERVICE_LINK), "В секции сервисов отсутствуют сервисы"
        self.browser.find_element(*MainPageLocators.MAIN_MENU_SERVICES).click()
        self.browser.find_element(*MainMenuLocators.MAIN_MENU_ALL_SERVICE_LINK).click()

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

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False