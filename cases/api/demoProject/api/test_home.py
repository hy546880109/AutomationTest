'''
Author: HY\harry hy546880109@qq.com
Date: 2023-04-19 17:03:08
LastEditors: hy hy546880109@qq.com
LastEditTime: 2023-04-19 23:05:37
FilePath: /AutomationTest/cases/api/demoProject/api/test_home.py
Description: 
'''
from common.hamcrest.hamcrest import assert_that
from base.api.demoProject.api_demoProject_client import API_DemoProject_Client
from common.md5Passwd import Md5_add
from common.readXlsx import ReadFile
import pytest
import ujson

file_path = 'test_data/api/api_test_case.csv'
f = ReadFile(file_path)

@pytest.fixture()
def username_password_success():
    case_data_success = ujson.loads(f.read_iat(0,6))
    user = case_data_success['code']
    passwd = case_data_success['password']
    except_result = ujson.loads(f.read_iat(0,7))
    code_number = except_result['code']
    return user, passwd, code_number

class TestLogin:
    def setup_class(self):
        self._api_demoProject_client=API_DemoProject_Client()
        self._login_path=f.read_iat(0,3)

    @pytest.mark.login_success
    def test_login_success(self,username_password_success):
        user,passwd,code_number = username_password_success
        data = {'code':user, 'password':Md5_add(passwd)}
        params = ujson.dumps(data)
        request_api = self._api_demoProject_client.doRequest
        httpResponse = request_api.post_with_form(self._login_path,params)
        print(f">>>{httpResponse.body}")
        assert_that(200).is_equal_to(httpResponse.status_code)
        assert_that(code_number).is_equal_to(ujson.loads(httpResponse.body)['code'])
        assert_that(ujson.loads(httpResponse.body)['data']['code']).contains('cs')

    
        