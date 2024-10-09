stroka = input("Введите строку: ")
stroka = list(stroka)
minus = ["а", "е", "о"]
for i in stroka:
    if i in minus:
        stroka.remove(i)
print(stroka)