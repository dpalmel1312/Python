renta= input ("Dime tu renta")

if (renta < 10000):
    print ("Tipos de impositivo 5%")
elif (renta>=10000 or renta<20000):
    print ("Tipos de impositivo 15%")
elif (renta>=20000 or renta<35000):
    print ("Tipos de impositivo 20%")
elif (renta>=35000 or renta<60000):
    print ("Tipos de impositivo 30%")
elif (renta>=60000):
    print ("Tipos de impositivo 45%")
    