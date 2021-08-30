from settings import HEADERS

from utils.utils_hh.utils_proxy import get_proxy
from utils.utils_hh.utils_storage import txt_local_storage
from lxml import etree
import requests


def main():

    web_dict = {
        "资讯": "https://iot.ofweek.com/CATList-132200-8100-iot-{0}.html",
    }

    # 循环栏目
    for key, value in web_dict.items():
        num = 971
        print(type(value))
        print(value.format(num))
        url = value.format(num)
        response = requests.get(url = url,headers = HEADERS,proxies=get_proxy())
        response_text = response.text

        tree = etree.HTML(response_text)
        div_list = tree.xpath('//div[@class="main_left"]/div[@class="list_model"]')
        for div in div_list:
            title = div.xpath('./div/h3/a/text()')[0]
            print(title)
if '__name__' == '__main__':
    main()