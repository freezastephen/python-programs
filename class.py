class Student:
    studCount = 0
    
    def __init__(self,rollnumber,name):
        self.rollnumber = rollnumber
        self.name = name
        Student.studCount+= 1
    def totalCount(self):
        print("total number of students"),Student.studCount
    def student(self):
        print ("roll number:"),self.rollnumber,("name:"),self.name

stud1=Student(2018246041,"ram")
stud2=Student(2018246042,"krishna")

stud1.student()
stud2.student()

print Student.studCount