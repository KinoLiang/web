# -*- coding:utf-8 -*-
# @time   :2020/10/26 17:18
# @Author   :Kino
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time

options = Options()
options.debugger_address = "127.0.0.1:9222"
driver = webdriver.Chrome(options=options)
driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
print('打开企业微信-【通讯录】页面')
print(driver.get_cookies())
time.sleep(5)
driver.quit()
print('关闭浏览器')

