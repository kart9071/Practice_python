with open("Hello.txt","rb") as file1:
    print("the position of the pointer before reading the file",file1.tell())
    file1.read(10)
    print("the position of the pointer after reading the file",file1.tell())
    file1.seek(3,1)
    print("the position of the file after seek is",file1.tell())
    print(file1.read())
    file1.close()