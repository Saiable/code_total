'''
@Author  ：Devil~华
@Date    ：2021/4/6 20:01 
@Function：
'''

# 用来添加当前文件的目录
import sys
from os.path import dirname, abspath
from html import unescape as HtmlParse
sys.path.append(dirname(abspath(__file__)))
sys.path.append(dirname(dirname(abspath(__file__))))

import logging
from utils.utils_zzh import *


class IndustryInfo:
    def __init__(self, tb_name):
        self.tb_name = tb_name
        self.store = ItemToPG(tb_name=self.tb_name)
        self.rf_filter = RFPDupeFilter(tb_name=self.tb_name)

        self.DATA = DATA
        self.get_proxy = get_proxy
        self.get_retry = get_retry
        self.send_kafka = send_kafka
        self.check_is_today = check_is_today
        self.date_time_format = date_time_format
        self.time_format = time_format
        self.HtmlParse = HtmlParse
        self.get_content_loop = get_content_loop
        self.get_content_noloop = get_content_noloop
        self.get_content_zzsm = get_content_zzsm
        self.get_html = get_html
        self.post_html = post_html
        self.get_retry = get_retry
        self.plastic_html = plastic_html
        self.logger = Logger(init_file=__file__, file_name="./LOG_INDUSTRY/行业资讯_error.log",
                             logging_level=logging.DEBUG).logger_fh()

        self.BREAK_COUNT = 10
        self.COUNT = 0
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36 Edg/89.0.774.50"
        }
