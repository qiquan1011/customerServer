import time
from selenium.webdriver import ActionChains

from common.Unit import unit
from common.base import BaseCommon
from common.log import Log
from public.login import login

logg=Log()
class Quality_inspection():
    def __init__(self,driver):
        self.driver=driver
        self.login=login(self.driver)
        self.baseCom=BaseCommon(self.driver)
        self.quality_inspection_data = unit().operaYaml("C:/Users/yunwen/PycharmProjects/customerServer/data/pageData/chat_Record.yaml")
        self.data = unit().operaYaml("C:/Users/yunwen/PycharmProjects/customerServer/data/pageData/serverSatisficing.yaml")
        self.iframe_data = unit().operaYaml("C:/Users/yunwen/PycharmProjects/customerServer/data/pageData/iframe.yaml")
    def Quality_inspection_iframe(self):
        self.login.weadmin_Login()
        time.sleep(3)
        try:
            ele = self.baseCom.untilTime("XPATH", self.data["customer"])
            ActionChains(self.driver).move_to_element(ele).perform()
        except:
            logg.logger.error("ele not find")
        try:
            elem = self.baseCom.untilTime("XPATH", self.data["customer_text"])
            elem.click()
        except:
            print("can not find elem")
        try:
            elem = self.baseCom.untilTime("XPATH", self.quality_inspection_data["Quality_inspection"]["quality_inspection_text"])
            elem.click()
        except:
            print("can not find elem")
        #质检表单配置iframe
        try:
            iframe_satisf = self.baseCom.untilTime("XPATH", self.iframe_data["iframe"]["quality_inspection"])
            # iframe_satisf = self.severSatisFicing.serverSatisficing_iframe()
            self.driver.switch_to.frame(iframe_satisf)
        except:
            print("can not find iframe_satisf")

    def newly_added(self):
        pass


    

