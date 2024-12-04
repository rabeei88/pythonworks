
text="this is a simple programming question to find word with maximum numbers of character"

#step1 split text to words

words=text.split(" ")
print(words)

#words=['this', 'is', 'a', 'simple', 'programming', 'question', 'to', 'find', 'word', 'with', 'maximum', 'numbers', 'of', 'character']

def get_length(w):

    return len(w)

srt_words=sorted(words,key=get_length,reverse=True)

print(srt_words)



def get_count(w):

    return words.count(w)

frequent_word=max(words,key=get_count)

print(frequent_word)