import mysql.connector as msc
from mysql.connector import errorcode

cnx = 0
def init():
  global cnx
  cnx = msc.connect(
    user='anish', 
    password= 'kertbert01', 
    database='academic_insti_copy',
    host='localhost',
    port=3306
  )
# query = ("SELECT rollNo FROM enrollment")
# cursor = cnx.cursor()
# cursor.execute(query)
# for (rollNo) in cursor:
#   print(rollNo)
