from common.Unit import unit


class serviceSummary():
    def __init__(self,driver):
        self.driver=driver
        self.data=unit().operaYaml("C:/Users/yunwen/PycharmProjects/customerServer/data/pageData/service_Summary.yaml")
        self.iframe_data=unit().operaYaml("C:/Users/yunwen/PycharmProjects/customerServer/data/pageData/iframe.yaml")
    #服务小结
    def service_Summary(self):
        return self.driver.find_element_by_xpath(self.data["service_Summary"]["serviceSummary"])
    #服务小结iframe
    def serviceSummary_Iframe(self):
        return self.driver.find_element_by_xpath(self.data["iframe"]["service_Summary"])

    #时间选择框
    def chooseTime(self):
        return self.driver.find_element_by_xpath(self.data["service_Summary"]["chooseTime"])

    #最近三个月
    def Last_three_months(self):
        return self.driver.find_element_by_xpath(self.data["service_Summary"]["Last_three_months"])

    #列表中的访客姓名
    def list_visitorName(self):
        return self.driver.find_element_by_xpath(self.data["service_Summary"]["list_visitorName"])


