import json
import os
import platform
import random
import time
from multiprocessing.dummy import Pool as ThreadPool
from stuff.config_reader import *
import requests
from termcolor import colored, cprint
import stuff.config_reader
from stuff.file_creator import BASIC_PATH
import colorama
colorama.init()


class proxy:
    proxys = []
    invalid = 0
    working = []


def proxy_getter():
        if Checker.Proxy.proxy:
            if Checker.Proxy.api_use:
                print('Sending proxy api request')
                proxies = requests.get(Checker.Proxy.api_link).content.decode().splitlines()
            else:
                proxies = open(BASIC_PATH + "/proxies.txt").readlines()

            if Checker.Proxy.proxy_check:
                proxy.proxys = checkproxies(proxies, ProxyChecker.Settings.thread_amount, ProxyChecker.Settings.timeout / 1000, ProxyChecker.Settings.proxy_judge)
            else:
                proxy.proxys = proxies


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

               proxyy = proxy.proxys[random.randrange(0, len(proxy.proxys), 1)]
               proxy_dict = {
                   'http': "http://" + proxyy.replace("\n", ""),
                   'https': "https://" + proxyy.replace("\n", "")
               }
               try:
                   answer = requests.post('https://authserver.mojang.com/authenticate', data=request_body, headers=headers, proxies=proxy_dict, timeout=15).content
                   break
               except Exception as e:
                   if Checker.debug:
                       print(proxy)
                       print(e)
                   #proxy.proxys.remove(proxyy)
                   #print("\nInvalid request, repeating.")
                   time.sleep(2)
                   continue

       answer_json = json.loads(answer)
   except Exception as e:
       answer_json = 'Invalid credentials'
   return answer_json

def checkproxies(proxies ,threads, timeout, proxyjudge):
    myip = str(requests.get("https://api.ipify.org/").content.decode())
    windows = False

    if platform.system() == "Windows":
        import ctypes
        windows = True
    def proxy_checker(x):
        proxie = proxies[x].replace("\n", "")
        proxy_dict = {
            'http': "http://" + proxie,
            'https': "https://" + proxie
                }
        if windows:
            ctypes.windll.kernel32.SetConsoleTitleW(
                "MART by scorpion3013 | " +
                "Proxies left: " + str(len(proxies) - (len(proxy.working)+ proxy.invalid)) +
                " | Working: " + str(len(proxy.working)) +
                " | Bad: " + str(proxy.invalid))
        try:
            r = requests.get(proxyjudge, proxies=proxy_dict, timeout=timeout).content.decode()
            if r.__contains__(myip):
                if Checker.Proxy.use_transparent:
                    proxy.working.append(proxies[x])
                    cprint("" + proxie + " Working but transparent", "yellow")
                else:
                    proxy.invalid = proxy.invalid + 1
                    cprint("" + proxie + " Working but transparent", "red")


            else:
                cprint("" + proxie + " Working", "green")
                proxy.working.append(proxies[x])
        except:
            #cprint("\n" + proxie + " Not Working", "red")
            proxy.invalid = proxy.invalid + 1

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
    print(colored("\n\nYou have " + str(len(proxy.working)) + " working proxies.", "magenta"))
    return proxy.working
