from pages.main_page import MainPage
from pages.launch_page import LaunchPage

class Application:

    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.launch_page = LaunchPage(driver)