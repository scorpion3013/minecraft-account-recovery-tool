import json
import math
import random
import re

import requests

from stuff.file_creator import BASIC_PATH


def remove_empty_lines_and_newlines(listt):

    for i in range(0, len(listt)):
        listt[i] = listt[i].replace("\n", "")
    list(filter(None, listt))
    return listt


def under_four_character_long(username):
    if len(username) <= 3:
        return True
    else:
        return False


class Keys:
    hypixelkeys = remove_empty_lines_and_newlines(open(BASIC_PATH + "/hypixel_api_keys.txt").readlines())





def hypixel_check_api(username):
    both = ['', '']
    try:
        api_key = str(random.choice(Keys.hypixelkeys))
        request_response = requests.get(
            'https://api.hypixel.net/player?key=' + api_key + "&name=" + username).content
        answer_json = json.loads(request_response)
        rank = ''
        level = ''
        try:
            level = math.floor(-2.5 + math.sqrt(12.25 + 8 * 10 ** -4 * answer_json["player"]['networkExp']))
        except:
            pass
        try:
            rank = rank + '|' + str(answer_json["player"]['rank'])
        except:
            pass
        try:
            rank = rank + '|' + str(answer_json["player"]['newPackageRank']).replace('_PLUS', '+')
        except:
            pass
        try:
            rank = rank + '|' + str(answer_json["player"]['packageRank']).replace('_PLUS', '+')
        except:
            pass
        try:
            if not str(answer_json["player"]['monthlyPackageRank']) == 'NONE':
                rank = rank + '|' + str(answer_json["player"]['monthlyPackageRank']).replace('SUPERSTAR', 'MVP++')
        except:
            pass
        if rank == '':
            both[0] = 'False'
        else:
            both[0] = rank
        if level == '':
            both[1] = 0
        else:
            both[1] = int(level)
        return both
    except:
        print('Hypixel API is Down')
        both[1] = 0
        both[0] = 'False'
        return both


def hypixel_check_plank(username):
    both = ['False', '']
    try:
        request_response = str(requests.get('https://plancke.io/hypixel/player/stats/' + username).text)
        if request_response.__contains__("Hypixel Api down"):
            print('Hypixel API is Down or Plank error')
            both[1] = 0
            both[0] = 'False'
        else:
            if request_response.__contains__("Player not found"):
                both[1] = 0
                both[0] = 'False'
            else:
                both[1] = re.search(r"<b>Level:<\/b> (\d*).\d*<br \/>", request_response).group(1)
                both[0] = re.search(r"content=\"\[([\S]*)]", request_response).group(1)
            return both
    except:
        return both


def mineplex_check(username):
    both = ['False', '']
    try:
        response = str(requests.get('https://www.mineplex.com/players/' + username).text)
        if response.__contains__("That player cannot be found."):
            both[1] = 0
            both[0] = 'False'
        else:
            both[1] = re.search(r">Level (.*)<\/b>", response).group(1)
            both[0] = re.search(r"Rank\(\'(.*)\'\)", response).group(1)
            if both[0].lower() == "player":
                both[0] = "False"
        return both
    except Exception as e:
        return both

def hivemc_rank_check(username):
    try:
        response = str(requests.get('https://www.hivemc.com/player/' + username).text)
        if response.__contains__("That player cannot be found."):
            return False
        else:
            match = "{group}".format(group=re.search(r"<p class=\"rank.*\">(.*)<\/p>", response).group(1))
            if match.lower() == "regular":
                return False
            else:
                return match
    except:
        return False
        
def namemc_searches(username):
    try:
        response = str(requests.get('https://namemc.com/search?&q={0}'.format(username), headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'}))
        match = "{group}".format(group=re.search(r"Searches: (.*)/", response).group(1))
        if int(match) == 1: return str(0)
        return match
    except:
        return False