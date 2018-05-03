#!/usr/bin/env python
from selenium.webdriver.common.by import By
from common.BasePage import BasePage

'''
Create on 2018-3-1
author:linjian
summary:所有页面元素定位都在此层定义，UI一旦有更改，只需在修改这一层页面对象属性即可。
'''


#继承BasePage类
class LoginPage(BasePage):
    #定位器，通过元素属性定位元素对象
    username_loc = (By.ID, 'loginname1')
    password_loc = (By.ID, 'code1')
    loginSubmit_loc = (By.ID, 'tcode1')

    #操作
    #通过继承覆盖（Overriding）方法：如果子类和父类的方法名相同，优先用子类自己的方法。
    #打开网页
    def open(self):
        self._open(self.baseurl)

    def input_username(self, username):
        self.find_element(*self.username_loc).send_keys(username)

    def input_password(self, password):
        self.find_element(*self.password_loc).send_keys(password)

    def click_submit(self):
        self.find_element(*self.loginSubmit_loc).click()

    #检查登录是否成功
    def check_login(self):
        return self.driver.title == '我的企商'
