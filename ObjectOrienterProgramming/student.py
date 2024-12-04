#student [id,name,course]
#set_students()
#display_students

class student:
    
    name=str
    rollnum:int
    age:int
    course:str

#initializing attributes of student class
    def set_students(self,name,rollnum,age,course):
        self.name=name
        self.rollnum=rollnum
        self.age=age
        self.course=course

    def display(self):
        print(self.name,self.rollnum,self.age,self.course)

student_instance1=student()

student_instance1.set_students("rabeeh",7,21,"python django")
student_instance1