#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shelve
from time import sleep
from selenium.webdriver.common.by import By

from page.main_page import MainPage


class TestContacts:

    def test_add_contacts(self, driver):
        # 初始化跳转到【通讯录】页签，点击【添加成员】按钮
        addmemberpage = MainPage(driver).goto_addmember()
        # 在添加成员页面完成成员信息（姓名、账号、手机号码）输入，并提交
        addmemberpage.add_member('梁山伯', '2020102701', '13424300901')
        # 提交成功后，获取新的通信联系人姓名列表，判定新增的成员是否在列表里面
        assert addmemberpage.get_member('梁山伯')



