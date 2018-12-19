import yaml
config = yaml.load(open('config.yml','r'))


class Checker:
    debug = bool(config['checker']["b_debug"])
    check_amount = int(config['checker']['i_check_amount'])
    class Cape:
        liquidbounce = bool(config['checker']['capes']['b_liquidbounce'])
        optifine = bool(config['checker']['capes']['b_optifine'])
        labymod = bool(config['checker']['capes']['b_labymod'])
        minecon = bool(config['checker']['capes']['b_minecon'])
        fivezig = bool(config['checker']['capes']['b_5zig'])

    class Hypixel:
        method = int(config['checker']['hypixel']['i_method'])
        check_api_keys = bool(config['checker']['hypixel']['b_check_api_keys'])
        api_keys = str(config['checker']['hypixel']['s_api_keys'])

    class Rank:
        mineplex_rank = bool(config['checker']['rank']['b_mineplex'])
        hypixel_rank = bool(config['checker']['rank']['b_hypixel'])
        hivemc_rank = bool(config['checker']['rank']['b_hivemc'])

    class Level:
        hypixel_level = bool(config['checker']['level']['b_hypixel'])
        hypixel_min_level = int(config['checker']['level']['i_minlevel_hypixel'])
        mineplex_level = bool(config['checker']['level']['b_mineplex'])
        mineplex_min_level = int(config['checker']['level']['i_minlevel_mineplex'])

    class Threads:
        thread_amount = int(config['checker']['threads']['i_threads'])

    class Proxy:
        proxy = bool(config['checker']['proxy']['b_proxy'])
        proxy_check = bool(config['checker']['proxy']['b_check'])
        use_transparent = bool(config['checker']['proxy']['b_use_transparent'])

class ProxyChecker:
    class Settings:
        timeout = int(config['proxy_checker']['i_timeout'])
        thread_amount = int(config['proxy_checker']['i_threads'])
        proxy_judge = str(config['proxy_checker']['s_proxy_judge'])
