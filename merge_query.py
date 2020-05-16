from lib.v1_mysql_op import lang_lib
from lib.v1_common import mysql_op
import pymysql as db
import pandas as pd
pd.set_option('display.max_columns', 500)

# dw_op = lang_lib(db_name='new_dw')
# cur_dw = dw_op.conn.cursor()

old_dw = lang_lib(db_name='dw')
cur_old_dw = old_dw.conn.cursor(db.cursors.DictCursor) # 加入這段可以匯入表頭

# sql = f"""
# select *
# from lang_share.duration_log_from_prod_2019
# limit 10
# """

sql = f"""
select *
from lang_report.users
limit 10;
"""

cur_old_dw.execute(sql)
data = pd.DataFrame(cur_old_dw.fetchall())

print(data)



# sql = f"""
# ## 近 7 日的觀看時長
# SELECT pfid, SUM(ts) AS watch_duration
# FROM lang_share.duration_log_from_prod
# WHERE LEFT(reg_time, 10) >= CURDATE()-INTERVAL 7 DAY # 近 7 日的觀看紀錄
# #AND LENGTH(pfid)=7
# AND pfid='4758621'
# GROUP BY pfid
# ;
# """

# cur_dw.execute(sql)
# data = pd.DataFrame(cur_dw.fetchall())

# print(data)
