with open("new.txt","r") as file1:
    with open("hi.txt","a+") as file2:
            buf=file1.readline()
            word=buf.split('/n')
            print(word)