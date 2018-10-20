import requests
import re

def under_four_character_long(USERNAME):
    if len(USERNAME) <= 3:
        return True
    else:
        return False
def hypixel_rank_check(USERNAME):
	response = str(requests.get('https://plancke.io/hypixel/player/stats/' + USERNAME).text)
	if response.__contains__("Player not found"): return False
	else:
		rank = re.search("\"\[.*?\]", response)
		if(bool(rank) != False):
			match = re.search("\"\[.*?\]", response).group().split("[")[1].split("]")[0]
			return match
		return False
def hypixel_level_check(USERNAME):
    request_response = requests.get('https://plancke.io/hypixel/player/stats/' + USERNAME).content
    if (str(request_response).__contains__("Player not found")):
        return False
    else:
        match = re.search("<b>Level:</b> [1-9]*[^><]*[1-9]*", str(request_response)).group()
        level = match.split("</b> ")
        return level[1]
def mineplex_rank_check(USERNAME):
	response = str(requests.get('https://www.mineplex.com/players/' + USERNAME).text)
	if response.__contains__("That player cannot be found."): return False
	else:
		match = re.search("Rank\(\'.*?\'\)", response).group().split("('")[1].split("')")
		if (match[0] == "PLAYER"): return False 
		return match[0]

#OG-Account check planned