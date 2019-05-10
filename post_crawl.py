import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

import sys
import io
import json

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')  # out utf-8

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}  # 處理popup通知
chrome_options.add_experimental_option("prefs", prefs)

mail = ''  # FB帳密
pwd = ''  # FB帳密

chromedriver = "chromedriver"
driver = webdriver.Chrome(chromedriver, chrome_options=chrome_options)

builder = ActionChains(driver)  # 模擬鼠標

driver.maximize_window()  # 最大化視窗

driver.get('https://www.facebook.com/')

driver.find_element_by_name('email').send_keys(mail)
driver.find_element_by_name('pass').send_keys(pwd)

driver.find_element_by_xpath("//input[@value='登入']").click()

driver.get('https://www.facebook.com/twherohan/')

time.sleep(0.5)

driver.find_element_by_xpath("//div[@data-key='tab_posts']").click()  # 點擊貼文頁面

time.sleep(3)  # wait for loading

posts = driver.find_elements_by_xpath("//div[@class='_1dwg _1w_m _q7o']")  # 第一筆貼文

try:
    posts[0].find_element_by_css_selector('.see_more_link').click()  # 點擊"更多"
except NoSuchElementException:
    print("no see more")
time.sleep(0.5)

while True:
    review = driver.find_element_by_xpath("//div[@data-testid='UFI2CommentsList/root_depth_0']")

    ele = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((
        By.XPATH, "//a[@data-testid='UFI2CommentsPagerRenderer/pager_depth_0']")))
