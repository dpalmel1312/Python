punt=float(input("Dime tu puntuacion en la empresa: "))
cantdinero=0
if(punt==0.0):
    cantdinero=2400*punt
    print("Tu nivel de la empresa es Inaceptable y tu cantidades: ",punt)
elif(punt==0.4):
    cantdinero=2400*punt
    print("Tu nivel de la empresa es Aceptable y tu cantidades: ",punt)
elif(punt>=0.6):
    cantdinero=2400*punt
    print("Tu nivel de la empresa es Memoriable y tu cantidades: ",punt)