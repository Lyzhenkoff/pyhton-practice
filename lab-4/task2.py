a = [1,3,5,6]
b = [1,3,6,7]
res = []

for elem in a:
    if elem in b:
        res.append(elem)
print(res)