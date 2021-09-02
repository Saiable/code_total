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

    def create_table(self):
        conn, cursor = self.connect_psql()
        sql = """CREATE TABLE student (
        id serial4 PRIMARY KEY, 
        num int4,
        name varchar(25));"""
        # 执行语句
        cursor.execute(sql)
        print("student table created successfully")
        # 事物提交
        conn.commit()
        # 关闭数据库连接
        conn.close()

if __name__ == '__main__':
    store = Postgresql()
    store.create_table()