
 # task3


source_word="REGULATE"
target_word="LATE"
 # is a kangaroo word


# character_count={}
# for ch in source_word:
#     if ch in character_count:
#         character_count[ch]+=1
#     else:
#         character_count[ch]=1    #one method
        # print(character_count)   




character_count={ch:source_word.count(ch) for ch in source_word} #dictionary method
# print(character_count)

is_kangaroo=True
for ch in target_word:
    if ch in character_count and character_count.get(ch)>0:
        character_count[ch]-=1
    else:
        is_kangaroo=False
        break
print(is_kangaroo)