"""
数据入PG库
"""
import re
import psycopg2
import psycopg2.extras
import logging

import sys
from os.path import dirname, abspath
sys.path.append(dirname(abspath(__file__)))
sys.path.append(dirname(dirname(abspath(__file__))))

from utils.config import PG_SQL_LOCAL
from utils.log_template import Logger
logger = Logger(init_file=__file__, file_name= "./LOG_INDUSTRY/行业资讯-PG库日志.log",
                logging_level=logging.ERROR).logger_fh()   # pg 库 日志文件


class ItemToPG():
    """
    将数据存储到mysql数据库中
    """

    def __init__(self, tb_name):

        self.tb_name = tb_name
        self.PG_SQL_LOCAL = PG_SQL_LOCAL

    def connectPostgreSQL(self):
        """
        PG库连接
        """
        try:
            conn = psycopg2.connect(**self.PG_SQL_LOCAL)
            cursor = conn.cursor()
            return conn, cursor
        except Exception as err:
            logger.error("数据库连接失败,  %s" % err)
            return None, None

    def createPostgreSQL(self, meta, table_name):

        conn, cursor = self.connectPostgreSQL()
        ks = meta.keys()
        sql = "create table " + table_name + " ("
        sql += "id serial primary key,"
        for each in ks:
            sql += each + " text,"  # each field use text to store
        sql = sql[:-1]
        sql += ");"

        try:
            cursor.execute(sql)
            conn.commit()
            logger.info("创建 %s 表成功" % table_name)
            return None
        except Exception as err:
            conn.rollback()
            logger.error("创建 %s 表失败, 已回滚! %s" % (table_name, err))
            return err
        finally:
            conn.close()
            cursor.close()

    def insertPostgreSQL(self, meta, tb_name):
        """
        插入采集到的数据到PG库,sql注入的方法,防止转义字符无法插入
        """
        conn, cursor = self.connectPostgreSQL()
        data_dict = meta
        ks = data_dict.keys()
        vs = [data_dict.get(k) if data_dict.get(k) else "" for k in ks]
        sql = "insert into " + tb_name + " (" + ",".join(ks) + ") values ("
        for each in vs:
            sql += "%s" + ","  # 转义字符的处理
        sql = sql[:-1] + ")"

        args = list(meta.values())
        try:
            cursor.execute(sql, args)
            conn.commit()
            logger.info("插入数据 %s 成功" % str(meta))
            return None
        except Exception as err:
            conn.rollback()
            logger.error("插入数据 %s 失败, 已回滚! %s" % (str(meta), err))
            return err
        finally:
            conn.close()
            cursor.close()

    def add_field(self, meta, tb_name):
        """
        表字段进行了添加以后要对数据库的表结构进行修改
        """

        # 获取哪些字段需要进行添加的操作
        coloumns = self.query_coloumns(tb_name=tb_name)
        current_keys = list(meta.keys())
        fields = []
        for field in current_keys:
            if field not in coloumns:
                fields.append(field)

        # 进行扩展字段的添加处理
        conn, cursor = self.connectPostgreSQL()
        for field in fields:
            sql = "alter TABLE {0} add if not exists {1} text;".format(tb_name, field)
            try:
                cursor.execute(sql)
                conn.commit()
                logger.info("%s 添加字段 %s 成功" % (tb_name, field))
            except Exception as err:
                conn.rollback()
                logger.error("%s 添加字段 %s 失败, 已回滚! %s" % (tb_name, field, err))
                return err
        conn.close()
        cursor.close()
        return None

    def query_coloumns(self, tb_name):
        """
        查询当前表有哪些字段
        """
        conn, cursor = self.connectPostgreSQL()
        sql = "select * from {0} where id < 100 LIMIT 100".format(tb_name)
        coloumns = []
        try:
            cursor.execute(sql)
            coloumns = [row[0] for row in cursor.description]
            logger.info("%s 表字段有:%s" % (tb_name, str(coloumns)))
        except Exception as err:
            conn.rollback()
            logger.error("查询 %s 表字段 %s 失败" % (tb_name, err))
        finally:
            conn.close()
            cursor.close()

        return coloumns

    def process_item(self, item):

        err = self.insertPostgreSQL(item, self.tb_name)

        # 如果是表不存在, 就创建表并且重新插入数据
        if '"{0}" does not exist'.format(self.tb_name) in str(err):
            err = self.createPostgreSQL(item, self.tb_name)
            if err is None:
                err = self.insertPostgreSQL(item, self.tb_name)
        # 如果是 表字段不一致, 那么插入表字段
        elif re.findall('column (.+?) of relation (.+?) does not exist', str(err)):
            err = self.add_field(item, tb_name=self.tb_name)
            if err is None:
                err = self.insertPostgreSQL(item, self.tb_name)

if __name__ == "__main__":
    store = ItemToPG(tb_name="industry_info.tb_i")
    data = {}
    data["title"] = "123"
    data["static_url"] = ''
    data["abstract"] = '123'
    data["author"] = ''
    data["author1"] = ''
    store.process_item(item=data)

