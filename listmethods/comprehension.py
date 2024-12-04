
arr=[3,5,7,9]

square=[num**2 for num in arr]

print(square)

arr=[3,5,6,7,8,9]

square=[num**2 for num in arr]
print("square list",square)

add_ten=[num+10 for num in arr]
print("add ten",add_ten)

odd_numbers=[num for num in arr if num%2!=0]
print("odd num",odd_numbers)

even_numbers=[num for num in arr if num%2==0]
print("even num",even_numbers)

num_gt_number=[num for num in arr if num>5]
print("num>5",num_gt_number)

#

text=("apple","iphone","orange","potatto","tomatto")

starting_vowel=[w for w in text if w[0] in ["a","e","i","o","u"]]

print(starting_vowel)

consonent_word=[w for w in text if w[0] not in ["a","e","i","o","u"]]

print(consonent_word)

long=max([len(w) for w in text ])

longest_word=[w for w in text if len(w)==long]

print(longest_word)

#

 
