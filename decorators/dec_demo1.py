
class Person:
    name=str
    age=int

    def __init__(self,name,age):
      self.name=name
      self.age=age

    @property
    def get_age(self):
      print(self.age)

    @property
    def get_name(self):
      print(self.name)

person_instance=Person("RABI",21)
person_instance.get_name

 # @property : if we want to convert method to attribute
 # decorator already define chytha function lek puthya features add cheyyal without changing the function definition 
  