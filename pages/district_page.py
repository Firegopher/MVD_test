from .base_page import BasePage
from .locators import DistrictPageLocators
from selenium.webdriver.support.ui import Select

class DistrictPage(BasePage):
    def fill_the_fields_find_by_address_inset(self):
        self.browser.find_element(*DistrictPageLocators.FIND_BY_ADDRESS_INSET).click()
        subject_rf = Select(self.browser.find_element(*DistrictPageLocators.SUBJECT_RF))
        subject_rf.select_by_value("7700000000000")
        street = Select(self.browser.find_element(*DistrictPageLocators.STREET))
        street.select_by_value("77000000000024100")
        self.browser.find_element(*DistrictPageLocators.SEARCH_BUTTON).click()

    def should_be_search_results(self):
        assert "Москва" in self.browser.find_element(*DistrictPageLocators.SEARCH_RESULT).text, "Город в результатах поиска не соответствует ожидаемому"
        assert "Авиамоторная" in self.browser.find_element(*DistrictPageLocators.SEARCH_RESULT).text, "Улица в результатах поиска не соответствует ожидаемой"