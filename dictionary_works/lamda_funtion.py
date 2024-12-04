#lambda funtion



#lambda funtion for adding 2 numbers

add=lambda n1,n2:n1+n2

print(add(10,20))


#lambda funtion for subtrating 2 numbers

sub=lambda n1,n2:n1-n2

print(sub(10,2))


#lambda for finding cube of a number

cube=lambda n:n**3

print(cube(4))


#lambda for finding square of a number

square=lambda n:n**2

print(square(3))


#max_two string

max_two=lambda str1,str2:str1 if len(str1)>len(str2) else str2

print(max_two("apple","banana"))


#min_two string 

min_two=lambda str1,str2:str1 if len(str1)<len(str2) else str2

print(min_two("grapes","strawberry"))





# def smart_sub(num1,num2):
#     return num1-num2 if num1>num2 else num2-num1
# print(smart_sub(2,8))


smart_sub=lambda num1,num2:num1-num2 if num1>num2 else num2-num1

print(smart_sub(10,20))


#..

words=["hello","hai","text","morning","apple"]

# def get_length(words):
#       return len(words)
# print(max(words,key=get_length))

# get_length=lambda word:len(word)

def get_length(w):

    return len(w)

srt_words=sorted(words,key=get_length,reverse=True)

print(srt_words)