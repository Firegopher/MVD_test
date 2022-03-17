from selenium.webdriver.common.by import By
from selenium import webdriver
import time
link = "https://66.xn--j1agbc.xn--b1aew.xn--p1ai/all_media" 
def test_services_block():
    try:
        browser = webdriver.Chrome()
        browser.implicitly_wait(1)
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, '#details-button.secondary-button.small-link').click() 
        browser.find_element(By.CSS_SELECTOR, '#proceed-link.small-link').click()
        browser.find_element(By.XPATH, '//a[@href="/press/Videoarhiv"]').click()
        browser.find_element(By.CSS_SELECTOR, '.news-inner__list li:nth-child(1) .news-inner__link').click()
        video = browser.find_element(By.CSS_SELECTOR, '.videos iframe')
        link_videoplayer = str(video.get_attribute("src"))
        browser.get(link_videoplayer)
        browser.find_element(By.CSS_SELECTOR, ".mejs-play button").click()
        browser.find_element(By.CSS_SELECTOR, ".mejs-pause button").click()
    finally:
        browser.quit()


    