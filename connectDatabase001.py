# python 连接mysql数据
import pymysql
import pandas as pd
import time

# 打开数据库连接
# 参数顺序：连接IP，用户名，密码，连接的数据库
db = pymysql.connect("1.11.11.11", "root", "1234!", "")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()


# 获取union_all结果集
def get_union_all_function():
    sql = """
    """
    try:
        datas = pd.read_sql(sql, db)
        return datas[['create_date', 'perform_status_name', 'verification_ratio', 'perform_desc', 'businessType',
                      'act_terminal_id', 'position_code', 'act_code', 'user_id', 'cost_store_item_id',
                      'cost_store_id']]
    except:
        print("Error: unable to fetch data")

    # 关闭数据库连接\
    cursor.close()
    db.close()


def get_tah_id():
    sql = """
        SELECT tah.cost_store_item_id,
                tah.cost_store_id,
                (CASE WHEN (tah.id is NULL) 
                       THEN 0
                      ELSE tah.id  
                END) as id
        From xpp_sfa.ts_act_terminal tah
        WHERE tah.cost_store_item_id is NOT NULL
    """
    try:
        datas = pd.read_sql(sql, db)
        return datas
    except:
        print("Error: unable to fetch data")

    # 关闭数据库连接\
    cursor.close()
    db.close()


def get_tm_position_pp():
    sql = """
            SELECT pp.POSITION_LEVEL,pp.POSITION_CODE
            From xpp_mdm.tm_position pp
        """
    try:
        datas = pd.read_sql(sql, db)
        return datas
    except:
        print("Error: unable to fetch data")

    # 关闭数据库连接\
    cursor.close()
    db.close()


def get_ts_act_head():
    sql = """
                SELECT hd.cost_code
                From xpp_sfa.ts_act_head hd where hd.cost_type IN ('400', '500')
            """
    try:
        datas = pd.read_sql(sql, db)
        return datas
    except:
        print("Error: unable to fetch data")

    # 关闭数据库连接\
    cursor.close()
    db.close()


def get_tm_user():
    sql = """
                    SELECT tu.FULLNAME,tu.username,tu.id
                    From xpp_mdm.tm_user tu
                """
    try:
        datas = pd.read_sql(sql, db)
        return datas
    except:
        print("Error: unable to fetch data")

    # 关闭数据库连接\
    cursor.close()
    db.close()


# 输出最终的结果集
def get_data_mergr():
    start = time.time()
    df = get_union_all_function()
    df_1 = pd.merge(left=df, right=get_tm_position_pp(), how='left', left_on=['position_code'],
                    right_on=['POSITION_CODE'])
    df_2 = pd.merge(left=df_1, right=get_ts_act_head(), how='left', left_on=['act_code'],
                    right_on=['cost_code'])
    df_3 = pd.merge(left=df_2, right=get_tm_user(), how='left', left_on=['user_id'], right_on=['id'])
    end = time.time()
    print('时间差', int(end - start))
    return df_3[['cost_store_item_id', 'create_date', 'perform_status_name', 'verification_ratio', 'perform_desc',
                 'POSITION_LEVEL', 'businessType', 'FULLNAME', 'username']]


print(get_data_mergr())
