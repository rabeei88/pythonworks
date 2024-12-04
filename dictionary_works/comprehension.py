
arr=[10,20,30,10,2,20,3,5,1,2]
#result={key:value iteration condition}

result={num:num**2 for num in arr}

print(result)

#

even_square={num:num**2 for num in arr if num%2==0}

odd_cube={num:num**3 for num in arr if num%2!=0}

print(even_square)

print(odd_cube)

#

frequency_count={num:arr.count(num)for num in arr}

print(frequency_count)