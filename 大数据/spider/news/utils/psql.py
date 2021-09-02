import psycopg2
from config import POSTGRES_CONFIG

class Postgresql():
    def __init__(self):
        self.POSTGRES_CONFIG = POSTGRES_CONFIG

    # 链接数据库
    def connect_psql(self):
        try:
            conn = psycopg2.connect(**self.POSTGRES_CONFIG)
            cursor = conn.cursor()
            return conn, cursor
        except Exception as err:
            print(err)

if __name__ == '__main__':
    store = Postgresql()
    store.connect_psql()