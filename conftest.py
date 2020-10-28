# -*- coding:utf-8 -*-
# @time   :2020/10/19 16:41
# @Author   :Kino

import pytest, os, time, shelve
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

@pytest.fixture(scope='session', autouse=True)
def get_cookies():
    print("开始获取cookies")
    options = Options()
    options.debugger_address = "127.0.0.1:9222"
    driver = webdriver.Chrome(options=options)
    driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    cookies = driver.get_cookies()
    # 写入到shelve
    db = shelve.open("cookies")
    db['cookie'] = cookies
    db.close()
    yield
    #driver.quit()
    print("测试结束")

@pytest.fixture(scope='function', autouse=True)
def driver():
    print("测试用例开始：获取浏览器")
    driver = webdriver.Chrome()
    # 读取shelve中的cookies
    db = shelve.open("cookies")
    cookies = db['cookie']
    db.close()
    # 利用读取的cookie 完成登录操作
    driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()
    yield driver
    driver.quit()
    print("测试用例结束：关闭浏览器")



if __name__ == '__main__':
    pytest.main(['-s'])

