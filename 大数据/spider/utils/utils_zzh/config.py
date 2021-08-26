'''
跟爬虫相关的配置文件信息
'''

# kafka的相关信息
KAFKA_HOST = '192.168.0.14:9092'

# PG库的配置信息
PG_SQL_LOCAL = {
    'database': 'enterprise_open_information_mobile',
    'user': 'postgres',
    'password': 'pg$#aHTF',
    'host': '192.168.0.14',
    'port': "5432"
}


# redis的配置信息

Redis_LOCAL = {
    'host': '127.0.0.1',
    'port': 6379,
    # 'password': 'foobared123',
    'db': 1,
    'max_connections': 128,  # 最大连接数
    'decode_responses': True, # 编码为utf-8
}