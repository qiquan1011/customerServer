import json
import os

import requests
import time
from selenium import webdriver

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from common.Unit import unit
from common.base import BaseCommon
from common.log import Log
from public.login import login

logg=Log()
customer_cl=[]
class transfer_to_labor():
    def __init__(self,driver):
        self.driver=driver
        self.login=login(self.driver)
        self.basecom=BaseCommon(self.driver)
        self.data=unit().operaYaml("C:/Users/yunwen/PycharmProjects/customerServer/data/pageData/channl.yaml")
        self.iframe_data=unit().operaYaml("C:/Users/yunwen/PycharmProjects/customerServer/data/pageData/iframe.yaml")
        self.login_data = unit().operaYaml("C:/Users/yunwen/PycharmProjects/customerServer/data/inputData/login.yaml")
#转人工
    def Transfertolabor(self):
        #登录后台，打开访客端

        try:
            self.login.weadmin_Login()
            channl_elem=self.basecom.untilTime("XPATH",self.data["channl"])
            ActionChains(self.driver).move_to_element(channl_elem).perform()
            channl_text_elem=self.basecom.untilTime("XPATH",self.data["channl_text"])
            channl_text_elem.click()



            web_channl_elem=self.basecom.untilTime("XPATH",self.data["web_channl"])
            ActionChains(self.driver).click(web_channl_elem).perform()



            iframe_elem=self.basecom.untilTime("XPATH",self.iframe_data["iframe"]["web_channl"])
            self.driver.switch_to.frame(iframe_elem)

            debugging_elem=self.basecom.untilTime("XPATH",self.data["debugging"])
            debugging_elem.click()
            time.sleep(5)
            url = self.driver.current_url
            print(url)



        #切换回前一个窗口
            all_handles = self.driver.window_handles
            curr_handles=self.driver.current_window_handle
            print(curr_handles)
            for handle in all_handles:
                if handle == curr_handles:
                    self.driver.switch_to.window(handle)
            time.sleep(5)


        #退出管理端

            person_message_elem=self.basecom.untilTime("XPATH",self.data["person_message"])
            ActionChains(self.driver).move_to_element(person_message_elem).perform()
            self.driver.switch_to.default_content()
            login_out_elem=self.basecom.untilTime("XPATH",self.data["out_login"])
            ActionChains(self.driver).click(login_out_elem).perform()

            time.sleep(4)
        #登录座席端

            username_elem=self.basecom.untilTime("XPATH",self.data["username"])
            username_elem.send_keys(self.login_data["customer_login"]["username"])
            time.sleep(3)

            password_elem=self.basecom.untilTime("XPATH",self.data["password"])
            password_elem.send_keys(self.login_data["customer_login"]["password"])
            time.sleep(3)

            login_elem=self.basecom.untilTime("XPATH",self.data["login"])
            login_elem.send_keys(Keys.ENTER)
            time.sleep(3)

            customer_elem=self.basecom.untilTime("XPATH",self.data["customer"])
            customer_elem.click()
            time.sleep(5)

            choose_skill_elem=self.basecom.untilTime("XPATH",self.data["choose_skill"])
            choose_skill_elem.click()
            time.sleep(3)

            skill_status_elem=self.basecom.untilTime("XPATH",self.data["skill_status"])
            skill_status_elem.click()
            time.sleep(3)

            online_elem=self.basecom.untilTime("XPATH",self.data["online"])
            online_elem.click()
            time.sleep(3)

            affirm_elem=self.basecom.untilTime("XPATH",self.data["affirm"])
            affirm_elem.click()


            time.sleep(5)
            self.basecom.fresh()
        #切回访客端转人工
            self.switch_windows()

            Transfer_to_labor_elem=self.basecom.untilTime("XPATH",self.data["Transfer_to_labor"])
            Transfer_to_labor_elem.click()



        #切回坐席端，验证转人工是否成功
            self.switch_windows()

            result_elem=self.basecom.untilTime("XPATH",self.data["visitor_name"])
            result_elem_text=result_elem.text
            return result_elem_text
        except:
            logg.logger.error("无法定位元素，请联系管理员")

#封装切换窗口方法
    def switch_windows(self):
        all_handles = self.driver.window_handles
        curr_handles = self.driver.current_window_handle
        print(curr_handles)
        for handle in all_handles:
            if handle != curr_handles:
                self.driver.switch_to.window(handle)
                time.sleep(5)
#发送文字表情
    def send_news_text(self):
        self.Transfertolabor()
        try:
            send_news_text_elem=self.basecom.untilTime("XPATH",self.data["send_news"]["send_news_text"])
            #send_news_text_elem.click()
            send_news_text_elem.send_keys("你好，我是小弟弟，你是谁")

            send_news_button_elem=self.basecom.untilTime("XPATH",self.data["send_news"]["send_news_button"])
            send_news_button_elem.click()

            time.sleep(3)

            result_text_elem=self.driver.find_elements_by_xpath(self.data["send_news"]["result_text"])
            #result_text_elem_text=result_text_elem.text
            print(result_text_elem)
            for result in result_text_elem:
                if result.text=="你好，我是小弟弟，你是谁":
                    return result.text


            picture_elem=self.basecom.untilTime("XPATH",self.data["picture"])
            ActionChains(self.driver).move_to_element(picture_elem).perform()
            time.sleep(3)
            login_out_elem=self.basecom.untilTime("XPATH",self.data["login_out"])
            login_out_elem.click()
            time.sleep(3)

            login_out_confirm_elem=self.basecom.untilTime("XPATH",self.data["login_out_confirm"])
            login_out_confirm_elem.click()
            time.sleep(3)
        except:
            logg.logger.error("无法定位到元素，请联系管理员检查一下")

#发送表情消息
    def send_news_expression(self):
        try:
            self.Transfertolabor()
            send_news_expression_elem=self.basecom.untilTime("XPATH",self.data["send_news"]["send_news_expression"])
            ActionChains(self.driver).click(send_news_expression_elem).perform()

            send_expression_elem=self.basecom.untilTime("XPATH",self.data["send_news"]["send_expression"])
            ActionChains(self.driver).click(send_expression_elem).perform()

            send_news_button_elem = self.basecom.untilTime("XPATH", self.data["send_news"]["send_news_button"])
            send_news_button_elem.click()
            time.sleep(3)

            result_text_elem = self.driver.find_elements_by_xpath(self.data["send_news"]["result_expression"])
            print(result_text_elem)

            picture_elem=self.basecom.untilTime("XPATH",self.data["picture"])
            ActionChains(self.driver).move_to_element(picture_elem).perform()
            time.sleep(3)
            login_out_elem=self.basecom.untilTime("XPATH",self.data["login_out"])
            login_out_elem.click()
            time.sleep(3)
            login_out_confirm_elem=self.basecom.untilTime("XPATH",self.data["login_out_confirm"])
            login_out_confirm_elem.click()
            time.sleep(3)
            return result_text_elem
        except:
            logg.logger.error("无法定位到元素，请联系管理员检查一下")
#发送视频消息
    def send_news_vidio(self):

        try:
            self.Transfertolabor()
            file_button_elem=self.basecom.untilTime("XPATH",self.data["send_news"]["file_button"])
            ActionChains(self.driver).click(file_button_elem).perform()

            upload_button_elem=self.basecom.untilTime("XPATH",self.data["send_news"]["upload_button"])
            ActionChains(self.driver).click(upload_button_elem).perform()
            os.system("C:/Users/yunwen/PycharmProjects/customerServer/testFile/test_mp4.exe")
            time.sleep(3)
            affirm_button_elem=self.basecom.untilTime("XPATH",self.data["send_news"]["affirm_button"])
            affirm_button_elem.send_keys(Keys.ENTER)



            time.sleep(3)
            result_video_elem = self.driver.find_elements_by_xpath(self.data["send_news"]["result_video"])
            print(result_video_elem)

            picture_elem = self.basecom.untilTime("XPATH", self.data["picture"])
            ActionChains(self.driver).move_to_element(picture_elem).perform()
            time.sleep(3)
            login_out_elem = self.basecom.untilTime("XPATH", self.data["login_out"])
            login_out_elem.click()
            time.sleep(3)

            login_out_confirm_elem = self.basecom.untilTime("XPATH", self.data["login_out_confirm"])
            login_out_confirm_elem.click()
            time.sleep(3)
            return result_video_elem
        except:
            logg.logger.error("无法定位到元素，请联系管理员检查一下")

#发送文件消息
    def send_news_docx(self):
        #self.Transfertolabor()
        try:
            self.Transfertolabor()
            file_button_elem = self.basecom.untilTime("XPATH", self.data["send_news"]["file_button"])
            ActionChains(self.driver).click(file_button_elem).perform()

            upload_button_elem = self.basecom.untilTime("XPATH", self.data["send_news"]["upload_button"])
            ActionChains(self.driver).click(upload_button_elem).perform()
            os.system("C:/Users/yunwen/PycharmProjects/customerServer/testFile/test_docx.exe")
            time.sleep(3)
            affirm_button_elem = self.basecom.untilTime("XPATH", self.data["send_news"]["affirm_button"])
            affirm_button_elem.send_keys(Keys.ENTER)

            time.sleep(3)
            result_docx_elem = self.driver.find_element_by_xpath(self.data["send_news"]["result_docx"])
            print(result_docx_elem.text)

            picture_elem = self.basecom.untilTime("XPATH", self.data["picture"])
            ActionChains(self.driver).move_to_element(picture_elem).perform()
            time.sleep(3)
            login_out_elem = self.basecom.untilTime("XPATH", self.data["login_out"])
            login_out_elem.click()
            time.sleep(3)

            login_out_confirm_elem = self.basecom.untilTime("XPATH", self.data["login_out_confirm"])
            login_out_confirm_elem.click()
            time.sleep(3)
            return result_docx_elem.text
        except:
            logg.logger.error("无法定位到元素，请联系管理员检查一下")
#发送音频消息
    def send_news_audio(self):
        try:
            self.Transfertolabor()
            file_button_elem = self.basecom.untilTime("XPATH", self.data["send_news"]["file_button"])
            ActionChains(self.driver).click(file_button_elem).perform()

            upload_button_elem = self.basecom.untilTime("XPATH", self.data["send_news"]["upload_button"])
            ActionChains(self.driver).click(upload_button_elem).perform()
            os.system("C:/Users/yunwen/PycharmProjects/customerServer/testFile/test_mp3.exe")
            time.sleep(3)
            affirm_button_elem = self.basecom.untilTime("XPATH", self.data["send_news"]["affirm_button"])
            affirm_button_elem.send_keys(Keys.ENTER)

            time.sleep(3)
            result_docx_elem = self.driver.find_element_by_xpath(self.data["send_news"]["result_audio"])
            print(result_docx_elem)

            picture_elem = self.basecom.untilTime("XPATH", self.data["picture"])
            ActionChains(self.driver).move_to_element(picture_elem).perform()
            time.sleep(3)
            login_out_elem = self.basecom.untilTime("XPATH", self.data["login_out"])
            login_out_elem.click()
            time.sleep(3)

            login_out_confirm_elem = self.basecom.untilTime("XPATH", self.data["login_out_confirm"])
            login_out_confirm_elem.click()
            time.sleep(3)
            return result_docx_elem
        except:
            logg.logger.error("无法定位到元素，请联系管理员检查一下")
#发送图片
    def send_news_picture(self):
        try:
            self.Transfertolabor()
            file_button_elem = self.basecom.untilTime("XPATH", self.data["send_news"]["file_button"])
            ActionChains(self.driver).click(file_button_elem).perform()

            upload_button_elem = self.basecom.untilTime("XPATH", self.data["send_news"]["upload_button"])
            ActionChains(self.driver).click(upload_button_elem).perform()
            os.system("C:/Users/yunwen/PycharmProjects/customerServer/testFile/test_jpg.exe")
            time.sleep(3)
            affirm_button_elem = self.basecom.untilTime("XPATH", self.data["send_news"]["affirm_button"])
            affirm_button_elem.send_keys(Keys.ENTER)

            time.sleep(3)
            result_picture_elem = self.driver.find_elements_by_xpath(self.data["send_news"]["result_picture"])
            print(result_picture_elem)

            picture_elem = self.basecom.untilTime("XPATH", self.data["picture"])
            ActionChains(self.driver).move_to_element(picture_elem).perform()
            time.sleep(3)
            login_out_elem = self.basecom.untilTime("XPATH", self.data["login_out"])
            login_out_elem.click()
            time.sleep(3)

            login_out_confirm_elem = self.basecom.untilTime("XPATH", self.data["login_out_confirm"])
            login_out_confirm_elem.click()
            time.sleep(3)
            return result_picture_elem
        except:
            logg.logger.error("未定位到元素，请来查看原因")
#发起邀评
    def send_Satisfacted_Invite(self):
        try:
            self.Transfertolabor()
            send_Satisfacted_Invite_elem=self.basecom.untilTime("XPATH",self.data["send_news"]["send_Satisfacted_Invite"])
            ActionChains(self.driver).click(send_Satisfacted_Invite_elem).perform()

            self.switch_windows()
            commonly_elem=self.basecom.untilTime("XPATH",self.data["send_news"]["commonly"])
            commonly_elem.click()
            time.sleep(3)
            feedback_elem=self.basecom.untilTime("XPATH",self.data["send_news"]["feedback"])
            feedback_elem.send_keys("小菜正在为您转人工哦,请耐心等待,您也可以继续和我交流哦,谢谢啦~")
            time.sleep(3)
            button_affirm_elem=self.basecom.untilTime("XPATH",self.data["send_news"]["button_affirm"])
            ActionChains(self.driver).click(button_affirm_elem).perform()
            time.sleep(4)

            chat_end_elem=self.basecom.untilTime("XPATH",self.data["send_news"]["chat_end"])
            chat_end_elem.click()

            replay_elems=self.basecom.untilTime("XPATH",self.data["send_news"]["replay"])
            replay_elems_text=replay_elems.text

            self.switch_windows()
            time.sleep(4)
            picture_elem = self.basecom.untilTime("XPATH", self.data["picture"])
            ActionChains(self.driver).move_to_element(picture_elem).perform()
            time.sleep(3)
            login_out_elem = self.basecom.untilTime("XPATH", self.data["send_news"]["Switching_system"])
            login_out_elem.click()
            time.sleep(3)
            all_handles = self.driver.window_handles
            print(all_handles)

            self.driver.switch_to.window(all_handles[-1])
            time.sleep(5)
            curr_handles = self.driver.current_window_handle
            print(curr_handles)

            customer_ele = self.basecom.untilTime("XPATH", self.data["send_news"]["customer"])
            ActionChains(self.driver).move_to_element(customer_ele).perform()
            customer_text_elem = self.basecom.untilTime("XPATH", self.data["send_news"]["customer_text"])
            customer_text_elem.click()
            time.sleep(2)
            customerservice_elem = self.basecom.untilTime("XPATH", self.data["send_news"]["customerservice"]["serverSatisficing"])
            customerservice_elem.click()
                # 人工客服iframe
            iframe_satisf = self.basecom.untilTime("XPATH", self.iframe_data["iframe"]["serverSatisficing"])
                # iframe_satisf = self.severSatisFicing.serverSatisficing_iframe()
            self.driver.switch_to.frame(iframe_satisf)

            list_Satisfied_elem=self.basecom.untilTime("XPATH",self.data["send_news"]["list_Satisfied"])
            list_Satisfied_elem_text=list_Satisfied_elem.text
            return list_Satisfied_elem_text

            #picture_elem = self.basecom.untilTime("XPATH", self.data["picture"])
            #ActionChains(self.driver).move_to_element(picture_elem).perform()
            #time.sleep(3)
            #login_out_elem = self.basecom.untilTime("XPATH", self.data["login_out"])
            #login_out_elem.click()
            #time.sleep(3)

            #login_out_confirm_elem = self.basecom.untilTime("XPATH", self.data["login_out_confirm"])
            #login_out_confirm_elem.click()
            #time.sleep(3)




        except:
            logg.logger.error("请留意，无法定位到元素")
            #self.switch_windows()

#填写服务小结
    def send_summary(self):
        try:
            self.Transfertolabor()
            summary_elem = self.basecom.untilTime("XPATH",self.data["send_news"]["summary"])
            ActionChains(self.driver).click(summary_elem).perform()

            summary_type_elem=self.basecom.untilTime("XPATH",self.data["send_news"]["summary_type"])
            ActionChains(self.driver).click(summary_type_elem).perform()

            summary_type_menu_elem=self.basecom.untilTime("XPATH",self.data["send_news"]["summary_type_menu"])
            ActionChains(self.driver).click(summary_type_menu_elem).perform()

            summary_remarks_elem=self.basecom.untilTime("XPATH",self.data["send_news"]["summary_remarks"])
            summary_remarks_elem.send_keys("俺乃燕人张翼得，尔等还不速速离去")

            summary_affirm_button_elem=self.basecom.untilTime("XPATH",self.data["send_news"]["summary_affirm_button"])
            summary_affirm_button_elem.click()

            close_chat_elem=self.basecom.untilTime("XPATH",self.data["send_news"]["close_chat"])
            close_chat_elem.click()

            close_chat_affirm_elem=self.basecom.untilTime("XPATH",self.data["send_news"]["close_chat_affirm"])
            close_chat_affirm_elem.click()

            picture_elem = self.basecom.untilTime("XPATH", self.data["picture"])
            ActionChains(self.driver).move_to_element(picture_elem).perform()
            time.sleep(3)
            login_out_elem = self.basecom.untilTime("XPATH", self.data["send_news"]["Switching_system"])
            login_out_elem.click()
            time.sleep(3)
            all_handles = self.driver.window_handles
            print(all_handles)

            self.driver.switch_to.window(all_handles[-1])
            time.sleep(5)
            curr_handles = self.driver.current_window_handle
            print(curr_handles)
            customer_ele = self.basecom.untilTime("XPATH", self.data["send_news"]["customer"])
            ActionChains(self.driver).move_to_element(customer_ele).perform()
            customer_text_elem = self.basecom.untilTime("XPATH", self.data["send_news"]["customer_text"])
            customer_text_elem.click()
            time.sleep(2)
            customerservice_elem = self.basecom.untilTime("XPATH",
                                                      self.data["send_news"]["service_Summary"]["serviceSummary"])
            customerservice_elem.click()
            # 人工客服iframe
            iframe_satisf = self.basecom.untilTime("XPATH", self.iframe_data["iframe"]["service_Summary"])
            # iframe_satisf = self.severSatisFicing.serverSatisficing_iframe()
            self.driver.switch_to.frame(iframe_satisf)

            list_summary_remarks_elem=self.basecom.untilTime("XPATH",self.data["send_news"]["list_summary_remarks"])
            list_summary_remarks_elem_text=list_summary_remarks_elem.text

            return  list_summary_remarks_elem_text
        except:
            logg.logger.error("出现问题，请来查看一下")

#创建讨论组
    def create_chat_group(self):
        try:
            self.Transfertolabor()
            self.get_customer_login()
            self.get_register()
            create_group_button_elem=self.basecom.untilTime("XPATH",self.data["send_news"]["create_group_button"])
            ActionChains(self.driver).click(create_group_button_elem).perform()

            after_kefu_elem=self.basecom.untilTime("XPATH",self.data["send_news"]["after_kefu"])
            ActionChains(self.driver).click(after_kefu_elem).perform()

            check_box_elem=self.basecom.untilTime("XPATH",self.data["send_news"]["check_box"])
            check_box_elem.click()

            choose_affirm_button_elem=self.basecom.untilTime("XPATH",self.data["send_news"]["choose_affirm_button"])
            choose_affirm_button_elem.click()

            chat_group_elem=self.basecom.untilTime("XPATH",self.data["send_news"]["chat_group"])
            chat_group_elem_text=chat_group_elem.text
            print(chat_group_elem_text)
            close_chat_elem = self.basecom.untilTime("XPATH", self.data["send_news"]["close_chat"])
            close_chat_elem.click()

            close_chat_affirm_elem = self.basecom.untilTime("XPATH", self.data["send_news"]["close_chat_affirm"])
            close_chat_affirm_elem.click()




            return chat_group_elem_text
            #chat_group_elem.click()
            '''
            visitor_name_elem=self.basecom.untilTime("XPATH",self.data["send_news"]["visitor_name"])
            visitor_name_elem_text=visitor_name_elem.text
            print(visitor_name_elem_text)
            return visitor_name_elem_text
            '''
        except:
            logg.logger.error("请求失败，请前往查看")


        '''   
            #options = webdriver.ChromeOptions()
            #options.add_argument("--incognito")
            #driver = webdriver.Chrome(chrome_options=options)

            #js='window.open("http://v5-dev-customer.faqrobot.net/webcustomer/index_standard.html#/login")'
            #self.driver.execute_script(js)
            #driver.get("http://v5-dev-customer.faqrobot.net/webcustomer/index_standard.html#/login")
            #driver.maximize_window()


            #all_handles = self.driver.window_handles
            #print(all_handles)

            #self.driver.switch_to.window(all_handles[-1])
            #time.sleep(5)
            #username_elem=self.basecom.untilTime("XPATH",self.data["send_news"]["customer_username"])
            #username_elem.send_keys("auto_kefu")

            password_elem=self.basecom.untilTime("XPATH",self.data["send_news"]["customer_password"])
            password_elem.send_keys("123456abc")

            customer_login_button_elem=self.basecom.untilTime("XPATH",self.data["send_news"]["customer_login_button"])
            customer_login_button_elem.click()

            choose_skill_elem = self.basecom.untilTime("XPATH", self.data["choose_skill"])
            choose_skill_elem.click()
            time.sleep(3)

            skill_status_elem = self.basecom.untilTime("XPATH", self.data["skill_status"])
            skill_status_elem.click()
            time.sleep(3)

            online_elem = self.basecom.untilTime("XPATH", self.data["online"])
            online_elem.click()
            time.sleep(3)

            affirm_elem = self.basecom.untilTime("XPATH", self.data["affirm"])
            affirm_elem.click()
        except:
            logg.logger.error("无法定位元素，请前往查看")
    '''

    def get_customer_login(self):
        send_pearm = {"username": "auto_kefu", "password": "123456abc", "isRememberMe": "false"}
        # baseUrl = local_read_Config.get_HTTP("baseUrl")
        header = {"Content-Type": "application/x-www-form-urlencoded",
                  "Authorization": "Basic bml5YXpob3U6MTIzNDU2YWJj",
                  "Referer": "http://v5-dev-customer.faqrobot.net/webcustomer/index_standard.html",
                  "Accept": "application/json, text/plain, */*"}
        customer_login = requests.post("http://v5-dev-customer.faqrobot.net/customerservice/login", params=send_pearm,
                                       headers=header)
        customer_cookie = requests.utils.dict_from_cookiejar(customer_login.cookies)
        if len(customer_cl) > 0:
            del customer_cl[-len(customer_cl):]
            print(customer_cl)
        for k, v in customer_cookie.items():
            if k + ":" + v:
                s = k + "=" + v

                customer_cl.append(s)
        login_customer_cookies = ";".join(customer_cl)

        print(login_customer_cookies)
        return login_customer_cookies

    # 获取客服信息
    def get_agentInfo(self):
        header = {"cookie":self.get_customer_login()}
        response = requests.get("http://v5-dev-customer.faqrobot.net/customerservice/webim/agent/agentInfo",
                                headers=header)
        print(response.json())
        tenantId = response.json()["data"]["agent"]["tenantId"]
        return tenantId

    # 客服上线技能组
    def get_register(self):
        send_param = [{"tenantId":"149","groupId":"1000010343","groupName":"售后客服","agentId":"30351",
                       "agentName":"","status":"ONLINE","orginStatus":"LEAVE","agentStatus":1,"orginAgentStatus":3}]
        data = json.dumps(send_param)
        header = {"Content-Type": "application/json;charset=UTF-8",
                  "cookie": self.get_customer_login()}
        register_response = requests.post("http://v5-dev-customer.faqrobot.net/customerservice/webim/agent/setUpAgentGroupStatus",
                                          data=data, headers=header)
        print("客服上线技能组：", register_response.json())

'''    
    def logout(self):
        header={"cookie":self.get_customer_login()}
        logout_reponse=requests.get("http://v5-dev-customer.faqrobot.net/customerservice/logout",headers=header)
        print(logout_reponse.json())
'''





































