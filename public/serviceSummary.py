import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from common.Unit import unit
from common.base import BaseCommon
from common.log import Log
from public.login import login

logg=Log()
class Sevice_Summary():
    def __init__(self,driver):
        self.driver=driver
        self.baseCom=BaseCommon(self.driver)
        self.login=login(self.driver)
        self.data = unit().operaYaml(
            "C:/Users/yunwen/PycharmProjects/customerServer/data/pageData/serverSatisficing.yaml")
        self.seviceSummary_data=unit().operaYaml("C:/Users/yunwen/PycharmProjects/customerServer/data/pageData/service_Summary.yaml")
        self.iframe_data = unit().operaYaml("C:/Users/yunwen/PycharmProjects/customerServer/data/pageData/iframe.yaml")
    def service_Summary_iframe(self):
        self.login.weadmin_Login()
        try:
            ele = self.baseCom.untilTime("XPATH", self.data["customer"])
            ActionChains(self.driver).move_to_element(ele).perform()
        except:
            logg.logger.error("ele not find")
        try:
            elem = self.baseCom.untilTime("XPATH", self.data["customer_text"])
            elem.click()
            time.sleep(2)
        except:
            logg.logger.error("can not find elem")

        try:
            elem = self.baseCom.untilTime("XPATH", self.seviceSummary_data["service_Summary"]["serviceSummary"])
            elem.click()
        except:
            print("can not find elem")
        # 人工客服iframe
        try:
            iframe_satisf = self.baseCom.untilTime("XPATH", self.iframe_data["iframe"]["service_Summary"])

            # iframe_satisf = self.severSatisFicing.serverSatisficing_iframe()

            self.driver.switch_to.frame(iframe_satisf)
        except:
            logg.logger.error("进入iframe失败，请检查")

    def time_search(self):
        self.service_Summary_iframe()
        try:
            chooseTime_elem=self.baseCom.untilTime("XPATH",self.seviceSummary_data["service_Summary"]["chooseTime"])
            chooseTime_elem.click()

        except:
            logg.logger.error("无法定位到chooseTime_elem")

        try:
            startTime_elem=self.baseCom.untilTime("XPATH",self.seviceSummary_data["service_Summary"]["startTime"])
            startTime_elem.send_keys(Keys.CONTROL,"a")
            startTime_elem.send_keys("2020-06-24")
            startTime_elem.send_keys(Keys.ENTER)
            time.sleep(2)

        except:
            logg.logger.error("无法定位到last_three_months_elem")

        try:
            list_visitor_name_elem=self.baseCom.untilTime("XPATH",self.seviceSummary_data["service_Summary"]["list_visitorName"])
            list_visitor_name=list_visitor_name_elem.text
        except:
            logg.logger.error("无法定位到list_visitor_name_elem")
        return list_visitor_name


    def visitor_Name_sarch(self):
        self.time_search()
        try:
            visitor_Name_elem=self.baseCom.untilTime("XPATH",self.seviceSummary_data["service_Summary"]["list_visitorName"])
            visitor_Name=visitor_Name_elem.text
        except:
            logg.logger.error("无法定位visitor_name")

        try:
            search_box_elem=self.baseCom.untilTime("XPATH",self.seviceSummary_data["service_Summary"]["search_box"])
            search_box_elem.send_keys(visitor_Name)
            search_box_elem.send_keys(Keys.ENTER)
            time.sleep(3)
        except:
            logg.logger.error("无法定位search_Box_elem")
        finally:
            list_visitor_Name_elem=self.baseCom.untilTime("XPATH",self.seviceSummary_data["service_Summary"]["list_visitorName"])
            list_visitor_Name=list_visitor_Name_elem.text
            return list_visitor_Name,visitor_Name

    def remark_search(self):
        self.time_search()
        try:
            choose_box_elem=self.baseCom.untilTime("XPATH",self.seviceSummary_data["service_Summary"]["choose_box"])
            choose_box_elem.click()
        except:
            logg.logger.error("无法定位到choose_box_elem")
        try:
            remark_elem=self.baseCom.untilTime("XPATH",self.seviceSummary_data["service_Summary"]["remarks"])
            remark_elem.click()
        except:
            logg.logger.error("无法定位到remark_elem")

        try:
            remarkElem=self.baseCom.untilTime("XPATH",self.seviceSummary_data["service_Summary"]["list_remark"])
            remark=remarkElem.text
            searchBox_elem=self.baseCom.untilTime("XPATH",self.seviceSummary_data["service_Summary"]["search_box"])
            searchBox_elem.send_keys(remark)
            searchBox_elem.send_keys(Keys.ENTER)
        except:
            logg.logger.error("无法定位到元素")
        finally:
            list_remark_elem=self.baseCom.untilTime("XPATH",self.seviceSummary_data["service_Summary"]["list_remark"])
            list_remark=list_remark_elem.text
            return list_remark ,remark

    def export(self):

        try:
            self.time_search()
            listVisitorname_elem=self.baseCom.untilTime("XPATH",self.seviceSummary_data["service_Summary"]["list_visitorName"])
            listVisitorname=listVisitorname_elem.text

            export_elem=self.baseCom.untilTime("XPATH",self.seviceSummary_data["service_Summary"]["export"])
            export_elem.click()
            time.sleep(10)
            return listVisitorname
        except:
            logg.logger.error("无法定位元素")


    def view_chatMessage(self):
        self.time_search()
        try:
            view_chatMessage_elem=self.baseCom.untilTime("LINK_TEXT",self.seviceSummary_data["service_Summary"]["view_chatMessage"])
            view_chatMessage_elem.click()
            time.sleep(2)
        except:
            logg.logger.error("无法定位到元素")

        try:
            no_chatMessage_elem=self.baseCom.untilTime("XPATH",self.seviceSummary_data["service_Summary"]["NO_chatMessage"])
            no_chatMessage=no_chatMessage_elem.text
            return  no_chatMessage
        except:
            logg.logger.error("无法定位元素")

    def add_service_type(self,inputData):
        self.service_Summary_iframe()

        try:
            service_type_elem = self.baseCom.untilTime("XPATH",
                                                       self.seviceSummary_data["service_Summary"]["service_type"])
            ActionChains(self.driver).move_to_element(service_type_elem).perform()
        except:
            logg.logger.error("无法找到元素")
        try:
            attend_elem = self.baseCom.untilTime("XPATH", self.seviceSummary_data["service_Summary"]["attend"])
            attend_elem.click()
            time.sleep(2)
        except:
            logg.logger.error("无法定位元素")

        try:
            service_type_name_elem = self.baseCom.untilTime("XPATH", self.seviceSummary_data["service_Summary"][
                'service_type_name'])
            service_type_name_elem.send_keys(inputData)

            confirm_button_elem = self.baseCom.untilTime("XPATH",
                                                         self.seviceSummary_data["service_Summary"]["add_confirm_button"])
            confirm_button_elem.click()
        except:
            logg.logger.error("无法验证成功")
        if inputData=="":

            try:
                result_elem = self.baseCom.untilTime("XPATH", self.seviceSummary_data["service_Summary"]["empty_prompt"])
                result = result_elem.text
                return result
            except:
                logg.logger.error("无法定位元素")

        else:
            try:
                result_elem = self.baseCom.untilTime("XPATH", self.seviceSummary_data["service_Summary"]["sucess_prompt"])
                result = result_elem.text
                print(result)
                return result

            except:
                logg.logger.error("无法定位元素")
            finally:
                self.delect_service_type()




    def delect_service_type(self):
        #self.service_Summary_iframe()

        #try:
            #iframe_satisf = self.baseCom.untilTime("XPATH", self.iframe_data["iframe"]["service_Summary"])

            #iframe_satisf = self.severSatisFicing.serverSatisficing_iframe()

            #self.driver.switch_to.frame(iframe_satisf)
        #except:
            #logg.logger.error("进入iframe失败，请检查")

        try:
            delect_service_type=self.baseCom.untilTime("XPATH",self.seviceSummary_data["service_Summary"]["delect_service_type"])
            delect_service_type.click()
            delect_button=self.baseCom.untilTime("XPATH",self.seviceSummary_data["service_Summary"]["delect_button"])
            delect_button.click()
            delect_confirm_button=self.baseCom.untilTime("XPATH",self.seviceSummary_data["service_Summary"]["delect_confirm_button"])
            delect_confirm_button.click()
        except:
            logg.logger.error("无法定位到元素")












