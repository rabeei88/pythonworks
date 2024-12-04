
text="ABAHDKDHBCEKDJJ"
#character_frequency{A:2,B:2}

character_frequency={ch:text.count(ch) for ch in text}

print(character_frequency)   #{'A': 2, 'B': 2, 'H': 2, 'D': 3, 'K': 2, 'C': 1, 'E': 1, 'J': 2}



#for loop method

for k,v in character_frequency.items():


    if v==1:

     print(k) 


#.....comprehension method

non_recursive_character=[k for k,v in character_frequency.item() if v==1]

print(non_recursive_character)


