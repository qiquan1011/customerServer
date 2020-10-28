# -*- coding:utf-8 -*-
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class BaseCommon(object):

    def __init__(self, driver):

        self.driver = driver

    def back(self):

        # 浏览器后退按钮
        self.driver.back()

    def forward(self):
        # 浏览器前进按钮
        self.driver.forward()

    def openUrl(self, url):
        self.driver.get(url)

    def maxBroswer(self):
        self.driver.maximize_window()

    def closeBrowser(self):

        self.driver.close()

    def quitBrowser(self):

        self.driver.quit()

    def fresh(self):

        self.driver.refresh()

    def screenshot(self, path):
        # path = "D:\baidu_img.jpg"
        self.driver.get_screenshot_as_file(path)

    def untilTime(self, attrib, attrCont):
        if attrib == "ID":
            elem=WebDriverWait(self.driver, 20, 0.5).until(
                EC.presence_of_element_located((By.ID, attrCont))
            )
        elif attrib == "CLASS_NAME":
             elem=WebDriverWait(self.driver, 20, 0.5).until(
                EC.presence_of_element_located((By.CLASS_NAME, attrCont))
            )
        elif attrib == "CSS_SELECTOR":
            elem=WebDriverWait(self.driver, 20, 0.5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, attrCont))
            )
        elif attrib == "XPATH":
            elem=WebDriverWait(self.driver, 20, 0.5).until(
                EC.presence_of_element_located((By.XPATH, attrCont))
            )
        elif attrib == "LINK_TEXT":
            elem=WebDriverWait(self.driver, 20, 0.5).until(
                EC.presence_of_element_located((By.LINK_TEXT, attrCont))
            )
        elif attrib == "PARTIAL_LINK_TEXT":
            elem=WebDriverWait(self.driver, 20, 0.5).until(
                EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, attrCont))
            )


        return  elem
    def geturl(self):

        self.driver.current_url()
