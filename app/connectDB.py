# -*- coding: utf-8 -*-
import pyodbc

def select_history_query(query):
    array = []
    con = pyodbc.connect("DRIVER={SQL Server};server=DESKTOP-CU9C662\SQLEXPRESS;database=search;uid=sa;pwd=root")
    cur = con.cursor()
    cur.execute("select top 10 str from query1 where str like '%"+query+"%' order by count desc")
   
    for row in cur:
        row=[x for x in row]
        array.append(row)
    cur.close()
    con.close()
    return array
def select_all_history_query(query):
    array = []
    con = pyodbc.connect("DRIVER={SQL Server};server=DESKTOP-CU9C662\SQLEXPRESS;database=search;uid=sa;pwd=root")
    cur = con.cursor()
    cur.execute("select str from query1")
   
    for row in cur:
        row=[x for x in row]
        array.append(row)
    cur.close()
    con.close()
    return array

def update_count_query(query):
    con = pyodbc.connect("DRIVER={SQL Server};server=DESKTOP-CU9C662\SQLEXPRESS;database=search;uid=sa;pwd=root")
    cur = con.cursor()
    cur.execute("update query1 set count=count+1 where id = (select id from query1 where str =N'"+query+"' and (N'"+query+"' IN (select str from query1)))")
    cur.close()
    con.close()
    return 0

    

def insert_query(query):
    con = pyodbc.connect("DRIVER={SQL Server};server=DESKTOP-CU9C662\SQLEXPRESS;database=search;uid=sa;pwd=root")
    cur = con.cursor()
    cur.execute("insert into query1(str) select N'"+query+"' where NOT(N'"+query+"' IN (select str from query1))")
    cur.commit()
    cur.close()
    con.close()
    return 1

# print(select_history_query('a'))

# print(insert_query(u'công việc'))
