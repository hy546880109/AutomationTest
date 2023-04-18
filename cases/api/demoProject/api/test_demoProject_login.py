
from common.hamcrest.hamcrest import assert_that
from base.api.demoProject.api_demoProject_client import API_DemoProject_Client
from common.md5Passwd import Md5_add
import pytest
import ujson

@pytest.fixture() 
def username_password():
    return 'cs', '123456'

class TestLogin:

    def setup_class(self):
        self._api_demoProject_client=API_DemoProject_Client()
        self._login_path='/login/'
        self.headers = {'Content-Type':'application/json'}

    # def test_get_index(self):
    #     httpResponse=self._api_demoProject_client.doRequest.post_with_form(self._login_path)
    #     assert_that(200).is_equal_to(httpResponse.status_code)

    @pytest.mark.search_kw
    def test_search_kw(self,username_password):
        user,passwd = username_password
        passwd = Md5_add(passwd)
        data = {'code':user, 'password':passwd}
        params = ujson.dumps(data)
        request_api = self._api_demoProject_client.doRequest
        request_api.setHeaders(self.headers)
        httpResponse = request_api.post_with_form(self._login_path,params)
        print(f">>>{httpResponse.body}")
        assert_that(200).is_equal_to(httpResponse.status_code)
        assert_that(0).is_equal_to(ujson.loads(httpResponse.body)['code'])
        assert_that(ujson.loads(httpResponse.body)['data']['code']).contains('cs')
