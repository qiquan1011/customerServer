import unittest

from selenium import webdriver

from common.Unit import unit
from common.base import BaseCommon
from public.transfer_to_labor import transfer_to_labor


class transfer_To_labor(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.basecom=BaseCommon(self.driver)
        self.basecom.maxBroswer()
        self.data=unit().operaYaml("C:/Users/yunwen/PycharmProjects/customerServer/data/pageData/login.yaml")
        self.basecom.openUrl(self.data["url"]["webadmin"])
        self.Transfer_To_labor=transfer_to_labor(self.driver)

    def test_transfer_To_Labor(self):
        result=self.Transfer_To_labor.Transfertolabor()
        self.assertIsNotNone(result)
    def test_send_news_text(self):
        result=self.Transfer_To_labor.send_news_text()
        self.assertEqual(result,"你好，我是小弟弟，你是谁")

    def test_send_expression(self):
        result=self.Transfer_To_labor.send_news_expression()
        self.assertIsNotNone(result,msg="有问题，请找管理员处理一下")

    def test_send_vidio(self):
        result=self.Transfer_To_labor.send_news_vidio()
        self.assertIsNotNone(result,msg="出问题了，请来查看")

    def test_send_docx(self):
        result=self.Transfer_To_labor.send_news_docx()
        self.assertEqual(result,"点击下载文件 > test.docx")

    def test_send_audio(self):
        result=self.Transfer_To_labor.send_news_audio()
        self.assertIsNotNone(result,msg="出现问题，请及时处理")

    def test_send_Satisfacted_Invite(self):
        result=self.Transfer_To_labor.send_Satisfacted_Invite()
        self.assertEqual(result,"一般")

    def test_send_summary(self):
        result=self.Transfer_To_labor.send_summary()
        self.assertEqual(result,"俺乃燕人张翼得，尔等还不速速离去")

    def test_send_picture(self):
        result=self.Transfer_To_labor.send_news_picture()
        self.assertIsNotNone(result,msg="出现问题，请前来查看")

    def test_create_chat_group(self):
        result=self.Transfer_To_labor.create_chat_group()
        self.assertEqual(result,'讨论组（1）')


    def tearDown(self):
        self.basecom.quitBrowser()
if __name__=="__main__":
    unittest.main()