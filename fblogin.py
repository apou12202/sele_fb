import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import JavascriptException, NoSuchElementException, StaleElementReferenceException

import sys
import io
import json


sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')  # out utf-8

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}  # 處理popup通知
chrome_options.add_experimental_option("prefs", prefs)

mail = 'apou12201@gmail.com'  # FB帳密
pwd = 'w890829w'  # FB帳密

chromedriver = "chromedriver"
driver = webdriver.Chrome(chromedriver, chrome_options=chrome_options)

builder = ActionChains(driver)  # 模擬鼠標

driver.maximize_window()  # 最大化視窗

driver.get('https://www.facebook.com/')

driver.find_element_by_name('email').send_keys(mail)
driver.find_element_by_name('pass').send_keys(pwd)

driver.find_element_by_xpath("//input[@value='登入']").click()
