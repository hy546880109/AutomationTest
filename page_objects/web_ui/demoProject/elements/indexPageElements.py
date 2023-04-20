'''
Author: HY\harry hy546880109@qq.com
Date: 2023-04-17 12:29:12
LastEditors: HY\harry hy546880109@qq.com
LastEditTime: 2023-04-20 17:12:09
FilePath: \AutomationTest\page_objects\web_ui\demoProject\elements\indexPageElements.py
Description: 
'''
#-*- coding:utf8 -*-
# 作者 yanchunhuo
# 创建时间 2018/01/19 22:36
# github https://github.com/yanchunhuo
from page_objects.createElement import CreateElement
from page_objects.web_ui.wait_type import Wait_Type as Wait_By
from page_objects.web_ui.locator_type import Locator_Type
class IndexPageElements:
    def __init__(self):
        self.path = '/login'
        self.title = CreateElement.create(None,None,None,Wait_By.TITLE_IS,'智慧城市物联云平台')
        self.user_name = CreateElement.create(Locator_Type.ID,'username',wait_type=Wait_By.PRESENCE_OF_ELEMENT_LOCATED)
        self.passwd =  CreateElement.create(Locator_Type.ID,'password',wait_type=Wait_By.PRESENCE_OF_ELEMENT_LOCATED)
        self.code =  CreateElement.create(Locator_Type.ID,'message',wait_type=Wait_By.PRESENCE_OF_ELEMENT_LOCATED)
        self.login_button =  CreateElement.create(Locator_Type.ID,'button',wait_type=Wait_By.ELEMENT_TO_BE_CLICKABLE)
