# python 连接mysql数据
import pymysql
import pandas as pd
import time

# 打开数据库连接
# 参数顺序：连接IP，用户名，密码，连接的数据库
db = pymysql.connect("127.0.0.1", "root", "root123", "test001")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()


def get_product():
    sql = """
        select p.product_id productId,p.product_name productName from xpp_product p
    """
    try:
        datas = pd.read_sql(sql, db)
        return datas[['productId', 'productName']]
    except:
        print("Error: unable to fetch data")

    # 关闭数据库连接\
    cursor.close()
    db.close()


def get_xpp_query():
    sql = """
            SELECT
                x.open_id openId,
                x.product_id productId,
                substring(x.create_time, 0, 13) createTime
            FROM
                xpp_query x
            WHERE x.create_time < '2020-04-01 00:00:00'
        """
    try:
        datas = pd.read_sql(sql, db)
        return datas[['openId', 'productId', 'createTime']]
    except:
        print("Error: unable to fetch data")

    # 关闭数据库连接\
    cursor.close()
    db.close()


def get_xpp_king():
    sql = """SELECT
            t.code_num codeNum,
            t.iphone,
            t.nickname,
            t.open_id openId,
            t.price,
            t.prize,
            t.uuid,
            substring(t.create_time, 0, 13) createTime
        FROM
            data002 t
        """
    try:
        datas = pd.read_sql(sql, db)
        return datas[['codeNum', 'iphone', 'nickname', 'openId', 'price', 'prize', 'uuid', 'createTime']]
    except:
        print("Error: unable to fetch data")

    # 关闭数据库连接\
    cursor.close()
    db.close()


# 输出最终的结果集
def get_data_mergr():
    start = time.time()
    df = get_xpp_king()
    df_1 = pd.merge(left=df, right=get_xpp_query(), how='inner', on=['openId', 'createTime'])
    df_2 = pd.merge(left=df_1, right=get_product(), how='left', left_on=['productId'],
                    right_on=['productId'])
    end = time.time()
    print('时间差', int(end - start))
    return df_2[
        ['codeNum', 'iphone', 'nickname', 'openId', 'price', 'prize', 'uuid', 'productId', 'productName', 'createTime']]


def write_data_csv():
    # 将数据转化成DataFrame数据格式
    data = pd.DataFrame(get_data_mergr())
    data_1 = data.set_index("codeNum", drop=True)
    pd.DataFrame.to_csv(data_1, "F:\\test_001\\data003.csv", encoding="utf_8_sig")
    print("写入成功")


def main():
    print(get_data_mergr())
    # write_data_csv()


if __name__ == '__main__':
    main()