import mysql.connector
import streamlit as st

#connection

con = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    passwd="",
    db="myDb",
)

cur=con.cursor()

# fetching data to python 

def view_all_data():
    con = mysql.connector.connect(host="localhost",port="3306",user="root",passwd="",db="myDb")
    cur.execute("select * from insurance order by id asc")
    data = cur.fetchall()
    con.close()
    return data
