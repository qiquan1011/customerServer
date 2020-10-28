import unittest

import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys

from common.Unit import unit
from common.base import BaseCommon
from common.log import Log
from public.login import login

logg=Log()
class Chat_Record():
    def __init__(self,driver):
        self.driver=driver
        self.login=login(self.driver)
        self.baseCom=BaseCommon(self.driver)
        self.chat_Record_data=unit().operaYaml("C:/Users/yunwen/PycharmProjects/customerServer/data/pageData/chat_Record.yaml")
        self.data = unit().operaYaml("C:/Users/yunwen/PycharmProjects/customerServer/data/pageData/serverSatisficing.yaml")
        self.iframe_data = unit().operaYaml("C:/Users/yunwen/PycharmProjects/customerServer/data/pageData/iframe.yaml")
    def chat_Record_iframe(self):
        try:
            self.login.weadmin_Login()
            time.sleep(3)

            customer_ele = self.baseCom.untilTime("XPATH", self.data["customer"])
            ActionChains(self.driver).move_to_element(customer_ele).perform()

            customer_text_elem = self.baseCom.untilTime("XPATH", self.data["customer_text"])
            customer_text_elem.click()

            chat_Record_text_elem = self.baseCom.untilTime("XPATH", self.chat_Record_data["chat_Record"]["chat_Record_text"])
            chat_Record_text_elem.send_keys(Keys.ENTER)

        # 聊天记录iframe

            iframe_satisf = self.baseCom.untilTime("XPATH", self.iframe_data["iframe"]["chat_Record"])
            # iframe_satisf = self.severSatisFicing.serverSatisficing_iframe()
            self.driver.switch_to.frame(iframe_satisf)
        except:
            logg.logger.error("无法定位元素，请速来查看")
    #时间搜索
    def time_search(self):

        try:
            self.chat_Record_iframe()
            chooseTime_elem=self.baseCom.untilTime("XPATH",self.chat_Record_data["chat_Record"]["chooseTime"])
            chooseTime_elem.click()
            time.sleep(3)

            now_twoMouth_ele=self.baseCom.untilTime("XPATH",self.chat_Record_data["chat_Record"]["now_twoMouth"])
            now_twoMouth_ele.click()
            time.sleep(3)
        except:
            logg.logger.error("无法定位元素，请速来查看")
    #渠道搜索
    def search_channel(self):

        try:
            self.time_search()
            channel_elem=self.baseCom.untilTime("XPATH",self.chat_Record_data["chat_Record"]["channel"])
            channel_elem.click()

            pc_channel_ele=self.baseCom.untilTime("XPATH",self.chat_Record_data["chat_Record"]["pc_channel"])
            pc_channel_ele.click()

            channel_name_element=self.baseCom.untilTime("XPATH",self.chat_Record_data["chat_Record"]["channel_name"])
            channel_name_element.click()
            time.sleep(2)
        except:
            logg.logger.error("无法定位元素，请速来查看")


    def statisfic_search(self):

        try:
            self.time_search()
            satisficing_elem=self.baseCom.untilTime("XPATH",self.chat_Record_data["chat_Record"]["satisficing"])
            satisficing_elem.click()


            very_satisficing_ele=self.baseCom.untilTime("XPATH",self.chat_Record_data["chat_Record"]["very_satisficing"])
            very_satisficing_ele.click()
            time.sleep(2)
        except:
            logg.logger.error("无法定位元素，请前来查看")

    def group_search(self):

        try:
            self.time_search()
            group_elem=self.baseCom.untilTime("XPATH",self.chat_Record_data["chat_Record"]["group"])
            group_elem.click()

            groupName_elem=self.baseCom.untilTime("XPATH",self.chat_Record_data["chat_Record"]["groupName"])
            groupName_elem.click()
            time.sleep(2)

            list_groupName_elem=self.baseCom.untilTime("XPATH",self.chat_Record_data["chat_Record"]["list_groupName"])
            groupName=list_groupName_elem.text
            return groupName

        except:
            logg.logger.error("无法定位元素，请前来查看")

    def agent_search(self):

        try:
            self.time_search()
            choose_agent=self.baseCom.untilTime("XPATH",self.chat_Record_data["chat_Record"]["agent"])
            choose_agent.click()
            time.sleep(2)

            agentName=self.baseCom.untilTime("XPATH",self.chat_Record_data["chat_Record"]["agentName"])
            agentName.click()
            time.sleep(2)

            list_agentName_elem=self.baseCom.untilTime("XPATH",self.chat_Record_data["chat_Record"]["list_agentName"])
            list_agentName=list_agentName_elem.text
            return list_agentName
        except:
            logg.logger.error("无法定位到元素，请速来查看")

    def visitorName_search(self):

        try:
            self.time_search()
            list_visitor_elem=self.baseCom.untilTime("XPATH",self.chat_Record_data["chat_Record"]["list_visitorName"])
            list_visitorName=list_visitor_elem.text

            list_visitorName_elem=self.baseCom.untilTime("XPATH",self.chat_Record_data["chat_Record"]["visitorName"])
            list_visitorName_elem.send_keys(list_visitorName)

            list_visitorName_elem.send_keys(Keys.ENTER)
            time.sleep(2)

            list_visitor_element = self.baseCom.untilTime("XPATH",
                                                       self.chat_Record_data["chat_Record"]["list_visitorName"])
            list_visitor_name = list_visitor_element.text
            return list_visitor_name,list_visitorName
        except:
            logg.logger.error("无法定位元素，请前来查看")

    def exportChatRecord(self):

        try:
            self.time_search()
            exportChatRecord_elem=self.baseCom.untilTime("XPATH",self.chat_Record_data["chat_Record"]["exportChatRecord"])
            exportChatRecord_elem.click()
            time.sleep(5)

            list_visitor_element = self.baseCom.untilTime("XPATH",
                                                       self.chat_Record_data["chat_Record"]["list_visitorName"])
            list_visitor_name = list_visitor_element.text
            return list_visitor_name
        except:
            logg.logger.error("无法定位元素，请前来查看")

    def View_chat_history(self):

        try:
            self.time_search()
            list_visitorName_elem=self.baseCom.untilTime("XPATH",self.chat_Record_data["chat_Record"]["list_visitorName"])
            list_visitorName=list_visitorName_elem.text
            view_chat_elem=self.baseCom.untilTime("LINK_TEXT",self.chat_Record_data["chat_Record"]["View_chat_history"])
            view_chat_elem.click()
            time.sleep(3)

            self.driver.switch_to.default_content()

            iframe_elem=self.baseCom.untilTime("XPATH",self.iframe_data["iframe"]["view_chat_Record"])
            self.driver.switch_to.frame(iframe_elem)
            list_visitor_elem=self.baseCom.untilTime("CSS_SELECTOR",self.chat_Record_data["chat_Record"]["list_VisitorName"])
            list_visitor_elem_text=list_visitor_elem.text
            return list_visitor_elem_text ,list_visitorName
        except:
            logg.logger.error("无法定位元素，请前来查看")








