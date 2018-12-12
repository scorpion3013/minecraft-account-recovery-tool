import yaml
config = yaml.load(open('config.yml','r'))


class Checker:
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

    class Level:
        hypixel_level = bool(config['checker']['level']['b_hypixel'])
        hypixel_min_level = int(config['checker']['level']['i_minlevel_hypixel'])

    class Threads:
        thread_amount = int(config['checker']['threads']['i_threads'])

    class Proxy:
        proxy = bool(config['checker']['proxy']['b_proxy'])
        proxy_check = bool(config['checker']['proxy']['b_check'])

class ProxyChecker:
    class Settings:
        timeout = int(config['proxy_checker']['i_timeout'])
        thread_amount = int(config['proxy_checker']['i_threads'])
        recheck_amount = int(config['proxy_checker']['i_recheck_amount'])
        proxy_judge = str(config['proxy_checker']['s_proxy_judge'])
