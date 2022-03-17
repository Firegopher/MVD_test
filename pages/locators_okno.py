from selenium.webdriver.common.by import By

class MainPageLocators():
    HEADER = (By.CSS_SELECTOR, ".header")
    MENU_STATE_AUTHORITIES = (By.CSS_SELECTOR, ".web-site__button.hidden-block__anchor")
    SITE_LOGO_TITLE = (By.CSS_SELECTOR, ".top-logo__title")
    MAIN_MENU_MVD = (By.CSS_SELECTOR, "#menu-1 li.top-list__item:first-child")
    MAIN_MENU_OPEN = (By.CSS_SELECTOR, ".header__menu.open")
    INTRO_SECTION = (By.CSS_SELECTOR, ".intro")
    ALL_NEWS_LINK = (By.CSS_SELECTOR, ".top-news__all-link")
    SERVICES_SECTION = (By.CSS_SELECTOR, ".services__list")
    SERVICE_LINK = (By.CSS_SELECTOR, ".services__list .services__item:nth-child(1)")
    NEWS_SECTION = (By.CSS_SELECTOR, ".news.section")
    NEWS_CONTENT = (By.CSS_SELECTOR, ".news.section .news-list__item")
    SPEACH_SECTION = (By.CSS_SELECTOR, ".section.speach")
    SPEACH_SECTION_CONTENT = (By.CSS_SELECTOR, ".speach__content")
    SECTION_MAP = (By.CSS_SELECTOR, ".section.map")
    SECTION_MAP_REGION = (By.CSS_SELECTOR, "#map-region_78")
    SECTION_RESOURCES = (By.CSS_SELECTOR, ".section.resources")
    SECTION_RESOURCES_LINK = (By.CSS_SELECTOR, ".section.resources .resources__item:nth-child(1)")
    FOOTER = (By.CSS_SELECTOR, ".footer")
    SITE_MAP_LINK = (By.CSS_SELECTOR, ".footer .footer-menu__item:nth-child(1)")







