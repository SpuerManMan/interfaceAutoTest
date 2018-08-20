#coding=utf-8
import os
from interfaceAutoTest import readConfig
from xlrd import open_workbook


def get_xlsx(xlsx_name,sheet_Name):
    xlsx=[]
    # 创建excel路径
    xlsxPath=os.path.join(readConfig.proDir,'testFile',xlsx_name)
    #读取xlsx文件
    file=open_workbook(xlsxPath)
    #读取指定sheet
    sheet=file.sheet_by_name(sheet_Name)
    #读取rows
    rows=sheet.nrows
    for row in range(rows):
        if sheet.row_values(row)[0]!='no':
            xlsx.append(sheet.row_values(row))
    return xlsx


#xls=get_xlsx('case.xlsx','Sheet1')
#print(xls)
