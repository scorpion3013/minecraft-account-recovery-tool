import json
import os
import random
from multiprocessing.dummy import Pool as ThreadPool
from stuff.config_reader import *
import requests
from termcolor import colored
import stuff.config_reader
from stuff.file_creator import BASIC_PATH
import colorama
colorama.init()


class proxy:
    proxys = []

def proxy_getter():
        if Checker.Proxy.proxy:
            if Checker.Proxy.proxy_check:
                proxy.proxys = checkproxies(ProxyChecker.Settings.thread_amount, ProxyChecker.Settings.timeout / 1000, ProxyChecker.Settings.proxy_judge)
            else:
                proxy.proxys = open(BASIC_PATH + "/proxies.txt").readlines()

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

       if not stuff.config_reader.Checker.Proxy.proxy:
           answer = requests.post('https://authserver.mojang.com/authenticate', data=request_body, headers=headers).content
       else:
           while True:

               proxyy = str(random.choice(proxy.proxys))
               proxy_dict = {
                   'http': "http://" + proxyy.replace("\n",""),
                   'https': "http://" + proxyy.replace("\n","")
               }
               try:
                   answer = requests.post('https://authserver.mojang.com/authenticate', data=request_body, headers=headers, proxies=proxy_dict, timeout=10).content
                   break
               except Exception as e:
                   #print(e)
                   proxy.proxys.remove(proxyy)
                   print("Proxy removed cause it was shit.")
                   continue

       answer_json = json.loads(answer)
   except Exception as e:
       print(e)
       answer_json = 'Invalid credentials'
   return answer_json

def checkproxies(threads, timeout, proxyjudge):
    myip = str(requests.get("https://api.ipify.org/").content.decode())
    proxies = open(BASIC_PATH + "/proxies.txt").readlines()
    working = []

    def proxy_checker(x):
        proxie = proxies[x].replace("\n", "")
        proxy_dict = {
            'http': "http://" + proxie,
            'https': "http://" + proxie
                }
        try:
            r = requests.get(proxyjudge, proxies=proxy_dict, timeout=timeout).content.decode()
            if r.__contains__(myip):
                print(colored(proxie + " Working but transparent", "yellow"))
            else:
                print(colored(proxie + " Working", "green"))
                working.append(proxies[x])
        except:
            print(colored(proxie + " Not Working", "red"))

    def theads_two(numbers, threads=threads):
        pool = ThreadPool(threads)
        results = pool.map(proxy_checker, numbers)
        pool.close()
        pool.join()
        return results

    if __name__ == "stuff.checker":
        countt = []
        for x in range(len(proxies)):
            countt.append(int(x))
        threads_one = theads_two(countt, threads)
    print(colored("\n\nYou have " + str(len(working)) + " working proxies.", "magenta"))
    return working
