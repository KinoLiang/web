#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 基类 ：最基本的方法， driver 实例化， find()等
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time


class BasePage:
    # driver: WebDriver
    base_url = ""

    def __init__(self, driver: WebDriver = None):
        if driver == None:
            # 第一次初始化
            options = Options()
            options.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=options)
            # 设置隐式等待时间
            self.driver.implicitly_wait(5)
        else:
            # 进行页面跳转的操作
            self.driver = driver

        # base_url 打开某个页面
        if self.base_url != "":
            self.driver.get(self.base_url)

    def close(self):
        time.sleep(3)
        self.driver.quit()

    # 使用显示等待方法进行元素定位
    def find(self, by, locator, timeout=10):
        try:
            driver = self.driver
            element = WebDriverWait(driver, timeout, 0.5).until(lambda driver: driver.find_element(by, locator))
            return element
        except:
            return False

    def finds(self, by, locator, timeout=10):
        try:
            driver = self.driver
            elements = WebDriverWait(driver, timeout, 0.5).until(lambda driver: driver.find_elements(by, locator))
            return elements
        except:
            return False

    def wait_for_click(self, locator, timeout=10):
        element: WebElement = WebDriverWait(self.driver, timeout).until(
            expected_conditions.element_to_be_clickable(locator))
        return element

    # app显示等待方法
    def wait(self, method, value, t=30):
        try:
            driver = self.driver
            element = ''
            if method == 'id':
                element = WebDriverWait(driver, t, 0.5).until(lambda driver: driver.find_element_by_id(value))
            elif method == 'name':
                element = WebDriverWait(driver, t, 0.5).until(lambda driver: driver.find_element_by_name(value))
            elif method == 'classname':
                element = WebDriverWait(driver, t, 0.5).until(lambda driver: driver.find_element_by_classname(value))
            elif method == 'xpath':
                element = WebDriverWait(driver, t, 0.5).until(lambda driver: driver.find_element_by_xpath(value))
            elif method == 'accessibility_id':
                element = WebDriverWait(driver, t, 0.5).until(
                    lambda driver: driver.find_element_by_accessibility_id(value))
            elif method == 'android_uiautomator':
                element = WebDriverWait(driver, t, 0.5).until(
                    lambda driver: driver.find_element_by_android_uiautomator(value))
            elif method == 'ios_uiautomation':
                element = WebDriverWait(driver, t, 0.5).until(
                    lambda driver: driver.find_element_by_ios_uiautomation(value))
            elif method == 'link_text':
                element = WebDriverWait(driver, t, 0.5).until(lambda driver: driver.find_element_by_link_text(value))
            elif method == 'tag_name':
                element = WebDriverWait(driver, t, 0.5).until(lambda driver: driver.find_element_by_tag_name(value))
            elif method == 'partial_link_text':
                element = WebDriverWait(driver, t, 0.5).until(
                    lambda driver: driver.find_element_by_partial_link_text(value))
            return element
        except Exception as e:
            return False
