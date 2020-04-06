a = [1, 2, 3, 4]
b = []

for i in a:
    for j in a:
        for k in a:
            n = i*100 + j*10 + k*1
            b.append(n)
print(b)
print(len(b))
