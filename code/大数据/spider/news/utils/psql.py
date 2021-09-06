import psycopg2
from config import POSTGRES_CONFIG

class Postgresql():
    def __init__(self,table_name):
        self.POSTGRES_CONFIG = POSTGRES_CONFIG
        self.table_name = table_name
    # 链接数据库
    def connect_psql(self):
        try:
            conn = psycopg2.connect(**self.POSTGRES_CONFIG)
            cursor = conn.cursor()
            print('connect success')
            return conn, cursor
        except Exception as err:
            print(err)

    def create_table(self,data_dict):
        conn, cursor = self.connect_psql()
        keys = data_dict.keys()
        sql = "create table {0} (id serial primary key,".format(self.table_name)
        for field in keys:
            sql += field + " text,"
        sql = "{0});".format(sql[:-1])
        try:
            cursor.execute(sql)
            conn.commit()
            print("{0}表创建成功".format(self.table_name))
        except Exception as err:
            conn.rollback()
            print(err)
        finally:
            cursor.close()
            conn.close()

    def insert_psql(self, data_dict):
        conn, cursor = self.connect_psql()
        keys = data_dict.keys()
        values = [data_dict.get(key) if data_dict.get(key) else "" for key in keys]
        sql = "insert into {0} ({1}) values (".format(self.table_name,','.join(keys))
        for each in values:
            sql += "%s" + ","  # 转义字符的处理
        sql = sql[:-1] + ")"

        args = list(data_dict.values())
        try:
            cursor.execute(sql,args)
            conn.commit()
            print('数据插入成功')
        except Exception as err:
            conn.rollback()
            print(err)
            return err
        finally:
            cursor.close()
            conn.close()

    def process_data(self,data_dict):
        self.create_table(data_dict)
        self.insert_psql(data_dict)

if __name__ == '__main__':
    store = Postgresql(table_name='public.test33')
    datas = {
        'aa':11,
        'bb':22,
    }
    store.process_data(datas)