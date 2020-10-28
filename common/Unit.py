# -*- encoding:utf-8 -*-
import os

import xlrd
import yaml


from common.log import Log
from redConfig import porDir


class unit():
    def __init__(self):
        pass
    def operaYaml(self,filename):
        file=open(filename,"r",encoding="utf-8")
        data = yaml.load(file, Loader=yaml.FullLoader)
        file.close()
        return data
    #读取测试数据
    def readExcel(self,excel_name,sheet_name):
        cls = []
        # 获取excel路径
        excelPath = os.path.join(porDir, "data", "inputData", excel_name)

        # 打开文件
        try:
            file = xlrd.open_workbook(excelPath)
            sheet = file.sheet_by_name(sheet_name)
            nrows = sheet.nrows
            for i in range(nrows):
                    cls.append(sheet.row_values(i))

            return cls
        except FileExistsError:
            Log().logger.error("文件打开失败")
         #读取导出表格数据
    #def readexcel_Dowload(self):

        #excelName='客服满意度' + '(' + i+=1 +')' + '.xlsx'
