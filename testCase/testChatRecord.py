import os
import unittest
import warnings
from glob import glob

import xlrd
from selenium import webdriver

from common.Unit import unit
from common.base import BaseCommon
from page.chat_Record import chatRecord
from public.chatRecord import Chat_Record


class Main(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter("ignore", ResourceWarning)
        self.driver = webdriver.Chrome()

        self.baseCom=BaseCommon(self.driver)
        self.baseCom.maxBroswer()
        self.chatRecord=Chat_Record(self.driver)
        self.record_Chat=chatRecord(self.driver)
        self.data = unit().operaYaml('C:/Users/yunwen/PycharmProjects/customerServer/data/pageData/login.yaml')
        self.baseCom.openUrl(self.data['url']['webadmin'])

    def test_time_search(self):
        self.chatRecord.time_search()
        self.assertIsNotNone(self.record_Chat.list_Count().text,msg="出问题了，快来产看")

    def test_channel_search(self):
        self.chatRecord.search_channel()
        self.assertIsNotNone(self.record_Chat.list_Count().text,msg="出问题了，快来查看一下")

    def test_satisfic_search(self):
        self.chatRecord.statisfic_search()
        self.assertIsNotNone(self.record_Chat.list_Count().text,msg="出问题了,快来查看一下")

    def test_group_search(self):
        result=self.chatRecord.group_search()
        self.assertEqual(result,"售前客服")
    def test_agent_search(self):
        result=self.chatRecord.agent_search()
        self.assertEqual(result,"思思")

    def test_visitorName_search(self):
        result=self.chatRecord.visitorName_search()
        self.assertEqual(result[0],result[1])

    def test_exportChatRecord(self):
        cls=[]
        result=self.chatRecord.exportChatRecord()
        try:
            file = xlrd.open_workbook("C:/Users/yunwen/Downloads/聊天记录.xlsx")
            sheet = file.sheet_by_name("Sheet1")
            nrows = sheet.nrows

            for i in range(nrows):
                a=sheet.row_values(i)[1]
                print(a)
                cls.append(a)
            print(cls)
        except Exception as e:
            print(e)
        finally:
            self.assertIn(result,cls)
        for infile in glob(os.path.join("C:/Users/yunwen/Downloads", "聊天记录*")):
            os.remove(infile)
        #self.assertIn(result,cls)
    def test_View_chat_history(self):
        result=self.chatRecord.View_chat_history()
        self.assertEqual(result[0],result[1])


    def tearDown(self) :
        self.baseCom.closeBrowser()

if __name__=="__main__":
    unittest.main()










