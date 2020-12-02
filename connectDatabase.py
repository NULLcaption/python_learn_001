# python 连接mysql数据
import pymysql

# 打开数据库连接
# 参数顺序：连接IP，用户名，密码，连接的数据库
db = pymysql.connect("localhost", "root", "root123", "bootdo")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 查询的sql
sql = "select * from sys_role"

try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        role_id = row[0]
        role_name = row[1]
        remark = row[2]
        # 打印结果
        print(f"role_id={role_id},role_name={role_name},remark={remark}")
except:
    print("Error: unable to fetch data")

# 关闭数据库连接
db.close()
