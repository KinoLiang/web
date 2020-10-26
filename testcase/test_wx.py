#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shelve
from time import sleep
from selenium.webdriver.common.by import By

class TestWX:

    def test_add_contacts(self, driver):
        # 找到"导入联系人"按钮
        driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
        # 上传
        driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_uploadInputMask").send_keys(
            r"C:\Users\Administrator\Downloads\通讯录批量导入模板.xlsx")
        # 验证 上传文件名
        filename = driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_fileNames").text
        assert "通讯录批量导入模板.xlsx" == filename
        sleep(3)


