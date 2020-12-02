# 爬虫获取天猫的评论数据，写到本地文件中
from urllib import request
import time
import os


# 写入函数
def find_message(url, x, j):
    wp = request.urlopen(url)  # 打开连接
    content = wp.read()  # 获取页面内容
    fp = open("data.txt", "w+b")  # 打开一个文本文件
    fp.write(content)  # 写入数据
    fp.close()  # 关闭文件
    print("file" + ":" + str(j) + ".txt")
    time.sleep(1)


# 主函数
x = 0
for j in range(1, 5):
    try:
        print("正在获取第{}页评论数据!".format(j))
        url = 'https://rate.tmall.com//list_detail_rate.htm?itemId=16451598759&spuId=937770135&sellerId=725677994&order=3&currentPage='+str(j)+'&append=0&content=1&tagId=&posi=&picture=&ua=098%23E1hvrpvEvbQvU9CkvvvvvjiPPscw6jDEnLFOAjrCPmPv1jDnPFshtjlbPL5O6jlnn2kjvpvhvvpvvvhCvvOvCvvvphvEvpCW2jDHvvauKWjxsLpZwxkQrfFCKdyIvWmy%2BE7rVC69rWoQABoXfHTQD7zvdiB%2Bm7zvaNo0HsCNQ4my%2B27rEcqvacc6%2Bulz8dmxfwmK5dyCvm9vvvvvphvvvvvv9DCvpvFSvvmmZhCv2CUvvUEpphvWwpvv9DCvpv11uphvmvvv92WM%2FHa6kphvC99vvOC0L9GCvvLMMQvvRphvCvvvvvm5vpvhvvmv99%3D%3D&isg=BEpKLulwJUNpoKmhq-3jlKTkmzDmOM21nRnN3dSD5B0sh-pBvMkEp2j1k7P-d0Yt&_ksTS=1539742095352_351&callback=jsonp352'
        find_message(url, x, j)
        time.sleep(5)
        # 设置时间间隔（这个不要忽视）
    except BaseException:
        continue
