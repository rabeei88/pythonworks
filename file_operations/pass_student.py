
f1=open("C:\\Users\\HP\\OneDrive\\Desktop\\pythonworks\\datasets\\all_students.txt","r")
f2=open("C:\\Users\\HP\\OneDrive\\Desktop\\pythonworks\\datasets\\fail_students.txt","r")

all_std=set()
fail_std=set()

for line in f1:

 line=line.rstrip("\n")

 all_std.add(line)

for line in f2:
 
 line=line.rstrip("\n")

 fail_std.add(line)

pass_std=all_std.difference(fail_std) 

print(pass_std)


