from .pages.main_page import MainPage

def test_user_can_see_header(browser):
    link = "https://xn--b1aew.xn--p1ai/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_header()

def test_user_can_see_main_menu(browser):
    link = "https://xn--b1aew.xn--p1ai/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_main_menu()

def test_user_can_see_news_section(browser):
    link = "https://xn--b1aew.xn--p1ai/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_news_section()

def 