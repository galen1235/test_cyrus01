
# coding:utf-8

from run_method import RunMain
from handle_excel import *
import json


class RunTestCase:
    def __init__(self):
        self.Runmain = RunMain()  # 实例化调用get/post请求基类
        self.data = HandleExcel()  # 实例化操作excel文件类

    def go_run(self):
        rows_count = self.data.get_rows()   # 获取excel行数
        for i in range(1,rows_count):      # 利用行数进行迭代处理每个接口
            url = self.data.get_value(i, get_url())  # 循环获取url的值

            method = self.data.get_value(i,get_method())  # 循环获取method的值
            data = self.data.get_value(i, get_params()) # 循环获取请求参数

            headers = self.data.get_value(i,get_header())
            headers = json.loads(headers)

            expectvalue = self.data.get_value(i,get_expectvalue())

            '''
            is_run = self.data.get_value(i, get_priority())  # 获取是否运行，即判断excel中priority是不是"H"
            if is_run == 'H':
            '''
            res = self.Runmain.run_main(url, method,headers, data) # 调用get/post主函数

            if expectvalue in res:
                print(f'测试通过{res}')
                self.data.write_value(i, get_resultvalue(), 'pass')
            else:
                print(f"测试不通过{res}")
                self.data.write_value(i, get_resultvalue(), 'fail')


#
if __name__ == '__main__':
    run = RunTestCase()
    run.go_run()