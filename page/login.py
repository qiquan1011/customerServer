# -*- coding:utf-8 -*-
from common.Unit import unit
class Login():
    def __init__(self,driver):
        self.driver=driver
        self.webadinData=unit().operaYaml("C:/Users/yunwen/PycharmProjects/customerServer/data/pageData/login.yaml")


    def userName(self):
        return self.driver.find_element_by_xpath(self.webadinData['login']['username']) #username

    def password(self):
        return self.driver.find_element_by_xpath(self.webadinData['login']['password']) #password

    def login_Btn(self):
        return self.driver.find_element_by_xpath(self.webadinData['login']['login-btn'])    #登录按钮

    def backstage(self):
        return self.driver.find_element_by_xpath(self.webadinData['login']['backstage'])  #登录后台

    def customer_age(self):
        return  self.driver.find_element_by_xpath(self.webadinData['login']['customer']) #登录坐席端

    def close_chat(self):
        return self.driver.find_element_by_xpath(self.webadinData["close_chat"]) #关闭小弹窗