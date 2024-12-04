from json import load
f2=open("C:\\Users\\HP\\OneDrive\\Desktop\\pythonworks\\file data sets\\country.json","r")
data2=load(f2)
for name in data2:
    print(len(name))