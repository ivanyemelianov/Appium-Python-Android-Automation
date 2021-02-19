from selenium.webdriver.common.by import By

from pages.base_page import Page


class LaunchPage(Page):
    DONE_BTN = (By.ID, 'com.graph.weather.forecast.channel:id/tvDone')

    def tap_done(self):
        self.click(*self.DONE_BTN)
