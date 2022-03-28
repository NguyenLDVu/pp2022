courselist=[]
studentlist=[]
marks=[]

class student:
    def __init__(self,ID,Name,DoB):
        self._ID=ID
        self._Name=Name
        self._DoB=DoB
        self._marklist={}
    
    def getID(self):
        return self._ID

    def getName(self):
        return self._Name

    def getDoB(self):
        return self._DoB

    def getMark(self,a):
        return self._marklist[a]
    
    def addMark(self,courseID, mark):
        self._marklist[courseID]=mark

    def printstudent(self):
        print(f"{self._ID} - {self._Name} - {self._DoB}")

class course:
    def __init__(self,id,name):
        self._Id=id
        self._name=name

    def getId(self):
        return self._Id
    
    def getname(self):
        return self._name

    def printcourse(self):
        print(f"{self._Id} - {self._name}")

def input_student(nst):
    for i in range(0, nst):
        print(f"Student {i+1}'s information: ")
        ID = input(" Student ID : ")
        name = input(" Student name : ")
        DoB = input(" Student DoB (dd/mm/yyyy) : ")
        studentlist.append(student(ID,name,DoB))

def input_course(nc):
    for j in range(0,nc):
        print(f" Course {j+1}'s information: ")
        Id = input(" Course ID : ")
        Name = input(" Course's Name : ")
        courselist.append(course(Id,Name))

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
            student_num = int(input(" Enter the number of students "))
            print(f"There are {student_num} student(s) in this class")
        elif option==2:
            course_num = int(input(" Enter the number of courses "))
            print(f"There are {course_num} course(s) in this class")
        elif option==3:
            if student_num>0:
                input_student(student_num)
            else:
                while (student_num<=0):
                    print("-> Please enter a correct number of student first")
                    student_num = int(input(" Enter the number of students "))
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
                    course_num = int(input(" Enter the number of courses "))
                    if (course_num>0):
                        input_course(course_num)
                    else:
                        print("-> Invalid number of course !")
        elif option==5:
            if len(courselist)<=0:
                print("There are no courses detail, please input!")
            else: 
                print("Course List ")
                for i in range(0,course_num):
                    print(f"{i+1} . {courselist[i].getname()}")
                if len(courselist)>0:
                    course_seletion = int(input("Choose a course: (by the order) ")) -1
                    if (course_seletion<0) & (course_seletion>course_num):
                        print("-> Invalid input !")
                    else:
                        for k in range(0, student_num ):
                            studentlist[k].addMark(course_seletion,input(f"Mark for student {studentlist[k].getName()}: "))
        elif option==6:
            print(" Student List ")
            for i in range(0,student_num):
                studentlist[i].printstudent()
        elif option==7:
            print(" Course List ")
            for i in range(0,course_num):
                courselist[i].printcourse()
        elif option==8:
            print(" ->  Marsheet: ")
            for i in range (0,course_num):
                print("course: ",courselist[i].getname())
                print("  Order.   ID   -   Name   -   Mark")
                for j in range (0,student_num):
                    try:
                        print(f"   {j+1}.     {studentlist[j].getID()}   -   {studentlist[j].getName()}   -   {studentlist[j].getMark(i)}")
                    except:
                        print("-> Do not have data yet")
                        break
        else:
            print("-> Option is invalid, please choose again ")
        
main()
        
