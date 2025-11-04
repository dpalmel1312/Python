edad = input("Ingrese su edad: ")
ingresosm = input("Ingrese sus ingresos mensuales: ")
if int(edad) >= 16:
    if int(ingresosm) >= 1000:
        print("Usted debe tributar.")
    else:
        print("Usted no debe tributar.")