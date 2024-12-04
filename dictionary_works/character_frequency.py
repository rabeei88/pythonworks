
text="ABAABBC"

#most recursive character
#non recursive character

def get_count(char):

    return text.count(char)

most_frequency_character=max(text,key=get_count)
print(most_frequency_character)

least_frequency_character=min(text,key=get_count)
print(least_frequency_character)


