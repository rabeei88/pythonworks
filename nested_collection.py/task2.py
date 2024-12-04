

#task2

student_data={
    "hari":[40,45,35],
    "vipin":[34,40,35],
    "vinay":[40,45,35],
    "bijoy":[33,38,35],
    "anvin":[32,30,40]
}


#index=4  bijoy avg mark
index=4
for i,element in enumerate(student_data):
    if i+1==index:
        print(element)
        marks=student_data.get(element)
        avg=sum(marks)/len(marks)
        print(avg)


# print name and avg mark
std_avg_mark={k:sum(v)/len(v) for k,v in student_data.items()}
print(std_avg_mark)