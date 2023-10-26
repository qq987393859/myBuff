# -*- coding: utf-8 -*-
import requests
import json
import time
import random

def postVX(name, minP, qgP, dis):
    text = str(name) + "当前可以捡漏，现价为" + str(minP) + ", 最高求购价为" + str(qgP)
    url = 'http://wx.xtuis.cn/oYaozRu6CrpmDOFHqj4rJ0scu.send?text=' + name + '&desp='  + text
    try:
        if (float(minP) / float(qgP)) < float(dis):
            requests.get(url)  
            print(name + "微信推送成功")
    except ZeroDivisionError as e:
        print(e)
        print(name)

datas = {}
detail = {}

class Good(object):
    def __init__(self, n, i, qgP, minP) -> None:
        self.name = n
        self.id = i
        self.qgPrice = qgP
        self.minPrice = minP


url = 'https://buff.163.com/api/market/goods'
param = {
    'game': 'csgo',
    'page_num': '1',
    "category": "csgo_type_musickit",
    "sort_by": "price.asc",
    "use_suggestion": "0",
    '_': '1698151750774'
}
header = {
    'authority': 'buff.163.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    # 'cookie': 'Device-Id=kqmGJDf6Qkl6zveRCLkA; Locale-Supported=zh-Hans; steam_info_to_bind=; NTES_P_UTID=C2fynd8JTyuwf6puCpWqsy8ic8u7dXwi|1679896267; nts_mail_user=csgowork@163.com:-1:1; _ntes_nnid=77c26dba47767fc07a96e0725b190eed,1679896312860; _ntes_nuid=77c26dba47767fc07a96e0725b190eed; ANTICSRF=6fb8e92ec315e3be48b0ffa41a1c8d34; to_steam_processing_click230413T18367867951=1; to_steam_processing_click230413T18368117301=1; to_steam_processing_click230413T18363521281=1; to_steam_processing_click230413T18363551641=1; to_steam_processing_click230413T18363560371=1; to_steam_processing_click230413T18363595731=1; to_steam_processing_click230413T18363853961=1; to_steam_processing_click230413T18363874561=1; __bid_n=187c0d878edf7238f44207; NTES_CMT_USER_INFO=540083097%7C%E6%9C%89%E6%80%81%E5%BA%A6%E7%BD%91%E5%8F%8B0wcgep%7Chttp%3A%2F%2Fcms-bucket.nosdn.127.net%2F2018%2F08%2F13%2F078ea9f65d954410b62a52ac773875a1.jpeg%7Cfalse%7CeWQuNDViNGUwY2RkN2E1NDYyM2JAMTYzLmNvbQ%3D%3D; FPTOKEN=q2dywMV2z+tszjm3/AiQ0yygGi5+M8HTL/tXuuukOMqnvKsjn5ADoDfyefScz/W0W1vOsNx9/lySErzbckaJts5Xf4TI7BcQfZ7tJWHFOf+4FtWQf6mm/GHZDOqKYjyAR3hP85o13wOOkxbnid33H2LHfrQo79BN3KmaDjvrkMO5xwmZO8l8BDwells9M2gr28phPkKPy6iQT43j0J8Xzh8A7KLLhDnzRJjfSz6x3USh2iTUYLL9JkOivwp1YfcQuNwLduNtWkvfokYG9Lo+tK8Xzo8zhqr39eOH0FJ7s1/yAXZINwnF2bF6tz5Titn/m2YX0BnGsILKxnlYa1d/ZsVdC5RZYEbZSV4RzeaL5FXjece40MVxz/b/DzGk+E7tg6pt98SCjD5hCpLiX/s+Ng==|e1iTqySNC9GgBxMa2V9fae1Lvb4okZ+M4RuPxJxz1uQ=|10|46f1e8c88109f6d4549805fab3c5722d; game=csgo; NTES_YD_SESS=Dg78nxKhp0e.ec_NRnuE4kwWX8t7p9egMrakgpoOg7slybvYyrnuZzrVxUbEIVGsR4sKz9zMyr8AJMSzRhdX_kJJU8wj1EiKlUMODo0GpesZ_7kv6W433LMxXa7jwXk2D.lDD1ooxVOOpi_xBoogb8DRTZif6vskmnsuptT8LtFszIKX2ZsmUUrEEG2r9YRlhQBqIEjLv2GkbpeifjehZNL9XaIQ.Y3cEgJxHV6aeXuPc; S_INFO=1698196857|0|0&60##|13260933011; P_INFO=13260933011|1698196857|1|netease_buff|00&99|null&null&null#shh&null#10#0#0|&0|null|13260933011; remember_me=U1106797087|MltrYkyLgZpUU89NuSogY8oNjfZg2kBR; session=1-55M1UOaE7qzAU74BqECPVh-55FcwNSdFdT9BIGZZL_u92033646919; csrf_token=IjliY2NjZjc5YzRkMTMzNTUyZjIxMDFhYzgxMDhkYTkzZjAxZDEyYzEi.GBoEog.qTFjzV-CcazIlikcEqeKMUy4Zac',
    'referer': 'https://buff.163.com/market/csgo',
    'sec-ch-ua': '"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.61',
    'x-requested-with': 'XMLHttpRequest',
}

cookie = {
    'Device-Id': 'kqmGJDf6Qkl6zveRCLkA',
    'Locale-Supported': 'zh-Hans',
    'steam_info_to_bind': '',
    'NTES_P_UTID': 'C2fynd8JTyuwf6puCpWqsy8ic8u7dXwi|1679896267',
    'nts_mail_user': 'csgowork@163.com:-1:1',
    '_ntes_nnid': '77c26dba47767fc07a96e0725b190eed,1679896312860',
    '_ntes_nuid': '77c26dba47767fc07a96e0725b190eed',
    'ANTICSRF': '6fb8e92ec315e3be48b0ffa41a1c8d34',
    'to_steam_processing_click230413T18367867951': '1',
    'to_steam_processing_click230413T18368117301': '1',
    'to_steam_processing_click230413T18363521281': '1',
    'to_steam_processing_click230413T18363551641': '1',
    'to_steam_processing_click230413T18363560371': '1',
    'to_steam_processing_click230413T18363595731': '1',
    'to_steam_processing_click230413T18363853961': '1',
    'to_steam_processing_click230413T18363874561': '1',
    '__bid_n': '187c0d878edf7238f44207',
    'NTES_CMT_USER_INFO': '540083097%7C%E6%9C%89%E6%80%81%E5%BA%A6%E7%BD%91%E5%8F%8B0wcgep%7Chttp%3A%2F%2Fcms-bucket.nosdn.127.net%2F2018%2F08%2F13%2F078ea9f65d954410b62a52ac773875a1.jpeg%7Cfalse%7CeWQuNDViNGUwY2RkN2E1NDYyM2JAMTYzLmNvbQ%3D%3D',
    'FPTOKEN': 'q2dywMV2z+tszjm3/AiQ0yygGi5+M8HTL/tXuuukOMqnvKsjn5ADoDfyefScz/W0W1vOsNx9/lySErzbckaJts5Xf4TI7BcQfZ7tJWHFOf+4FtWQf6mm/GHZDOqKYjyAR3hP85o13wOOkxbnid33H2LHfrQo79BN3KmaDjvrkMO5xwmZO8l8BDwells9M2gr28phPkKPy6iQT43j0J8Xzh8A7KLLhDnzRJjfSz6x3USh2iTUYLL9JkOivwp1YfcQuNwLduNtWkvfokYG9Lo+tK8Xzo8zhqr39eOH0FJ7s1/yAXZINwnF2bF6tz5Titn/m2YX0BnGsILKxnlYa1d/ZsVdC5RZYEbZSV4RzeaL5FXjece40MVxz/b/DzGk+E7tg6pt98SCjD5hCpLiX/s+Ng==|e1iTqySNC9GgBxMa2V9fae1Lvb4okZ+M4RuPxJxz1uQ=|10|46f1e8c88109f6d4549805fab3c5722d',
    'game': 'csgo',
    'NTES_YD_SESS': 'Dg78nxKhp0e.ec_NRnuE4kwWX8t7p9egMrakgpoOg7slybvYyrnuZzrVxUbEIVGsR4sKz9zMyr8AJMSzRhdX_kJJU8wj1EiKlUMODo0GpesZ_7kv6W433LMxXa7jwXk2D.lDD1ooxVOOpi_xBoogb8DRTZif6vskmnsuptT8LtFszIKX2ZsmUUrEEG2r9YRlhQBqIEjLv2GkbpeifjehZNL9XaIQ.Y3cEgJxHV6aeXuPc',
    'S_INFO': '1698196857|0|0&60##|13260933011',
    'P_INFO': '13260933011|1698196857|1|netease_buff|00&99|null&null&null#shh&null#10#0#0|&0|null|13260933011',
    'remember_me': 'U1106797087|MltrYkyLgZpUU89NuSogY8oNjfZg2kBR',
    'session': '1-55M1UOaE7qzAU74BqECPVh-55FcwNSdFdT9BIGZZL_u92033646919',
    'csrf_token': 'IjliY2NjZjc5YzRkMTMzNTUyZjIxMDFhYzgxMDhkYTkzZjAxZDEyYzEi.GBoEog.qTFjzV-CcazIlikcEqeKMUy4Zac',
}

if __name__=='__main__':
    category = input('请输入种类名称:')
    discount = input('请输入折扣：')
    param['category'] = category
    param['_'] = str(int(time.time() * 1000))

    try:
        response = requests.get(url=url, params=param, cookies=cookie, headers=header)
        total_page = response.json()['data']['total_page']
        #print(total_page)
    except requests.exceptions.RequestException as e:
        print(e)
    except KeyError as e:
        print(response.json())
    except NameError as e:    
        print(response.json())

    for i in range(1, int(total_page)+1):
        param['page_num'] = str(i)
        param['_'] = str(int(time.time() * 1000))

        try:
            response = requests.get(url=url, params=param, cookies=cookie, headers=header)
            items = response.json()['data']['items']
            itemLen = len(items)
            for j in range(itemLen):
                key = items[j]['name']
                idValue = items[j]['id']
                qgPrice = items[j]['buy_max_price']
                minPrice = items[j]['sell_min_price']
                postVX(key, minPrice, qgPrice, discount)
                obj = Good(key, idValue, float(qgPrice), float(minPrice))
                datas[idValue] = obj
                #print(key, idValue)
        except requests.exceptions.RequestException as e:
            print(e)
        time.sleep(3)
    for key in datas:
        print(str(key) + "\t"+ str(datas[key].name) + "\t\t" + str(datas[key].minPrice) + "\t" + str(datas[key].qgPrice))



