from selenium.webdriver.common.by import By
from appium import webdriver
from pages.base_page import Page


class MainPage(Page):

    TEMPERATURE = (By.ID, 'com.graph.weather.forecast.channel:id/tvTypeTemperature')
    TIME_ITEM = (By.ID, 'com.graph.weather.forecast.channel:id/tvHourItem')
    CANCEL_BTN = (By.ID, 'com.graph.weather.forecast.channel:id/md_buttonDefaultNegative')
    WIND_SPEED = (By.ID, 'com.graph.weather.forecast.channel:id/tv_rain_probability')

    def tap_cancel(self):
        self.wait(15)
        self.click(*self.CANCEL_BTN)

    def verify_temperature_celsius(self):
        result_temperature = self.find_element(*self.TEMPERATURE).text
        assert 'C' == result_temperature, f'Expected C to be in {result_temperature}'

    def verify_12h_timeformat(self):
        time_element = self.find_element(*self.TIME_ITEM).text
        assert 'am' or 'pm' in time_element, f'Expected am or pm in {time_element}'
        
    def verify_kmh_wind_speed(self):
        wind_speed = self.find_element(*self.WIND_SPEED).text
        assert 'km/h' in wind_speed, f'Expected am or pm in {wind_speed}'
