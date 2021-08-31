from os.path import dirname, abspath
from urllib.parse import urljoin
from copy import deepcopy
from lxml import etree
import re,json,time,traceback,sys

from industry_templete import IndustryInfo

sys.path.append(dirname(abspath(__file__)))
sys.path.append(dirname(dirname(abspath(__file__))))

class Spider(IndustryInfo):
    website_name = '维科网'
    website_subsource = '快讯'
    media_type = '网媒'
    content_source_type = '原贴'

    def __init__(self, tb_name='industry.ofweek'):
        self.tb_name = tb_name
        self.COUNT = 0
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
        }
        super(Spider, self).__init__(tb_name=tb_name)


    def start(self):
        web_dict = {
            "资讯": "https://iot.ofweek.com/CATList-132200-8100-iot-{0}.html",
        }
        # 循环栏目
        for key, value in web_dict.items():
            # 必带
            self.COUNT = 0  # 每次调用之前不要忘记这个参数,不然一直累加没有重置会出问题
            self.rf_filter.delete_value_expire()  # 每次启动爬虫前调用redis时间清除函数

            # 单个栏目循环
            for i in range(1, 5):
                value1 = value.format(str(i))
                try:
                    is_break = self.get_page(key=key, value=value1)
                except Exception as err:
                    pass

    def get_page(self, key, value):
        """
        列表页
        """
        url = value

        # 不要用requests, 使用封装好的get或者post请求, 默认encode_html为True, 所以置为False的参数必须带着
        # 返回的二进制使用的是 html 字段, 不要更改
        html = self.get_html(url, headers=self.headers, timeout=10, encode_html=False)
        if html:
            pass
        else:
            # 根据实际情况返回True或者False
            return True

        # html编码问题, 除非获取出来的编码不在这些里,不然就不要自定义编码
        if html.encoding in ["gb2312", "GB2312", "gbk", "GBK"]:
            html.encoding = "gbk"
        elif html.apparent_encoding in ["gb2312", "GB2312", "gbk", "GBK"]:
            html.encoding = 'gbk'
        elif html.encoding in ["UTF-8", "utf-8", "utf8"]:
            html.encoding = 'utf-8'
        elif html.apparent_encoding in ["UTF-8", "utf-8", "utf8"]:
            html.encoding = 'utf-8'
        else:
            html.encoding = html.apparent_encoding

        # etree完的字段是 response , 尽量不要改动为别的变量名
        response = etree.HTML(html.text)
        a_list = response.xpath('//div[@class="main_left"]/div[@class="list_model"]/div')

        # 列表循环
        for a in a_list:

            # try 必须带
            try:
                title = a.xpath('./h3/a/text()')[0]
                title_url = a.xpath('./h3/a/@href')[0]
                title_url = urljoin(url, title_url)
                release_time = a.xpath('./div[@class="tag"]/span[@class="date"]/text()')[0]
                release_time = release_time.split("|")[-1].strip()
            except Exception as err:
                err_lo = traceback.format_exc()
                continue

            # 用来标准化时间格式的
            if release_time:
                release_time = self.date_time_format(release_time)
            else:
                continue

            # 检查是否是当天的, 变量是标准的时间格式, 如果遇到时间戳,转换为标准时间格式
            is_today = self.check_is_today(release_time)
            if is_today:
                pass
            else:
                 # 根据实际情况来使用continue还是return True
                continue

            # 返回True说面插入成功,不是重复url否则就是采集过了
            # 根据实际情况调用三种去重规则
            not_repet_url = self.rf_filter.add_title_url(title, title_url)
            if not_repet_url:
                pass
            else:
                self.COUNT += 1
                continue  # 千万注意的东西, 不要忘,不要忘

            # 正文及html正文获取, 这两个字段是必须要的
            content, content_html = self.get_content(title_url)

            data = deepcopy(self.DATA)
            # 下面的字段都是必须要的
            data['industry_id'] = '-1'
            data['spider_id'] = '001'
            data["title"] = title
            data["content"] = content.strip()
            data['website_name'] = self.website_name
            data['website_subsource'] = key
            data['release_time'] = release_time
            data['static_url'] = title_url
            data['into_db_time'] = int(time.time())
            data['media_type'] = self.media_type
            data['content_source_type'] = self.content_source_type
            data['html_content'] = self.HtmlParse(content_html)
            data['html_content'] = self.plastic_html(data['html_content']).replace("\x00", "\uFFFD")
            time.sleep(1)

            # 发数据到kafka以及入PG库, 调试时注释, 调试完放开注释
            self.send_kafka(meta=data)
            self.store.process_item(item=data)

        # 根据截止条数判断是不是停止本栏目的采集
        if self.COUNT >= self.BREAK_COUNT:
            return True
        else:
            return False

    def get_content(self):
        pass

    def main(self):
        pass


