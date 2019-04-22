import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8') # out utf-8

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications": 2}  # 處理popup通知
chrome_options.add_experimental_option("prefs", prefs)

mail = 'apou12201@gmail.com'  # FB帳密
pwd = 'w890829w'  # FB帳密

chromedriver = "chromedriver"
driver = webdriver.Chrome(chromedriver, chrome_options=chrome_options)

builder = ActionChains(driver) # 模擬鼠標

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


# ------------------------載入留言------------------------


cnt = 0
while True:

    # WebDriverWait(driver, 8).until_not(EC.presence_of_element_located(
    #     (By.CSS_SELECTOR, '.mls.img._55ym._55yn._55yo')))
    ele = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((
        By.XPATH, "//a[@data-testid='UFI2CommentsPagerRenderer/pager_depth_0']")))

    a = post.find_element_by_xpath("//a[@data-testid='UFI2CommentsPagerRenderer/pager_depth_0']")
    a.location_once_scrolled_into_view
    #

    time.sleep(10)
    ele.click()

    cnt += 1

    if cnt > 2:   #預設 5 (302則留言# )
        break
# ------------------------載入留言------------------------

reviews = driver.find_element_by_xpath("//ul[@class='_7791']")  # 貼文留言(ALL)

# ------------------------留言查看更多------------------------

# for open_review in post.find_elements(By.CSS_SELECTOR, '._5v47.fss'):
#     open_review.click()
# print('ok (2)\n')

# ele = WebDriverWait(driver, 5).until(EC.visibility_of_element_located((
#     By.XPATH, "//a[@class='_5v47 fss']")))

# for i in reviews.find_elements_by_link_text("查看更多"):
#     time.sleep(1)
#     i.click()

# for ele in reviews.find_elements(By.CSS_SELECTOR, '._5v47.fss'):
#     try:
#         ele.click()
#     # 有時候會在這邊被觸發
#     except ElementClickInterceptedException:
#         print('bug')
#     except UnknownMethodException:
#         print('bug')
#
# print('ok 2\n')

# for i in driver.find_elements_by_xpath("//ul[@class='_7791']//li//a[@class='_5v47 fss']"):
#     time.sleep(0.1)
#     # print(i.text)  # 確定有找到"查看更多"
try:
    for more_see in driver.find_element_by_xpath("//ul[@class='_7791']").find_elements(By.CSS_SELECTOR, '._5v47.fss'):
        # builder.move_to_element(more_see).click(more_see).perform()
        # time.sleep(0.5)
        print(more_see.text)

except StaleElementReferenceException:
    print('bug')
# ------------------------留言查看更多------------------------



# ------------------------抓取留言者------------------------

reviewers = reviews.find_element_by_xpath("//ul[@class='_7791']").find_elements_by_xpath("//a[@class='_6qw4']")

# ------------------------抓取留言者------------------------



# ------------------------抓取留言------------------------
# post_reviews = reviews.find_element_by_xpath("//ul[@class='_7791']").find_element_by_xpath("//span[@class='_3l3x']").text

post_reviews = reviews.find_element_by_xpath("//ul[@class='_7791']").find_elements_by_xpath(
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

for i in range(len(reviewers)):
    # print(post_reviews[i].text + '\n')
    save_reviews += post_reviews[i].text + '\n\n'
    # print(save_reviews)

    # print(len(reviewers))
    # print(len(post_reviews))
# ------------------------印出結果(test)------------------------



# ------------------------儲存結果------------------------
save_reviews.encode('utf-8').decode("cp950", "ignore")
file = open("text.txt", 'w', encoding='utf-8')
file.write("Posters : \n" + poster + '\n\n')
file.write("Content : \n" + post_content + '\n\n')
file.write("Review_count : " + str(len(post_reviews)) + '\n\n')
file.write("Reviews : \n" + save_reviews)
file.close()
# ------------------------儲存結果------------------------