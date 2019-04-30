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

mail = 'apou_12203@yahoo.com.tw'  # FB帳密
pwd = 'c890829c'  # FB帳密

chromedriver = "chromedriver"
driver = webdriver.Chrome(chromedriver, chrome_options=chrome_options)

builder = ActionChains(driver)  # 模擬鼠標

driver.maximize_window()  # 最大化視窗

driver.get('https://www.facebook.com/')
time.sleep(0.01)
driver.find_element_by_name('email').send_keys(mail)
time.sleep(0.01)
driver.find_element_by_name('pass').send_keys(pwd)
time.sleep(0.01)

driver.find_element_by_xpath("//input[@value='登入']").click()

driver.get("")

# ------------------------心情區塊------------------------
emo_area = driver.find_element_by_xpath("//ul[@class='uiList _5i_n _4kg _6-h _6-j _6-i']")
# ------------------------心情區塊------------------------

# ------------------------抓取憤怒------------------------
angry_list = []

time.sleep(0.5)
angry_area = emo_area.find_element_by_xpath("./li[4]")
time.sleep(0.5)
js = "document.getElementById('reaction_profile_browser1').remove();document.getElementById('reaction_profile_pager1').remove();"
js1 = "document.getElementById('reaction_profile_browser3').remove();document.getElementById('reaction_profile_pager3').remove();"
js2 = "document.getElementById('reaction_profile_browser4').remove();document.getElementById('reaction_profile_pager4').remove();"
js3 = "document.getElementById('reaction_profile_browser7').remove();document.getElementById('reaction_profile_pager7').remove();"
js4 = "document.getElementById('reaction_profile_browser2').remove();document.getElementById('reaction_profile_pager2').remove();"

try:
    driver.execute_script(js)
    time.sleep(0.5)
    driver.execute_script(js1)
    time.sleep(0.5)
    driver.execute_script(js2)
    time.sleep(0.5)
    driver.execute_script(js3)
    time.sleep(0.5)
    driver.execute_script(js4)
    time.sleep(0.5)

except JavascriptException:
    print(JavascriptException)

while True:
    try:
        time.sleep(2)
        angry_more = angry_area.find_element_by_xpath("//div[@id='reaction_profile_pager8']")
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, " + str(angry_more.location.get("y")) + ")")
        time.sleep(2)
        angry_more.click()
        time.sleep(1)
    except NoSuchElementException:
        break
time.sleep(0.5)
angry_people = angry_area.find_elements_by_xpath("//div[@class='_5j0e fsl fwb fcb']")

for p in angry_people:
    time.sleep(0.05)
    angry_list.append(p.text)

driver.quit()
driver.close()

# ------------------------抓取憤怒------------------------


# ------------------------儲存結果------------------------
with io.open("output/test_angry.json", 'w', encoding='utf-8') as file:
    json.dump(angry_list, file, ensure_ascii=False, indent=4)
# ------------------------儲存結果------------------------
#
# driver.close()
