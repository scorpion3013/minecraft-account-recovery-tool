import os
import time

BASIC_PATH = str(os.getcwd())
CURRENT_TIME = str(time.strftime('[%d-%m-%Y %H-%M-%S]'))
FOLDER_PATH = BASIC_PATH + os.sep + 'result' + os.sep + CURRENT_TIME + os.sep
txt_names = ['unsecure', 'minecon', 'optifine', '5zig', 'labymod', 'special_name', 'working', 'hypixelRank',
             'hypixelLevel', 'mineplexRank', "hive", "mineplexLevel"]


def create_files():
    if not os.path.exists(FOLDER_PATH):
        os.makedirs(FOLDER_PATH)
