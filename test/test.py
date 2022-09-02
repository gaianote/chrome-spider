from chromespider.spider  import ChromeSpider
from selenium.webdriver.common.by import By
import time

def login(driver, phone_number, password):
    driver.get("https://d.weidian.com/weidian-pc/login")
    driver.find_element(By.XPATH, '//*[@placeholder="手机号"]').send_keys(phone_number)
    driver.find_element(By.XPATH, '//*[@placeholder="输入登录密码"]').send_keys(password)
    driver.find_element(By.XPATH, '//*[text()="进入微店"]').click()
    time.sleep(3)


def insert_cookies():
    accounts = [("10000952701", "wd123456"), ("15233200179", "wd123456")]
    for account in accounts:
        spider = ChromeSpider()
        driver = spider.get_driver()
        driver.get("https://d.weidian.com/weidian-pc/login")
        login(driver,account[0],account[1])
        spider.save_cookie("weidian.com",account[0])
        driver.quit()

def login_by_cookies():
    accounts = [("10000952701", "wd123456"), ("15233200179", "wd123456")]
    for account in accounts:
        spider = ChromeSpider()
        driver = spider.get_driver()
        driver.get("https://d.weidian.com/weidian-pc/login")
        spider.login_by_cookie("weidian.com",account[0])
    # spider.login_by_cookie("weidian.com", "10000952701")
        driver.get("https://d.weidian.com/weidian-pc/weidian-loader/#/pc-vue-micro-index/index")
# login_by_cookies()
accounts = [("10000952701", "wd123456"), ("15233200179", "wd123456")]

spider = ChromeSpider()
driver = spider.get_driver()
driver.get("https://d.weidian.com/weidian-pc/login")
spider.login_by_cookie("weidian.com","15233200179")
driver.get("https://weidian.com/weidian-h5/user/index.html?spider_token=62ea")
input()
driver.get("https://h5.weidian.com/decoration/uni-mine/?umk=1661824000&wfr=c&ifr=itemdetail&spider_token=158d#/")

input("wait for input ...")
driver.quit()
# spider2 = ChromeSpider()
# driver2 = spider2.get_driver()
# driver2.get("https://d.weidian.com/weidian-pc/login")
# spider2.login_by_cookie("weidian.com","10000952701")
# driver2.get("https://weidian.com/weidian-h5/user/index.html?spider_token=62ea")
