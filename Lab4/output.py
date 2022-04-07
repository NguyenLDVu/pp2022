import math
import numpy as np
import inputs

def showGPA(numstd,numcour):
    result=[]
    print(" Show GPA : ")
    for i in range(0,numstd):
        avg=[]
        sumcr=[]
        for j in range(0,numcour):
            avg.append(inputs.studentlist[i].getMark(j))
            sumcr.append(inputs.courselist[j].getcredit())
        gpa=round(np.dot(avg,sumcr)/np.sum(sumcr),1)
        result.append({'name':inputs.studentlist[i].getName(),'GPA':gpa})
    print(sorted(result, key=lambda x:x['GPA'], reverse=True))

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
            9. GPA 
            """, end="")
        option = int(input("Your option: "))
        if option==0:
            print("Done!")
            break
        elif option==1:
            student_num = int(input(" Enter the number of students "))
            print(f"There are {student_num} student(s) in this class")
        elif option==2:
            course_num = int(input(" Enter the number of courses "))
            print(f"There are {course_num} course(s) in this class")
        elif option==3:
            if student_num>0:
                inputs.input_student(student_num)
            else:
                while (student_num<=0):
                    print("-> Please enter a correct number of student first")
                    student_num = int(input(" Enter the number of students "))
                    if (student_num>0):
                        inputs.input_student(student_num)
                    else:
                        print("-> Invalid number of student !")
        elif option==4:
            if course_num>0:
                inputs.input_course(course_num)
            else:
                while (course_num<=0):
                    print("-> Please enter a correct number of course first")
                    course_num = int(input(" Enter the number of courses "))
                    if (course_num>0):
                        inputs.input_course(course_num)
                    else:
                        print("-> Invalid number of course !")
        elif option==5:
            if len(inputs.courselist)<=0:
                print("There are no courses detail, please input!")
            else: 
                print("Course List ")
                for i in range(0,course_num):
                    print(f"{i+1} . {inputs.courselist[i].getname()}")
                if len(inputs.courselist)>0:
                    course_seletion = int(input("Choose a course: (by the order) ")) -1
                    if (course_seletion<0) & (course_seletion>course_num):
                        print("-> Invalid input !")
                    else:
                        for k in range(0, student_num ):
                            inputs.studentlist[k].addMark(course_seletion,int(input(f"Mark for student {inputs.studentlist[k].getName()}: ")))
        elif option==6:
            print(" Student List ")
            for i in range(0,student_num):
                inputs.studentlist[i].printstudent()
        elif option==7:
            print(" Course List ")
            for i in range(0,course_num):
                inputs.courselist[i].printcourse()
        elif option==8:
            print(" ->  Marsheet: ")
            for i in range (0,course_num):
                print("course: ",inputs.courselist[i].getname())
                print("  Order.   ID   -   Name   -   Mark")
                for j in range (0,student_num):
                    try:
                        print(f"   {j+1}.     {inputs.studentlist[j].getID()}   -   {inputs.studentlist[j].getName()}   -   {inputs.studentlist[j].getMark(i)}")
                    except:
                        print("-> Do not have data yet")
                        break
        elif option==9:
            showGPA(student_num,course_num)
        else:
            print("-> Option is invalid, please choose again ")
        

        
