import requests
import json
class Get_auth():
    def get_token(self):
        url = "http://pre.xinyao888.net/api/auth/login"
        headers = {"Content-Type": "application/vnd.sc-api.v1.json",
                   "Origin": "http://pre.xinyao888.net",
                   "Authorization": "bearer null"
                   }
        data = {"username":"will00","password":"d3ad4cee4afad22711421f651119d0d4","validcode":"","grant_type":"password","client_id":"10000002","nonce":"b1b9479b27eb8dc34506d79fa8eaf7f8"}
        r = requests.post(url=url,headers=headers,data=json.dumps(data))
        try:
            token = json.loads(r.text)["data"]["token_type"] + " " + json.loads(r.text)["data"]["token"]
            return token
        except TypeError as err:
            message = json.loads(r.text)["message"]
            return message


token = Get_auth()
print(token.get_token())