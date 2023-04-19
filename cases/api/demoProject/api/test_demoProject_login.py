'''
Author: hy hy546880109@qq.com
Date: 2023-04-19 22:51:18
LastEditors: hy hy546880109@qq.com
LastEditTime: 2023-04-19 23:05:24
FilePath: /AutomationTest/cases/api/demoProject/api/test_demoProject_login.py
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

@pytest.fixture()
def username_password_fail1():
    case_data_fail = ujson.loads(f.read_iat(1,6))
    user = case_data_fail['code']
    passwd = case_data_fail['password']
    except_result = ujson.loads(f.read_iat(1,7))
    code_number= except_result['code']
    return user, passwd, code_number

@pytest.fixture()
def username_password_fail2():
    case_data_fail = ujson.loads(f.read_iat(2,6))
    user = case_data_fail['code']
    passwd = case_data_fail['password']
    except_result = ujson.loads(f.read_iat(2,7))
    code_number= except_result['code']
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

    
    def test_login_not_create(self,username_password_fail1):
        user, passwd, code_number = username_password_fail1
        data = {'code': user, 'password': Md5_add(passwd)}
        params = ujson.dumps(data)
        request_api = self._api_demoProject_client.doRequest
        httpResponse = request_api.post_with_form(self._login_path, params)
        print(f">>>{httpResponse.body}")
        assert_that(200).is_equal_to(httpResponse.status_code)
        assert_that(code_number).is_equal_to(ujson.loads(httpResponse.body)['code'])
        assert_that(ujson.loads(httpResponse.body)['message']).contains('账户未创建请联系管理员')

    def test_login_passwd_fail(self,username_password_fail2):
        user, passwd, code_number = username_password_fail2
        data = {'code': user, 'password': Md5_add(passwd)}
        params = ujson.dumps(data)
        request_api = self._api_demoProject_client.doRequest
        httpResponse = request_api.post_with_form(self._login_path, params)
        print(f">>>{httpResponse.body}")
        assert_that(200).is_equal_to(httpResponse.status_code)
        assert_that(code_number).is_equal_to(ujson.loads(httpResponse.body)['code'])
        assert_that(ujson.loads(httpResponse.body)['message']).contains('输入的密码错误')

