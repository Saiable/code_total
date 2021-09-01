'''
跟爬虫相关的配置文件信息
'''

# kafka的相关信息
# KAFKA_HOST = '192.168.0.14:9092'

# PG库的配置信息
PG_SQL_LOCAL = {
    'database': 'komablog',
    'user': 'postgres',
    'password': 'psqlsai@345',
    'host': '1.116.68.249',
    'port': "5432"
}


# redis的配置信息

Redis_LOCAL = {
    'host': '1.116.68.249',
    'port': 6380,
    'password': 'foobaredsai',
    'db': 1,
    'max_connections': 128,  # 最大连接数
    'decode_responses': True, # 编码为utf-8
}

