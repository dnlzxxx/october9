from random import randint
spisok = []
for i in range(10):
    spisok.append(randint(1,10))
print(spisok)
for i in range(len(spisok)):
    spisok.pop(0)
print(spisok)