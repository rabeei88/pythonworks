 
words=["hello","hai","hello","hai","hai"]
word_count={}

for w in words:
    if w in word_count:
        word_count[w]+=1
    else:
        word_count[w]=1
print(word_count)



#...........

words=["hello","hai","this","is","this","is","hello"]

#word frequency
word_frequency={w:words.count(w) for w in words}

print(word_frequency)

recursive_works=[k for k,v in word_frequency.items() if v>1]  

print(recursive_works)


#display non recursive

#most_recursive





