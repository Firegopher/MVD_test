import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors') #Игнорирование ошибок сертифатов
options.add_argument('--ignore-ssl-errors') #Игнорирование ошибок SSL сертификатов
options.add_experimental_option('excludeSwitches', ['enable-logging']) #Игнорирование логов и сообщений от DevTools
link = "https://xn--j1agbc.xn--b1aew.xn--p1ai/" 

@pytest.fixture
def browser():
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(1)
    yield browser
    browser.quit()

def test_header():
    print('Проверка хэдера')
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, ".web-site__button.hidden-block__anchor").click()


def test_access():
    try:
        browser = webdriver.Chrome(options=options)
        expecting_title = 'МИНИСТЕРСТВО ВНУТРЕННИХ ДЕЛ'
        print("Проверка доступа к сайту")
        #browser.implicitly_wait(1)
        browser.get(link)
        actual_title = browser.find_element(By.CLASS_NAME, value="top-logo__title").text
        assert expecting_title in actual_title, "Отсутствует доступ к сайту"
    finally:
        browser.quit()

def test_main_menu():
    try:
        browser = webdriver.Chrome(options=options)
        print("Проверка главного меню")
        #browser.implicitly_wait(1)
        browser.get(link)
        browser.find_element(By.CLASS_NAME, value="top-list__link").click()
        browser.find_element(By.CSS_SELECTOR, value="#submenu > div.submenu__item.active > ul > li:nth-child(1) > a").click()
    finally:
        browser.quit()

def test_news_block():
    try:
        browser = webdriver.Chrome(options=options)
        print("Проверка новостного блока")
        #browser.implicitly_wait(1)
        browser.get(link)
        browser.find_element(By.CLASS_NAME, value="top-news__all-link").click()
    finally:
        browser.quit()

def test_services_block():
    try:
        browser = webdriver.Chrome(options=options)
        print("Проверка блока сервисов")
        #browser.implicitly_wait(1)
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "body > section.section.services > div > ul > li:nth-child(1) > a > dl").click()
    finally:
        browser.quit()

def test_map_block():
    try:
        browser = webdriver.Chrome(options=options)
        print('Проверка блока "МВД в регионах"')
        #browser.implicitly_wait(1)
        browser.get(link)
        browser.find_element(By.ID, "map-region_87").click()
    finally:
        browser.quit()

def test_resources():
    try:
        browser = webdriver.Chrome(options=options)
        print('Проверка блока полезных ресурсов')
        #browser.implicitly_wait(1)
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "body > section.section.resources > div > ul > li:nth-child(1) > a").click()
    finally:
        browser.quit()
    
def test_footer():
    try:
        browser = webdriver.Chrome(options=options)
        print('Проверка футера')
        #browser.implicitly_wait(1)
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "body > footer > div > div.footer__nav > div.footer__menu-box.footer-menu > ul > li:nth-child(1) > a").click()
    finally:
        browser.quit()

