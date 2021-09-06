import requests

if __name__ == "__main__":
    url = "https://www.qcc.com/api/search/searchMind?pageSize=5&person=true&searchKey=%E6%BE%8E%E6%B9%83%E8%89%BA%E6%9C%AF%E5%9F%B9%E8%AE%AD&suggest=true"
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 6.1; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 86.0.4240.198  Safari / 537.36'
    }

    json_ids = requests.get(url=url,headers=headers).text
    print(json_ids)