# import os
# os.remove("hello/hi.txt")
# os.remove("new.txt")
import os
if os.path.exists("hello/hi.txt"):
    print("the file exist")
    x=int(input("press 10 to delete the file..or 0 to exit.."))
    if(x==10):
        os.remove("hello/hi.txt")
        os.rmdir("hello")
    else:
        exit()
else:
    print("the file not exist")