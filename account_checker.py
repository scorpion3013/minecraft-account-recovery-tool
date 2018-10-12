import json
import requests


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



       answer = requests.post('https://authserver.mojang.com/authenticate',data=request_body, headers=headers,).content

       answer_json = json.loads(answer)
   except Exception as e:
       print(e)
       answer_json = 'Invalid credentials'
   return answer_json



