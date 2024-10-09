from random import randint
spisok = []
summa = 0
for i in range(10):
    spisok.append(randint(1, 10000))
print(spisok)
print(sum(spisok)/len(spisok))
