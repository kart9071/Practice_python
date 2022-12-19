def myfun(n):
    return lambda a:a+n
tripler=myfun(3)

print(tripler(4))
