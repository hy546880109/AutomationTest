'''
Author: HY\harry hy546880109@qq.com
Date: 2023-04-17 12:29:12
LastEditors: HY\harry hy546880109@qq.com
LastEditTime: 2023-04-20 17:35:57
FilePath: \AutomationTest\page_objects\web_ui\demoProject\pages\indexPage.py
Description: 
'''
#-*- coding:utf-8 -*-
# 作者 yanchunhuo
# 创建时间 2018/01/19 22:36
# github https://github.com/yanchunhuo
from page_objects.web_ui.demoProject.elements.indexPageElements import IndexPageElements
from page_objects.web_ui.demoProject.pages.searchPage import SearchPage
class IndexPage:
    def __init__(self,browserOperator):
        self._browserOperator=browserOperator
        self._indexPageElements=IndexPageElements()
        self._browserOperator.explicit_wait_page_title(self._indexPageElements.title)
        self._browserOperator.get_screenshot('login')

    def _input_username(self,username):
        self._browserOperator.sendText(self._indexPageElements.user_name,username)
        self._browserOperator.get_screenshot('username')

    def _input_passwd(self,password):
        self._browserOperator.sendText(self._indexPageElements.passwd,password)
        self._browserOperator.get_screenshot('passwd')

    def _input_code(self,tow_code):
        self._browserOperator.sendText(self._indexPageElements.code,tow_code)
        self._browserOperator.get_screenshot('code')

    def _click_login_button(self):
        self._browserOperator.click(self._indexPageElements.login_button)
        self._browserOperator.get_screenshot('button')

    def login_case(self, user,passwd,code):
        self._input_username(user)
        self._input_passwd(passwd)
        self._input_code(code)
        self._click_login_button()
        return IndexPage(self._browserOperator)


    def getElements(self):
        return self._indexPageElements