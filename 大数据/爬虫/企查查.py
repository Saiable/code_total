import requests

if __name__ == "__main__":
    url = "https://www.qcc.com/api/search/searchMind?"
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 6.1; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 86.0.4240.198  Safari / 537.36'
    }
    data = {
        'pageSize': '5',
        'person': 'true',
        'searchKey': '澎湃艺术培训',
        'suggest': 'true'
    }
    json_ids = requests.post(url=url,headers=headers,data=data).text()
    print(json_ids)