import os
import unittest
from glob import glob

import xlrd
import ddt
from selenium import webdriver
from selenium.webdriver import ActionChains

from common.Unit import unit
from common.base import BaseCommon
from public.serviceSummary import Sevice_Summary, logg
readExcel=unit().readExcel("testData.xlsx","serviceTypeName")

@ddt.ddt()
class main(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.basecom=BaseCommon(self.driver)
        self.basecom.maxBroswer()
        self.data = unit().operaYaml('C:/Users/yunwen/PycharmProjects/customerServer/data/pageData/login.yaml')
        self.basecom.openUrl(self.data['url']['webadmin'])
        self.serviceSummary=Sevice_Summary(self.driver)
        self.seviceSummary_data=unit().operaYaml("C:/Users/yunwen/PycharmProjects/customerServer/data/pageData/service_Summary.yaml")

    def test_tineSearch(self):
        result=self.serviceSummary.time_search()
        self.assertIsNotNone(result,msg="出现bug，请前往查看")

    def test_visitorNameSearch(self):
        result=self.serviceSummary.visitor_Name_sarch()
        self.assertEqual(result[0],result[1])

    def test_remark_search(self):
        result=self.serviceSummary.remark_search()
        self.assertEqual(result[0],result[1])

    def test_export(self):
        cls=[]
        result=self.serviceSummary.export()
        try:
            file = xlrd.open_workbook("C:/Users/yunwen/Downloads/服务小结.xlsx")
            sheet = file.sheet_by_name("Sheet1")
            nrows = sheet.nrows

            for i in range(nrows):
                a = sheet.row_values(i)[0]
                print(a)
                cls.append(a)
            print(cls)
        except Exception as e:
            print(e)
        finally:
            self.assertIn(result, cls)
        for infile in glob(os.path.join("C:/Users/yunwen/Downloads", "服务小结*")):
            os.remove(infile)
    def test_view_chatMessage(self):
        result=self.serviceSummary.view_chatMessage()
        self.assertIsNot(result,"暂无聊天记录")
    @ddt.data(*readExcel)
    @ddt.unpack
    def test_add_service_type(self,inputData,Result):
        fially_result=self.serviceSummary.add_service_type(inputData)
        #self.serviceSummary.delect_service_type()
        self.assertEqual(Result,fially_result)
        #self.serviceSummary.delect_service_type()

    #def test_delect_service_type(self):
        #self.serviceSummary.delect_service_type()

    def tearDown(self):
        self.basecom.quitBrowser()
if __name__=="__main__":
    unittest.main()


