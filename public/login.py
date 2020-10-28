# -*- coding: utf-8 -*-
import time

from common.Unit import unit
from page.login import Login
class login():
    def __init__(self,driver):
        self.driver=driver
        self.data=unit().operaYaml("C:/Users/yunwen/PycharmProjects/customerServer/data/inputData/login.yaml")
        self.login=Login(self.driver)

    #输入正确的用户名及密码
    def weadmin_Login(self):
        self.login.userName().send_keys(self.data['webadmin_login']['username'])
        time.sleep(2)

        self.login.password().send_keys(self.data['webadmin_login']['password'])
        time.sleep(2)

        self.login.login_Btn().click()
        time.sleep(2)

        self.login.backstage().click()
        time.sleep(2)

        self.login.close_chat().click()

    #只输入用户名，不输入密码
    def webadmin_Login_username(self):
        self.login.userName().send_keys(self.data['webadmin_login']['username'])
        time.sleep(2)

        self.login.login_Btn().click()
        time.sleep(2)
    #只输入密码，不输入用户名
    def webadmin_Login_password(self):
        self.login.password().send_keys(self.data['webadmin_login']['password'])
        time.sleep(3)
        self.login.login_Btn().click()
        time.sleep(3)
    #用户名与密码都不填写，直接登录
    def webadmin_Login_Allnull(self):
        self.login.login_Btn().click()
        time.sleep(3)

    #输入错误的用户名及密码
    def webadmin_Login_All_Errror(self):
        self.login.userName().send_keys(self.data['webadmin_login']['username_error'])
        time.sleep(2)
        self.login.password().send_keys(self.data['webadmin_login']['password_error'])
        time.sleep(2)
        self.login.login_Btn().click()
        time.sleep(2)

    def webcustomer_login(self):
        self.login.userName().send_keys(self.data['customer_login']['username'])
        time.sleep(2)
        self.login.password().send_keys(self.data['customer_login']['password'])
        time.sleep(2)
        self.login.login_Btn().click()
        time.sleep(2)
        self.login.customer_age().click()
        time.sleep(2)




