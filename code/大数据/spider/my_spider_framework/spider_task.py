
from os import mkdir
import requests 
import time
import json

from requests.sessions import HTTPAdapter
from settings import START_URL, HEADERS, DATA
from utils.utils_strorage import content_local_storage,txt_local_storage
from utils.utils_os import my_mkdir
import re
from utils.utils_parse import regex_parse
from bs4 import BeautifulSoup
from lxml import etree
from utils.utils_ocr import parse_ocr,query_account_nfo
from settings import OCR_USERNAME,OCR_PASSWORD
from multiprocessing.dummy import Pool


if __name__ =='__main__':
    
    def single_parse():
        my_mkdir('./qiutu')

        response = requests.get(url=START_URL['pic_demo']['index_url'],headers=HEADERS)

        ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
        src_list = regex_parse(ex,response,re.S)

        for src in src_list:
            src = 'https:' + src
            time.sleep(1)
            response = requests.get(url=src,headers=HEADERS)
            img_name = src.split('/')[-1]

            img_path = './qiutu/'+ img_name
            
            content_local_storage(response,img_path)
            time.sleep(1)
    
    def multi_parse():
        template_url = START_URL['pic_demo']['template_url']
        my_mkdir('./qiutu')

        for i in range(1, 3):
            next_url = template_url % i

            response = requests.get(url=next_url,headers=HEADERS)

            ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
            src_list = regex_parse(ex,response,re.S)

            for src in src_list:
                src = 'https:' + src
                time.sleep(1)
                response = requests.get(url=src,headers=HEADERS)
                img_name = src.split('/')[-1]

                img_path = './qiutu/'+ img_name
                
                content_local_storage(response,img_path)
                time.sleep(1)
            print(next_url+'start')

    def sanguo():
        response = requests.get(url=START_URL['sanguo'],headers=HEADERS)
        response_text = response.text.encode('ISO-8859-1')

        soup = BeautifulSoup(response_text,'lxml')
        li_list = soup.select('.book-mulu > ul > li')
        for li in li_list:
            title = li.a.string
            detail_url = 'https://www.shicimingju.com' + li.a['href']
            print(detail_url)
            detail_response = requests.get(url=detail_url,headers=HEADERS)
            detail_response_text = detail_response.text.encode('ISO-8859-1')
            soup_detail = BeautifulSoup(detail_response_text,'lxml')
            detail_tag = soup_detail.find('div', class_='chapter_content')
            detail_content = detail_tag.text
            print(detail_content)
            break
            time.sleep(1)
    
    def ershoufang():
        response = requests.get(url=START_URL['ershoufang'],headers=HEADERS)
        response_text = response.text
        tree = etree.HTML(response_text)
        # txt_local_storage(response)
        div_list = tree.xpath('//*[@id="__layout"]/div/section/section[3]/section[1]/section[2]/div')
        for div in div_list:
            title = div.xpath('.//div[@class="property-content-title"]/h3/text')[0]
            print(title)
    
    def meitu():
        my_mkdir('./meitu')
        response = requests.get(url=START_URL['img_02'],headers=HEADERS)
        response_text = response.text
        tree = etree.HTML(response_text)
        li_list = tree.xpath('//ul[@class="clearfix"]/li')
        detail_url_list = []
        for li in li_list:
            detail_url = li.xpath('./a/@href')[0]
            detail_url_list.append('https://pic.netbian.com' + detail_url)
        print(detail_url_list)
        for detail_ele in detail_url_list:
            response_detail = requests.get(url=detail_ele,headers=HEADERS)
            response_detail_text = response_detail.text.encode('ISO-8859-1')

            tree_detail = etree.HTML(response_detail_text)
            img_src = tree_detail.xpath('//div[@class="photo-pic"]/a/img/@src')[0]
            img_src = 'https://pic.netbian.com' + img_src
            img_response = requests.get(url=img_src,headers=HEADERS)
            img_name = tree_detail.xpath('//div[@class="photo-pic"]/a/img/@title')[0] + '.jpg'

            filepath = './meitu/' + img_name
            content_local_storage(img_response,filepath)
            print(img_name+'下载完成')
            time.sleep(1)
    

    def gsw():
        # query_account_nfo(OCR_USERNAME,OCR_PASSWORD)
        # print(OCR_USERNAME)
        # parse_ocr('./imgs/ocr/02.jpg',OCR_USERNAME,OCR_PASSWORD)
        
        response_index = requests.get(url=START_URL['gsw_index'],headers=HEADERS).text
        tree = etree.HTML(response_index)
        img_src = tree.xpath('//div[@class="lg_content"]/ul/li[3]/img/@src')[0]
        img_src = 'https://www.gushiwen.com' + img_src
        print(img_src)

        response_code = requests.get(url=img_src,headers=HEADERS).content

        with open('code.jpg','wb') as fw:
            fw.write(response_code)

        code_parse= parse_ocr('./code.jpg',OCR_USERNAME,OCR_PASSWORD)
        print(code_parse)
        DATA = {
            "user": "2495620791@qq.com",
            "pass": "spidertest",
            "imgvc": code_parse,
        }
        print(DATA)

        session = requests.Session()

        response_login = session.post(url=START_URL['gsw_login'],data=DATA,headers=HEADERS)
        print(response_login.status_code)

        url_content = 'https://www.gushiwen.com/u.html'
        respnse_content = session.get(url=url_content,headers=HEADERS)
        txt_local_storage(respnse_content,'login.html')
    
    def gsw02():
        # query_account_nfo(OCR_USERNAME,OCR_PASSWORD)
        # print(OCR_USERNAME)
        # parse_ocr('./imgs/ocr/02.jpg',OCR_USERNAME,OCR_PASSWORD)
        
        response_index = requests.get(url=START_URL['gsw_index_02'],headers=HEADERS).text
        tree = etree.HTML(response_index)
        img_src = tree.xpath('//img[@id="imgCode"]/@src')[0]
        img_src = 'https://so.gushiwen.cn' + img_src
        print(img_src)

        response_code = requests.get(url=img_src,headers=HEADERS).content

        with open('code.jpg','wb') as fw:
            fw.write(response_code)

        code_parse= parse_ocr('./code.jpg',OCR_USERNAME,OCR_PASSWORD)
        print(code_parse)
        DATA = {
            "__VIEWSTATE": "FOYWS8XbFqsK27us0uWu2uH71qfF7kVPAPPPzvNEmlkt7Yjr4recOFdWJvtse6c9tf/dRHJVamxhHPVJ4WtmGo9BH0p+vHDe4hDaDwX3lPHqftgDRSUQliIdp/0=",
            "__VIEWSTATEGENERATOR": "C93BE1AE",
            "from": "http",
            "email": "2495620791@qq.com",
            "pwd": "spidertest",
            "code": "D5CM",
            "denglu": "登录",
        }


        # print(DATA)

        # session = requests.Session()

        # response_login = session.post(url=START_URL['gsw_login'],data=DATA,headers=HEADERS)
        # print(response_login.status_code)

        # url_content = 'https://www.gushiwen.com/u.html'
        # respnse_content = session.get(url=url_content,headers=HEADERS)
        # txt_local_storage(respnse_content,'login.html')

    def proxy_test():
      pass
    
    def get_page(str):
        print('downloading...')
        time.sleep(2)
        print('donwnloaded successed!',str)
    

    def get_video():
        url_index = 'https://www.pearvideo.com/category_5'
        data = []
        response_index_text = requests.get(url=url_index,headers=HEADERS).text

        tree = etree.HTML(response_index_text)
        li_list = tree.xpath('//ul[@id="listvideoListUl"]/li')
        print(li_list)
        for li in li_list:
            url_detail = li.xpath('./div/a/@href')[0]
            url_detail = 'https://www.pearvideo.com/'+url_detail
            print(url_detail)

            response_detail = requests.get(url=url_detail,headers=HEADERS).text
            tree2 = etree.HTML(response_detail)
            url_video = tree2.xpath('//div[@class="main-video-box"]/div/video/@src')
            print(url_video)

    def test():
        url = 'https://www.pearvideo.com/videoStatus.jsp?contId=1738511&mrd=0.28387496915018784'

        resposne = requests.get(url=url,headers=HEADERS)
        print(resposne.status_code)
        content_local_storage(resposne,'test.mp4')
    test()