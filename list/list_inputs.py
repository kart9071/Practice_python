print("list inputs")
list=[]
n=int(input("Enter any number"))
for i in range(0,n):
    element=int(input("Enter the number to insert"))
    list.insert(i,element)
#for c in range(len(list)):
 #   print(list[c])
[print(x) for x in list]
