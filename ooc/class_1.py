class myclass:
    def __init__(self,name,usn,department):
        self.name=name
        self.usn=usn
        self.department=department
    def creating_list(self):
        list1=[]
        list1.append(self.name)
        list1.append(self.usn)
        list1.append(self.department)
        print(list1)

name=input("Enter name of the student")
usn=input("Enter the usn of student")
department=input("Enter the department of student")
p1=myclass(name,usn,department)
p1.creating_list()
# del p1

