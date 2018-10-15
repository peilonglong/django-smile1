#!/usr/bin/evn python
# -*- coding: urf-8 -*-
from __future__ import print_function

import pymysql

conn = pymysql.connect(host='ngaribata.mysql.rds.aliyuncs.com', port=3306, user='houxr', passwd='******',
                       db='eh_base_feature4')

cur = conn.cursor()

sql = "select * from houxrusers"
cur.execute(sql)

print("执行的sql:" + sql)
print(cur.description)

for row in cur:
    print(row)

cur.close()
conn.close()
