num1 = input("dime un numero: ")
num2 = input("dime otro numero: ")
if num2 == "0":
    print("Error, no se puede dividir por 0")
else:
    cociente = int(num1) / int(num2)
    print("El cociente es: ", cociente)

