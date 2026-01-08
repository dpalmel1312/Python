palabra = input("Introduce una palabra: ")
letra = input("Introduce una letra: ")
cont = 0
for i in palabra:
    if i == letra:
        cont = cont+1
print("Aparece ", cont , " veces")