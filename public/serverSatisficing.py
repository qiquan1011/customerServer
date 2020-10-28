import datetime
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from common.Unit import unit
from common.base import BaseCommon
from common.log import Log
from page.serverSatisficing import serverSatisficing
from public.login import login

logg=Log()
class ServerSatisficing():
    def __init__(self,driver):
        self.driver=driver
        self.severSatisFicing=serverSatisficing(self.driver)
        self.baseCom = BaseCommon(self.driver)
        self.data = unit().operaYaml("C:/Users/yunwen/PycharmProjects/customerServer/data/pageData/serverSatisficing.yaml")
        self.iframe_data = unit().operaYaml("C:/Users/yunwen/PycharmProjects/customerServer/data/pageData/iframe.yaml")
        self.weadmin_login = login(self.driver)

    def serverSatisficing_iframe(self):

        try:
            self.weadmin_login.weadmin_Login()
            customer_ele=self.baseCom.untilTime("XPATH", self.data["customer"])
            ActionChains(self.driver).move_to_element(customer_ele).perform()

            customer_text_elem=self.baseCom.untilTime("XPATH", self.data["customer_text"])
            customer_text_elem.click()
            time.sleep(2)

            serverSatisficing_elem=self.baseCom.untilTime("XPATH", self.data["customerservice"]["serverSatisficing"])
            serverSatisficing_elem.click()

        # 人工客服iframe

            iframe_satisf=self.baseCom.untilTime("XPATH", self.iframe_data["iframe"]["serverSatisficing"])

            #iframe_satisf = self.severSatisFicing.serverSatisficing_iframe()

            self.driver.switch_to.frame(iframe_satisf)
        except:
            print("无法定位元素，请速来查看")

        #人工客服,时间查询
    def timeSearch(self):


        try:
            self.serverSatisficing_iframe()
            chooseTime_elem=self.baseCom.untilTime("XPATH", self.data["customerservice"]["chooseTime"])
            chooseTime_elem.click()

            startTime_elem=self.baseCom.untilTime("XPATH",self.data["customerservice"]["startTime"])

            startTime_elem.send_keys(Keys.CONTROL,"a")

            startTime_elem.send_keys("2020-07-03")
            startTime_elem.send_keys(Keys.ENTER)
        except:
            print("无法定位元素，请前来查看")


        time.sleep(3)
    def very_Dissatisfied(self):
        #self.serverSatisficing_iframe()

        try:
            self.timeSearch()
            satisfaction_elem=self.baseCom.untilTime("XPATH",self.data["condition_Satisfaction"]["satisfaction"])
            satisfaction_elem.click()

            very_Dissatisfied_elem=self.baseCom.untilTime("XPATH",self.data["condition_Satisfaction"]["very_Dissatisfied"])
            time.sleep(3)
            very_Dissatisfied_elem.click()
        except:
            print("无法定位元素，请前来查看")

    def dissatisfied(self):

        try:
            self.timeSearch()
            satisfaction_elem=self.baseCom.untilTime("XPATH", self.data["condition_Satisfaction"]["satisfaction"])
            satisfaction_elem.click()

            dissatisfied_ele=self.baseCom.untilTime("XPATH",self.data["condition_Satisfaction"]["dissatisfied"])
            time.sleep(3)
            dissatisfied_ele.click()
        except:
            logg.logger.error("无法定位，前来查看")
    def commonly(self):

        try:
            self.timeSearch()
            satisfaction_elem=self.baseCom.untilTime("XPATH", self.data["condition_Satisfaction"]["satisfaction"])
            satisfaction_elem.click()

            commonly_ele=self.baseCom.untilTime("XPATH",self.data["condition_Satisfaction"]["commonly"])
            time.sleep(3)
            commonly_ele.click()

        except:
            logg.logger.error("无法定位，请速来查看")




    def satisfied(self):

        try:
            self.timeSearch()
            satisfaction_ele=self.baseCom.untilTime("XPATH", self.data["condition_Satisfaction"]["satisfaction"])
            satisfaction_ele.click()

            satisfied_elem=self.baseCom.untilTime("XPATH",self.data["condition_Satisfaction"]["satisfied"])
            time.sleep(3)
            satisfied_elem.click()
        except:
            logg.logger.error("无法定位，请速来查看")


    def very_Satisfied(self):

        try:
            self.timeSearch()
            satisfaction_elem=self.baseCom.untilTime("XPATH", self.data["condition_Satisfaction"]["satisfaction"])
            satisfaction_elem.click()

            time.sleep(3)

            very_Satisfied_ele=self.baseCom.untilTime("XPATH", self.data["condition_Satisfaction"]["very_Satisfied"])
            time.sleep(3)
            very_Satisfied_ele.click()
        except:
            logg.logger.error("无法定位，请前来查看")

    def customer_Search(self):

        try:
            self.timeSearch()
            customer_elem=self.baseCom.untilTime("XPATH",self.data["condition_Satisfaction"]["customer"])
            customer_elem.click()


            customer_Name_ele=self.baseCom.untilTime("XPATH",self.data["condition_Satisfaction"]["customer_Name"])
            time.sleep(3)
            customer_Name_ele.click()
        except:
            logg.logger.error("无法定位元素，请速来查看")

    def down_loade(self):

        try:
            self.timeSearch()
            downlode_elem=self.baseCom.untilTime("XPATH",self.data["condition_Satisfaction"]["downlode"])
            downlode_elem.click()
            time.sleep(20)
        except:
            logg.logger.error("无法定位元素，请速来查看")

    def look_message(self):

        try:
            self.timeSearch()
            chatList_elem=self.baseCom.untilTime("XPATH",self.data["condition_Satisfaction"]["chatList"])
            chatList_elem.click()
            time.sleep(3)
        except :
            logg.logger.error("无法定位元素，请速来查看")

















