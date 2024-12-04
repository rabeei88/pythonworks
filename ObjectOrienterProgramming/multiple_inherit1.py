class Person:
    name=str
    age=int

    def __init__(self,name,age):
        self.name=name
        self.age=age

    
    def display_person_info(self):

        print(self.name,self.age)


class Employee:
    emp_id=int
    salary=int

    def __init__(self,emp_id,salary):
        self.emp_id=emp_id
        self.salary=salary

    def display_emp_info(self):
        print(self.emp_id,self.salary)
 

class Manager(Person,Employee):
    def __init__(self,name,age,emp_id,salary,department):
        Person.__init__(self,name,age)
        Employee.__init__(self,emp_id,salary)
        self.department=department
    
    def display_manager_info(self):
        self.display_person_info()
        self.display_emp_info()
        print(self.department)

manager_instance=Manager("rabeeh",22,1,40000,"hr")
manager_instance.display_manager_info()

        