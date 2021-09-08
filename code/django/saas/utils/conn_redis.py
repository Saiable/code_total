# 链接到数据库
from django.shortcuts import HttpResponse
from django_redis import get_redis_connection

def index(request):
    #去连接池中获取一个连接
    conn = get_redis_connection("defalut")
    # 默认读取defalut的配置，也可以读取其他的，比如master的配置，在settings.py中配置好即可
    # 后期读写分离的时候可以用到
    conn.set('k1','v1',ex=10)
    value = conn.get('k1')
    print(value)
    return HttpResponse('ok')