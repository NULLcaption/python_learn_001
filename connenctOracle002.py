"""
python3连接oracle实战02
"""
import cx_Oracle as oracle
import pandas as pd
from sqlalchemy import create_engine

ip = '0.0.0.0'
port = '0'
uname = 'xp'  # 用户名
pwd = '123'  # 密码
tnsname = 'orcl'  # 实例名

# 定义变量
v_pricetype = "'A'"  # 目标量类型
v_org_id = "51601"  # 组织
v_kunnr = "05260002"  # 经销商
v_matnr = "'V1'"  # 品项
v_year = '2020'  # 年
v_month = '01'  # 月

sql_org = "select min(t.price), min(t.ratio) " \
          "from crm.xpp_tb_goals_price t where t.delflag = 0 and t.pricetype = {v_pricetype} " \
          "and t.orgid = {v_org_id} and t.kunnr is null and t.matnr = {v_matnr} " \
          "and {v_year} || {v_month} between t.year_s || t.month_s and t.year_l || t.month_l"

sql_kunnr = "select min(t.price), min(t.ratio) " \
            "from crm.xpp_tb_goals_price t " \
            "where t.delflag = 0 and t.pricetype = {v_pricetype} " \
            "and t.kunnr = {v_kunnr} and t.matnr = {v_matnr} " \
            "and {v_year} || {v_month} between t.year_s || t.month_s and t.year_l || t.month_l"

sql_kunnr_kunag = "select min(t.price), min(t.ratio) " \
                  "from crm.xpp_tb_goals_price t " \
                  "left join crm.crm_tb_kunnr_kunag a on t.kunnr = a.kunnr " \
                  "left join crm.crm_tb_kunnr_kunag b on a.kunag = b.kunag " \
                  "where t.delflag = 0 and t.pricetype = {v_pricetype} " \
                  "and b.kunnr = {v_kunnr} and t.matnr = {v_matnr} " \
                  "and {v_year} || {v_month} between t.year_s || t.month_s and t.year_l || t.month_l"

sql_org_kunnr = "select min(t.price), min(t.ratio) " \
                "from crm.xpp_tb_goals_price t " \
                "left join crm.crm_tb_kunnr a on t.orgid = a.org_id " \
                "where t.delflag = 0 and t.pricetype = {v_pricetype} " \
                "and a.kunnr = {v_kunnr} and t.matnr = {v_matnr} " \
                "and {v_year} || {v_month} between t.year_s || t.month_s and t.year_l || t.month_l"

print(sql_org.format_map(vars()))

print(sql_kunnr.format_map(vars()))

print(sql_kunnr_kunag.format_map(vars()))

print(sql_org_kunnr.format_map(vars()))


# 获取价格
def get_price(sql_org):
    dsnStr = oracle.makedsn(ip, port, service_name=tnsname)
    connect_str = "oracle://%s:%s@%s" % (uname, pwd, dsnStr)
    create_engine(connect_str)

    datas = pd.read_sql(sql_org, connect_str)

    print(datas)


get_price(sql_org_kunnr.format_map(vars()))
