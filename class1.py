class Student:
    studCount = 0
    
    def __init__(self,rollnumber,name,mark1,mark2):
        self.rollnumber = rollnumber
        self.name = name
        self.mark1= mark1
        self.mark2=mark2
        Student.studCount+= 1
    def totalCount(self):
        print("total number of students"),Student.studCount
    def student(self):
        print ("roll number:"),self.rollnumber,("name:"),self.name,("mark1:"),self.mark1,("mark2:"),self.mark2
        print ("total:"),self.mark1+self.mark2
        print ("average:"),self.mark1+self.mark2/2

stud1=Student(2018246041,"ram",60,80)
stud2=Student(2018246042,"krishna",70,90)

stud1.student()
stud2.student()

print Student.studCount