from mvd.pages.wanted_page import WantedPage
import pytest

@pytest.mark.saniti
def test_wanted_person_search(browser):
    link = "https://xn--b1aew.xn--p1ai/wanted"
    page = WantedPage(browser, link)
    page.open()
    page.fill_the_fields()
    page.alert_fill_the_captha()
    page.press_search_button()
    page.should_be_wanted_search_result()
