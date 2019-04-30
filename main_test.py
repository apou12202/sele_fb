import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from split import split

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
# driver.get('https://www.facebook.com/profile.php?id=100004254313589')

time.sleep(1)

# driver.find_element_by_link_text('貼文').click()  # 貼文頁面

post = driver.find_element_by_xpath("//div[@class='_1dwg _1w_m _q7o']")  # 第一筆貼文
# post = driver.find_element_by_css_selector('._1dwg._1w_m._q7o')

post.find_element_by_css_selector('.see_more_link').click()  # 點擊"更多"

time.sleep(1)

poster = post.find_element_by_xpath("//span[@class='fwn fcg']").text  # PO文者

post_content = driver.find_element_by_xpath("//div[@class='_5pbx userContent _3576']").text  # PO文內容

post.find_element_by_xpath("//a[@class='_3hg- _42ft']").click()

time.sleep(0.5)

# ------------------------選擇過濾(全部留言)------------------------
# # try:
# driver.find_element_by_xpath("//div[@id='u_7_y']/a[@id='js_6a']").find_element_by_xpath("//a[@class='_2pm3 _21q1 _p']").click() # 點擊留言過濾
# btn = driver.find_element_by_xpath("//div[@class='_3w53']/a[@class='_2pm3 _21q1 _p']")\
#     .find_elements_by_xpath("//li[@class='_54ni __MenuItem']")
# btn[2].click()
#
# # except NoSuchElementException:
# #     print('bug')
#
#

# ------------------------選擇過濾(全部留言)------------------------


# ------------------------載入留言------------------------


cnt = 0
while True:
    if cnt >= 2:  # 預設 1 (52則留言(50+2) )
        break
    # WebDriverWait(driver, 8).until_not(EC.presence_of_element_located(
    #     (By.CSS_SELECTOR, '.mls.img._55ym._55yn._55yo')))
    ele = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((
        By.XPATH, "//a[@data-testid='UFI2CommentsPagerRenderer/pager_depth_0']")))

    a = post.find_element_by_xpath("//a[@data-testid='UFI2CommentsPagerRenderer/pager_depth_0']")
    a.location_once_scrolled_into_view
    time.sleep(5)
    ele.click()

    cnt += 1

# ------------------------載入留言------------------------

reviews = driver.find_element_by_xpath("//div[@class='_3w53']")  # 貼文留言區塊ALL)

# ------------------------留言查看更多------------------------
for ele in reviews.find_elements(By.CSS_SELECTOR, '._5v47.fss'):
    driver.execute_script("window.scrollTo(0, " + str(ele.location_once_scrolled_into_view.get('y')) + ")")
    time.sleep(1)
    ele.click()

# ------------------------留言查看更多------------------------


# ------------------------抓取留言者------------------------
reviewer_list = []
reviewer_elements = reviews.find_element_by_xpath("//ul[@class='_7791']"
                                                  ).find_elements_by_xpath("//a[@class='_6qw4']")
for i in reviewer_elements:
    reviewer_list.append(i.text)
# ------------------------抓取留言者------------------------


# ------------------------抓取留言------------------------
# post_reviews = reviews.find_element_by_xpath("//ul[@class='_7791']"
# ).find_element_by_xpath("//span[@class='_3l3x']").text
temp_save = ""
cnt1 = 0
text_split = []
# "//div[@class='_72vr']"

review_all = reviews.find_element_by_xpath("//ul[@class='_7791']").find_elements_by_xpath(
        "//div[@class='_72vr']")

for re in range(len(review_all)):
    text = {
        "reviewer": reviewer_list[re],
        "review": review_all[re].text
    }
    text_split.append(text)

    cnt1 += 1

    # if re.find_element_by_xpath("//span[@class='_3l3x']"):
    #     print("True")
    #     cnt1 += 1
    # elif re.find_element_by_tag_name("img"):
    #     print("0")
    # else:
    #     print("1")

    # print(re.text)  # 成功印出所有留言
    # temp_save += re.find_element_by_xpath("//span[@class='_3l3x']").text + '\n'
    # temp_save = re.find_element_by_xpath("//div[@class=' _6qw3']").text

    # print(re.text)

# print(temp_save)
print(cnt1)

# ---------------test 單一留言區塊 文字抓取------------------
# text_split = []
#
# test = reviews.find_element_by_xpath("//ul[@class='_7791']").find_elements_by_xpath(
#         "//div[@class='_72vr']")
# print(test[10].text)          # 只能抓到第一筆留言 即便跑index
# text_split.append(test[10].text)

# for re in test:
#     text_split.append(re.text)

# ---------------test 單一留言區塊 文字抓取------------------

All_reviews = reviews.find_element_by_xpath("//ul[@class='_7791']").find_elements_by_xpath(
    "//div[@class='_72vr']")  # 抓留言者 + 內容
# ------------------------抓取留言------------------------


# ------------------------印出結果(test)------------------------
save_reviews = ""

# print("Poster : " + poster
#       + '\n' +
#       "Content : " + post_content
#       + '\n' +
#       "Review : "
#       )

# for re in reviews.find_element_by_xpath("//ul[@class='_7791']").find_elements_by_xpath("//span[@class='_3l3x']"):
#     print(re.text)  #  測試 span[@class='_3l3x']

for i in range(len(review_all)):
    # print(post_reviews[i].text + '\n')
    save_reviews += All_reviews[i].text + '\n\n'
    # print(save_reviews)

    # print(len(reviewers))
    # print(len(post_reviews))
# ------------------------印出結果(test)------------------------


# ------------------------儲存結果------------------------
# save_reviews.encode('utf-8').decode("cp950", "ignore")
# file = open("text.txt", 'w', encoding='utf-8')
# file.write("Posters : \n" + poster + '\n\n')
# file.write("Content : \n" + post_content + '\n\n')
# file.write("Review_count : " + str(len(All_reviews)) + '\n\n')
# file.write("Reviews : \n" + save_reviews)
# file.close()

#
# temp_save.encode('utf-8').decode("cp950", "ignore")
# file = open("text_temp.txt", 'w', encoding='utf-8')
# file.write(temp_save)
# file.close()

# temp_save.encode('utf-8').decode("cp950", "ignore")
# file = open("text_split.txt", 'w', encoding='utf-8')
# file.write(text_split)
# file.close()


with io.open("output/text_split.json", 'w', encoding='utf-8') as file:
    json.dump(text_split, file, ensure_ascii=False, indent=4)
# ------------------------儲存結果------------------------
split()

driver.close()
