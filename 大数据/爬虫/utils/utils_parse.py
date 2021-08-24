
import re
'''
数据解析
'''

def regex_parse(ex,response,pattern):
    response_text = response.text
    parse_list = re.findall(ex,response_text,pattern)

    return parse_list