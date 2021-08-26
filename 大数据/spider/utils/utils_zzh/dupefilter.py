"""
redis去重
"""

import hashlib
import logging
import traceback

import redis
from collections import Counter
import time

# 用来添加当前文件的目录
import sys
from os.path import dirname, abspath
sys.path.append(dirname(abspath(__file__)))
sys.path.append(dirname(dirname(abspath(__file__))))

# redis配置
from utils.config import Redis_LOCAL

# 日志输出
from utils.log_template import Logger
logger = Logger(init_file=__file__, file_name="./LOG_INDUSTRY/行业资讯-redis日志.log",
                logging_level=logging.ERROR).logger_fh()  # redis日志文件


class RFPDupeFilter:
    '''
    设置三种去重方式,第一种是按照title去重,
    第二种是按照url去重,
    第三种是按照title和url去重
    可以获取 title字典的长度以及url字典的长度,
    主要是用于判断后面更新的时候采集的页数的
    老化机制设置为七天前的数据删除
    '''

    def __init__(self, tb_name):
        """
        初始化函数, 分别初始化 redis连接以及 url字典和title字典
        """
        self.tb_name = tb_name
        self.redis = ''  # redis对象
        self.queue_url = 'rqyq_industry_history_url:' + tb_name
        self.queue_title = 'rqyq_industry_history_title:' + tb_name
        self.conn_pool = redis.ConnectionPool(**Redis_LOCAL)  # 连接池

    def get_redis(self):
        # 获去一个redis连接对象
        while True:
            try:
                redis1 = redis.Redis(connection_pool=self.conn_pool)
                redis1.ping()
            except Exception as e:
                err = traceback.format_exc()
                logger.error(err)
                time.sleep(10)
                self.conn_pool = redis.ConnectionPool(**Redis_LOCAL)  # 出问题重新生成一下redis池
            else:  # 执行没有问题
                self.redis = redis1
                return

    def redis_decorator(func):
        """
        redis对象生成装饰器, 不用这个装饰器也可以,只要在每个用到redis的
        代码中调用一下self.get_redis() 就可以了
        """
        def b(self, *args, **kwargs):
            self.get_redis()
            return func(self, *args, **kwargs)
        return b

    @redis_decorator
    def get_title_len(self):
        """
        获取title字典的长度
        """
        title_length = self.redis.hlen(self.queue_title)
        logger.info("%s 字典长度为 %s" % (self.queue_title, str(title_length)))
        return title_length

    @redis_decorator
    def get_url_len(self):
        """
        获取 url字典的长度
        """
        url_length = self.redis.hlen(self.queue_url)
        logger.info("%s 字典长度为 %s" % (self.queue_url, str(url_length)))
        return url_length

    @redis_decorator
    def is_save(self):
        """
        判断是运行初始爬虫还是更新爬虫
        """
        title_length = self.get_title_len()
        url_length = self.get_url_len()
        is_save = title_length or url_length  # 返回的数字
        is_save_flag = True if is_save >= 1 else False
        logger.info("%s 是否采集过: %s" % (self.tb_name, str(is_save_flag)))
        return is_save_flag


    def get_md5(self, val):
        """
        把目标数据进行哈希，用哈希值去重更快
        """
        md5 = hashlib.md5()
        md5.update(val.encode('utf-8'))
        return md5.hexdigest()

    @redis_decorator
    def add_title(self, title):
        """
        在字典中添加一个 title的哈希值
        """
        now_time = round(time.time())
        is_exist = self.exist_title(title)
        if is_exist:
            logger.info("%s 已经采集过,插入失败" % title)
            return False
        else:
            pipe = self.redis.pipeline(transaction=True)  # 开启原子性操作失误
            # 将 title添加到字典中
            pipe.hset(name=self.queue_title, key=self.get_md5(title), value=now_time)  # 注意是 保存set的方式
            res = pipe.execute()
            logger.info("%s 未采集,插入成功" % title)
            return True

    @redis_decorator
    def exist_title(self, title):
        """
        判断 title的哈希值是否存在于字典中
        """
        pipe = self.redis.pipeline(transaction=True)  # 开启原子性操作失误
        pipe.hexists(self.queue_title, self.get_md5(title))
        res = pipe.execute()  # 提交所有的操作
        dict_count = Counter(res)  # 统计返回的结果

        count_rp = dict_count.get(1)
        if count_rp:
            logger.info("%s 已存在" % title)
            return True
        else:
            logger.info("%s 未存在" % title)
            return False

    @redis_decorator
    def add_url(self, url):
        """
        在字典中添加一个 url的哈希值
        """
        now_time = round(time.time())  # 当前时间
        is_exist = self.exist_url(url)
        if is_exist:
            logger.info("%s 已经采集过,插入失败" % url)
            return False
        else:
            pipe = self.redis.pipeline(transaction=True)  # 开启原子性操作失误
            # 将 url添加到字典中
            pipe.hset(name=self.queue_url, key=self.get_md5(url), value=now_time)  # 注意是 保存set的方式
            res = pipe.execute()
            logger.info("%s 未采集,插入成功" % url)
            return True

    @redis_decorator
    def exist_url(self, url):
        """
        判断 url的哈希值是否存在于字典中
        """
        pipe = self.redis.pipeline(transaction=True)  # 开启原子性操作失误
        pipe.hexists(self.queue_url, self.get_md5(url))
        res = pipe.execute()  # 提交所有的操作
        dict_count = Counter(res)  # 统计返回的结果
        count_rp = dict_count.get(1)
        if count_rp:
            logger.info("%s 已存在" % url)
            return True
        else:
            logger.info("%s 未存在" % url)
            return False

    @redis_decorator
    def add_title_url(self, title, url):
        """
        在 queue中字典中添加一个值,
        如果在程序中先判断是否已经插入过,可以省略判断是否存在的代码
        保险起见,暂时先留着
        如果只直接插入的话,这行代码必须留着,
        如果插入成功的话返回 True, 说明这个url没有采集过
        否则就是False ,说明已经存在了
        """
        now_time = round(time.time())
        is_exist = self.exist_title_url(title, url)
        if is_exist:
            logger.info("%s 和 %s 已经采集过, 插入失败" % (title, url))
            return False
        else:
            pipe = self.redis.pipeline(transaction=True)  # 开启原子性操作失误
            # 将 url添加到字典中
            pipe.hset(name=self.queue_url, key=self.get_md5(url), value=now_time)  # 注意是 保存set的方式
            # 将title的hash值添加到字典中
            pipe.hset(name=self.queue_title, key=self.get_md5(title), value=now_time)  # 注意是 保存set的方式
            res = pipe.execute()
            logger.info("%s 和 %s 未采集, 插入成功" % (title, url))
            return True

    @redis_decorator
    def exist_title_url(self, title, url):
        """
        判断queue字典中是否包含这个url的哈希值
        """
        pipe = self.redis.pipeline(transaction=True)  # 开启原子性操作失误
        pipe.hexists(self.queue_url, self.get_md5(url))
        pipe.hexists(self.queue_title, self.get_md5(title))
        res = pipe.execute()  # 提交所有的操作
        dict_count = Counter(res)  # 统计返回的结果

        # 查看一下标题和url是否有已经存在于redis库中的,
        # 只要返回 1 的个数超过1,那么必然有一个存在于库中,
        # 那么返回True
        # 否则返回 False
        count_rp = dict_count.get(1)
        if count_rp:
            logger.info("%s 和 %s 已存在" % (title, url))
            return True
        else:
            logger.info("%s 和 %s 未存在" % (title, url))
            return False

    @redis_decorator
    def delete_value_expire(self):
        """
        删除七天前的数据
        """
        now_time = round(time.time())
        seven_days_ago = now_time - 3600 * 30 * 24  # 30天前
        # seven_days_ago = now_time - 180  # 180秒前

        # 获取 url字典的所有键值对
        pipe = self.redis.pipeline(transaction=True)  # 开启原子性操作失误
        pipe.hgetall(self.queue_url)
        res = pipe.execute()  # 提交所有的操作

        # 查看value的时间戳是不是七天前的 如果是的话就去删除这个键值对
        for data_list in res:
            for key, value in data_list.items():
                if int(value) < seven_days_ago:  # 如果取出来的时间是七天前的数据,那就删除这个键值
                    self.delete_key_value(name=self.queue_url, key=key)

        pipe = self.redis.pipeline(transaction=True)  # 开启原子性操作失误
        pipe.hgetall(self.queue_title)
        res = pipe.execute()  # 提交所有的操作
        for data_list in res:
            for key, value in data_list.items():
                if int(value) < seven_days_ago:  # 如果取出来的时间是七天前的数据,那就删除这个键值
                    self.delete_key_value(name=self.queue_title, key=key)
        return True

    @redis_decorator
    def delete_key_value(self, name, key):
        """
        删除字典中一个键值对,name是字典名,key是键
        """
        pipe = self.redis.pipeline(transaction=True)  # 开启原子性操作失误
        pipe.hdel(name, key)
        res = pipe.execute()  # 提交所有的操作

    @redis_decorator
    def delete_queue(self):
        """
        删除不要的方案queue,防止内存占用过多
        """
        res1 = self.redis.delete(self.queue_url)
        res2 = self.redis.delete(self.queue_title)
        if res1 or res2:  # 只要删除一个成功说明肯定都会成功的
            return True
        else:
            return False


if __name__ == '__main__':
    test = RFPDupeFilter('history_1111')
    res = test.add_title_url("1213", "哈哈哈======www.baidu.com1113")
    print(res)
    res = test.add_title("1214443")
    print(res)
    res = test.delete_value_expire()
    print(res)
    res = test.get_url_len()
    print(res)
    res = test.is_save()
    print(res)
