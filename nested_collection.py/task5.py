

lst1=["apple","mango","onion","potatto"]
lst2=[100,200]
#{"apple":100,"mango":200,"onion:1","potatto":2}


result={}

for i in range(0,len(lst2)):

    list_one_index_element=lst1[i]
    list_two_index_element=lst2[i]

    result[list_one_index_element]=list_two_index_element


    balance_element=lst1[len(lst2):]

    for index,element in enumerate(balance_element):

        result[element]=index+1

print(result)
















# another method

# fruits=["apple","mango","onion","potatto"]

# price=[100,200]

# fruitswithprice={k:p for k,p in zip(fruits,price)}

# print(fruitswithprice)