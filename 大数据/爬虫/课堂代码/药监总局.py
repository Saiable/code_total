import requests

if __name__ == "__main__":
    url = "http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList"
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 6.1; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 86.0.4240.198  Safari / 537.36'
    }
    data = {
        'on': 'true',
        'page': 1,
        'pageSize': 15,
        'productName': '婕珞芙',
        'conditionType': 2,
        'applyname': '',
        'applysn': '',
    }
    json_ids = requests.post(url=url,headers=headers,data=data).json()
    print(json_ids)