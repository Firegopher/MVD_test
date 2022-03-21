from .base_page import BasePage
from .locators import AllMediaPageLocators
import time


class AllMediaPage(BasePage):
    def should_work_radio(self):
        self.browser.find_element(*AllMediaPageLocators.RADIO_PLAY_BUTTON).click()
        assert self.is_element_present(*AllMediaPageLocators.RADIO_PAUSE_BUTTON), "Радио не воспроизсодится"

    def should_work_video(self):
        self.browser.find_element(*AllMediaPageLocators.VIDEO_NEWS).click()
        self.browser.switch_to.frame(self.browser.find_element(*AllMediaPageLocators.WINDOW_FRAME))
        self.browser.find_element(*AllMediaPageLocators.VIDEO_WINDOW_PLAY_BUTTON).click()
        assert self.is_element_present(*AllMediaPageLocators.VIDEO_WINDOW_STOP_BUTTON), "Видео не воспроизводится"

    def should_work_audio(self):
        self.browser.find_element(*AllMediaPageLocators.AUDIO_PLAY_BUTTON).click()
        assert self.is_element_present(*AllMediaPageLocators.AUDIO_PAUSE_BUTTON), "Аудиофайлы не воспроизводятся"