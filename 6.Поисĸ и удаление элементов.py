a = [1, 3, 4, 5]
b = [4, 5, 6, 7]
x = []
for i in b:
    if i not in a:
        x.append(i)
print(x)