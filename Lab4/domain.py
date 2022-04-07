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
    def __init__(self,id,name,credit):
        self._Id=id
        self._name=name
        self._cr=credit

    def getId(self):
        return self._Id
    
    def getname(self):
        return self._name

    def getcredit(self):
        return self._cr

    def printcourse(self):
        print(f"{self._Id} - {self._name}")