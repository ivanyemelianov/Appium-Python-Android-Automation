from appium import webdriver

desired_capabilities = {
    "platformName": "Android",
    "platformVersion": "9",
    "deviceName": "Android Emulator",
    "app": "C:/Users/Daniel/PycharmProjects/AndroidAutomation/Basic/Weatherforecast_v71_apkpure.com.apk",
    "autoGrantPermissions": True,
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_capabilities=desired_capabilities)

driver.implicitly_wait(10)

