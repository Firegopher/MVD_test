from selenium.webdriver.common.by import By

class MainPageLocators():
    HEADER = (By.CSS_SELECTOR, ".ln-header")
    SITE_LOGO_TITLE = (By.CSS_SELECTOR, ".bn-logo-name")
    MAIN_MENU = (By.CSS_SELECTOR, "#menu-1")
    MAIN_MENU_OPENED = (By.CSS_SELECTOR, ".selected.active")
    NEWS_SECTION = (By.CSS_SELECTOR, ".ln-content.wrapper.clearfix")
    NEWSLINE = (By.CSS_SELECTOR, ".active #type-news-2")
    ALL_NEWS_LINK = (By.CSS_SELECTOR, "#type-news-2 .link-n")
    SERVICES_SECTION = (By.CSS_SELECTOR, ".bn-left-menu.b-desktop-section")
    SERVICE_LINK = (By.CSS_SELECTOR, ".bn-left-menu.b-desktop-section a:nth-child(1)")
    PUBLIC_OPINION_SECTION = (By.CSS_SELECTOR, ".bn-block-col")
    MASS_MEDIA_ABOUT_US_SECTION = (By.CSS_SELECTOR, ".bn-block.type-1.margin2.b-desktop-section.b-tablet-section")
    QUIZ_SECTION = (By.CSS_SELECTOR, ".bn-opros")
    SPEACH_SECTION = (By.CSS_SELECTOR, ".bn-block.type-3.margin2")
    STATE_AUTHORITIES_SITES_SECTION = (By.CSS_SELECTOR, ".bn-block.type-3.margin2")
    RESOURCES_SECTION = (By.CSS_SELECTOR, ".m-b2")
    FOOTER = (By.CSS_SELECTOR, ".footer")
    SITE_MAP_LINK = (By.CSS_SELECTOR, ".ln-footer")







