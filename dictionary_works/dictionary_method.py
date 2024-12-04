#dictionary methods
#employee id,name,department,age,salary


employee={"id":17,"name":"rabi","department":"bsc cs","age":21,"salary":15000}

print(employee.get("salary"))#get(key)
#invalid key return none


employee.pop("salary")#pop(key)remove

print(employee)

#return all keys =>keys()

for k in employee.keys():


    print(k)


#fetch all values =>values()

for v in employee.values():

 print(v)




for k,v in employee.items():
   print(k,v)









#dictionary methods 


#get()
#pop()
#keys() return all values
#values() return all values
#items() return all keys and values