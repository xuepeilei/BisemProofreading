# -*- coding: UTF-8 -*-  
'''
Created on 2017年4月5日

@author: xue
公共数据库头
'''

import pymysql

connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='******',
    db='bisem',
    charset='utf8'
)
if (not connect.open):
    connect = pymysql.Connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='******',
        db='bisem',
        charset='utf8'
    )
cursor = connect.cursor()
