# coding=utf-8
import sqlite3

con = sqlite3.connect("db.sqlite3")
sql1="select name from sqlite_master"
sql2="select * from auth_user_groups"
sql3='select * from sqlite_master where type="table" and name="auth_user_groups"'
cons = con.execute(sql3)

j = cons.fetchall()

for i in j:
    for k in i:
        print "%s\t"%k,
    print '\n'

cons.close()