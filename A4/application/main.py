import config
import student_enrollment as se
import addition_courses as ad
def main():
  config.init()
  print("Hi, Welcome to dbms assg 4")
  while True :
    print("Press 1 for adding a course and 2 for enrolling a student")
    query_type = int(input())
    if query_type == 1:
      inp = ad.take_input() 
      print(ad.add_course(inp, config.cnx))
    elif query_type == 2:
      roll_no, course_id = se.take_input()
      if se.student_enroll(roll_no, course_id, config.cnx) == True:
        print("Hurrah Student Is enrolled")
      else :
        print("Sorry he does not have the required prereqs")
    config.cnx.commit()
    print("Do you want to quit? (Y/N)")
    c = input()
    if c.lower() == "y":
      break
if __name__ == "__main__":
  main()
      


  
