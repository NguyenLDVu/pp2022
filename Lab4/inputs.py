import math
import domain

courselist=[]
studentlist=[]
marks=[]

def input_student(nst):
    for i in range(0, nst):
        print(f"Student {i+1}'s information: ")
        ID = input(" Student ID : ")
        name = input(" Student name : ")
        DoB = input(" Student DoB (dd/mm/yyyy) : ")
        studentlist.append(domain.student(ID,name,DoB))

def input_course(nc):
    for j in range(0,nc):
        print(f" Course {j+1}'s information: ")
        Id = input(" Course ID : ")
        Name = input(" Course's Name : ")
        cr=int(input(" Course's credit: "))
        courselist.append(domain.course(Id,Name,cr))