#!/usr/bin/env python
import unittest, time
from pages.LoginPage import LoginPage

'''
Create on 2018-3-2
author:linjian
summary:使用unittest框架编写测试用例
'''


class LoginTest(unittest.TestCase):
    def setUp(self):
        url = 'http://m.8673h.com/Login/login/login.html'
        self.username = '18668167812'
        self.password = '123456'
        self.loginpage = LoginPage(base_url=url)

    def tearDown(self):
        self.loginpage.driver.quit()

    #用例执行体
    def test_sign(self):
        '''登录页面测试用例'''
        #声明signpage对象
        #执行具体操作
        self.loginpage.open()
        self.loginpage.input_username(self.username)
        self.loginpage.input_password(self.password)
        self.loginpage.click_submit()
        time.sleep(2)
        assert self.loginpage.check_login()
        time.sleep(5)

        # if __name__ == "__main__":
        # 	unittest.main()
