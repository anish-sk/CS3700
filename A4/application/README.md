# DBMS Assignment 4A
## Group 15 - Members
- Arnhav Abhijit Datar        CS18B003
- Aniswar Srivatsa Krishnan   CS18B050
- Arihant Samar		            CS18B052
- Nischith	Shadagopan M N    CS18B102
- Shreesha G Bhat             CS18B103

## System Requirements
- Python interpreter (Python 3 or above)
- MySql/Mariadb service with the academic\_insti database preloaded
- Appropriate privileges to access the database
  - Modify the following variables in the **config.py** with the appropriate configurations in your system
    1. user - name of the user of the MySql database
    2. password - password for the MySql database
    3. database - name of the database instance where academic\_insti is loaded
    4. host - hostname of the MySql database connection
    5. port - port where the MySql database is present
- Install the following libraries
  1. **mysql-connector-python**
  2. **tkinter**

## Instructions
python **app.py**

## Implementation
- We have two files, one for each of the functionalities. The *add_course*() function in *addition_courses.py* and the *student_enroll*() function in *student_enrollment.py* are the functions which implement the course addition and student enrollment functionalities respectively.  
- There also exists a *execute_query.py* which runs the SQL command as required.
- In the *add_course*() function the following steps are done. 
  - Check if the teacher ID exists
  - Check if a course entry exists with the given course ID and given dept ID. 
  - Check if no other teaching entry exists for that course in even sem 2006 in the same classroom. 
  - If another teaching entry exists for the same professor for the same course then update the classroom entry else add a new entry into the teaching table 
- Similarly in *student_enroll*() function the following steps are done
  - First check if the course is offered in even sem of 2006
  - Then we check whether the student exists
  - Then we check if pre-requisites are cleared
  - If a duplicate entry exists, then MySql returns appropriate error messages
  - Finally we insert into enrollment table
