import requests
import  os, sys
import time
# 获得父级目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 把父级路径添加到环境变量中
sys.path.append(BASE_DIR)
# from utils.utils_proxy import aa
# print(aa)

from utils.utils_proxy import get_proxy
headers ={
    'User-Agent':'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50'}

url = 'https://www.ip138.com/'
url2 = 'https://tool.lu/ip/'

response = requests.get(url=url2,headers=headers,proxies=get_proxy()) # ,proxies={"http":"175.147.100.26:8080"}
# response_decode = response.text.encode('ISO-8859-1')
print(response.status_code)
try:
    if response.status_code == 200:
        with open('./temp_file/ip.html', 'w',encoding='utf-8') as fr:
            fr.write(response.text)
except Exception as e:
    print('异常：', e)



