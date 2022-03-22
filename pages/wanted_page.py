from .base_page import BasePage
from .locators import WantedPageLocators
from selenium.webdriver.support.ui import Select
import time

class WantedPage(BasePage):
    def fill_the_fields(self):
        self.browser.find_element(*WantedPageLocators.SURNAME_FIELD).send_keys("Мамонов")
        self.browser.find_element(*WantedPageLocators.NAME_FIELD).send_keys("Дмитрий")
        select = Select(self.browser.find_element(*WantedPageLocators.BIRTH_YEAR_FIELD))
        select.select_by_value("1981")
        self.browser.find_element(*WantedPageLocators.EMAIL_FIELD).send_keys("test@test.ru")

    def press_search_button(self):
        self.browser.find_element(*WantedPageLocators.SEARCH_BUTTON).click()

    def alert_fill_the_captha(self):
        self.browser.execute_script("alert('Заполните каптчу вручную за 40 секунд')")
        time.sleep(40)
        assert self.browser.find_element(*WantedPageLocators.CAPTCHA_FIELD).text != None, "Каптча не заполнена"

    def should_be_wanted_search_result(self):
        assert self.browser.find_element(*WantedPageLocators.WANTED_SEARCH_RESULT).text == "МАМОНОВ ДМИТРИЙ ЕВГЕНЬЕВИЧ", "Результаты поиска не соответствуют ожидаемым"
