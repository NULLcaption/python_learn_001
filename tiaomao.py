import json
import time
import re
import pymysql
from urllib import request


def find_message(url, x, j):
    print('已有' + str(x) + '页无法获取')
    # 读取网页数据
    html = request.urlopen(url).read()
    # 筛选json格式数据
    # jsondata = request.search('^[^(]*?\((.*)\)[^)]*$', html).group(1)
    # 用json加载数据
    data = json.loads(html.decode("utf-8"))
    # 数据保存在变量里
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='root123', db='bootdo', charset='utf8')
    cur = conn.cursor()
    # 连接mysql
    print('连接成功!!!!')
    try:
        for i in range(0, len(data['rateDetail']['rateList'])):
            # print(str(i + 1) + data['rateDetail']['rateList'][i])
            name = data['rateDetail']['rateList'][i]['displayUserNick']
            # 处理过的用户名
            content = data['rateDetail']['rateList'][i]['rateContent']
            # 当天评论
            time = data['rateDetail']['rateList'][i]['rateDate']
            # 评论日期
            iphonetype = data['rateDetail']['rateList'][i]['auctionSku']
            # 机型
            appenddays = data['rateDetail']['rateList'][i]['appendComment']['days']
            # 追加评论的天数
            appendtime = data['rateDetail']['rateList'][i]['appendComment']['commentTime']
            # 追加评论的时间
            appendcontent = data['rateDetail']['rateList'][i]['appendComment']['content']
            # 追加评论的内容
            cur.execute(
                "insert into iphonex(用户名,当天评论,当天时间,机型,追加天数,追加时间,追加评论) values (\"%s\",\"%s\",\"%s\",\"%s\",%d,\"%s\","
                "\"%s\")" % (
                str(name), str(content), str(time), str(iphonetype), int(appenddays), str(appendtime),
                str(appendcontent)))
        print(str(j + 1) + "页数据已经保存")
        # 数据插入mysql
        return x
    except BaseException:
        x += 1
        print('已有' + str(x) + '页无法获取')
        print("####此页无法获取####")
        return x


# 主函数
x = 0
for j in range(1, 5):
    try:
        print("正在获取第{}页评论数据!".format(j))
        url = 'https://rate.tmall.com//list_detail_rate.htm?itemId=16451598759&spuId=937770135&sellerId=725677994' \
              '&order=3&currentPage='+str(j)+'&append=0&content=1&tagId=&posi=&picture=&ua=098' \
              '%23E1hvrpvEvbQvU9CkvvvvvjiPPscw6jDEnLFOAjrCPmPv1jDnPFshtjlbPL5O6jlnn2kjvpvhvvpvvvhCvvOvCvvvphvEvpCW2jDHvvauKWjxsLpZwxkQrfFCKdyIvWmy' \
                                             '%2BE7rVC69rWoQABoXfHTQD7zvdiB%2Bm7zvaNo0HsCNQ4my%2B27rEcqvacc6' \
                                             '%2Bulz8dmxfwmK5dyCvm9vvvvvphvvvvvv9DCvpvFSvvmmZhCv2CUvvUEpphvWwpvv9DCvpv11uphvmvvv92WM' \
                                             '%2FHa6kphvC99vvOC0L9GCvvLMMQvvRphvCvvvvvm5vpvhvvmv99%3D%3D' \
                                             '&isg=BEpKLulwJUNpoKmhq-3jlKTkmzDmOM21nRnN3dSD5B0sh-pBvMkEp2j1k7P-d0Yt&_ksTS=1539742095352_351&callback=jsonp352 '
        x = find_message(url, x, j)
        time.sleep(5)
        # 设置时间间隔（这个不要忽视）
    except BaseException:
        continue