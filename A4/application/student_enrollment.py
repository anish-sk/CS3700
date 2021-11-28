import execute_query as exe

def get_all_prereq(course_id, cnx):
  # return a list of prereqs
  st = "SELECT preReqCourse FROM prerequisite WHERE courseId = "+course_id
  query = (st)
  cursor = cnx.cursor()
  exe.execute_query_without_input(query, cursor)
  # cursor.execute(query, (course_id))
  #print(cursor.rowcount)
  ls = [item[0] for item in cursor.fetchall()]
  #print(ls)
  return ls

def sanity_check_teaching(course_id, cnx):
  st = "select * from teaching as t where t.courseID = '%s' and t.sem = 'Even' and t.year = 2006" % (course_id)
  query = (st)
  cursor = cnx.cursor() 
  exe.execute_query_without_input(query, cursor)
  if len(cursor.fetchall()) == 0:
    return False 
  return True

def sanity_check_student(roll_number, cnx):
  st = "select * from student as s where s.rollNo = '%s'" % (roll_number)
  query = (st)
  cursor = cnx.cursor() 
  exe.execute_query_without_input(query, cursor)
  if len(cursor.fetchall()) == 0:
    return False 
  return True

def check_grades(roll_number, cnx):
  # return a list which all courses he/she has passed
  st = "SELECT courseId FROM enrollment WHERE grade <> 'U' AND rollNo = "+roll_number
  query = (st)
  cursor = cnx.cursor()
  # cursor.execute(query, (roll_number))
  exe.execute_query_without_input(query, cursor)
  ls = [item[0] for item in cursor.fetchall()]
  #print(ls)
  return ls

def student_enroll(roll_number, course_id, cnx):
  # check if the course is offered in even sem of 2006
  
  if not sanity_check_teaching(course_id, cnx): 
    return "Course is not offered"

  # check if the student exists
  if not sanity_check_student(roll_number, cnx):
    return "No such student"

  # check if get_all_prereq is subset of check_grades
  
  ls1 = get_all_prereq(course_id,cnx)
  ls2 = set(check_grades(roll_number,cnx))
  for it in ls1:
    if(it not in ls2):
      return "Prerequisites not satisfied"

  st = "INSERT INTO enrollment (rollNo, courseId, sem, year) VALUES ("+roll_number+", "+course_id+", 'Even', 2006)"
  #print(st)
  query = (st)
  cursor = cnx.cursor()
  res = exe.execute_query_without_input(query, cursor)
  ls2 = set(check_grades(roll_number,cnx))
  #print(ls2)
  # cursor.execute(query, (roll_number, course_id))
  if res == None:
    return "Success"
  else:
    return "Failure in executing query"

def take_input():
  print("Enter the Roll Number of the student")
  roll_number = input()
  print("Enter the course Id to register for")
  course_id = input()
  return (roll_number, course_id)


