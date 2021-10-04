import redis

# conn = redis.Redis(host='1.116.68.249',port='6380',password='foobaredsai',encoding='utf-8')
conn = redis.Redis(host='1.116.68.249',port='6380',encoding='utf-8')

# 设置k1的值为v1，过期时间为10秒
conn.set('k1','v1',ex=10)
value = conn.get('k1')
print(value)
# from django_redis import get_redis_connection
# def redis_test():
#     conn = get_redis_connection()
#     conn.set('k1', 'v1', ex=10)
#     value = conn.get('k1')
#     print(value)
# redis_test()
