edad=input("Dime la edad de tu hijo: ")

if(edad<4):
    print("Tu hijo entra gratis")
elif(edad>=4 or edad<18):
    print("Son 5€ de entrada")
elif(edad>18):
    print("Son 10€ de entrada")