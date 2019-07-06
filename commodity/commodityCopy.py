# coding: utf-8

import requests
import json

from consts import *
from user.login import *


def commodity_page():
    """
    curl 'https://app.zhidianlife.com/zdsms/apis/commodity/page' -H 'Accept: application/json, text/plain, */*' -H 'Referer: https://zdshop.zhidianlife.com/' -H 'Origin: https://zdshop.zhidianlife.com' -H 'jsessionid: 30549780AA379CA8312136E2E763C220' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36' -H 'Content-Type: application/json' --data-binary '{"productName":"","productCode":"","isEnable":"1","categoryNo1":"","categoryNo2":"","categoryNo3":"","shopBrandId":"","pageNum":1,"pageSize":20,"serviceName":"primaryCommodityHandlerService"}' --compressed
    :return:
    """
    payload = {"productName": "", "productCode": "", "isEnable": "0", "categoryNo1": "", "categoryNo2": "",
               "categoryNo3": "", "shopBrandId": "", "pageNum": 1, "pageSize": 40,
               "serviceName": "primaryCommodityHandlerService"}
    r = requests.post(url=COMMODITY_PAGE, data=json.dumps(payload), headers=JSON_HEADER)
    print(r.text)


def commodity_copy(productIdList, serviceName):
    url = COMMODITY_COPY + "?"
    for index in range(len(productIdList)):
        if index == 0:
            url += "productIdList=" + productIdList[index]
        else:
            url += "&productIdList=" + productIdList[index]
        url += "&serviceName=" + serviceName

    print(url)
    r = requests.post(url=url, headers=JSON_HEADER)
    print(r.text)


if __name__ == '__main__':
    userList = [User('18578638326', '')]
    productIdList = ['01024fd4d0294f5e991863d4906313aa']
    serviceName = 'warehouseCommodityHanderService'

    for u in userList:
        login_user(u)
        commodity_copy(productIdList, serviceName)
        commodity_page()
