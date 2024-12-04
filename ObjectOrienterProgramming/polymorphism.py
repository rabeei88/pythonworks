#method overloading

class Operator:
    def add(self,num1,num2):
        print(num1+num2) #this method do not work because python is interpreted language 

    def add(self,num1,num2,num3):
        print(num1+num2+num3)


obj=Operator()
obj.add(10,20,30)
obj.add(100,200)