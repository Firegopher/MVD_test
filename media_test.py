from selenium.webdriver.common.by import By
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors') #Игнорирование ошибок сертифатов
options.add_argument('--ignore-ssl-errors') #Игнорирование ошибок SSL сертификатов
options.add_experimental_option('excludeSwitches', ['enable-logging']) #Игнорирование логов и сообщений от DevTools
link = "https://78.xn--j1agbc.xn--b1aew.xn--p1ai/all_media" 

def test_radio():
    try:
        browser = webdriver.Chrome(options=options)
        print('Проверка работы радио')
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".bir-stat").click()
        link_radio = "https://78.xn--j1agbc.xn--b1aew.xn--p1ai/all_media/radio"
        browser.get(link_radio)
        browser.find_element(By.CSS_SELECTOR, ".mejs-play").click()
        browser.find_element(By.CSS_SELECTOR, ".mejs-pause").click()
    finally:
        browser.quit()

def test_video():
    try:
        browser = webdriver.Chrome(options=options)
        browser.implicitly_wait(1)
        print('Проверка воспроизведения видео')
        browser.get(link)
        browser.find_element(By.XPATH, '//a[@href="/Videoarhiv"]').click()
        browser.find_element(By.CSS_SELECTOR, '.news-inner__list li:nth-child(1) .news-inner__link').click()
        video = browser.find_element(By.CSS_SELECTOR, '.videos iframe')
        link_videoplayer = str(video.get_attribute("src"))
        browser.get(link_videoplayer)
        browser.find_element(By.CSS_SELECTOR, ".mejs-play button").click()
        browser.find_element(By.CSS_SELECTOR, ".mejs-pause button").click()
    finally:
        browser.quit()

