from selenium.webdriver import ActionChains

from common.Unit import unit


class serverSatisficing():
    def __init__(self,driver):
        self.driver=driver
        self.data = unit().operaYaml("C:/Users/yunwen/PycharmProjects/customerServer/data/pageData/serverSatisficing.yaml")
        self.iframe_data = unit().operaYaml("C:/Users/yunwen/PycharmProjects/customerServer/data/pageData/iframe.yaml")
    def customer(self):
        return self.driver.find_element_by_xpath(self.data["customer"])

    def customer_text(self):
       return self.driver.find_element_by_xpath(self.data["customer_text"])

    #客服满意度
    def serverSatisficing(self):
        #ele=self.driver.find_element_by_xpath(self.data["customer"])
        #ActionChains(self.driver).move_to_element(ele).perform()
        #self.driver.find_element_by_xpath(self.data["customer_text"]).click()

        return self.driver.find_element_by_xpath(self.data["customerservice"]["serverSatisficing"])

    #客服满意度iframe
    def serverSatisficing_iframe(self):
        return self.driver.find_element_by_xpath(self.iframe_data["iframe"]["serverSatisficing"])
    #时间选择框
    def chooseTime(self):
        return self.driver.find_element_by_xpath(self.data["customerservice"]["chooseTime"])
    #选择最近三个月时间查询
    def threeMonths(self):
        return self.driver.find_element_by_xpath(self.data["customerservice"]["threeMonths"])

    #开始时间
    def startTime(self):
        return self.driver.find_element_by_xpath(self.data["customerservice"]["startTime"])

    #结束时间
    def endTime(self):
        return self.driver.find_element_by_xpath(self.data["customerservice"]["endTime"])


    #总计数据条数
    def allListCount(self):
        return self.driver.find_element_by_xpath(self.data["customerservice"]["allListCount"])
    #满意度
    def satisfaction(self):
        return self.driver.find_element_by_xpath(self.data["condition_Satisfaction"]["satisfaction"])
    #全部满意度
    def allSatisfaction(self):
        return self.driver.find_element_by_xpath(self.data["condition_Satisfaction"]["allSatisfaction"])
    #非常不满意
    def very_Dissatisfied(self):
        return self.driver.find_element_by_xpath(self.data["condition_Satisfaction"]["very_Dissatisfied"])
    #不满意
    def dissatisfied(self):
        return self.driver.find_element_by_xpath(self.data["condition_Satisfaction"]["dissatisfied"])
    #一般
    def commonly(self):
        return self.driver.find_element_by_xpath(self.data["condition_Satisfaction"]["commonly"])
    #满意
    def satisfied(self):
        return self.driver.find_element_by_xpath(self.data["condition_Satisfaction"]["satisfied"])
    #非常满意
    def very_Satisfied(self):
        return self.driver.find_element_by_xpath(self.data["condition_Satisfaction"]["very_Satisfied"])
    #列表满意度
    def list_Satisfied(self):
        return self.driver.find_element_by_xpath(self.data["condition_Satisfaction"]["list_Satisfied"])

    #接待客服选择框
    def choose_CustomerName(self):
        return self.driver.find_element_by_xpath(self.data["condition_Satisfaction"]["customer"])

    #选择客服
    def customer_Name(self):
        return self.driver.find_element_by_xpath(self.data["condition_Satisfaction"]["customer_Name"])
    def list_customer(self):
        return self.driver.find_element_by_xpath(self.data["condition_Satisfaction"]["list_customer"])
    #导出
    def down_looade(self):
        return self.driver.find_element_by_xpath(self.data["condition_Satisfaction"]["downlode"])

    #访客id
    def visitorId(self):
        return  self.driver.find_element_by_xpath(self.data["condition_Satisfaction"]["visitorId"])

    #会话日志按钮
    def chatList(self):
        return  self.driver.find_element_by_xpath(self.data["condition_Satisfaction"]["chatList"])
    #聊天记录中的访客ID
    def message_visitorId(self):
        return self.driver.find_element_by_xpath(self.data["condition_Satisfaction"]["message_visitorId"])
