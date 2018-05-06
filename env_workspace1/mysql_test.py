# -*- coding: utf-8 -*-
# @Time    : 2018/5/2 22:52
# @Author  : Matthew
# @Site    : 
# @File    : mysql_test.py
# @Software: PyCharm
import MySQLdb
conn= MySQLdb.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='74161',
        db ='menu',
        )
cur = conn.cursor()
cur.execute("create table student(id int ,name varchar(20),class varchar(30),age varchar(10))")
cur.close()
conn.close()