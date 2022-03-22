from .pages.search_page import SearchPage
import pytest


@pytest.mark.saniti
def test_search(browser):
    link = "https://xn--b1aew.xn--p1ai"
    page = SearchPage(browser, link)
    page.open()
    page.open_search_field()
    page.fill_search_field()
    page.should_be_articles_in_search_result()
    page.should_be_files_in_search_result()
