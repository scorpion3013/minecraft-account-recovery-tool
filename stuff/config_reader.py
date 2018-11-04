import yaml
config = yaml.load(open('../config.yml','r'))
dump = yaml.dump
class cape:
    liquidbounce = dump(config['checker']['capes']['b_liquidbounce'])
    optifine = dump(config['checker']['capes']['b_optifine'])
    labymod = dump(config['checker']['capes']['b_labymod'])
    minecon = dump(config['checker']['capes']['b_minecon'])
    fivezig = dump(config['checker']['capes']['b_5zig'])
class hypixel:
    method = dump(config['checker']['hypixel']['i_method'])
    check_api_keys = dump(config['checker']['hypixel']['b_check_api_keys'])
    api_keys = dump(config['checker']['hypixel']['s_api_keys'])
class rank:
    mineplex_rank = dump(config['checker']['rank']['b_mineplex'])
    hypixel_rank = dump(config['checker']['rank']['b_hypixel'])

class level:
    hypixel_level = dump(config['checker']['level']['b_hypixel'])
    hypixel_min_level = dump(config['checker']['level']['i_minlevel_hypixel'])


print(dump(config['checker']['capes']['b_liquidbounce']))