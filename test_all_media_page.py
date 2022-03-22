from mvd.pages.all_media_page import AllMediaPage
import pytest

@pytest.mark.saniti
def test_radio(browser):
    link = "https://66.xn--b1aew.xn--p1ai/all_media"
    page = AllMediaPage(browser, link)
    page.open()
    page.should_work_radio()

@pytest.mark.saniti
def test_video(browser):
    link = "https://66.xn--b1aew.xn--p1ai/all_media"
    page = AllMediaPage(browser, link)
    page.open()
    page.should_work_video()

@pytest.mark.saniti
def test_audio(browser):
    link = "https://66.xn--b1aew.xn--p1ai/all_media"
    page = AllMediaPage(browser, link)
    page.open()
    page.should_work_audio()
