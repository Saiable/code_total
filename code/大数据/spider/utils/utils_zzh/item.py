'''
item 文件, 全量爬虫的所有字段及默认值
'''

from copy import deepcopy


data = {}
data['industry_id'] = '-1'
data['spider_id'] = '001'
data["title"] = ''
data["content"] = ''
data['website_name'] = ''
data['website_subsource'] = ''
data['read_times'] = ''
data['release_time'] = ''
data['forward_times'] = ''
data['like_times'] = ''
data['comment_times'] = ''
data['location'] = ''
data['lat'] = ''
data['lon'] = ''
data['static_url'] = ''
data['publisher'] = ''
data['publisher_id'] = ''
data['into_db_time'] = ''
data['match_key_words'] = ''
data['media_type'] = ''
data['content_source_type'] = ''
data['important_events'] = ''
data['tag'] = ''
data['main_company_name'] = ''
data['main_company_introduction'] = ''
data['abstract'] = ''
data['text_type_label'] = ''
data['news_label'] = ''
data['web_image_url'] = ''
data['html_content'] = ''
data['is_special_news'] = '0'
data['special_news_name'] = ''
data['special_news_introduction'] = ''

DATA = deepcopy(data)