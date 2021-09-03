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
        sql = "create table {0} (id serial primary key,".format(table_name)
        for field in keys:
            sql += field + " text,"
        sql = "{0});".format(sql[:-1])
        try:
            cursor.execute(sql)
            conn.commit()
            print("{0}表创建成功".format(table_name))
        except Exception as err:
            conn.rollback()
            print(err)
        finally:
            cursor.close()
            conn.close()
    def insert_psql(self, data_dict, table_name):
        """
        插入采集到的数据到PG库,sql注入的方法,防止转义字符无法插入
        """
        conn, cursor = self.connect_psql()
        keys = data_dict.keys()
        values = [data_dict.get(key) if data_dict.get(key) else "" for key in keys]
        print(values)
        # sql = "insert into " + tb_name + " (" + ",".join(ks) + ") values ("
        # for each in vs:
        #     sql += "%s" + ","  # 转义字符的处理
        # sql = sql[:-1] + ")"
        # 
        # args = list(meta.values())
        # try:
        #     cursor.execute(sql, args)
        #     conn.commit()
        #     logger.info("插入数据 %s 成功" % str(meta))
        #     return None
        # except Exception as err:
        #     conn.rollback()
        #     logger.error("插入数据 %s 失败, 已回滚! %s" % (str(meta), err))
        #     return err
        # finally:
        #     conn.close()
        #     cursor.close()
if __name__ == '__main__':
    store = Postgresql()

    datas = {
        'title': 'aaa',
        'content': 'aaaa',
        'string1':''
    }
    temp = []
    for data in datas:
        if datas.get(data):
            temp.append(datas.get(data))
        else:
            temp.append('')
    print('temp:',temp)
    store.insert_psql(data_dict=datas,table_name="public.commit_test")