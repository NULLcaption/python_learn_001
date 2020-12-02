"""
手机号码SHA-256加密
data_sha = hashlib.sha256(phone.encode('utf-8')).hexdigest()
df = pd.read_excel("F:\\test_data\\1030xpp_q.xlsx")
"""
import pandas as pd
import numpy as np
import hashlib
import openpyxl

df = pd.read_excel("F:\\test_data\\20201030xpp_jbn.xlsx")
fileSavePath = 'F://test_data/20201030xpp_jbn.txt'  # 错误信息储存路径
data = pd.DataFrame(df)
phone = data['手机号']
# print(phone)
phone_list = np.array(phone).tolist()
# print(phone_list)
for index in range(len(phone_list)):
    try:
        data_sha = hashlib.sha256(str(phone_list[index]).encode('utf-8')).hexdigest()
        print(str(phone_list[index]) + "," + data_sha)
        with open(fileSavePath, 'a', encoding='utf-8')as f:
            f.write(str(phone_list[index]) + "," + data_sha)
            f.write('\n')
            f.close()
    except:
        print('错误')
        continue


print("加密完成")
