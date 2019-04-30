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

driver.get('https://www.facebook.com/twherohan/')

time.sleep(1)

post = driver.find_element_by_xpath("//div[@class='_1dwg _1w_m _q7o']")  # 第一筆貼文

post.find_element_by_css_selector('.see_more_link').click()  # 點擊"更多"

time.sleep(1)

post.find_element_by_xpath("//a[@class='_3hg- _42ft']").click()  # 點擊留言

time.sleep(0.5)


# # ------------------------載入留言------------------------
#
#
# cnt = 0
# while True:
#     if cnt >= 2:  # 預設 1 (52則留言(50+2) )
#         break
#     ele = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((
#         By.XPATH, "//a[@data-testid='UFI2CommentsPagerRenderer/pager_depth_0']")))
#
#     a = post.find_element_by_xpath("//a[@data-testid='UFI2CommentsPagerRenderer/pager_depth_0']")
#     a.location_once_scrolled_into_view
#
#     time.sleep(7)
#     ele.click()
#
#     cnt += 1
#
# # ------------------------載入留言------------------------
#
# reviews = driver.find_element_by_xpath("//div[@class='_3w53']")  # 貼文留言區塊ALL)
#
# # ------------------------留言查看更多------------------------
# for ele in reviews.find_elements(By.CSS_SELECTOR, '._5v47.fss'):
#     driver.execute_script("window.scrollTo(0, " + str(ele.location_once_scrolled_into_view.get('y')) + ")")
#     time.sleep(1)
#     ele.click()
#
# # ------------------------留言查看更多------------------------
#
#
# # ------------------------抓取留言者------------------------
# reviewer_list = []
# reviewer_elements = reviews.find_element_by_xpath("//ul[@class='_7791']"
#                                                   ).find_elements_by_xpath("//a[@class='_6qw4']")
# for i in reviewer_elements:
#     reviewer_list.append(i.text)
# # ------------------------抓取留言者------------------------
#
#
# # ------------------------抓取留言------------------------
# temp_save = ""
# cnt1 = 0
# text_split = []
#
# review_all = reviews.find_element_by_xpath("//ul[@class='_7791']").find_elements_by_xpath(
#         "//div[@class='_72vr']")
#
# for re in range(len(review_all)):
#     text = {
#         "reviewer": reviewer_list[re],
#         "review": review_all[re].text
#     }
#     text_split.append(text)
#
#     cnt1 += 1
#
# print(cnt1)
#
# # ------------------------抓取留言------------------------
#
#
# # ------------------------儲存結果------------------------
# with io.open("text_split.json", 'w', encoding='utf-8') as file:
#     json.dump(text_split, file, ensure_ascii=False, indent=4)
# # ------------------------儲存結果------------------------


# ------------------------改model------------------------

#  設定 迴圈 ( if 有留言 就爬留言+刪除 else 加載留言.click() ) *預設第一筆優先點擊

js = "document.getElementById('js_7').remove()"
driver.execute_script(js)

text_split = []
post = driver.find_element_by_xpath("//div[@class='_1dwg _1w_m _q7o']")  # 第一筆貼文
time.sleep(1)
reviews = driver.find_element_by_xpath("//div[@class='_3w53']")  # 貼文留言區塊ALL)

while True:
    try:
        # more_re = reviews.find_element_by_xpath("//a[@data-testid='UFI2CommentsPagerRenderer/pager_depth_0']")
        more_re = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//a[@data-testid='UFI2CommentsPagerRenderer/pager_depth_0']")))

        # driver.execute_script("window.scrollTo(0, " + str(more_re.location.get('y')) + ")")

        more_re.click()  # click review more

        review_all = reviews.find_element_by_xpath("//ul[@class='_7791']").find_elements_by_xpath(
            "//div[@class='_72vr']")

        # for re in range(len(review_all)):
        #     text = {
        #         "reviewer": reviewer_list[re],
        #         "review": review_all[re].text
        #     }
        #     text_split.append(text)

        js = "var a = document.getElementsByTagName('li');" \
             "for (var i = 0 , len = " + str(len(review_all)) + "; i < len; i++){a[0].parentNode.removeChild(a[0])};"

        driver.execute_script(js)
        time.sleep(5)

    except NoSuchElementException:
        break

