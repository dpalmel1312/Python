numentero = int(input("Introduce un número entero positivo: "))
for i in range(1, numentero ):
    print(' ' * (numentero - i) + '*' * i)