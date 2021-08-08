import sqlite3  
  
con = sqlite3.connect("task.db")  
print("Database opened successfully")  
  
con.execute("create table tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT NOT NULL, description TEXT NOT NULL)")  
  
print("Table created successfully")  
  
con.close()  