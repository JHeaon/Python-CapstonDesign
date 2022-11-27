import time
import urllib.request
from selenium import webdriver
from datetime import datetime


def play(img):

    opener = urllib.request.build_opener()
    opener.addheaders = [
        ('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    urllib.request.install_opener(opener)
    driver = webdriver.Chrome(
        "C:/Users/heaon/Desktop/cpst/Python-CapstonDesign/Kyebraiile/main/chromedriver.exe")

    driver.get("https://angelina-reader.ru/")
    driver.find_element_by_css_selector(
        "body > div.site-wrapper > div.site-wrapper__top > div > main > div.site-block.load-block > div.load-block__agree > div:nth-child(1) > label").click()
    time.sleep(1)
    driver.find_element_by_css_selector(
        "#file-input_loadpc").send_keys(img)

    time.sleep(1)
    answer = driver.find_element_by_css_selector(
        "body > div.site-wrapper > div.site-wrapper__top > div.site-content.site-content_result_1and2.container > div.site-content__col.site-content__col_tline > div > div:nth-child(2) > div > div > tt").text

    return answer
