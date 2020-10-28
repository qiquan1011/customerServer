
from common.Unit import unit


class chatRecord():
    def __init__(self,driver):
        self.driver=driver
        self.data=unit().operaYaml("C:/Users/yunwen/PycharmProjects/customerServer/data/pageData/chat_Record.yaml")
        self.iframe_data=unit().operaYaml("C:/Users/yunwen/PycharmProjects/customerServer/data/pageData/iframe.yaml")
    #
    def chat_Record_text(self):
        return self.driver.find_element_by_xpath(self.data["chat_Record"]["chat_Record_text"])

    def chat_Record_iframe(self):
        return  self.driver.find_element_by_xpath(self.iframe_data["iframe"]["chat_Record"])

    def chooseTime(self):
        return self.driver.find_element_by_xpath(self.data["chat_Record"]["chooseTime"])
    def startTime(self):
        return  self.driver.find_element_by_xpath(self.data["chat_Record"]["startTime"])

    def endTime(self):
        return self.driver.find_element_by_xpath(self.data["chat_Record"]["endTime"])
    #最近2个月
    def now_twoMouth(self):
        return self.driver.find_element_by_xpath(self.data["chat_Record"]["now_twoMouth"])
    #列表总条数
    def list_Count(self):
        return  self.driver.find_element_by_xpath(self.data["chat_Record"]["list_Count"])
    #渠道
    def channel_choose(self):
        return self.driver.find_element_by_xpath(self.data["chat_Record"]["channel"])

    #网页渠道
    def pc_channel(self):
        return self.driver.find_element_by_xpath(self.data["chat_Record"]["pc_channel"])
    #渠道售前技术
    def channel_name(self):
        return self.driver.find_element_by_xpath(self.data["chat_Record"]["channel_name"])

    #满意度选择框
    def choose_satisfic(self):
        return self.driver.find_element_by_xpath(self.data["chat_Record"]["satisficing"])

    #非常满意
    def very_satisfic(self):
        return self.driver.find_element_by_xpath(self.data["chat_Record"]["very_satisficing"])
    #技能组选择框
    def choose_group(self):
        return self.driver.find_element_by_xpath(self.data["chat_Record"]["group"])
    #售前技能组
    def groupName(self):
        return self.driver.find_element_by_xpath(self.data["chat_Record"]["groupName"])
    #列表中的技能组

    def list_groupName(self):
        return self.driver.find_element_by_xpath(self.data["chat_Record"]["list_groupName"])

    #客服选择框
    def choose_agent(self):
        return self.driver.find_element_by_xpath(self.data["chat_Record"]["agent"])

    #kefu01

    def agentName(self):
        return self.driver.find_element_by_xpath(self.data["chat_Record"]["agentName"])

    #列表中的客服姓名
    def list_agentName(self):
        return self.driver.find_element_by_xpath(self.data["chat_Record"]["list_agentName"])

    #列表中访客姓名
    def list_visitorName(self):
        return self.driver.find_element_by_xpath(self.data["chat_Record"]["list_visitorName"])

    #访客信息输入框

    def visitorName(self):
        return self.driver.find_element_by_xpath(self.data["chat_Record"]["visitorName"])

    #导出
    def exportChatRecord(self):
        return self.driver.find_element_by_xpath(self.data["chat_Record"]["exportChatRecord"])

    #查看聊天消息
    def View_chat_history(self):
        return self.driver.find_element_by_xpath(self.data["chat_Record"]["View_chat_history"])

    def list_VisitorName(self):
        return self.driver.find_element_by_selector(self.data["chat_Record"]["list_VisitorName"])








