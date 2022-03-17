from selenium.webdriver.common.by import By
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors') #Игнорирование ошибок сертифатов
options.add_argument('--ignore-ssl-errors') #Игнорирование ошибок SSL сертификатов
options.add_experimental_option('excludeSwitches', ['enable-logging']) #Игнорирование логов и сообщений от DevTools
link = "https://xn--j1agbc.xn--b1aew.xn--p1ai/" 

def test_subunit_list():
    try:
        browser = webdriver.Chrome(options=options)
        print("Проверка соответствия страницы")
        #browser.implicitly_wait(1)
        browser.get(link)
        browser.find_element(By.XPATH, '//section//a[@href="https://окно.мвд.рф/request_main"]').click()
        title = browser.find_element(By.CLASS_NAME, 'text-page__title').text
        element = "Список подразделений для приема обращений"
        assert str(title) == element, "Отсутствует заголовок {element}"
        subunit_1 = browser.find_element(By.XPATH, '/html/body/div[3]/div/div/form/div[1]/label/div/span').text
        assert str(subunit_1) == "Министерство внутренних дел Российской Федерации", "Отсутствует подразделение: Министерство внутренних дел Российской Федерации"
        element = ("Министерство внутренних дел Российской Федерации", "Главное управление экономической безопасности и противодействия коррупции", "Главное управление уголовного розыска", "Главное управление по противодействию экстремизму")
        subunit_3 = browser.find_element(By.XPATH, '/html/body/div[3]/div/div/form/div[3]/label/div/span').text
        assert str(subunit_3) == "Главное управление экономической безопасности и противодействия коррупции", "Отсутствует подразделение: Главное управление экономической безопасности и противодействия коррупции"
        subunit_4 = browser.find_element(By.XPATH, '/html/body/div[3]/div/div/form/div[4]/label/div/span').text
        assert str(subunit_4) == "Главное управление уголовного розыска", "Отсутствует подразделение: Главное управление уголовного розыска"
        subunit_5 = browser.find_element(By.XPATH, '/html/body/div[3]/div/div/form/div[5]/label/div/span').text
        assert str(subunit_5) == "Главное управление по противодействию экстремизму", "Отсутствует подразделение: Главное управление по противодействию экстремизму"
        subunit_6 = browser.find_element(By.XPATH, '/html/body/div[3]/div/div/form/div[6]/label/div/span').text
        assert str(subunit_6) == "Главное управление по обеспечению охраны общественного порядка и координации взаимодействия с органами исполнительной власти субъектов РФ", "Отсутствует подразделение: Главное управление по обеспечению охраны общественного порядка и координации взаимодействия с органами исполнительной власти субъектов РФ"
        subunit_7 = browser.find_element(By.XPATH, '/html/body/div[3]/div/div/form/div[7]/label/div/span').text
        assert str(subunit_7) == "Главное управление по обеспечению безопасности дорожного движения", "Отсутствует подразделение: Главное управление по обеспечению безопасности дорожного движения"
        subunit_8 = browser.find_element(By.XPATH, '/html/body/div[3]/div/div/form/div[8]/label/div/span').text
        assert str(subunit_8) == "Организационно-аналитический департамент", "Отсутствует подразделение: Организационно-аналитический департамент"
        subunit_9 = browser.find_element(By.XPATH, '/html/body/div[3]/div/div/form/div[9]/label/div/span').text
        assert str(subunit_9) == "Министерство внутренних дел Российской Федерации", "Отсутствует подразделение: Министерство внутренних дел Российской Федерации"
        subunit_10 = browser.find_element(By.XPATH, '/html/body/div[3]/div/div/form/div[10]/label/div/span').text
        assert str(subunit_10) == "Министерство внутренних дел Российской Федерации", "Отсутствует подразделение: Министерство внутренних дел Российской Федерации"
        subunit_11 = browser.find_element(By.XPATH, '/html/body/div[3]/div/div/form/div[11]/label/div/span').text
        assert str(subunit_11) == "Министерство внутренних дел Российской Федерации", "Отсутствует подразделение: Министерство внутренних дел Российской Федерации"
        subunit_12 = browser.find_element(By.XPATH, '/html/body/div[3]/div/div/form/div[12]/label/div/span').text
        assert str(subunit_12) == "Министерство внутренних дел Российской Федерации", "Отсутствует подразделение: Министерство внутренних дел Российской Федерации"
        subunit_13 = browser.find_element(By.XPATH, '/html/body/div[3]/div/div/form/div[13]/label/div/span').text
        assert str(subunit_13) == "Министерство внутренних дел Российской Федерации", "Отсутствует подразделение: Министерство внутренних дел Российской Федерации"
        subunit_14 = browser.find_element(By.XPATH, '/html/body/div[3]/div/div/form/div[14]/label/div/span').text
        assert str(subunit_14) == "Министерство внутренних дел Российской Федерации", "Отсутствует подразделение: Министерство внутренних дел Российской Федерации"
        subunit_15 = browser.find_element(By.XPATH, '/html/body/div[3]/div/div/form/div[15]/label/div/span').text
        assert str(subunit_15) == "Министерство внутренних дел Российской Федерации", "Отсутствует подразделение: Министерство внутренних дел Российской Федерации"
        subunit_16 = browser.find_element(By.XPATH, '/html/body/div[3]/div/div/form/div[16]/label/div/span').text
        assert str(subunit_16) == "Министерство внутренних дел Российской Федерации", "Отсутствует подразделение: Министерство внутренних дел Российской Федерации"
        subunit_17 = browser.find_element(By.XPATH, '/html/body/div[3]/div/div/form/div[17]/label/div/span').text
        assert str(subunit_17) == "Министерство внутренних дел Российской Федерации", "Отсутствует подразделение: Министерство внутренних дел Российской Федерации"
        subunit_18 = browser.find_element(By.XPATH, '/html/body/div[3]/div/div/form/div[18]/label/div/span').text
        assert str(subunit_18) == "Министерство внутренних дел Российской Федерации", "Отсутствует подразделение: Министерство внутренних дел Российской Федерации"
        subunit_19 = browser.find_element(By.XPATH, '/html/body/div[3]/div/div/form/div[19]/label/div/span').text
        assert str(subunit_19) == "Министерство внутренних дел Российской Федерации", "Отсутствует подразделение: Министерство внутренних дел Российской Федерации"
        subunit_20 = browser.find_element(By.XPATH, '/html/body/div[3]/div/div/form/div20]/label/div/span').text
        assert str(subunit_20) == "Министерство внутренних дел Российской Федерации", "Отсутствует подразделение: Министерство внутренних дел Российской Федерации"
        subunit_21 = browser.find_element(By.XPATH, '/html/body/div[3]/div/div/form/div[21]/label/div/span').text
        assert str(subunit_21) == "Министерство внутренних дел Российской Федерации", "Отсутствует подразделение: Министерство внутренних дел Российской Федерации"
        subunit_22 = browser.find_element(By.XPATH, '/html/body/div[3]/div/div/form/div[22]/label/div/span').text
        assert str(subunit_22) == "Министерство внутренних дел Российской Федерации", "Отсутствует подразделение: Министерство внутренних дел Российской Федерации"
        subunit_23 = browser.find_element(By.XPATH, '/html/body/div[3]/div/div/form/div[23]/label/div/span').text
        assert str(subunit_23) == "Министерство внутренних дел Российской Федерации", "Отсутствует подразделение: Министерство внутренних дел Российской Федерации"
        subunit_24 = browser.find_element(By.XPATH, '/html/body/div[3]/div/div/form/div[24]/label/div/span').text
        assert str(subunit_24) == "Министерство внутренних дел Российской Федерации", "Отсутствует подразделение: Министерство внутренних дел Российской Федерации"
    finally:
        browser.quit()