from chrome_spider import Spider


if __name__ == "__main__":
    spider = Spider()
    driver = spider.get_driver()
    driver.get("https://baidu.com")