import mysql.connector as msc

def execute_query_with_input(query, cursor, inp):
  try:
    return cursor.execute(query, inp)
  except msc.Error as e:
    msg = 'Failure in executing query {0}. Error: {1}'.format(query, e)
    #print(msg)
    return msg

def execute_query_without_input(query, cursor):
  try:
    cursor.execute(query)
  except msc.Error as e:
    msg = 'Failure in executing query {0}. Error: {1}'.format(query, e)
    #print(msg)
    return msg 