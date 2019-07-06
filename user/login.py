# coding: utf-8
import json
import time
from io import BytesIO

import requests

from consts import *
from PIL import Image
import pytesseract


def capt_fetch():
    """
    获取验证码
    :return:
    """
    r = requests.get(url=IMAGE_CODE)
    f = BytesIO(r.content)
    im = Image.open(f)
    # im.show()
    return im


def capt_download():
    """
    将Image类型的验证码对象保存到本地

    :require Image: from PIL import Image
    :require os: import os

    :require capt_fetch(): 从nbsc网站获取验证码
    :require CAPT_PATH: 验证码保存路径

    :param:
    :return:
    """
    capt = capt_fetch()
    capt.show()

    text = input("请输入验证码中的字符：")
    suffix = str(int(time.time() * 1e3))
    capt.save(CAPT_PATH + text + "_" + suffix + ".jpg")


def capt_text():
    # im = Image.open('./capt/4350_1562229758804.jpg')
    im = capt_fetch()
    # 放大图片，不然识别不出来
    out = im.resize((120, 40))
    text = pytesseract.image_to_string(out, lang='eng')
    print(text)
    return text


def login(account, password):
    capt = capt_text()
    if capt is None:
        print('获取验证码为空')
    payload = {"account": account, "loginType": 0, "newType": 0, "password": password, "verifyCode": capt}
    jsonParam = json.dumps(payload)
    print(jsonParam)
    r = requests.post(url=LOGIN_URL, data=jsonParam, headers={'Content-Type': 'application/json'})
    print(r.content.decode('UTF-8'))
    result = json.loads(r.content)
    print(result)
    sid = result['result']['sid']
    JSON_HEADER['jsessionid'] = sid
    FORM_HEADER['jsessionid'] = sid
    return sid


def login_user(u):
    return login(u.account, u.password)


class User:

    def __init__(self, a, p):
        self.account, self.password = a, p

    def account(self):
        return self.account;

    def password(self):
        return self.password;


if __name__ == '__main__':
    sid = login('', '')
    if sid is None:
        print('获取登录sid为空')
