# coding=utf-8
import sqlite3

con = sqlite3.connect("db.sqlite3")
sql1="select name from sqlite_master"
sql2="select * from auth_user_groups"
sql3='select * from sqlite_master where type="table" and name="auth_user_groups"'
sql4='select * from auth_user'
sql5="update auth_user set password='admin9' where username='admin9'"
sql6='drop table testadmin_databaseinfo'
cons = con.execute(sql1)
#con.commit()
j = cons.fetchall()

for i in j:
    for k in i:
        print "%s\t"%k,
    print '\n'

cons.close()
# if __name__=="__main__":
#
#     from django.db import connection
#
#     cursor = connection.cursor()
#     cursor.excute(sql1)
#     j = cons.fetchall()
#
#     for i in j:
#         for k in i:
#             print "%s\t" % k,
#         print '\n'