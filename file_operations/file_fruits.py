
f=open("C:\\Users\\HP\\OneDrive\\Desktop\\pythonworks\\datasets\\fruits.txt","r")

fruits=[]

for line in f:

    fruits.append(line.rstrip("\n"))

print(fruits)