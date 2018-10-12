import requests
import base64
import json


def minecon_cape_request(UUID):
    try:
        request_reponse = requests.get('https://sessionserver.mojang.com/session/minecraft/profile/' + UUID).json()
        request_reponse_decoded = json.loads(base64.b64decode(request_reponse["properties"][0]["value"]))
        if str(request_reponse_decoded).__contains__("Cape"):
            return True
        else:
            return False
    except Exception as e:
        print(e)
        pass

def five_zig_cape_request(UUID):
    try:
        request_reponse = requests.get('http://textures.5zig.net/textures/2/' + UUID).content
        if len(str(request_reponse)) > 10:
            return True
        else:
            return False
    except Exception as e:
        print(e)
        pass
def optifine_cape_request(USERNAME):
    try:
        request_reponse = requests.get('http://s.optifine.net/capes/' + USERNAME + '.png').content
        if not str(request_reponse).__contains__('Not found'):
            return True
        else:
            return False
    except Exception as e:
        print(e)
        pass
def laby_mod_cape_request(UUID):
    try:
        uuid_with_dashes = UUID[:8] + '-' + UUID[8:12] + '-' + UUID[12:16] + '-' + UUID[16:20] + '-' + UUID[20:]
        request_reponse = requests.get('http://capes.labymod.net/capes/' + uuid_with_dashes).content
        if not str(request_reponse).__contains__('Not Found'):
            return True
        else:
            return False
    except Exception as e:
        print(e)
        pass