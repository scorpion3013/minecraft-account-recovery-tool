import json
import requests
import random
import os
from file_creator import BASIC_PATH
def account_login(email_username, password):
   try:
       proxy = str((random.choice(list(open(BASIC_PATH + os.sep + 'proxies.txt'))))).replace('\n','')
       headers = {"content-type": "application/json"}
       request_body = json.dumps({
           'agent': {
               'name': 'Minecraft',
               'version': 1
           },
           'username': email_username,
           'password': password,
           'requestUser': 'true'
       })
       http_proxy = "http://" + proxy
       https_proxy = "https://" + proxy

       proxyDict = {
           "http": http_proxy,
           "https": https_proxy,
       }

       answer = requests.post('https://authserver.mojang.com/authenticate',data=request_body, headers=headers, proxies=proxyDict).content

       answer_json = json.loads(answer)
   except Exception as e:
       print(e)
       answer_json = 'Invalid credentials'
   return answer_json



