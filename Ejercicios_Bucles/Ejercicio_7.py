numeroentero = int(input("Introduce un número entero positivo: "))
for i in range(1, numeroentero + 1):
    print(' ' * (numeroentero - i) + '*' * i)