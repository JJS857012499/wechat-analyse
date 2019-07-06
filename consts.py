# coding: utf-8

JSON_HEADER = {"Accept": "application/json, text/plain, */*",
               "Content-Type": "application/json",
               "jsessionid": "30549780AA379CA8312136E2E763C220",
               "Origin": "https://zdshop.zhidianlife.com",
               "Referer": "https://zdshop.zhidianlife.com/",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}

FORM_HEADER = {"Accept": "application/json, text/plain, */*",
               "Content-Type": "application/x-www-form-urlencoded",
               "jsessionid": "30549780AA379CA8312136E2E763C220",
               "Origin": "https://zdshop.zhidianlife.com",
               "Referer": "https://zdshop.zhidianlife.com/",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"}

CAPT_PATH = './capt/'

BASE_URL = 'https://app.zhidianlife.com'
# 验证码
IMAGE_CODE = BASE_URL + '/passport/cmm/imageCode';
# 登录
LOGIN_URL = BASE_URL + '/passport/merchant/v2/login'

# 商品列表
COMMODITY_PAGE = BASE_URL + '/zdsms/apis/commodity/page'
# 商品复制
COMMODITY_COPY = BASE_URL + '/zdsms/apis/commodity/batchCopyCommodity'