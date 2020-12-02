"""
爬虫获取国家统计局官网的省市区县街道
获取地址：http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2019/index.html
"""
import random
import re
import requests
import time
import sys

fileSavePath = 'F://test_data/China_Province_2019.txt'  # 数据储存路径
fileSavePath2 = 'F://test_data/China_Province_2019_mistake.txt'  # 错误信息储存路径
results2 = []
results3 = []
results4 = []
results5 = []
Dates1 = []

n = 0
# 获取一级 省份、直辖市信息
url = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2019/index.html'
response = requests.get(url)
response.raise_for_status()  # 如果 HTTP 请求返回了不成功的状态码,Response.raise_for_status() 会抛出一个 HTTPError异常
response.encoding = response.apparent_encoding  # response.apparent_encoding从内容中分析出的响应内容编码方式
pattern = re.compile("<a href='(.*?)'>(.*?)<")  # 正则表达式提取目标字段
result1 = list(set(re.findall(pattern, response.text)))  # 从首层页面获取进入第二层页面的html

# 从一级城市获取二级城市信息
for cycle1 in range(len(result1)):
    try:
        url1 = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2019/{0}'.format(result1[cycle1][0])  # 一级城市url
        id1 = result1[cycle1][0][:2]  # 一级城市编码
        address1 = result1[cycle1][1]  # 一级城市
        response1 = requests.get(url1)
        response1.raise_for_status()
        response1.encoding = response1.apparent_encoding
        response1.close()
        pattern1 = re.compile("<a href='(.*?)'>(.*?)<")  # 正则表达式提取目标字段
        result2_1 = list(set(re.findall(pattern1, response1.text)))
        result2 = []
        for result in result2_1:  # 爬取的城市信息和城市代码混在一起，需要将代码清除
            if '0' not in result[1]:
                result2.append(result)
    except:
        print("Unexpected error:", sys.exc_info())
        with open(fileSavePath2, 'a', encoding='utf-8')as f:
            f.write('{0}|一级错误|一级错误|一级错误|{1}\n'.format('xd', sys.exc_info()))
            f.close()
        time.sleep(10)
        continue
    time.sleep(random.random() * 5)  # 模拟用户浏览，防止因为爬取太频繁导致ip被封。
    # 从二级城市获取三级城市信息
    for cycle2 in range(len(result2)):
        try:
            url2 = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2019/{0}'.format(result2[cycle2][0])  # 二级城市url
            id2 = result2[cycle2][0][3:7]  # 二级城市编码
            address2 = result2[cycle2][1]  # 二级城市
            response2 = requests.get(url2)
            response2.raise_for_status()
            response2.encoding = response2.apparent_encoding
            response2.close()
            pattern2 = re.compile("<a href='(.*?)'>(.*?)<")
            result3_1 = list(set(re.findall(pattern2, response2.text)))
            result3 = []
            for result in result3_1:
                if '0' not in result[1]:
                    result3.append(result)

        except:
            print("Unexpected error:", sys.exc_info())
            with open(fileSavePath2, 'a', encoding='utf-8')as f:
                f.write('{0}|二级错误|二级错误|二级错误|{1}\n'.format('xd', sys.exc_info()))
                f.close()
            time.sleep(10)
            continue
        time.sleep(random.random() * 5)  # 模拟用户浏览，防止因为爬取太频繁导致ip被封。
        # 从三级城市获取四级城市信息
        for cycle3 in range(len(result3)):
            try:
                url3 = 'http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2019/{0}/{1}'.format(result3[cycle3][0][3:5],
                                                                                              result3[cycle3][
                                                                                                  0])  # 三级城市url
                id3 = result3[cycle3][0][3:9]  # 三级城市编码
                address3 = result3[cycle3][1]  # 三级城市
                response3 = requests.get(url3)
                response3.raise_for_status()
                response3.encoding = response3.apparent_encoding
                response3.close()
                pattern3 = re.compile("<a href='(.*?)'>(.*?)<")
                result4_1 = list(set(re.findall(pattern3, response3.text)))
                result4 = []
                for result in result4_1:
                    if '0' not in result[1]:
                        result4.append(result)
                if result4:
                    for cycle4 in range(len(result4)):
                        address = '{0}|{1}|{2}|{3}|{4}|{5}|{6}|{7}' \
                            .format(id1, address1,
                                    id2, address2,
                                    id3, address3,
                                    result4[cycle4][0][3:12], result4[cycle4][1])
                        print(address)
                        with open(fileSavePath, 'a', encoding='utf-8')as f:
                            f.write(address)
                            f.write('\n')
                            f.close()
            except:
                print("Unexpected error:", sys.exc_info())
                with open(fileSavePath, 'a', encoding='utf-8')as f:
                    f.write('{0}|三级错误|三级错误|三级错误|{1}\n'.format(address2, sys.exc_info()))
                    f.close()
                time.sleep(10)
                continue
        time.sleep(random.random() * 5)  # 模拟用户浏览，防止因为爬取太频繁导致ip被封。
    time.sleep(random.random() * 5)  # 模拟用户浏览，防止因为爬取太频繁导致ip被封。

print('一级城市导出完成！')
