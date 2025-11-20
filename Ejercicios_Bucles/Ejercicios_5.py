cant = input("Dime la cantidad a invertir")
interes = input("Dime el interes")
años = int(input("Dime los años"))
for i in range(0,años):
    cantidad = float(cant) + (float(cant)*float(interes)/100)
    print("El capital en año  ", i+1, " es de ", cant )

