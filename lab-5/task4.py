a = [1,3,9,6,7,5]
b = []

a.sort()
print(a)
for elem in a:
    if elem % 3 == 0:
        b.append(elem)
print(b)

def myFun (a,b):
    a.sort()
    print(a)
    for elem in a:
        if elem % 3 == 0:
            b.append(elem)
        return print(b)

myFun(a,b)