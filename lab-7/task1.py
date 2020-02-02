A = [1,3,2,4,10]
for elem in A:
    h = elem * elem
    A.append(h)
A.reverse()
print(A)