import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def browser(request):
    #print("\nstart browser for test..")
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging']) #Игнорирование сообщений от DevTools
    #options.add_experimental_option("prefs", {"profile.default_content_setting_values.geolocation": 1})
    browser = webdriver.Chrome(options=options)
    yield browser
    #print("\nquit browser..")
    browser.quit()