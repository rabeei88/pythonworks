from json import load
f=open("C:\\Users\\HP\\OneDrive\\Desktop\\pythonworks\\file data sets\\employee.json","r")
data=load(f)
# print(data)
for emp in data:
    print(emp)