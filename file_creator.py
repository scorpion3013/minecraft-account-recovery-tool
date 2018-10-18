import os
import time

BASIC_PATH = str(os.getcwd())
CURRENT_TIME = str(time.strftime('[%d-%m-%Y %H-%M-%S]'))
FOLDER_PATH = BASIC_PATH + '\\result\\' + CURRENT_TIME + '\\'
txt_names = ['insecure', 'minecon', 'optifine', '5zig', 'labymod', 'special_name', 'working', 'hypixelRank', 'hypixelLevel']


def create_files():
    if not os.path.exists(FOLDER_PATH):
        os.makedirs(FOLDER_PATH)
    for x in range(len(txt_names)):
        if not os.path.exists(FOLDER_PATH + txt_names[x] + '.txt'):
            open(FOLDER_PATH + txt_names[x] + '.txt', 'a').close()
