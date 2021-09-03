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
            print('connect success')
            return conn, cursor
        except Exception as err:
            print(err)

    def create_table(self,data_dict,table_name):
        conn, cursor = self.connect_psql()
        keys = data_dict.keys()
        sql = "create table " + table_name + "(id serial primary key,"
        for field in keys:
            sql += field + " text,"
        sql = sql[:-1] + ");"
        print(sql)
        conn.close()

if __name__ == '__main__':
    store = Postgresql()

    data = {
        'title': 'aaa',
        'content': 'aaaa',
    }

    store.create_table(data_dict=data,table_name="test.mytable")