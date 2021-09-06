'''
代理IP的获取
'''


def get_proxy():
    """
    获取代理IP
    :return:
    """
    host2 = "u6213.20.tn.16yun.cn"
    port2 = "6227"
    user2 = '16DSPOXD'
    password2 = '580803'
    
    proxy_meta = "http://%(user)s:%(password)s@%(host)s:%(port)s" % {
        "host": host2,
        "port": port2,
        "user": user2,
        "password": password2,
    }

    proxies = {
        "http": proxy_meta,
        "https": proxy_meta,
    }
    return proxies

