import sqlite3
import mysql.connector
import os
import time
#Execute below mention command to install libraries
#pip install mysql-connector-python
#pip install sqlite3

#Here you can set the configaration of your mysql server.
mydb = mysql.connector.connect(
      host="sg1",
      user="rdbn",
      passwd="mo",
      database="rdb"
    )
def insert_to_mysql(date,open1,high,low,close,adj,volume):  
    cursor_mysql = mydb.cursor()
    #In mysql you have to create table named 'table_data' and below mentioned column
    sql = "INSERT INTO table_data (Date,Open,High,Low,Close,Adj_close,Volume) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    val = (date,open1,high,low,close,adj,volume)
    cursor_mysql.execute(sql,val)
    mydb.commit()
    

def fetch_from_sqlite(path):
    conn_lite = sqlite3.connect(path)  
    print("Opened database successfully");  
    cursor_lite = conn_lite.cursor()
    cursor_lite.execute("SELECT name FROM sqlite_master WHERE type='table';")
    list1=cursor_lite.fetchall()
    print(list1)
    #list2=list(list1[0])
    for l in list1:
        str1="select * from "+list(l)[0]
        data = conn_lite.execute(str1);
        for row in data:
            insert_to_mysql(row[0],row[1],row[2],row[3],row[4],row[5],row[6])
    conn_lite.close()
    print("All records inserted to mysql Database")
    os.remove(path)

if __name__=='__main__':
    #just pass the path of sqlite file here
    path="path_to_sqlite_file"
    if os.path.exists(path):
        fetch_from_sqlite(path)
    else:
        print("The file does not exist")
        time.sleep(3)
    
