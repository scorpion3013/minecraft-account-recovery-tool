import requests
import re
import json
import math


def under_four_character_long(USERNAME):
    if len(USERNAME) <= 3:
        return True
    else:
        return False


def hypixel_checkAPI(USERNAME):
    both = ['', '']
    try:
        request_response = requests.get(
            'https://api.hypixel.net/player?key=79326ca4-54b2-4a8a-a5b4-d9ee111f674b&name=' + USERNAME).content
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


def hypixel_checkPLANK(USERNAME):
    both = ['False', '']
    try:
        request_response = str(requests.get('https://plancke.io/hypixel/player/stats/' + USERNAME).text)
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


def mineplex_rank_check(USERNAME):
    response = str(requests.get('https://www.mineplex.com/players/' + USERNAME).text)
    if response.__contains__("That player cannot be found."):
        return False
    else:
        match = "{group}".format(group=re.search(r"Rank\(\'(.*)\'\)", response).group(1))
        if (match.lower() == "player"):
            return False
        else:
            return match

