import xlrd
import xlwt
# import xlutils
from xlutils.copy import copy
import os

def readexcel(pathname):
    # 读取Excel
    data = xlrd.open_workbook(pathname)
    table = data.sheets()[0]
    nrows = table.nrows #行数
    ncols = table.ncols #列数

    for i in range(0, nrows):
        rowValues = table.row_values(i)
        for item in rowValues:
            print(item)

# 写Excel文件
'''往EXCEl单元格写内容，每次写一行sheet:页签名称；row：行内容列表；rowIndex：行索引;
　isBold:true:粗字段，false:普通字体'''
def WriteSheetRow(sheet, rowValueList, rowIndex, isBold):
    i = 0
    style = xlwt.easyxf('font:bold 1')
    # style = xlwt.easyxf('font: bold 0, color red;') #红色字体
    # style2 = xlwt.easyxf('pattern: pattern solid, fore_color yellow; font: bold on;') #设置Excel单元格的背景为黄色，字体为粗体
    for value in rowValueList:
        strValue = str(value)
        if isBold:
            sheet.write(rowIndex, i, style)
        else:
            sheet.write(rowIndex, i, strValue)
        i = i + 1

def save_excel(strfile):
    wbk = xlwt.Workbook()
    sheet = wbk.add_sheet('sheet1', cell_overwrite_ok=True)
    headlist = ['Title1', 'Title2', 'Title3', 'Title4', 'Total']
    rowindex = 0
    WriteSheetRow(sheet, headlist, rowindex, False)
    for i in range(1, 11):
        rowindex = rowindex + 1
        valuelist = []
        for j in range(1, 5):
            valuelist.append(j*i)
        WriteSheetRow(sheet, valuelist, rowindex, False)
    wbk.save(strfile)

def add_info(filepath):
    oldwb = xlrd.open_workbook(filepath)
    print(oldwb)
    newwb = copy(oldwb)
    print(newwb)
    newws = newwb.get_sheet(0)
    newws.write(12, 0, 'value1')
    newws.write(12, 1, 'value2')
    newws.write(12, 2, 'value3')
    print("write new values ok")
    newwb.save(r"D:\datacatch\test3.xls")
    pass

def getcolindex(name):
    list1 = ["SJJZ.TY.DZSWJ.nsrdlyz", "SJJZ.SB.cx.cwbaxxCx", "C00.TY.YBSB.nsrsfxxcx", "SJJZ.TY.DZSWJ.nsrdlyz",\
             "Fxsw.FP.cx.YbjcJxXxFpXx","SJJZ.TY.DZSWJ.nsrdlyz", "ETax.SB.SbSubmit3.91061001059"]
    indexofname = list1.index(name)
    if(indexofname > -1):
        return indexofname+1
    return -1

def getrowindex(nsr,table):
    rows = table.nrows
    for i in range(1, rows):
        if(nsr==table(rows, 0)):
            return i
    return rows+1

def writewb(sheet, row, col):
    s = "已录入"
    s2 = "未录入"
    if(sheet.cell(row, 1)==''):
        for i in range (1, 8):
            sheet.write(row, i, s2)
    sheet.write(row, col, s)

def readLog(filename, table):
    a = filename.split('_')
    nsrsbh = a[0]
    sid = a[1][0:-4]
    # print(nsrsbh+" "+sid)
    rows = getrowindex(nsrsbh,table)
    cols = getcolindex(nsrsbh)
    writewb(table, rows, cols)
    pass

def catchFile(pathname, sourcepath, savepath):
    oldwb = xlrd.open_workbook(sourcepath)
    newwb = copy(oldwb)
    sheet = newwb.get_sheet(0)
    list1 = os.listdir(pathname)
    for i in range(0, len(list1)):
        path = os.path.join(pathname, list1[i])
        listfile1 = os.listdir(path)
        for j in range(0, len(listfile1)):
            readLog(listfile1[j], sheet)

    newwb.save(savepath)
    pass


def main():
    # add_info(r"D:\datacatch\test3.xls")
    catchFile(r'D:\datacatch\cal', r'D:\datacatch\test3.xls', r'D:\datacatch\test4.xls')
    # readexcel(r'D:\datacatch\test3.xls')
    pass

main()