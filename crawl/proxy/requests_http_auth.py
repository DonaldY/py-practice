import requests

# 代理服务器
proxyHost = "http-dyn.abuyun.com"
proxyPort = "9020"

# 代理隧道验证信息
proxyUser = "1"
proxyPass = "1"

proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
    "host": proxyHost,
    "port": proxyPort,
    "user": proxyUser,
    "pass": proxyPass,
}

proxies = {
    "http": proxyMeta,
    "https": proxyMeta,
}

try:
    response = requests.get('https://httpbin.org/get', proxies=proxies)
    print(response.headers)
    print(response.text)
except requests.exceptions.ConnectionError as e:
    print('Error', e.args)