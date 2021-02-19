from appium import webdriver
from app.application import Application

def before_scenario(context, scenario):

    desired_capabilities = {
        "platformName": "Android",
        "platformVersion": "9",
        "deviceName": "Android Emulator",
        "app": "C:/Users/Daniel/PycharmProjects/AndroidAutomation/Basic/Weatherforecast_v71_apkpure.com.apk",
        "autoGrantPermissions": True,
    }
    context.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_capabilities)
    context.driver.implicitly_wait(10)
    context.app = Application(context.driver)

def after_scenario(context, scenario):
    context.driver.quit()

