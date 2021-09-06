"""
跟 html文本获取相关的函数
"""
import traceback

from newspaper import Article
import requests
import time

# 用不上了
def get_content_zzsm(url, proxies=None, headers=None):
    """
    获取的正文信息中有 郑重声明的时候,使用标题替换 正文
    """
    content = ''
    for i in range(10):
        try:
            news = Article(url, language='zh', proxies=proxies, headers=headers, timeout=10)
            news.download()
            news.parse()
            content = news.text
            delet_c = '郑重声明'
            if delet_c in content:
                title = news.title
                content = title
            return content
        except Exception as err:
            content = ''
    return content

# 用不上了
def get_content_noloop(url, proxies=None, headers=None):
    """
    只获取一次 正文信息,出现异常则返回 空字符串
    """
    try:
        news = Article(url, language='zh', proxies=proxies, headers=headers, timeout=10)
        news.download()
        news.parse()
        content = news.text
        content_html = news.html
    except:
        content = ''
        content_html = ''
    return content, content_html

# 用不上了
def get_content_loop(url, proxies=None, headers=None):
    """
    循环十次获取 正文, 获取不到返回 空字符串
    """
    content = ''
    content_html = ''
    for i in range(10):
        try:
            news = Article(url, language='zh', proxies=proxies, headers=headers, timeout=10)
            news.download()
            news.parse()
            content = news.text
            content_html = news.html
            return content, content_html
        except Exception as err:
            content = ''
            content_html = ''

    return content, content_html

# 用不上了
def get_retry(url, headers=None, timeout=5, params=None, retry_nums=3, proxies=None, delay=3):
    """
    请求重试,返回html
    """
    html = ''
    for i in range(1, retry_nums + 1):
        try:
            html = requests.get(url=url, headers=headers, timeout=timeout, params=params, proxies=proxies)
            html.encoding = html.apparent_encoding
            break
        except Exception as e:
            print('-requests_retry函数-url-{}请求遇到错误-'.format(url), e)
            html = ''
            time.sleep(delay)
    return html


def get_html(url=None, headers=None, timeout=10, params=None, retry_nums=10, proxies=None, delay=1, encode_html=True):
    """
    请求重试,返回html(二进制)
    """
    html = ''
    for i in range(1, retry_nums + 1):
        try:
            html = requests.get(url=url, headers=headers, timeout=timeout, params=params, proxies=proxies)
            if html:
                if encode_html:  # 默认从html文本中获取编码格式
                    html.encoding = html.apparent_encoding
                break
        except Exception as e:
            error_location = traceback.format_exc()
            print('-requests_retry函数-url-{}请求遇到错误-'.format(url), error_location)
            html = ''
            time.sleep(delay)
    return html


def post_html(url=None, headers=None, timeout=10, data=None, retry_nums=10, proxies=None, delay=1, encode_html=True):
    """
    请求重试,返回html(二进制)
    """
    html = ''
    for i in range(1, retry_nums + 1):
        try:
            html = requests.post(url=url, headers=headers, timeout=timeout, data=data, proxies=proxies)
            if html:
                if encode_html:  # 默认从html文本中获取编码格式
                    html.encoding = html.apparent_encoding
                break
        except Exception as e:
            error_location = traceback.format_exc()
            print('-requests_retry函数-url-{}请求遇到错误-'.format(url), error_location)
            html = ''
            time.sleep(delay)
    return html