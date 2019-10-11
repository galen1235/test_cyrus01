# -*- coding: utf-8 -*-
import requests
import json

# url = 'http://pre.123ssc.net/api/auth/login?client=m'
#
# headers = {'Content-Type': 'application/vnd.sc-api.v1.json',
#            'Origin': 'http://pre.123ssc.net'}
# data = {"flag":"login","Submit":"json","nonce":"5630bff4c12256e42bdf64fde17be651","username":"galen12","password":"d3ad4cee4afad22711421f651119d0d4","loginpass":"hV8t7+9vp87RA+cnuQnocmnGmGd3NZTv1m7QeZ3zDcCYX2lyZDgtM2FbRMiVS8XZyE+fsohpwTOpzs6BSk3VzNCdOFw4quVFQdvA1C7UO3IrBUT8ZR8GW6d5lBOphBw2yTpcbxJZwAEoQyZhBizxEl8jQBcgHci3iTkQVYQhUDM=","validcode":"","key":""}
#
# r = requests.post(url= url,headers=headers,data=json.dumps(data))
# result = r.text
# print(result.encode('utf-8').decode('unicode_escape'))


#

# test1 = {'a':1,'b':'o'}
# test2 = {'a':1,'b':'o','c':3}
# print(type(test1))
# print(type(test2))
# if test1 in test2:
#     print("true")
# else:
#     print("false")


# import requests
#
# def captcha():
#     url = "http://pre.xinyao888.net/api/captcha"
#     # url = "http://123ssc.net/api/captcha"
#     # headers = {"Authorization": "bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwOlwvXC8xMjNzc2MubmV0XC9hcGlcL2F1dGhcL2xvZ2luIiwiaWF0IjoxNTcwNjE1NzkyLCJleHAiOjE1NzEyMjA1OTIsIm5iZiI6MTU3MDYxNTc5MiwianRpIjoiREw5YmcwbzRRQjZ4Sm1lZSIsInN1YiI6IjcxMzY5OSIsInBydiI6ImZjYzQ5NTNmZWQxMzlhODE3Yjk5MzRhNjc2NDIzOWJkNDA1ZGMwZTEiLCJ1c2VybmFtZSI6Imljb24wMDEiLCJzZXNzaWQiOiIwNDU3ZGU3ZTAyZTBkYjYxODhiYzEzOWU4MGU1MGRmNDc0NDk3ZjU4In0.OGM5NGEyZTY5ZTQ1NmE5YTVhMTZiNWE5ZjA5YzExMWExYTNjNTZmOTI1YzZiMzI0YjhmOTBiZTE5ZjA5NTc5ZQ",
#     #            "Content-Type": "application/vnd.sc-api.v1.json"}
#     headers = {"Authorization": "bearer null",
#                "Content-Type": "application/vnd.sc-api.v1.json"}
#     r = requests.get(url=url,headers=headers)
#     print(r.text)
#
# for i in range(1000):
#     captcha()

d1 = {"Content-Type": "application/vnd.sc-api.v1.json","Origin": "http://pre.xinyao888.net"}
d2 = {"a":"b"}
d3 = {}
d3.update(d1)
d3.update(d2)
print(d3)