import os
from datetime import date
from glob import glob

import time
import unittest
import warnings

import xlrd
from selenium import webdriver

from common.Unit import unit
from common.base import BaseCommon
from public import serverSatisficing
from public.login import login
from public.serverSatisficing import ServerSatisficing
from page.serverSatisficing import serverSatisficing

cls=[]
class Main(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.driver = webdriver.Chrome()
        self.baseCom = BaseCommon(self.driver)
        self.baseCom.maxBroswer()
        self.data = unit().operaYaml('C:/Users/yunwen/PycharmProjects/customerServer/data/pageData/login.yaml')

        #self.weadmin_login = login(self.driver)
        self.time_search=ServerSatisficing(self.driver)
        self.severSatisFicing = serverSatisficing(self.driver)
        self.baseCom.openUrl(self.data['url']['webadmin'])
        self.assertData = unit().operaYaml('C:/Users/yunwen/PycharmProjects/customerServer/data/pageData/Assert.yaml')
    #时间查询
    def test_Time_Seach(self):
        #登录访客端
       # self.weadmin_login.weadmin_Login()
        #time.sleep(3)
        #时间查询
        self.time_search.timeSearch()
        #aeert=self.severSatisFicing.allListCount().text
        self.assertIsNotNone(self.severSatisFicing.allListCount().text,msg="有问题，请及时查看")
    #满意度查询
    def test_very_Dissatisfied(self):
        #self.time_search.timeSearch()
        #time.sleep(3)
        self.time_search.very_Dissatisfied()
        time.sleep(3)
        self.assertEqual(self.severSatisFicing.list_Satisfied().text,"非常不满意")

    def test_dissatisfied(self):
        self.time_search.dissatisfied()
        time.sleep(3)
        self.assertEqual(self.severSatisFicing.list_Satisfied().text,"不满意")

    def test_commonly(self):
        self.time_search.commonly()
        time.sleep(3)
        self.assertEqual(self.severSatisFicing.list_Satisfied().text,"一般")

    def test_satisfied(self):
        self.time_search.satisfied()
        time.sleep(3)
        self.assertEqual(self.severSatisFicing.list_Satisfied().text,"满意")

    def test_very_Satisfied(self):
        self.time_search.very_Satisfied()
        time.sleep(3)
        self.assertEqual(self.severSatisFicing.list_Satisfied().text,"非常满意")
    #客服查询
    def test_customer_search(self):
        self.time_search.customer_Search()
        time.sleep(3)
        self.assertEqual(self.severSatisFicing.list_customer().text,"思思")
    #导出功能
    def test_down_loade(self):

        self.time_search.down_loade()

        try:
            file = xlrd.open_workbook("C:/Users/yunwen/Downloads/客服满意度.xls")
            sheet = file.sheet_by_name("Sheet1")
            nrows = sheet.nrows

            for i in range(nrows):
                a=sheet.row_values(i)[0]
                cls.append(a)
            print(cls)
        except Exception as e:
            print(e)
        for infile in glob(os.path.join("C:/Users/yunwen/Downloads", "客服满意度*")):
            os.remove(infile)
        self.assertIn(self.severSatisFicing.visitorId().text,cls)
    #查看聊天记录
    def test_look_message(self):
        self.time_search.look_message()
        self.assertIsNotNone(self.severSatisFicing.message_visitorId().text,msg="出现问题，请查看")

    def tearDown(self):
        self.baseCom.quitBrowser()

if __name__=="__main__":
    unittest.main()

