import requests
from utils.utils_proxy import get_proxy
from lxml import etree
from settings import HEADERS

def main():
    url_template = 'http://www.ctechw.com/htm/list_1_1.html'
    response = requests.get(url=url_template, headers=HEADERS, proxies=get_proxy())
    print(response.status_code)
    response_text = response.text
    # with open('aa.html','w',encoding='utf-8') as fw:
    #     fw.write(response_text)
    tree = etree.HTML(response_text)
    li_list = tree.xpath('//ul[@id="lists1"]/li[@class="textstyle"]')
    print(li_list)
    for li in li_list:
        try:
            title = li.xpath('./div[@class="listtext"]/h2/a/text()')[0]
            print(title)
        except Exception as e:
            print(e)

