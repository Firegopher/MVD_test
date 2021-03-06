from selenium.webdriver.common.by import By

class MainPageLocators():
    HEADER = (By.CSS_SELECTOR, ".ln-header")
    SITE_LOGO_TITLE = (By.CSS_SELECTOR, ".bn-logo-name")
    MAIN_MENU_MVD = (By.CSS_SELECTOR, "#menu-1 .selected:nth-child(1) a")
    MAIN_MENU_SERVICES = (By.CSS_SELECTOR, "#menu-1 .selected:nth-child(5) a")
    NEWS_SECTION = (By.CSS_SELECTOR, ".ln-content.wrapper.clearfix")
    NEWSLINE = (By.CSS_SELECTOR, ".active #type-news-2")
    ALL_NEWS_LINK = (By.CSS_SELECTOR, "#type-news-2 .link-n")
    SERVICES_SECTION = (By.CSS_SELECTOR, ".bn-left-menu.b-desktop-section")
    SERVICE_LINK = (By.CSS_SELECTOR, ".bn-left-menu.b-desktop-section a:nth-child(1)")
    PUBLIC_OPINION_SECTION = (By.CSS_SELECTOR, ".bn-block-col")
    ALL_QUIZ_LINK = (By.CSS_SELECTOR, ".no-auto-stripes tr:nth-child(1) a")
    MASS_MEDIA_ABOUT_US_LINK = (By.CSS_SELECTOR, ".bn-block.type-1.margin2.b-desktop-section.b-tablet-section h3")
    MASS_MEDIA_ABOUT_US_SECTION = (By.CSS_SELECTOR, ".bn-block.type-1.margin2.b-desktop-section.b-tablet-section")
    QUIZ_SECTION = (By.CSS_SELECTOR, ".bn-opros")
    SPEACH_SECTION = (By.CSS_SELECTOR, ".bn-block.type-3.margin2")
    STATE_AUTHORITIES_SITES_SECTION = (By.CSS_SELECTOR, ".bn-federal-site.wrapper")
    PRESIDENT_LINK = (By.CSS_SELECTOR, "div.bn-federal-site.wrapper .ico.i_nw:nth-child(1) a")
    RESOURCES_SECTION = (By.CSS_SELECTOR, ".m-b2")
    RESOURCE_BUTTON = (By.CSS_SELECTOR, "#button-1")
    RESOURCE_SECTION_OPEN = (By.CSS_SELECTOR, ".bs-holder2.advanced")
    FOOTER = (By.CSS_SELECTOR, ".ln-footer")
    SITE_MAP_LINK = (By.CSS_SELECTOR, "#link-2")
    SITE_MAP_OPEN = (By.CSS_SELECTOR, "#block-m")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.e-search-but.ico-but.b_sr")
    SEARCH_FIELD = (By.CSS_SELECTOR, "input[type='text']")

class MainMenuLocators():
    MAIN_MENU_OPENED = (By.CSS_SELECTOR, ".selected.active")
    MAIN_MENU_MINISTER_LINK = (By.CSS_SELECTOR, ".bm-cell.active ul li:nth-child(1) a")
    MAIN_MENU_ALL_SERVICE_LINK = (By.CSS_SELECTOR, ".bm-cell.active ul li:nth-child(1) a")

class AllMediaPageLocators():
    RADIO_PLAY_BUTTON = (By.CSS_SELECTOR, "#mep_3 .mejs-playpause-button.mejs-play button")
    RADIO_PAUSE_BUTTON = (By.CSS_SELECTOR, "#mep_3 .mejs-playpause-button.mejs-pause button")
    VIDEO_NEWS = (By.CSS_SELECTOR, ".slider2-container")
    VIDEO_WINDOW_PLAY_BUTTON = (By.CSS_SELECTOR, "#mep_0 div.mejs-overlay-button")
    VIDEO_WINDOW_STOP_BUTTON = (By.CSS_SELECTOR, ".mejs-button.mejs-playpause-button.mejs-pause")
    WINDOW_FRAME = (By.TAG_NAME, "iframe")
    AUDIO_PLAY_BUTTON = (By.CSS_SELECTOR, "#mep_0 .mejs-button.mejs-playpause-button.mejs-play")
    AUDIO_PAUSE_BUTTON = (By.CSS_SELECTOR, "#mep_0 .mejs-button.mejs-playpause-button.mejs-pause")

class RequestPageLocators():
    EXTRA_VALUE = (By.CSS_SELECTOR, ".sl-item:nth-child(25) .radio b")
    REQUEST_LIST_MVD = (By.CSS_SELECTOR, ".sl-item:nth-child(1) .radio b")
    PROCEED_BUTTON = (By.CSS_SELECTOR, "form .f-right")
    CHECKBOX = (By.CSS_SELECTOR, "label.checkbox")
    APPLY_BUTTON = (By.CSS_SELECTOR, ".f-right button.blue-button")
    REQUEST_FORM_ADDRESS_TITLE = (By.CSS_SELECTOR, ".bf-item:nth-child(1) .bf-item-title")
    REQUEST_FORM_SUBDIVISION = (By.CSS_SELECTOR, ".bf-item:nth-child(1) b")
    REQUEST_FORM_FULL_NAME_FIELD = (By.CSS_SELECTOR, "#mvd")
    REQUEST_FORM_DECLARANT_TITLE = (By.CSS_SELECTOR, ".bf-item:nth-child(2) .bf-item-title")
    REQUEST_FORM_CITIZEN_RADIOBUTTON = (By.CSS_SELECTOR, "input[value='0']")
    REQUEST_FORM_ORGANIZATION_RADIOBUTTON = (By.CSS_SELECTOR, "label input[value='1']")
    REQUEST_FORM_SURNAME_FIELD = (By.CSS_SELECTOR, "#surname_check")
    REQUEST_FORM_NAME_FIELD = (By.CSS_SELECTOR, "#firstname_check")
    REQUEST_FORM_PATRONYMIC_FIELD = (By.CSS_SELECTOR, "input[name='patronymic']")
    REQUEST_FORM_ANSWER_ADDRESS_TITLE = (By.CSS_SELECTOR, "#answer_type_check")
    REQUEST_FORM_EMAIL_ADDRESS = (By.CSS_SELECTOR, "#email_check")
    REQUEST_FORM_TELEPHONE = (By.CSS_SELECTOR, "#phone_check")
    REQUEST_FORM_LOCATION = (By.CSS_SELECTOR, ".select2.select2-container.select2-container--default")

class SearchPageLocators():
    SEARCH_RESULT_FILE = (By.XPATH, '//a[contains(@href, "Almanah_Professional")]')
    SEARCH_RESULT_ARTICLE = (By.CSS_SELECTOR, ".search_highlight")

class WantedPageLocators():
    SURNAME_FIELD = (By.CSS_SELECTOR, "input[name='s_family']")
    NAME_FIELD = (By.CSS_SELECTOR, "input[name='fio']")
    BIRTH_YEAR_FIELD = (By.CSS_SELECTOR, "select[name='d_year']")
    EMAIL_FIELD = (By.CSS_SELECTOR, "input[name='email']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.type-1.search-attention")
    CAPTCHA_FIELD = (By.CSS_SELECTOR, "input[name='captcha']")
    WANTED_SEARCH_RESULT = (By.CSS_SELECTOR, ".bs-item.clearfix .bs-item-title")

class DistrictPageLocators():
    YANDEX_MAP_GEOLOCATION_BUTTON = (By.CSS_SELECTOR, ".ymaps-2-1-79-float-button-icon.ymaps-2-1-79-float-button-icon_icon_geolocation")
    FIND_BY_ADDRESS_INSET = (By.CSS_SELECTOR, "#search-form-pill")
    SUBJECT_RF = (By.CSS_SELECTOR, "select.subject.select.select2-hidden-accessible")
    STREET = (By.CSS_SELECTOR, ".street.select.select2-hidden-accessible")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "#form-1 .blue-button.search")
    SEARCH_RESULT = (By.XPATH, '//*[@id="district_list"]/div[1]/div/div/div[2]/ul/li[3]')