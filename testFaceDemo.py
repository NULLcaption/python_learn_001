"""
利用百度AI接口学习人脸识别
"""
import base64
import json
import urllib

import requests
import urllib.request as urllib2

# 获取access_token
appid = ""
api_key = ""
secret_key = ""


def get_access_token():
    """
    其关access_token有效期一般有一个月
    """
    # 此变量赋值成自己API Key的值
    client_id = api_key

    # 此变量赋值成自己Secret Key的值
    client_secret = secret_key

    auth_url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + client_id + '&client_secret=' + client_secret

    header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
                   "Content-Type": "application/json"}

    # 请求获取到token的接口
    response_at = requests.get(auth_url, headers=header_dict)
    json_result = json.loads(response_at.text)
    access_token = json_result['access_token']
    return access_token


filepath = "E:\\py_data_html\\11.jpg"
with open(filepath, "rb") as fp:
    base64_data = base64.b64encode(fp.read())
image = str(base64_data, 'utf-8')

print(image)


# 人脸检测与分析
def parse_face_pic():
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
    params = "{\"image\":\""+image+"\",\"image_type\":\"BASE64\"," \
             "\"face_field\":\"faceshape,facetype\"} "
    access_token = get_access_token()
    request_url = request_url + "?access_token=" + access_token
    # 传入的参数为字节码格式
    data = urllib.parse.quote_plus(params).encode("utf-8")
    # 注意py2和py3的urllib的使用
    request = urllib2.Request(url=request_url, data=data)
    request.add_header('Content-Type', 'application/json')
    response = urllib2.urlopen(request)
    content = response.read()
    if content:
        print(content)


parse_face_pic()
