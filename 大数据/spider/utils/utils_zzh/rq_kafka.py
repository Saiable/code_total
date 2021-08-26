'''
kafka中存数据
'''
import sys
from os.path import dirname, abspath
sys.path.append(dirname(abspath(__file__)))
sys.path.append(dirname(dirname(abspath(__file__))))
import json
from kafka import KafkaProducer
from utils.config import KAFKA_HOST
from utils.time_handle import date_time_format
from utils.dupefilter import RFPDupeFilter


class UrlFilter(RFPDupeFilter):
    def __init__(self, tb_name="filter"):
        self.tb_name = tb_name
        super(UrlFilter, self).__init__(tb_name=tb_name)
        self.queue_url = 'rq_all_url:' + tb_name
        self.queue_title = 'rq_all_title:' + tb_name


def trfilter(title,url):
    """
    对title以及url做过滤处理
    """

    title_flag =False
    url_flag = False
    if title:
        title_flag = UrlFilter().add_title(title)
    if url:
        url_flag = UrlFilter().add_url(url)
    if title_flag or url_flag:
        return True
    else:
        return False




def send_kafka(meta):
    '''
    将meta数据组合成字符串发送到kafka中
    '''
    meta["release_time"] = date_time_format(meta["release_time"])
    values_list = list(meta.values())
    values_list = [str(line) if line is not None else '' for line in values_list]
    values = "${sp}".join(values_list)
    keys = meta.get("industry_id")
    content = meta.get("content")
    if meta.get("static_url"):
        not_repet_url = UrlFilter().add_url(meta.get("static_url"))
        if not_repet_url:
            pass
        else:
            return

    if content:
        producer = KafkaProducer(bootstrap_servers=KAFKA_HOST, ssl_check_hostname=False)
        msg_dict = {
            keys: values,
        }
        msg = json.dumps(msg_dict)
        producer.send('eoias_industry_crawler_result', msg.encode("utf-8"), partition=0)
        producer.close()
