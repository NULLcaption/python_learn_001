import pymysql  # 支持Python3.0
import xlrd
from datetime import datetime
from builtins import int

# 打开数据库
conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="root123", db="test001", charset="utf8")
# 打开游标
cur = conn.cursor()


# 将excel文件导入mysql中
def importExcelToMysql(path):
    # 删除表数据
    # cur.execute("delete from ods_bankdata_gs")
    # 根据Excel路径读取Excel
    workbook = xlrd.open_workbook(path)
    sheets = workbook.sheet_names()
    # 根据sheet名称获取sheet,sheets[0]为第一个表格名称
    worksheet = workbook.sheet_by_name(sheets[0])
    ##遍历行
    for i in range(1, worksheet.nrows):
        row = worksheet.row(i)

        ##初始化数组
        sqlstr = []
        ##遍历列
        for j in range(0, worksheet.ncols):
            ##构造数组
            sqlstr.append(worksheet.cell_value(i, j))

        ##插入数据库
        valuestr = [str(sqlstr[0]), int(sqlstr[1]), str(sqlstr[2]), str(sqlstr[3])]

        ##执行sql语句
        cur.execute(
            "insert into ods_bankdata_gs(name,phone,idnumber,bankname,instime) " +
            "values(%s,%s,%s,%s,sysdate())", valuestr)

    # 关闭游标
    cur.close()
    # 提交
    conn.commit()
    # 关闭连接
    conn.close()
    # 打印信息
    print("数据导入成功！")


# excel表的路径
read03path = r"F:\test\XPP\5.1.xlsx";

# 开始执行时间
starttime = datetime.now()
print(starttime)
##调用函数
importExcelToMysql(read03path)
# 结束时间
endtime = datetime.now()
print(endtime)
