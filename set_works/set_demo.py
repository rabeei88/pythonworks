
st=set()  #for empty set

st={10,20,30,10,40,"hello","hai",True}

print(st)



######set methods

##add()


colors={"red","green","blue"}

colors.add("yellow")

print(colors)


###

arr=[10,20,30,40,20,30]

st=set()

#fetch numbers from array

for num in arr:

    #add num to set

    st.add(num)

#display

print(st)


#.....................intersection

st1={10,20,30,40}

st2={10,20,50,60}

intersection_set=st1.intersection(st2)

print(intersection_set)


#...................union

st1={10,20,30,40,10}

st2={10,20,50,60,70}

union_set=st1.union(st2)

print(union_set)

#...............difference

st1={10,20,30,40,10}

st2={10,20,50,60,70}

difference_set=st1.difference(st2)

print(difference_set)


#........remove

st1={10,20,30,40,10}

st1.remove(10)

print(st1)



#colors...........

colors=["red","yellow","blue","red"]

colors_set=set(colors)

print(colors_set)


#........subset

st1={1,2,3}

st2={1,2,3,4,5}

print(st1.issubset(st2))


#.......superset


st1={1,2,3}

st2={1,2,3,4,5}

print(st2.issuperset(st1))


#...symdiff

st1={1,2,3,10,20}

st2={1,2,3,5,6}

symmetric_difference=st1.symmetric_difference(st2)

print(symmetric_difference)


#update...........

st1={1,2,3}

st2={1,2,3,4,5,6,1,2}

st1.update(st2)

print(st1 )

#.........

text="this is a text to remove duplicate words this text is simple"

#split the text into words

text2="this simple text remove duplicate words"

words=text.split(" ")

words2=text2.split(" ")

print(set(text2).issubset(text))



#..............
