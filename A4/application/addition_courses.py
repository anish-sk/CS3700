import execute_query as exe

"""
Steps in adding a course :
1) Check if the teacher ID exists. 
2) Check if a course entry exists with the given course ID and given dept ID. 
3) Check if no other teaching entry exists for that course in even sem 2006 in the same classroom. 
4) If another teaching entry exists for the same professor for the same course then update the classroom
Else add entry into the teaching table 
"""


def get_list_of_employees(cnx):  
  st = "select empId from professor"
  query = (st)
  cursor = cnx.cursor()
  exe.execute_query_without_input(query, cursor)
  ls = [item[0] for item in cursor.fetchall()]
  return ls

def sanity_check_course(course_id, dept_id, cnx):
  st = "select c.courseId, c.deptNo from course as c where c.courseID = '%s' and c.deptNo = %s" % (course_id, dept_id)
  query = (st)
  cursor = cnx.cursor() 
  exe.execute_query_without_input(query, cursor)
  if len(cursor.fetchall()) == 0:
    return False 
  return True

def check_for_update(course_id, teacher_id, cnx):
  st = "select * from teaching as t where t.courseId = '%s' and t.empId = '%s' and t.sem = 'Even' and t.year = 2006" % (course_id, teacher_id)
  query = (st)
  cursor = cnx.cursor() 
  exe.execute_query_without_input(query, cursor)
  if len(cursor.fetchall()) == 0:
    return False 
  return True

def sanity_check_teaching(course_id, classroom, teacher_id, cnx):
  st = "select t.courseId, t.classRoom from teaching as t where t.courseId = '%s' and t.classRoom = '%s' and sem = 'Even' and year = 2006" % (course_id, classroom)
  query = (st)
  cursor = cnx.cursor() 
  exe.execute_query_without_input(query, cursor)
  output = cursor.fetchall()
  if len(output) > 0:
    return False
  return True

def add_course(inp, cnx):
  (course_id, teacher_id, dept_id, classroom) = inp
  employees = get_list_of_employees(cnx)
  if teacher_id not in employees:
    return "Invalid Teacher ID"
  if not sanity_check_course(course_id, dept_id, cnx):
    return "Course does not exist"
  if not sanity_check_teaching(course_id, classroom, teacher_id, cnx):
    return "Teaching entry already exists for classroom"
  if check_for_update(course_id, teacher_id, cnx):
    st = "update teaching set classRoom = '%s' where empId = '%s' and courseId = '%s' and sem = 'Even' and year = '2006'" % (classroom, teacher_id, course_id)
    query = (st)
    cursor = cnx.cursor() 
    exe.execute_query_without_input(query, cursor)
    return "Classroom has been updated"
  else:
    st = "insert into teaching (empId, courseId, sem, year, classRoom) values ('%s', '%s', 'Even', 2006, '%s')" % (teacher_id, course_id, classroom)
    query = (st)
    cursor = cnx.cursor() 
    exe.execute_query_without_input(query, cursor)
    return "Course has been added"
  

def take_input():
  print("Enter the Course ID")
  course_id = input() 
  print("Enter the Teacher ID") 
  teacher_id = input()
  print("Enter the Department ID for the course")
  dept_id = input()
  print("Enter the classroom") 
  classroom = input()
  return (course_id, teacher_id, dept_id, classroom)


  
