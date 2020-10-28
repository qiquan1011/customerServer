import ddt
import time
import unittest

from selenium import webdriver


from common.Unit import unit
from common.base import BaseCommon


import warnings

from page.login import Login
readExcel=unit().readExcel("testData.xlsx","customer")

@ddt.ddt()
class Main(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter("ignore",ResourceWarning)
        self.driver=webdriver.Chrome()
        self.baseCom = BaseCommon(self.driver)
        self.baseCom.maxBroswer()
        self.data=unit().operaYaml('C:/Users/yunwen/PycharmProjects/customerServer/data/pageData/login.yaml')

        self.weadmin_login=Login(self.driver)
        self.baseCom.openUrl(self.data['url']['webadmin'])

         #输入正确的用户名及密码

    @ddt.data(*readExcel)
    @ddt.unpack
    def test_login(self,username,password,result):
        self.baseCom.untilTime("XPATH",self.data["login"]["username"])
        self.weadmin_login.userName().send_keys(username)
        self.baseCom.untilTime("XPATH",self.data["login"]["password"])
        self.weadmin_login.password().send_keys(password)
        self.baseCom.untilTime("XPATH",self.data["login"]["login-btn"])
        self.weadmin_login.login_Btn().click()
        time.sleep(2)
        self.assertEqual(self.driver.find_element_by_xpath(self.data["msg-content_username"]).text,result)

    #只输入用户名，不输入密码
    #def test_login_username(self):
        #self.weadmin_login.webadmin_Login_username()
        #self.baseCom.untilTime("XPATH",self.data["msg-content_username"])
        #self.assertEqual(self.driver.find_element_by_xpath(self.data['msg-content_username']).text,self.assertData['login_username'])

    #只输入密码，不输入用户名
    #def test_login_password(self):
        #self.weadmin_login.webadmin_Login_password()
        #self.assertEqual(self.driver.find_element_by_xpath(self.data['msg-content_password']).text,self.assertData['login_password'])
    #不输入密码及用户名
    #def test_login_Null(self):
        #self.weadmin_login.webadmin_Login_Allnull()
        #self.baseCom.untilTime("XPATH",self.data["All_Null"])
        #time.sleep(3)
        #self.assertEqual(self.driver.find_element_by_xpath(self.data['All_Null']).text,self.assertData['login_password'])
    #输入错误的用户名及密码
    #def test_login_all_Error(self):
        #self.weadmin_login.webadmin_Login_All_Errror()
        #self.assertEqual(self.driver.find_element_by_xpath(self.data['msg-content_AllError']).text,self.assertData['login_AllError'])

    #客服登录系统
    #def test_cus_login(self):
        #self.weadmin_login.webcustomer_login()
        #self.assertEqual(self.driver.find_element_by_xpath(self.data['myContent']).text,self.assertData['myContent'])

    def tearDown(self):
        self.baseCom.quitBrowser()



if __name__=="__main__":
    unittest.main()

