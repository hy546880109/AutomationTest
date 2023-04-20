'''
Author: HY\harry hy546880109@qq.com
Date: 2023-04-17 12:29:12
LastEditors: HY\harry hy546880109@qq.com
LastEditTime: 2023-04-20 18:24:10
FilePath: \AutomationTest\cases\web_ui\demoProject\test_demoProject_index.py
Description: 
'''
'''
Author: HY\harry hy546880109@qq.com
Date: 2023-04-17 12:29:12
LastEditors: HY\harry hy546880109@qq.com
LastEditTime: 2023-04-20 17:39:40
FilePath: \AutomationTest\cases\web_ui\demoProject\test_demoProject_index.py
Description: 
'''
from base.web_ui.demoProject.web_ui_demoProject_client import WEB_UI_DemoProject_Client
from page_objects.web_ui.demoProject.pages.indexPage import IndexPage
from common.hamcrest.hamcrest import assert_that

class TestIndex:
    def setup_class(self):
        self.demoProjectClient = WEB_UI_DemoProject_Client()
        self.indexPage=IndexPage(self.demoProjectClient.browserOperator)

    def test_search_empty_kw(self):
        self.indexPage.login_case('cs','123456','1234')
        assert_that(self.indexPage.getElements().title.wait_expected_value).is_equal_to(self.demoProjectClient.browserOperator.getTitle())

    def teardown_class(self):
        self.demoProjectClient.browserOperator.close()