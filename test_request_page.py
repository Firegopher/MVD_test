from .pages.base_page import BasePage
from .pages.request_page import RequestPage
import pytest

@pytest.mark.saniti
@pytest.mark.parametrize('position,value', [(1, "Министерство внутренних дел Российской Федерации"), 
                                            (3, "Главное управление экономической безопасности и противодействия коррупции"),
                                            (4, "Главное управление уголовного розыска"),
                                            (5, "Главное управление по противодействию экстремизму"),
                                            (6, "Главное управление по обеспечению охраны общественного порядка и координации взаимодействия с органами исполнительной власти субъектов РФ"),
                                            (7, "Главное управление по обеспечению безопасности дорожного движения"),
                                            (8, "Организационно-аналитический департамент"),
                                            (9, "Главное управление на транспорте"),
                                            (10, "Договорно-правовой департамент"),
                                            (11, "Главное управление собственной безопасности"),
                                            (12, "Следственный департамент"),
                                            (13, "Департамент государственной службы и кадров"),
                                            (14, "Департамент по финансово-экономической политике и обеспечению социальных гарантий"),
                                            (15, "Департамент по материально-техническому и медицинскому обеспечению"),
                                            (16, "Оперативное управление"),
                                            (17, 'ФКУ "Главный информационно-аналитический центр"'),
                                            (18, 'ФБГУ "Экспертно-криминалистический центр"'),
                                            (19, 'ФКУ НПО «Спецтехника и Связь»'),
                                            (20, "Департамент информационных технологий, связи и защиты информации"),
                                            (21, "Управление «К» МВД России"),
                                            (22, "Главное управление по вопросам миграции"),
                                            (23, "Управление по организации дознания"),
                                            (24, "Главное управление по контролю за оборотом наркотиков") ])
def test_request_list_is_match(browser, position, value):
    link = "https://xn--b1aew.xn--p1ai/request_main"
    page = RequestPage(browser, link)
    page.open()
    page.should_match_request_list(position, value)

@pytest.mark.saniti
def test_there_is_no_extra_in_requesl_list(browser):
    link = "https://xn--b1aew.xn--p1ai/request_main"
    page = RequestPage(browser, link)
    page.open()
    page.should_not_be_extra_in_request_list()

@pytest.mark.saniti
def test_address_block__title_in_request_form(browser):
    link = "https://xn--b1aew.xn--p1ai/request_main"
    page = RequestPage(browser, link)
    page.open()
    page.go_to_request_form()
    page.should_match_address_block_title_in_request_form()

@pytest.mark.saniti
def test_subdivision_in_address_block_in_request_form(browser):
    link = "https://xn--b1aew.xn--p1ai/request_main"
    page = RequestPage(browser, link)
    page.open()
    page.go_to_request_form()
    page.should_be_subdivision_in_address_block_in_request_form()

@pytest.mark.saniti
def test_full_name_field_in_address_block_in_request_form(browser):
    link = "https://xn--b1aew.xn--p1ai/request_main"
    page = RequestPage(browser, link)
    page.open()
    page.go_to_request_form()
    page.should_be_full_name_field_in_address_block_in_request_form()

@pytest.mark.saniti
def test_declarant_block_title_in_request_form(browser):
    link = "https://xn--b1aew.xn--p1ai/request_main"
    page = RequestPage(browser, link)
    page.open()
    page.go_to_request_form()
    page.should_be_declarant_block_title_in_request_form()

@pytest.mark.saniti
def test_citizen_radiobutton_in_declarant_block_in_request_form(browser):
    link = "https://xn--b1aew.xn--p1ai/request_main"
    page = RequestPage(browser, link)
    page.open()
    page.go_to_request_form()
    page.should_be_citizen_radiobutton_in_declarant_block_in_request_form()

@pytest.mark.saniti
def test_organization_radiobutton_in_declarant_block_in_request_form(browser):
    link = "https://xn--b1aew.xn--p1ai/request_main"
    page = RequestPage(browser, link)
    page.open()
    page.go_to_request_form()
    page.should_be_organization_radiobutton_in_declarant_block_in_request_form()

@pytest.mark.saniti
def test_surname_field_in_declarant_block_in_request_form(browser):
    link = "https://xn--b1aew.xn--p1ai/request_main"
    page = RequestPage(browser, link)
    page.open()
    page.go_to_request_form()
    page.should_be_surname_field_in_declarant_block_in_request_form()

@pytest.mark.saniti
def test_name_field_in_declarant_block_in_request_form(browser):
    link = "https://xn--b1aew.xn--p1ai/request_main"
    page = RequestPage(browser, link)
    page.open()
    page.go_to_request_form()
    page.should_be_name_field_in_declarant_block_in_request_form()

@pytest.mark.saniti
def test_patronymic_field_in_declarant_block_in_request_form(browser):
    link = "https://xn--b1aew.xn--p1ai/request_main"
    page = RequestPage(browser, link)
    page.open()
    page.go_to_request_form()
    page.should_be_patronymic_field_in_declarant_block_in_request_form()

@pytest.mark.saniti
def test_answer_address_block_title_in_request_form(browser):
    link = "https://xn--b1aew.xn--p1ai/request_main"
    page = RequestPage(browser, link)
    page.open()
    page.go_to_request_form()
    page.should_be_answer_address_block_title_in_request_form()

@pytest.mark.saniti
def test_email_address_field_in_request_form(browser):
    link = "https://xn--b1aew.xn--p1ai/request_main"
    page = RequestPage(browser, link)
    page.open()
    page.go_to_request_form()
    page.should_be_email_address_field_in_request_form()

@pytest.mark.saniti
def test_telephone_in_request_form(browser):
    link = "https://xn--b1aew.xn--p1ai/request_main"
    page = RequestPage(browser, link)
    page.open()
    page.go_to_request_form()
    page.should_be_telephone_in_request_form()

@pytest.mark.saniti
def test_location_in_request_form(browser):
    link = "https://xn--b1aew.xn--p1ai/request_main"
    page = RequestPage(browser, link)
    page.open()
    page.go_to_request_form()
    page.should_be_location_in_request_form()








