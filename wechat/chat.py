# -*- coding: utf-8 -*-
import json

import requests
from wxpy import *


# 调用云客智能聊天机器人API，发送消息并获得机器人的回复
def auto_reply(text):
    print('消息：' + text)
    url = "http://api.qingyunke.com/api.php?key=free&appid=0&msg=" + text
    r = requests.post(url)
    result = json.loads(r.content)
    content = result["content"]
    print("回复：" + content)
    return content


if __name__ == '__main__':
    bot = Bot(cache_path=True)
    group = bot.groups().search(keywords='😎😎😎')[0]


    @bot.register(chats=group, msg_types=None, except_self=False)
    def forward_message(msg):
        return auto_reply(msg.text)


    embed()
