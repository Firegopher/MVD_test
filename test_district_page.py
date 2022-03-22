from mvd.pages.district_page import DistrictPage
import pytest
import time

@pytest.mark.saniti
def test_district_module(browser):
    link = "https://mvd.ru/district"
    page = DistrictPage(browser, link)
    page.open()
    page.fill_the_fields_find_by_address_inset()
    page.should_be_search_results()
