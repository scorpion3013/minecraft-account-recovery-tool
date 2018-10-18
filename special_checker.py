import requests
import re

def under_four_character_long(USERNAME):
    if len(USERNAME) <= 3:
        return True
    else:
        return False
def hypixel_rank_check(USERNAME):
    try:
        request_response = requests.get('https://plancke.io/hypixel/player/stats/' + USERNAME).content
        if (str(request_response).__contains__("Player not found")): return False
        if str(request_response).__contains__("OWNER"): return 'Owner'
        elif str(request_response).__contains__("ADMIN"): return 'Admin'
        elif str(request_response).__contains__("MOD"): return 'Moderator'
        elif str(request_response).__contains__("HELPER"): return 'Helper'
        elif str(request_response).__contains__("BUILD TEAM"): return 'Builder'
        elif str(request_response).__contains__("YOUTUBE"): return 'YouTube'
        elif str(request_response).__contains__("MVP++"): return 'MVP++'
        elif str(request_response).__contains__("MVP+"): return 'MVP+'
        elif str(request_response).__contains__("MVP"): return 'MVP'
        elif str(request_response).__contains__("VIP+"): return 'VIP+'
        elif str(request_response).__contains__("VIP"): return 'VIP'
        else: return False
    except Exception as e:
        print(e)
        pass
def hypixel_level_check(USERNAME):
    request_response = requests.get('https://plancke.io/hypixel/player/stats/' + USERNAME).content
    if (str(request_response).__contains__("Player not found")):
        return False
    else:
        match = re.search("<b>Level:</b> [1-9]*[^><]*[1-9]*", str(request_response)).group()
        level = match.split("</b> ")
        return level[1]
    
#OG-Account check planned