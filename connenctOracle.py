"""
使用Python3连接oracle数据库并读取数据库 基础
"""
import cx_Oracle as oracle
import pandas as pd
from sqlalchemy import create_engine

# 配置数据库连接路径
conn = oracle.connect('p/123@10.0.0.10:1530/orcl')
# 连接数据库
cursor = conn.cursor()
# sql
cursor.execute("select t.* from crm.crm_tb_quality_checking t")
row = cursor.fetchall()
datas = pd.DataFrame(row)

cursor.close()
conn.commit()
conn.close()

print(datas);
