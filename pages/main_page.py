from selenium.webdriver.common.by import By

from pages.base_page import Page


class MainPage(Page):
    #SCREEN_LOCKED = ()
    TEMPERATURE = (By.ID, 'com.graph.weather.forecast.channel:id/tvTypeTemperature')

    CANCEL_BTN = (By.ID, 'com.graph.weather.forecast.channel:id/md_buttonDefaultNegative')

    def tap_cancel(self):
        self.click(*self.CANCEL_BTN)

    def verify_temperature(self):
        result_temperature = self.find_element(*self.TEMPERATURE).text
        assert 'C' == result_temperature, f'Expected C to be in {result_temperature}'
