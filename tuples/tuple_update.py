x=("hi","new","programme")
y=list(x)
print(type(y))
y.append("mine")
y.remove("programme")
x=tuple(y)
print(x)

