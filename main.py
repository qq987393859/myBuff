# -*- coding: utf-8 -*-
import requests
import sys
import json
import time
import random

buyerCookie = {
    'Device-Id': 'BSlDqva8Bo2mdfpKZ17T',
    'Locale-Supported': 'zh-Hans',
    'game': 'csgo',
    'to_steam_processing_click230404T17890537111': '1',
    'to_steam_processing_click230407T17944345271': '1',
    'to_steam_processing_click230407T17948754261': '1',
    'to_steam_processing_click230407T17945351461': '1',
    'to_steam_processing_click230408T17911689091': '1',
    'to_steam_processing_click230408T17914558031': '1',
    'to_steam_processing_click230408T17914278341': '1',
    'to_steam_processing_click230409T18314280811': '1',
    'to_steam_processing_click230414T18338832441': '1',
    'to_steam_processing_click230414T18338856481': '1',
    'to_steam_processing_click230414T18338857431': '1',
    'to_steam_processing_click230414T18338874811': '1',
    'to_steam_processing_click230414T18338885781': '1',
    'NTES_YD_SESS': 'Iz3Tk3o0j8Vos3LKgVa5i0ugmw.dWMrgUU50aRqGaEnwYtclYUOmhkrWiLrlZq_BEMRwNEpABfa8XkiSSB2U2IEvxpXxwBNmGOVAjAx24G4F5gxkT8emWQAEfzlNswdXxHrRHpfhXwMI5dmfy12ZgMZNf0I1A6BbXC0_jLSIpcl9TMhMWTC1k7cyZbnBdBkMppiPsOyiAEZrff63ahwtrGVTZ9sPeeKWQxZ2YjJpaCpdD',
    'S_INFO': '1698137441|0|0&60##|18916457313',
    'P_INFO': '18916457313|1698137441|1|netease_buff|00&99|null&null&null#shh&null#10#0|&0||18916457313',
    'remember_me': 'U1077592029|xiTziU9JoFi46n0olnvXDy0HrkWNswau',
    'session': '1-H4US6kkwegVCn_YOoB12ZhY_semj9o4x7o0RCJZICjtn2029265029',
    'steam_info_to_bind': '',
    'csrf_token': 'ImRlNjRlZTRmY2MzY2NiY2NhMjRjYjljNWMyY2I3YzlkNmYwNjM3MjAi.GBkayw.v7zgQH32d8FP-wmRSK2755SzqIs',
}
buyerHeader = {
    'authority': 'buff.163.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'content-type': 'application/json',
    # 'cookie': 'Device-Id=BSlDqva8Bo2mdfpKZ17T; Locale-Supported=zh-Hans; game=csgo; to_steam_processing_click230404T17890537111=1; to_steam_processing_click230407T17944345271=1; to_steam_processing_click230407T17948754261=1; to_steam_processing_click230407T17945351461=1; to_steam_processing_click230408T17911689091=1; to_steam_processing_click230408T17914558031=1; to_steam_processing_click230408T17914278341=1; to_steam_processing_click230409T18314280811=1; to_steam_processing_click230414T18338832441=1; to_steam_processing_click230414T18338856481=1; to_steam_processing_click230414T18338857431=1; to_steam_processing_click230414T18338874811=1; to_steam_processing_click230414T18338885781=1; NTES_YD_SESS=Iz3Tk3o0j8Vos3LKgVa5i0ugmw.dWMrgUU50aRqGaEnwYtclYUOmhkrWiLrlZq_BEMRwNEpABfa8XkiSSB2U2IEvxpXxwBNmGOVAjAx24G4F5gxkT8emWQAEfzlNswdXxHrRHpfhXwMI5dmfy12ZgMZNf0I1A6BbXC0_jLSIpcl9TMhMWTC1k7cyZbnBdBkMppiPsOyiAEZrff63ahwtrGVTZ9sPeeKWQxZ2YjJpaCpdD; S_INFO=1698137441|0|0&60##|18916457313; P_INFO=18916457313|1698137441|1|netease_buff|00&99|null&null&null#shh&null#10#0|&0||18916457313; remember_me=U1077592029|xiTziU9JoFi46n0olnvXDy0HrkWNswau; session=1-H4US6kkwegVCn_YOoB12ZhY_semj9o4x7o0RCJZICjtn2029265029; steam_info_to_bind=; csrf_token=ImRlNjRlZTRmY2MzY2NiY2NhMjRjYjljNWMyY2I3YzlkNmYwNjM3MjAi.GBkayw.v7zgQH32d8FP-wmRSK2755SzqIs',
    'origin': 'https://buff.163.com',
    'referer': 'https://buff.163.com/goods/',
    'sec-ch-ua': '"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.61',
    'x-csrftoken': 'ImRlNjRlZTRmY2MzY2NiY2NhMjRjYjljNWMyY2I3YzlkNmYwNjM3MjAi.GBkayw.v7zgQH32d8FP-wmRSK2755SzqIs',
    'x-requested-with': 'XMLHttpRequest',
}
buyerParam = {
    'game': 'csgo',
    'goods_id': '835463',
    'sell_order_id': '0813118007-70C1-137413628',
    'price': 0.04, 
    'pay_method': 3,
    'allow_tradable_cooldown': 0,
    'token': '',
    'cdkey_id': '',
}


def myPause():
    input('暂停')

flag = -1
overviewUrl = 'https://buff.163.com/api/market/goods'
param = {
    'game': 'csgo',
    'page_num': '1',
    "category": "csgo_type_musickit",
    "sort_by": "price.asc",
    "use_suggestion": "0",
    '_': '1698151750774',
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

#发送微信通知
def postVX(goodname, goodMinP):
    text = str(goodname) + "当前可以捡漏，现价为" + str(goodMinP) + "!\a"
    url = 'http://www.pushplus.plus/send?token=10380a351f1e4b7bb86d0e7d6ba85c0b&title=' + str(goodname) + '&content=' + text
    try:
        requests.get(url)
    except BaseException as e:
        print("发送微信通知出错：" + e)

#秒杀操作
def buy(price, id, tid):
    buyerHeader['referer'] += (str(id) + '?from=market')
    buyerParam['goods_id'] = str(id)
    buyerParam['_'] = str(int(time.time() * 1000))
    buyerParam['sell_order_id'] = str(tid)
    buyerParam['price'] = float(price)
    try:
        response  = requests.post('https://buff.163.com/api/market/goods/buy', cookies=buyerCookie, headers=buyerHeader, json=buyerParam)
    except BaseException as e:
        print('【购买】请求出错：' + str(e))
    else:
        print("\033[37m" + "捡漏结果： " + response.text + "\033[0m")
        try:
            datas = response.json()
        except BaseException as e:
            print('【购买】读取响应出错：' + str(e))
        else:
            if(datas['code'] == 'OK'):
                postVX(id, price)
                print("\033[32m购买成功!!!!!!!!!!!!!!!\033[0m")
                orderID = datas['data']['id']
                json_data = {
                    'bill_orders': [
                        str(orderID),
                    ],  
                    'game': 'csgo',
                }
                try:
                    res = requests.post('https://buff.163.com/api/market/bill_order/ask_seller_to_send_offer', cookies=buyerCookie, headers=buyerHeader, json=json_data)
                except BaseException as e:
                    print('【让卖家发货】请求出错：' + str(e))
                else:
                    if(res.json()['code'] == "OK"):
                        print("\033[32m让卖家发货成功！\033[0m")
                    else:
                        print("\033[31m让卖家发货失败！\033[0m")
                
    #print(id)
    #print("正在购买ing, " + str(price) + '元')
    #p = {}
    #postVX(id, price)

#修改param品类参数
def updateParamCate(cate):
    param['category'] = category
    pass

#修改param时间戳参数
def updateParamTime():
    param['_'] = str(int(time.time() * 1000))

#修改param页数参数
def updateParamPageNum(pagenum):
    param['page_num'] = str(pagenum)

def readCookieJson(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)

def compareP(minP, qgP, dis, id):
    if (float(qgP) > 0):
        if(float(minP) / float(qgP) < float(dis)):
            tradeid = queryTradeId(id)
            buy(minP, id, tradeid)
            time.sleep(3)   #需要删除的
            return tradeid
        else:
            return 0        #不满足折扣条件
    else:
        return -1           #没有求购

def queryTradeId(id):
    myParam = {
    'game': 'csgo',
    'goods_id': id,
    'page_num': '1',
    'sort_by': 'default',
    'allow_tradable_cooldown': '1',
    '_': str(int(time.time() * 1000)),
    }
    myHeader = {
    'authority': 'buff.163.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    # 'cookie': 'Device-Id=kqmGJDf6Qkl6zveRCLkA; Locale-Supported=zh-Hans; steam_info_to_bind=; NTES_P_UTID=C2fynd8JTyuwf6puCpWqsy8ic8u7dXwi|1679896267; nts_mail_user=csgowork@163.com:-1:1; _ntes_nnid=77c26dba47767fc07a96e0725b190eed,1679896312860; _ntes_nuid=77c26dba47767fc07a96e0725b190eed; ANTICSRF=6fb8e92ec315e3be48b0ffa41a1c8d34; to_steam_processing_click230413T18367867951=1; to_steam_processing_click230413T18368117301=1; to_steam_processing_click230413T18363521281=1; to_steam_processing_click230413T18363551641=1; to_steam_processing_click230413T18363560371=1; to_steam_processing_click230413T18363595731=1; to_steam_processing_click230413T18363853961=1; to_steam_processing_click230413T18363874561=1; __bid_n=187c0d878edf7238f44207; NTES_CMT_USER_INFO=540083097%7C%E6%9C%89%E6%80%81%E5%BA%A6%E7%BD%91%E5%8F%8B0wcgep%7Chttp%3A%2F%2Fcms-bucket.nosdn.127.net%2F2018%2F08%2F13%2F078ea9f65d954410b62a52ac773875a1.jpeg%7Cfalse%7CeWQuNDViNGUwY2RkN2E1NDYyM2JAMTYzLmNvbQ%3D%3D; FPTOKEN=q2dywMV2z+tszjm3/AiQ0yygGi5+M8HTL/tXuuukOMqnvKsjn5ADoDfyefScz/W0W1vOsNx9/lySErzbckaJts5Xf4TI7BcQfZ7tJWHFOf+4FtWQf6mm/GHZDOqKYjyAR3hP85o13wOOkxbnid33H2LHfrQo79BN3KmaDjvrkMO5xwmZO8l8BDwells9M2gr28phPkKPy6iQT43j0J8Xzh8A7KLLhDnzRJjfSz6x3USh2iTUYLL9JkOivwp1YfcQuNwLduNtWkvfokYG9Lo+tK8Xzo8zhqr39eOH0FJ7s1/yAXZINwnF2bF6tz5Titn/m2YX0BnGsILKxnlYa1d/ZsVdC5RZYEbZSV4RzeaL5FXjece40MVxz/b/DzGk+E7tg6pt98SCjD5hCpLiX/s+Ng==|e1iTqySNC9GgBxMa2V9fae1Lvb4okZ+M4RuPxJxz1uQ=|10|46f1e8c88109f6d4549805fab3c5722d; game=csgo; NTES_YD_SESS=Dg78nxKhp0e.ec_NRnuE4kwWX8t7p9egMrakgpoOg7slybvYyrnuZzrVxUbEIVGsR4sKz9zMyr8AJMSzRhdX_kJJU8wj1EiKlUMODo0GpesZ_7kv6W433LMxXa7jwXk2D.lDD1ooxVOOpi_xBoogb8DRTZif6vskmnsuptT8LtFszIKX2ZsmUUrEEG2r9YRlhQBqIEjLv2GkbpeifjehZNL9XaIQ.Y3cEgJxHV6aeXuPc; S_INFO=1698196857|0|0&60##|13260933011; P_INFO=13260933011|1698196857|1|netease_buff|00&99|null&null&null#shh&null#10#0#0|&0|null|13260933011; remember_me=U1106797087|MltrYkyLgZpUU89NuSogY8oNjfZg2kBR; session=1-55M1UOaE7qzAU74BqECPVh-55FcwNSdFdT9BIGZZL_u92033646919; csrf_token=IjliY2NjZjc5YzRkMTMzNTUyZjIxMDFhYzgxMDhkYTkzZjAxZDEyYzEi.GBoEog.qTFjzV-CcazIlikcEqeKMUy4Zac',
    'referer': 'https://buff.163.com/goods/'+str(id)+'?from=market',
    'sec-ch-ua': '"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.61',
    'x-requested-with': 'XMLHttpRequest',
}
    cookie = readCookieJson(sys.argv[1])
    try:
        response  = requests.get('https://buff.163.com/api/market/goods/sell_order', params=myParam, cookies=cookie, headers=myHeader)
    except BaseException as e:
        print('查询tradeID出错：' + e)
    else:
        try:
            price = response.json()['data']['items'][0]['price']
            tradeid = response.json()['data']['items'][0]['id']
            #updateTime = response.json()['data']['items'][0]['updated_at']
            #print(updateTime)
            return tradeid
        except BaseException as e:
            print("查询tradeID中解析JSON出错：" + str(e))
            return -1
    return -1


if __name__=='__main__':
    category = input('请输入种类名称:')
    discount = input('请输入折扣：')
    maxP = input('清输入最高价格：')
    updateParamCate(category)
    updateParamTime()
    cookie = readCookieJson(sys.argv[1])

    #print(param)
    #myPause() #暂停

    try:
        response = requests.get(url=overviewUrl, params=param, cookies=cookie, headers=header)
    except requests.exceptions.RequestException as e:
        print('【第一次】请求错误:' + e)
    except KeyError as e:
        print('【第一次】请求错误:' + response.json())
    except NameError as e:    
        print('【第一次】请求错误:' + response.json())
    else:
        total_page = response.json()['data']['total_page']

    #print(total_page)
    #myPause() #暂停
    
    while (total_page >= 1):
        for i in range(1, int(total_page)+1):
            print('当前扫描页数：' + str(i))  #需要删除
            updateParamPageNum(i)
            updateParamTime()
            try:
                response = requests.get(url=overviewUrl, params=param, cookies=cookie, headers=header)
            except BaseException as e:
                print('【爬虫ing】发生错误:' + e)
            else:
                try:
                    items = response.json()['data']['items']
                except BaseException as e:
                    print('读取【响应】【爬虫ing】发生错误:' + str(e) + response.text)
                    break
                #items = response.json()['data']['items']
                for j in range(len(items)):
                    idValue = items[j]['id'] #商品id
                    key = items[j]['name'] #商品名称
                    qgPrice = items[j]['buy_max_price'] #最高求购价
                    minPrice = items[j]['sell_min_price'] #最新底价
                    if(float(minPrice) > float(maxP)):
                        flag = -1
                        print('超过价格')
                        break
                    else:
                        flag = 1
                    result = compareP(minPrice, qgPrice, discount, idValue) #比较
                    #print('交易id：' + str(result))     #需要删除
                    if(result != -1):
                        if(result != 0):
                            pass
                            #buy(key, minPrice, result)
            if flag == -1:
                break
            t = random.randint(800,1000) / 1000
            print('暂停' + str(t) + "秒")        
            time.sleep(t)
        print('大循环结束一次！\n')
        time.sleep(random.randint(3, 120))
    print("请求的品类数据为空！ 结束程序")