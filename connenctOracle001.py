"""
python3连接oracle实战01
"""
import cx_Oracle as oracle
import pandas as pd
from sqlalchemy import create_engine

ip = '0.0.0.0'
port = '153'
uname = 'e'  # 用户名
pwd = '123'  # 密码
tnsname = 'orcl'  # 实例名

sql = "select t.* from crm.xpp_tb_goals_price t"


# 连接数据库并查询数据
def connect_data_base(sql):
    dsnStr = oracle.makedsn(ip, port, service_name=tnsname)
    connect_str = "oracle://%s:%s@%s" % (uname, pwd, dsnStr)
    create_engine(connect_str)

    datas = pd.read_sql(sql, connect_str)

    print(datas)


connect_data_base(sql)
