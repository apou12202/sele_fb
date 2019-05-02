import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import JavascriptException, NoSuchElementException

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
time.sleep(0.01)
driver.find_element_by_name('email').send_keys(mail)
time.sleep(0.01)
driver.find_element_by_name('pass').send_keys(pwd)
time.sleep(0.01)

driver.find_element_by_xpath("//input[@value='登入']").click()

driver.get('https://www.facebook.com/ufi/reaction/profile/browser/?ft_ent_identifier=ZmVlZGJhY2s6MjYzNzk4MjU3NjIxODc0NQ%3D%3D&av=100001602414974')

# ------------------------心情區塊------------------------
emo_area = driver.find_element_by_xpath("//ul[@class='uiList _5i_n _4kg _6-h _6-j _6-i']")
# ------------------------心情區塊------------------------

# ------------------------抓取大心------------------------
love_list = []


love_area = emo_area.find_element_by_xpath("./li[4]")

js = "try{document.getElementById('reaction_profile_browser1').remove();document.getElementById('reaction_profile_pager1').remove();}catch{}"
js1 = "try{document.getElementById('reaction_profile_browser3').remove();document.getElementById('reaction_profile_pager3').remove();}catch{}"
js2 = "try{document.getElementById('reaction_profile_browser4').remove();document.getElementById('reaction_profile_pager4').remove();}catch{}"
js3 = "try{document.getElementById('reaction_profile_browser7').remove();document.getElementById('reaction_profile_pager7').remove();}catch{}"
js4 = "try{document.getElementById('reaction_profile_browser8').remove();document.getElementById('reaction_profile_pager8').remove();}catch{}"

try:
    driver.execute_script(js)
    # time.sleep(0.05)
    driver.execute_script(js1)
    # time.sleep(0.05)
    driver.execute_script(js2)
    # time.sleep(0.05)
    driver.execute_script(js3)
    # time.sleep(0.05)
    driver.execute_script(js4)

except JavascriptException:
    print(JavascriptException)

while True:
    try:
        time.sleep(2)
        love_more = love_area.find_element_by_xpath("//div[@id='reaction_profile_pager2']")
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, " + str(love_more.location.get("y")) + ")")
        time.sleep(2)
        love_more.click()
        # time.sleep(1)
    except NoSuchElementException:
        break

love_people = love_area.find_elements_by_xpath("//div[@class='_5j0e fsl fwb fcb']")

for p in love_people:
    time.sleep(0.05)
    love_list.append(p.text)


# ------------------------抓取大心------------------------

# ------------------------儲存結果------------------------
with io.open("output/CrossAnalyze/test_love.json", 'w', encoding='utf-8') as file:
    json.dump(love_list, file, ensure_ascii=False, indent=4)
# ------------------------儲存結果------------------------

# driver.close()
