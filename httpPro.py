#coding=utf-8
import requests

#请求地址
targetUrl = "https://www.google.com"

#代理服务器
proxyHost = "127.0.0.1"
proxyPort = "33210"

proxyMeta = "http://%(host)s:%(port)s" % {

    "host" : proxyHost,
    "port" : proxyPort,
}

#pip install -U requests[socks]  socks5 
# proxyMeta = "socks5://%(host)s:%(port)s" % {

#     "host" : proxyHost,

#     "port" : proxyPort,

# }

proxies = {

    "http"  : proxyMeta,
    "https"  : proxyMeta
}

resp = requests.get(targetUrl, proxies=proxies)
print(resp.status_code)
print(resp.text)