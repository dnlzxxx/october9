from random import randint
spisok = []
for i in range(10):
    spisok.append(randint(1, 10000))
print(spisok)
print(min(spisok))