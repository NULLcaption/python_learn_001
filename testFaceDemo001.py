"""
利用百度AI接口学习人脸识别
"""
import base64
from aip import AipFace

# 获取access_token
APP_ID = ""
API_KEY = ""
SECRET_KEY = ""

# 连接AI接口
client = AipFace(APP_ID, API_KEY, SECRET_KEY)

# image = "http://b.hiphotos.baidu.com/image/pic/item/32fa828ba61ea8d3fcd2e9ce9e0a304e241f5803.jpg"
# imageType = "URL"
# 图片编码
filepath = "E:\\py_data_html\\22.jpg"
with open(filepath, "rb") as fp:
    base64_data = base64.b64encode(fp.read())
image = str(base64_data, 'utf-8')
imageType = "BASE64"

# 具体参数参照百度AI接口文档
options = {"face_field": "age,beauty,expression,gender", "max_face_num": 1, "face_type": "LIVE", "liveness_control": "LOW"}

result = client.detect(image, imageType, options)

print(result)
print(type(result))
