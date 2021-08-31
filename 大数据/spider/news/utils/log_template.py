'''
日志模板文件, 输出每天的日志文件
'''
import json
import logging
import logging.handlers
from concurrent_log import ConcurrentTimedRotatingFileHandler


class Logger():

    def __init__(self, init_file, file_name="日志.log", logging_level=logging.DEBUG):
        """
        默认设置handler将会处理的日志消息的最低严重级别,可以根据传递的参数改变
        :param logging_level: 传递的日志严重级别
        """
        self.init_file = init_file
        self.file_name = file_name

        JSON_LOGGING_FORMAT = json.dumps({
            "time": "%(asctime)s",
            "filepath": "%(pathname)s",
            "program": "%(filename)s",
            "function": "%(funcName)s",
            "line": "%(lineno)s",
            "level": "%(levelname)s",
            "message": "%(message)s",
        })      # 创建一个json输出格式

        self.formatter = logging.Formatter(
            fmt=JSON_LOGGING_FORMAT,
            datefmt='%Y-%m-%d %H:%M:%S')

        # logging.getLogger(name)方法进行初始化，name可以不填。
        # 通常logger的名字我们对应模块名，如聊天模块、数据库模块、验证模块等
        self.logger = logging.getLogger(init_file)  # 这里的 init_file 必须是调用这个类的程序给定的(在调用的程序中传递__file__即可)
        self.logger.setLevel(logging_level)  # 设置严重级别

    def logger_ch(self):
        """
        只打印日志信息到控制台
        :return: 返回一个logger
        """
        # 设置一个 控制台打印的logger日志
        ch = logging.StreamHandler()
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)
        return self.logger

    def logger_fh(self):
        """
        输出日志信息到文件,默认名是程序日志.log
        :param file_name: 输出文件名
        :return: 返回一个logger
        """
        # 设置一个输出到文件 xxx 的looger日志
        fh = ConcurrentTimedRotatingFileHandler(filename=self.file_name, when='MIDNIGHT', encoding='utf-8')
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)
        return self.logger

    def logger_cfh(self):
        """
        打印日志信息到控制台
        输出日志信息到文件,默认名是程序日志.log
        :param file_name: 输出文件名
        :return: 返回一个logger
        """
        # 设置一个 控制台打印的logger日志
        ch = logging.StreamHandler()
        ch.setFormatter(self.formatter)
        self.logger.addHandler(ch)

        fh = ConcurrentTimedRotatingFileHandler(filename=self.file_name, when='MIDNIGHT', encoding='utf-8')
        fh.setFormatter(self.formatter)
        self.logger.addHandler(fh)
        return self.logger


if __name__ == '__main__':
    logger = Logger(init_file="123", file_name="./日志.log").logger_fh()
    logger.info("hahah")
