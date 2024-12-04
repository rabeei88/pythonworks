
arr=["100","200","300","400","500","600","700","800"]

odd_position_elements=[arr[i] for i in range (len(arr)) if i%2!=0]

print(odd_position_elements)

for i in range(1,len(arr),2):

    elements=odd_position_elements.pop()

    arr[i]=elements

print(arr)

##

arr=["100","200","300","400","500","600","700","800"]

odd_position_elements=[num for index,num in enumerate(arr) if index%2!=0]

odd_position_elements.reverse()

print(odd_position_elements)

##

arr=["100","200","300","400","500","600","700","800"]

left=1

right=len(arr)-1

if right%2==0:

    right-=1

while(left<right):

    arr[left],arr[right]=arr[right],arr[left]

    left+=2

    right-=2

print(arr)

