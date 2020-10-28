import os
import unittest
from HTMLTestRunner import HTMLTestRunner

import redConfig
from common.log import Log
read_config=redConfig
logg=Log()
class allTest:
    def __init__(self):
        global logger,reportPath
        logger=logg.get_logger()
        reportPath=logg.get_report_path()
        self.caselistFile=os.path.join(read_config.porDir,"caseList.txt")
        self.caseFile=os.path.join(read_config.porDir,"testCase",)
        print(self.caseFile)
        self.caseList=[]

    def set_case_list(self):
        with open(self.caselistFile)  as fb:
            for value in fb.readlines():
                data=str(value)
                if data !="" and not data.startswith("#"):
                    self.caseList.append(data.replace("\n",""))
                    print(self.caseList)
        fb.close()

    #设置测试套件
    def set_suit_test(self):
        self.set_case_list()
        test_suit=unittest.TestSuite()
        suit_modld=[]
        for case in self.caseList:
            case_name=case.split("/")[-1]
            discover=unittest.defaultTestLoader.discover(self.caseFile,pattern="test*.py",top_level_dir=None)
            if discover not in suit_modld:
                suit_modld.append(discover)
            print("suit_modld是",suit_modld)
        if len(suit_modld)>0:
            for suit in suit_modld:
                for test_name in suit:
                    test_suit.addTest(test_name)
        else:
            return None
        return test_suit
    #执行测试计划
    def run_test(self):

        try:
            suit=self.set_suit_test()
            if suit is not None:
                logger.info("*************test start**************")
                with open(reportPath,"wb") as fp:
                    runner=HTMLTestRunner(stream=fp,title=u'customer_ui自动化测试',description=u'用例执行情况')
                    print(type(runner))
                    runner.run(suit)
            else:
                logger.info("Case does not exist ")
            #fp.close()
        except Exception as ex:
            logger.error(str(ex))
        finally:
            logger.info("**************test end**************")
            fp.close()
if __name__=="__main__":
    object=allTest()
    object.run_test()








