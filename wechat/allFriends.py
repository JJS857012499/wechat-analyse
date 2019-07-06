# coding: utf-8
import openpyxl as openpyxl
import options as opts
from pyecharts.charts import Geo, Bar
from pyecharts.datasets import COORDINATES
from wxpy import *


def get_friends_info(bot):
    list = [['昵称', '备注名称', '性别', '城市', '省份', '个人签名']]  # 把信息存储为一个二维列表,添加头部信息
    friends = bot.friends()
    for friend in friends:
        nickName = friend.raw.get('NickName', None)  # 获取所有好友信息 raw表示获取全部信息
        remarkName = friend.raw.get('RemarkName', None)
        sex = {1: "男", 2: "女", 0: "未知"}.get(friend.raw.get('Sex', None), None)
        city = friend.raw.get('City', None)
        province = friend.raw.get('Province', None)
        signature = friend.raw.get('Signature', None)
        list_0 = [nickName, remarkName, sex, city, province, signature]
        list.append(list_0)
    return list


def friends_info_to_excel(friends):
    wb = openpyxl.Workbook()
    sheet = wb.active
    for i in range(0, len(friends)):
        for j in range(0, len(friends[i])):
            sheet.cell(row=i + 1, column=j + 1, value=str(friends[i][j]))
    wb.save('./friends.xlsx')
    print('excel保存成功')


def cal_mVw(data):
    result = {}
    for i in data:
        if i == '男':
            result["男"] = result.get("男", 0) + 1
        elif i == '女':
            result["女"] = result.get("女", 0) + 1
        else:
            result["未知"] = result.get("未知", 0) + 1
    return result


def count_city(data):
    result = {}
    for i in data:
        if data is not "NaN" or data is not "nan":
            result[i] = result.get(i, 0) + 1
    return result


if __name__ == '__main__':
    bot = Bot(cache_path='True')
    # 机器人账号自身
    myself = bot.self
    # 发送消息给自己
    # bot.self.send('能收到吗？')

    friends_info = get_friends_info(bot)
    # friends_info_to_excel(friends_info)

    sexs = []
    for index in range(len(friends_info)):
        sexs.append(friends_info[index][2])

    manVSwoman = cal_mVw(sexs)
    print(manVSwoman)

    bar = Bar()
    bar.add_xaxis(list(manVSwoman.keys()))
    bar.add_yaxis("男女比例", list(manVSwoman.values()))
    bar.render(path='sex-render.html')

    citys = []
    for index in range(len(friends_info)):
        citys.append(friends_info[index][3])

    city_dict = count_city(citys)

    city_list = []
    for city in city_dict.keys():
        if city in COORDINATES:  # 在地图上才加进来
            city_list.append((city, str(city_dict[city])))
    print(city_list)

    geo = Geo().add_schema(maptype="china")
    geo.add('好友分布', city_list)
    geo.render(path='geo-render.html')
