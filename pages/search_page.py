from .base_page import BasePage
from .locators import SearchPageLocators

class SearchPage(BasePage):
    def should_be_articles_in_search_result(self):
        assert self.is_element_present(*SearchPageLocators.SEARCH_RESULT_ARTICLE), "В результатах поиска отсутствуют статьи"
    
    def should_be_files_in_search_result(self):
        assert self.is_element_present(*SearchPageLocators.SEARCH_RESULT_FILE), "В результатах поиска отсутствуют файлы"

    
