#create a dictionary employee with keys   eid,name,salary,department,exp

employee={"eid":13,"name":"rabeei","salary":15000,"department":"bsc cs","exp":2}
print(employee)
 
 #print salary

print(employee["salary"])

#add contact

employee["contact"]=8848775233
print(employee)

#update salary

employee["salary"]=20000
print(employee)

#if exp>4 update employee salary as  current_salary+10000 else current_salary+5000

if employee["exp"]>4:
    employee["salary"]+=10000
else:
    employee["salary"]+=5000
print(employee)

#add role as SDE if exp>5 else add role as IDE

if employee["exp"]>5:
    employee["role"]="SDE"
else:
    employee["role"]="IDE"
print(employee)