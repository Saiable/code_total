import json


'''
数据存储
'''

# json类型响应对象的本地存储
def json_local_storage(response, outfile = 'local_storage.json'):
    response_json = response.json()

    with open(outfile,'w',encoding='utf-8') as fw:
        json.dump(response_json,fp=fw,ensure_ascii=False)

# txt(string)类型响应对象的本地存储
def txt_local_storage(response, outfile = 'txt_strage.txt'):
    response_text = response.text

    with open(outfile, 'w', encoding='utf-8') as fw:
        fw.write(response_text)

# 二进制类型响应对象的本地存储
def content_local_storage(response, outfile = 'content_strage.jpg'):
    response_content = response.content

    with open(outfile, 'wb') as fw:
        fw.write(response_content)

# redis数据库存储
def redis_conn(host,port,password):
    pass




