

# coding:utf-8

import xlrd
from xlutils.copy import copy

class HandleExcel:
    """封装操作excel的方法"""

    def __init__(self, file='D:/test_cyrus/test_api.xls', sheet_id=0):
        self.file = file
        self.sheet_id = sheet_id
        self.data = self.get_data()
        # 为了在创建一个实例时就获得excel的sheet对象，可以在构造器中调用get_data()
        # 因为类在实例化时就会自动调用构造器，这样在创建一个实例时就会自动获得sheet对象了

    # 获取某一页sheet对象
    def get_data(self):
        data = xlrd.open_workbook(self.file)
        sheet = data.sheet_by_index(self.sheet_id)
        return sheet

    # 获取excel数据行数
    def get_rows(self):
        rows = self.data.nrows
        # t = self.get_data()  # 调用get_data()取得sheet对象(如果不在构造器获取sheet对象，就需要在方法内先获取sheet对象，再进行下一步操作，每个方法都要这样，所以还是写在构造器中方便)
        # rows = t.nrows
        return rows

    # 获取某个单元格数据
    def get_value(self, row, col):
        value = self.data.cell_value(row, col)
        return value

    # 向某个单元格写入数据
    def write_value(self, row, col, value):
        data = xlrd.open_workbook(self.file)  # 打开文件
        data_copy = copy(data)  # 复制原文件
        sheet = data_copy.get_sheet(0)  # 取得复制文件的sheet对象
        sheet.write(row, col, value)  # 在某一单元格写入value
        data_copy.save(self.file)  # 保存文件
'''
# 封装excel的列名常量
def get_caseseq():
    """获取caseSeq"""
    caseSeq = 0
    return caseSeq
'''
'''
def get_apitype():
    """获取apiType"""
    apiType = 1
    return apiType
'''
'''
def get_apiseq():
    """获取apiSeq"""
    apiSeq = 2
    return apiSeq
'''

def get_apiName():
    """获取apiName"""
    apiName = 0
    return apiName

'''
def get_priority():
    """获取priority"""
    priority = 4
    return priority

'''
def get_url():
    """获取url"""
    url = 1
    return url


def get_method():
    """获取method"""
    method = 2
    return method


def get_header():
    """获取header"""
    header = 3
    return header

'''
def get_purpose():
    purpose = 8
    return purpose

'''
def get_params():
    """获取params"""
    params = 4
    return params


def get_expectvalue():
    """获取expectValue"""
    expect = 5
    return expect
def get_resultvalue():
    result = 6
    return result


if __name__ == '__main__':
    test = HandleExcel()
    # print(test.get_data())
    # print(test.get_rows())
    # print(test.get_value(0, 0))
    print(test.get_value(1,get_header()))