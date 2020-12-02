# python 连接mysql数据
import pymysql
import pandas as pd
import time

# 打开数据库连接
# 参数顺序：连接IP，用户名，密码，连接的数据库
db = pymysql.connect("8.133.13.119", "xpp", "Xcrmpp@1234!", "xpp_sfa")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()


# 获取union_all结果集
def get_union_all_function():
    sql = """SELECT
                tad.create_date,
                tad.perform_status_name,
                tad.verification_ratio,
                tad.perform_desc,
                tad.businessType,
                tad.act_terminal_id,
                tad.position_code,
                tad.act_code,
                tad.user_id,
                tah.cost_store_item_id,
                tah.cost_store_id
            FROM
                (
                    SELECT
                        xpp_sfa.ts_terminal_display_info.create_date AS create_date,
                        (
                            CASE
                            WHEN (
                                xpp_sfa.ts_terminal_display_info.perform_status = '001'
                            ) THEN
                                '正常执行'
                            WHEN (
                                xpp_sfa.ts_terminal_display_info.perform_status = '003'
                            ) THEN
                                '部分执行'
                            WHEN (
                                xpp_sfa.ts_terminal_display_info.perform_status = '006'
                            ) THEN
                                '未执行'
                            END
                        ) AS perform_status_name,
                        xpp_sfa.ts_terminal_display_info.verification_ratio AS verification_ratio,
                        xpp_sfa.ts_terminal_display_info.perform_desc AS perform_desc,
                        xpp_sfa.ts_terminal_display_info.id AS id,
                        xpp_sfa.ts_terminal_display_info.act_terminal_id AS act_terminal_id,
                        xpp_sfa.ts_terminal_display_info.position_code AS position_code,
                        xpp_sfa.ts_terminal_display_info.act_code AS act_code,
                        xpp_sfa.ts_terminal_display_info.user_id AS user_id,
                        xpp_sfa.ts_terminal_display_info.visit_id AS visit_id,
                        0 AS businessType
                    FROM
                        xpp_sfa.ts_terminal_display_info
                    UNION ALL
                        SELECT
                            xpp_sfa.ts_act_display.create_date AS create_date,
                            xpp_sfa.ts_act_display.perform_status_name AS perform_status_name,
                            xpp_sfa.ts_act_display.verification_ratio AS verification_ratio,
                            xpp_sfa.ts_act_display.perform_desc AS perform_desc,
                            xpp_sfa.ts_act_display.id AS id,
                            xpp_sfa.ts_act_display.act_terminal_id AS act_terminal_id,
                            xpp_sfa.ts_act_display.position_code AS position_code,
                            xpp_sfa.ts_act_display.act_code AS act_code,
                            xpp_sfa.ts_act_display.user_id AS user_id,
                            xpp_sfa.ts_act_display.visit_id AS visit_id,
                            1 AS businessType
                        FROM
                            xpp_sfa.ts_act_display
                ) tad
            LEFT JOIN xpp_sfa.ts_act_terminal tah ON tah.id = tad.act_terminal_id
            WHERE DATE_FORMAT(tad.create_date, '%Y-%m-%d') >= '2020-08-11'
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
