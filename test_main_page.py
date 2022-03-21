from .pages.base_page import BasePage
from .pages.main_page import MainPage
from .pages.minister_page import MinisterPage
from .pages.news_page import NewsPage
from .pages.services_page import ServicesPage
from .pages.quiz_page import QuizPage
from .pages.media_about_page import MediaAboutPage
import pytest
import time

@pytest.mark.saniti
def test_header(browser):
    link = "https://xn--b1aew.xn--p1ai/"
    page = BasePage(browser, link)
    page.open()
    page.should_be_header()

@pytest.mark.saniti
def test_main_menu(browser):
    link = "https://xn--b1aew.xn--p1ai/"
    page = BasePage(browser, link)
    page.open()
    page.should_be_main_menu()
    page = MinisterPage(browser, browser.current_url)
    page.should_be_minister_url()

@pytest.mark.saniti
def test_news_section(browser):
    link = "https://xn--b1aew.xn--p1ai/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_news_section()
    page = NewsPage(browser, browser.current_url)
    page.should_be_news_url()

@pytest.mark.saniti
def test_services_section(browser):
    link = "https://xn--b1aew.xn--p1ai/"
    page = BasePage(browser, link)
    page.open()
    page.should_be_services_section()
    page = ServicesPage(browser, browser.current_url)
    page.should_be_services_url()

@pytest.mark.saniti
def test_public_opinion_section(browser):
    link = "https://xn--b1aew.xn--p1ai/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_public_opinion_section()
    page = QuizPage(browser, browser.current_url)
    page.should_be_quiz_url()

@pytest.mark.saniti
def test_mass_media_about_section(browser):
    link = "https://xn--b1aew.xn--p1ai/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_mass_media_about_section()
    page = MediaAboutPage(browser, browser.current_url)
    page.should_be_media_about_url()

@pytest.mark.saniti
def test_quiz_section(browser):
    link = "https://xn--b1aew.xn--p1ai/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_quiz_section()

@pytest.mark.saniti
def test_speach_section(browser):
    link = "https://xn--b1aew.xn--p1ai/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_speach_section()

@pytest.mark.saniti
@pytest.mark.xfail
def test_state_authorities_sites_section(browser):
    link = "https://xn--b1aew.xn--p1ai/"
    page = BasePage(browser, link)
    page.open()
    page.shoul_be_state_authorities_sites_section()

@pytest.mark.saniti
def test_resources_section(browser):
    link = "https://xn--b1aew.xn--p1ai/"
    page = BasePage(browser, link)
    page.open()
    page.should_be_resources_section()

@pytest.mark.saniti
def test_footer(browser):
    link = "https://xn--b1aew.xn--p1ai/"
    page = BasePage(browser, link)
    page.open()
    page.should_be_footer()