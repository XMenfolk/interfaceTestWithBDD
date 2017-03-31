# coding=utf-8
'''
@author: Angie
@desc: 操作测试库
'''

import mysql.connector
import datetime


# 配置数据库连接信息
def mysql_conn(db):
    try:
        conn = mysql.connector.connect(
                                            host='',
                                            port=3306,
                                            user='',
                                            passwd='',
                                            db=db,
                                        )
    except Exception as e:
        print '数据库连接失败',e
    else:
        return conn


# 更新数据
def update_order_queue(flag):
    sql = ''
    conn = mysql_conn('db_order')
    cur = conn.cursor()
    cur.execute(sql)
    conn.close()


# 查询数据
def mobileCode(mobile):
    createdTime = datetime.datetime.now().strftime('%b-%d-%y %H:%M:%S')
    sql = ''
    conn = mysql_conn('db_report')
    cur = conn.cursor()
    cur.execute(sql)
    try:
        message = cur.fetchall()[0][0]
        print message
        code = int(message[7:11])
    except Exception as e:
        print '查询无果', e
    conn.close()
    return code





