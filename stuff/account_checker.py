import json
import requests
import random
import os
from stuff.file_creator import BASIC_PATH

use_proxys = False


def account_login(email_username, password):

   try:

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
       if use_proxys == True:
           proxy = str((random.choice(list(open(BASIC_PATH + os.sep + 'proxies.txt'))))).replace('\n', '')
           http_proxy = "http://" + proxy
           https_proxy = "https://" + proxy

           proxyDict = {
               "http": http_proxy,
               "https": https_proxy,
           }
           answer = requests.post('https://authserver.mojang.com/authenticate', data=request_body, headers=headers,
                                  proxies=proxyDict).content
       else:
            answer = requests.post('https://authserver.mojang.com/authenticate',data=request_body, headers=headers).content

       answer_json = json.loads(answer)
   except Exception as e:
       print(e)
       answer_json = 'Invalid credentials'
   return answer_json



