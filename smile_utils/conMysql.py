#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
step 1: install mysql
>> pip install PyMySQL

step 2: create table
CREATE TABLE `houxrusers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(255) COLLATE utf8_bin NOT NULL,
  `password` varchar(255) COLLATE utf8_bin NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

"""

from __future__ import print_function

import pymysql.cursors

# connect to the database
connection = pymysql.connect(host='ngaribata.mysql.rds.aliyuncs.com',
                             user='houxr',
                             password='HxrOpDev2016_',
                             db='eh_base_feature4',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    # with connection.cursor() as cursor:
    #     # create a new record
    #     sql = " INSERT INTO `houxrusers` (`email`, `password`) VALUES (%s, %s) "
    #     cursor.execute(sql, ('houxiurong111@yeah.net', 'very-secret'))
    #     # connection is not autocommit by default. So you must commit to save
    #     # your changes.
    #     connection.commit()

    # with connection.cursor() as cursor:
    #     # read a single record.
    #     sql = "SELECT id,password FROM houxrusers WHERE email=%s"
    #     cursor.execute(sql, ('houxiurong2@yeah.net',))
    #     result = cursor.fetchone()
    #     print(result)

    with connection.cursor() as cursor:
        # read all date
        sql = "select * from base_bank "
        cursor.execute(sql)
        result = cursor.fetchall()

        for row in result:
            print(row)
finally:
    connection.close()
