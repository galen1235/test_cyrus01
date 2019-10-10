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

test1 = {'a':1,'b':'o'}
test2 = {'a':1,'b':'o','c':3}
print(type(test1))
print(type(test2))
if test1 in test2:
    print("true")
else:
    print("false")