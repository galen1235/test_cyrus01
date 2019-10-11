
# coding:utf-8

from run_method import RunMain
from handle_excel import *
import json
from auth import Get_auth

class RunTestCase:
    def __init__(self):
        self.Runmain = RunMain()  # 实例化调用get/post请求基类
        self.data = HandleExcel()  # 实例化操作excel文件类

    def go_run(self):
        rows_count = self.data.get_rows()   # 获取excel行数
        token = Get_auth().get_token()
        if token ==10039:
            print('登录接口重复提交！')
        else:
            for i in range(1, rows_count):  # 利用行数进行迭代处理每个接口
                api_name = self.data.get_value(i, get_apiName())
                url = self.data.get_value(i, get_url())  # 循环获取url的值

                method = self.data.get_value(i, get_method())  # 循环获取method的值
                data = self.data.get_value(i, get_params())  # 循环获取请求参数

                headers = self.data.get_value(i, get_header())
                d3 = {}
                d1 = eval(headers)
                d2 = {"Authorization": token}
                d3.update(d1)
                d3.update(d2)
                headers = json.dumps(d3)
                headers = json.loads(headers)
                expectvalue = self.data.get_value(i, get_expectvalue())
                '''
                is_run = self.data.get_value(i, get_priority())  # 获取是否运行，即判断excel中priority是不是"H"
                if is_run == 'H':
                '''
                res = self.Runmain.run_main(url, method, headers, data)  # 调用get/post主函数

                if expectvalue in res:
                    print(f'{api_name}测试通过{res}')
                    self.data.write_value(i, get_resultvalue(), 'pass')
                else:
                    print(f"{api_name}测试不通过{res}")
                    self.data.write_value(i, get_resultvalue(), 'fail')


if __name__ == '__main__':
    run = RunTestCase()
    run.go_run()