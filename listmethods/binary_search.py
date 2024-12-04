

arr=[4,5,7,20,15,18,22,25]

arr.sort()

search_element=int(input("enter number"))

low=0

upp=len(arr)-1

is_present=False

while(low<=upp):

    mid=(low+upp)//2

    if search_element==arr[mid]:

        is_present=True

        break

    elif search_element<arr[mid]:

        upp=mid-1

    elif search_element>arr[mid]:

        low=mid+1

print(is_present)


