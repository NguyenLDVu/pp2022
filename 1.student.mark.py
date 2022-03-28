import string

courselist=[]
studentlist=[]
marks=[]

def input_num(num):
    return int(input(f"Number of {num} in the class: "))

def input_student(nst):
    for i in range(0, nst):
        print(f"Student {i+1}'s information: ")
        ID = input(" Student ID : ")
        name = input(" Student name : ")
        DoB = input(" Student DoB (dd/mm/yyyy) : ")
        studentlist.append({"ID":ID,"name":name,"DoB":DoB})

def input_course(nc):
    for j in range(0,nc):
        print(f" Course {j+1}'s information: ")
        Id = input(" Course ID : ")
        Name = input(" Course's Name : ")
        courselist.append({"Id":Id,"Name":Name})

def input_mark(course_Selection,nst):
    for k in range(0, nst):
        mark=input((f"Mark for student {studentlist[k]['name']}: "))
        if "mark" not in studentlist[k]:
            studentlist[k]["mark"]={}
        studentlist[k]["mark"][course_Selection] = mark

def listStudent(studentlist,nst):
    if len(studentlist)<=0:
        print("-> There are no students details, please input!")
        return
    print("""-> Student list: (  Order. ID  -  Name - DoB  )  """)
    for i in range(0,nst):
        print(f"{i+1}. {studentlist[i]['ID']} - {studentlist[i]['name']} - {studentlist[i]['DoB']}")

def listcourse(courselist,nc):
    if len(courselist)<=0:
        print("There are no courses detail, please input!")
        return
    print("""-> Course list: (  Order.  ID   -  Name  ) """)
    for j in range(0,nc):
        print(f"{j+1}. {courselist[j]['Id']} - {courselist[j]['Name']}")

def main():
    student_num=0
    course_num=0
    option=1
    while (option!=0):
        print(""" Choose option :
                0. Exit
                1. Input number of students
                2. Input number of courses
                3. Input student information
                4. Input course Information
                5. Input mark
                6. List student
                7. List course
                8. Marksheet 
                Your option: """, end="")
        option = int(input())
        if option==0:
            print("Done!")
            break
        elif option==1:
            student_num = input_num("student")
            print(f"There are {student_num} student(s) in this class")
        elif option==2:
            course_num = input_num("course")
            print(f"There are {course_num} course(s) in this class")
        elif option==3:
            if student_num>0:
                input_student(student_num)
            else:
                while (student_num<=0):
                    print("-> Please enter a correct number of student first")
                    student_num = input_num("student")
                    if (student_num>0):
                        input_student(student_num)
                    else:
                        print("-> Invalid number of student !")
        elif option==4:
            if course_num>0:
                input_course(course_num)
            else:
                while (course_num<=0):
                    print("-> Please enter a correct number of course first")
                    course_num = input_num("course")
                    if (course_num>0):
                        input_course(course_num)
                    else:
                        print("-> Invalid number of course !")
        elif option==5:
            listcourse(courselist,course_num)
            if len(courselist)>0:
                course_seletion = int(input("Choose a course: (by the order) ")) -1
                if (course_seletion<0) & (course_seletion>course_num):
                    print("-> Invalid input !")
                else:
                    input_mark(course_seletion,student_num)
        elif option==6:
            listStudent(studentlist,student_num)
        elif option==7:
            listcourse(courselist,course_num)
        elif option==8:
            listcourse(courselist,course_num)
            print(" ->  Marsheet: ")
            for i in range (0,course_num):
                print(f"Course {courselist[i]['Name']}")
                print("  Order.   ID   -   Name   -   Mark")
                for j in range (0,student_num):
                    try:
                        print(f"   {j+1}.     {studentlist[j]['ID']}   -   {studentlist[j]['name']}   -   {studentlist[j]['mark'][i]}")
                    except:
                        print("-> Do not have data yet")
                        break
        else:
            print("-> Option is invalid, please choose again ")
           

main()