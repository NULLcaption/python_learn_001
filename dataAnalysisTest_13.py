"""
数据数据分析测试一：
案例：微信推广活动领取人数和活动的散点分布
"""
import pandas as pd
from numpy import *
from pyecharts import Bar

df = pd.read_excel("D:\Backup\Downloads\data_12.xls")

user_count = df["领取人数"]
detail_id = df["活动明细ID"]
plan_id = df['活动ID']
org_id = df["大区"]
org_id_1 = df["省区"]
org_id_2 = df["所属地区"]

def bar_test(org_id, user_count):
    X = pd.Series(unique(org_id)).values
    g1 = user_count.groupby(org_id).sum().round(2).values
    Y = pd.Series(g1).values
    bar = Bar("微信推广各大区活动领取人数")
    bar.add("", X, Y, mark_point=["average"])
    bar.render("E:\\py_data_html\\bar_test11.html")


def bar_test(org_id_1, user_count):
    X = pd.Series(unique(org_id_1)).values
    g1=user_count.groupby(org_id_1).sum().round(2).values
    Y = pd.Series(g1).values
    bar = Bar("微信推广各省区活动领取人数")
    bar.add("", X, Y, mark_point=["average"])
    bar.render("E:\\py_data_html\\bar_test12.html")


def bar_test(org_id_2, user_count):
    X = pd.Series(unique(org_id_2)).values
    g1=user_count.groupby(org_id_2).sum().round(2).values
    Y = pd.Series(g1).values
    bar = Bar("微信推广各个所属地区活动领取人数")
    bar.add("", X, Y, mark_point=["average"])
    bar.render("E:\\py_data_html\\bar_test13.html")


bar_test(org_id_1, user_count);