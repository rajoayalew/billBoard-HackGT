import sqlite3

con = sqlite3.connect("/datas/data.db")
cursor = con.cursor()
print ("Connected to database")

con.close()