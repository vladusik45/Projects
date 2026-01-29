from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time

options = UiAutomator2Options()
options.platformName = "Android"
options.deviceName = "Pixel_8_API_Baklava"
options.appPackage = "com.google.android.deskclock"
options.appActivity = "com.android.deskclock.DeskClock"
options.noReset = True

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

time.sleep(2)  

clock_icon = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Clock")')
clock_icon.click()

time.sleep(3)  

timer_tab = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Stopwatch")')
timer_tab.click()

stopwatch_btn = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiSelector().text("Start")')
stopwatch_btn.click()

driver.quit()