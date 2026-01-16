dic={}
elec=1
total=float(0)
while elec==1:
    art=input("Dime el nombre del articulo: ")
    precio=float(input("Dime el precio: "))
    dic.update({art:precio})
    total=total+precio
    elec=input("Añadir otro articulo(1) o Parar(0): ")

print("LISTA DE LA COMPRA")
for art in dic.keys():
    print(f"{art}          {dic[art]}")

print(f"Total          {total}")