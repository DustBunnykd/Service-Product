# importing required libraries
import mysql.connector
 
dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="#W15w2020#",
  database = "serviceDB"
)

# preparing a cursor object
cursorObject = dataBase.cursor()
 
# creating table 
Records = """CREATE TABLE  tbl_service  (
                  Services VARCHAR(255) NOT NULL
                   )"""
 
# table created
cursorObject.execute(Records) 
print("Service table created successfully")
# disconnecting from server
dataBase.close()