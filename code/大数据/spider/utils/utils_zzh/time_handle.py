"""
跟时间日期处理相关的函数
"""

import datetime
import re
import time


def check_is_today(pub_time):
    """
    检查 是不是当天的新闻数据
    :param pub_time:  2021-03-12 00:00:00 这种格式的数据
    :return: True说明是今天的数据,False说明不是今天的数据
    """
    try:
        pub_time_date = re.findall('\d{4}-\d{2}-\d{2}', pub_time)[0]
        date_time = datetime.datetime.now().strftime('%Y-%m-%d')
        if pub_time_date == date_time:
            return True
        else:
            return False
    except Exception as err:
        return False


def time_format(s):
    """
    将分钟,秒等转换成对应的时间
    """
    now_int = time.time()

    if '刚刚' in s:
        time_int = now_int

    elif '分钟' in s:
        nums = int(re.findall('\d+', s)[0])
        time_int = now_int - nums * 60

    elif '秒' in s:
        nums = int(re.findall('\d+', s)[0])
        time_int = now_int - nums

    elif '小时' in s:
        nums = int(re.findall('\d+', s)[0])
        time_int = now_int - nums * 3600

    elif '天' in s:
        nums = int(re.findall('\d+', s)[0])
        time_int = now_int - nums * 3600 * 24

    else:
        # print('获取时间信息格式错误，默认添加当前爬取时间-1天，不符合爬取时间要求')
        time_int = now_int - 3600 * 24

    format_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time_int))

    return format_time


def date_time_format(data):
    """"
    对时间进行标准化处理
    """
    char_list = ['|', '?', ':', '[', ']', '{', '}', '/', '\\']
    for line in char_list:
        data = data.strip(line)
    data = data.strip()
    date = ''
    try:
        date = datetime.datetime.strptime(data, "%Y-%m-%d %H:%M:%S")
    except:
        pass
    try:
        date = datetime.datetime.strptime(data, "%Y-%m-%d %H:%M")
    except:
        pass
    try:
        date = datetime.datetime.strptime(data, "%Y-%m-%d %H")
    except:
        pass
    try:
        date = datetime.datetime.strptime(data, "%Y-%m-%d")
    except:
        pass
    if not date:
        # date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        date = "################################################"
    return str(date)
