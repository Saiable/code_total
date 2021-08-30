'''
爬虫调度器
'''
from base.url_manage import URLManager
from base.data_store import *
from base.html_parse import *
from base.html_downloader import *


class SpiderMain(object):
    def __init__(self):
        self.manager = URLManager()
        self.downloader = HTMLDownload()
        self.parser = HTMLParser()
        self.output = DataOutput()

    def my_crawl(self, url):
        # 添加入口URL
        self.manager.add_new_url(url)
        # 判断url管理器中是否有新的url，同时判断抓取多少个url
        while (self.manager.has_new_url() and self.manager.old_url_size() < 100):
            try:
                # 从URL管理器获取新的URL
                new_url = self.manager.get_new_url()
                print(new_url)
                # HTML下载器下载网页
                html = self.downloader.download(new_url)
                # HTML解析器抽取网页数据
                new_urls, data = self.parser.parser(new_url, html)
                print(new_urls)
                # 将抽取的url添加到URL管理器中
                self.manager.add_new_urls(new_urls)
                # 数据存储器存储文件
                # self.output.store_data(data)
                print("已经抓取%s个链接" % self.manager.old_url_size())
            except Exception as e:
                print("failed")
                print(e)
                # 数据存储器将文件输出成指定的格式
                # self.output.output_html()

    def crawl(self, root_url):
        # 添加入口URL
        self.manager.add_new_url(root_url)
        # 判断url管理器中是否有新的url，同时判断抓取多少个url
        while (self.manager.has_new_url() and self.manager.old_url_size() < 100):
            try:
                # 从URL管理器获取新的URL
                new_url = self.manager.get_new_url()
                print(new_url)
                # HTML下载器下载网页
                html = self.downloader.download(new_url)
                # HTML解析器抽取网页数据
                new_urls, data = self.parser.parser(new_url, html)
                print(new_urls)
                # 将抽取的url添加到URL管理器中
                self.manager.add_new_urls(new_urls)
                # 数据存储器存储文件
                self.output.store_data(data)
                print("已经抓取%s个链接" % self.manager.old_url_size())
            except Exception as e:
                print("failed")
                print(e)
                # 数据存储器将文件输出成指定的格式
                self.output.output_html()


if __name__ == '__main__':
    spider_man = SpiderMain()
    url_template = "https://iot.ofweek.com/CATList-132200-8100-iot-{0}.html"
    for i in range(1,3)
        spider_man.crawl("http://www.runoob.com/w3cnote/page/{0}")