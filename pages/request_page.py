from .base_page import BasePage
from .locators import RequestPageLocators
from selenium.webdriver.common.by import By


class RequestPage(BasePage):
    def should_match_request_list(self, position, value):
        checked_value = str(self.browser.find_element(By.CSS_SELECTOR, f".sl-item:nth-child({position}) .radio b").text)
        assert value in checked_value, f"Отсутствует подразделение {value}, или расположено не в том порядке"

    def should_not_be_extra_in_request_list(self):
        assert self.is_not_element_present(*RequestPageLocators.EXTRA_VALUE), "В списке подраздений имеются лишние позиции"

    def go_to_request_form(self):
        self.browser.find_element(*RequestPageLocators.REQUEST_LIST_MVD).click()
        self.browser.find_element(*RequestPageLocators.PROCEED_BUTTON).click()
        self.browser.find_element(*RequestPageLocators.CHECKBOX).click()
        self.browser.find_element(*RequestPageLocators.APPLY_BUTTON).click()

    def should_match_address_block_title_in_request_form(self):
        expected_address_title = "Куда адресовано"
        address_title =  self.browser.find_element(*RequestPageLocators.REQUEST_FORM_ADDRESS_TITLE).text
        assert expected_address_title == address_title, f'Заголовок блока отображается "{address_title}" вместо "{expected_address_title}"'

    def should_be_subdivision_in_address_block_in_request_form(self):
        expected_subdivision = "Министерство внутренних дел Российской Федерации"
        subdivision = self.browser.find_element(*RequestPageLocators.REQUEST_FORM_SUBDIVISION).text
        assert expected_subdivision == subdivision, f'Выбранное подразделение отображается как "{subdivision}" вместо "{expected_subdivision}"'

    def should_be_full_name_field_in_address_block_in_request_form(self):
        assert self.is_element_present(*RequestPageLocators.REQUEST_FORM_FULL_NAME_FIELD), "Отсутствует поле ввода ФИО, должности"

    def should_be_declarant_block_title_in_request_form(self):
        expected_declarant_title = "Заявитель" 
        declarant_title = self.browser.find_element(*RequestPageLocators.REQUEST_FORM_DECLARANT_TITLE).text
        assert expected_declarant_title == declarant_title, f'Заголовок блока отображается "{declarant_title}" вместо "{expected_declarant_title}"'

    def should_be_citizen_radiobutton_in_declarant_block_in_request_form(self):
        assert self.is_element_present(*RequestPageLocators.REQUEST_FORM_CITIZEN_RADIOBUTTON), 'Отсутствует радиокнопка "Гражданин"'
    
    def should_be_organization_radiobutton_in_declarant_block_in_request_form(self):
        assert self.is_element_present(*RequestPageLocators.REQUEST_FORM_ORGANIZATION_RADIOBUTTON), 'Отсутствует радиокнопка "Организация"'

    def should_be_surname_field_in_declarant_block_in_request_form(self):
        assert self.is_element_present(*RequestPageLocators.REQUEST_FORM_SURNAME_FIELD), 'Отсутствует поле "Фамилия"'

    def should_be_name_field_in_declarant_block_in_request_form(self):
        assert self.is_element_present(*RequestPageLocators.REQUEST_FORM_NAME_FIELD), 'Отсутствует поле "Имя"'
    
    def should_be_patronymic_field_in_declarant_block_in_request_form(self):
        assert self.is_element_present(*RequestPageLocators.REQUEST_FORM_PATRONYMIC_FIELD), 'Отсутствует поле "Отчество"'

    def should_be_answer_address_block_title_in_request_form(self):
        expected_answer_address_title = "Адрес для ответа*" 
        answer_address_title = self.browser.find_element(*RequestPageLocators.REQUEST_FORM_ANSWER_ADDRESS_TITLE).text
        assert expected_answer_address_title == answer_address_title, f'Заголовок блока отображается "{answer_address_title}" вместо "{expected_answer_address_title}"'

    def should_be_email_address_field_in_request_form(self):
        assert self.is_element_present(*RequestPageLocators.REQUEST_FORM_EMAIL_ADDRESS), 'Отсутствует поле "Адрес электронной почты"'

    def should_be_telephone_in_request_form(self):
        assert self.is_element_present(*RequestPageLocators.REQUEST_FORM_EMAIL_ADDRESS), 'Отсутствует поле "Телефон"'

    def should_be_location_in_request_form(self):
        assert self.is_element_present(*RequestPageLocators.REQUEST_FORM_LOCATION), 'Отсутствует поле "Телефон"'
