dic={}
stop=True
cantcobrada=0
cantPorCobrar=0

while (stop!=False):
    print(
        "1.AÑadir una factura(1)" \
        "2.Pagar factura existente(2)" \
        "3.Terminar(3)"
        )
    que=input("Escoge: ")
    if(que=="1"):
        cod=input("Dime el codigo de la factura: ")
        cost=int(input("Dime el coste de la factura: "))
        dic.update({cod:cost})
        cantPorCobrar+=cost
        print(f"Cantidad cobrada: {cantcobrada}")
        print(f"Cantida pendiente de cobarar: {cantPorCobrar}")

    elif(que=="2"):
        cod=input("Dime el codigo de la factura: ")
        precio=dic[cod]
        cantcobrada+=precio
        cantPorCobrar-=precio
        dic.pop(cod)
        print(f"Cantidad cobrada: {cantcobrada}")
        print(f"Cantida pendiente de cobarar: {cantPorCobrar}")
        
    elif(que=="3"):
        stop=False
        print(f"Cantidad cobrada: {cantcobrada}")
        print(f"Cantida pendiente de cobarar: {cantPorCobrar}")
        
    else:
        print("Error")
    

