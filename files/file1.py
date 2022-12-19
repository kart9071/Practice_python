

# f=open("../new.txt","r")
# print(f.read(5))
# f.close()

p=open("../hello/hi.txt","r")
for x in p:
    print(x)
n=open("../hello/hi.txt","a")
n.write("now the file has more content")
n.close()
p.close()