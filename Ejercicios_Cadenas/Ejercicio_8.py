precio = float (input ("dime el precio del producto en euros: "))
parte = str(precio).split(".")
print ("El precio en euros es: ", parte[0], " y los centimos son: ", parte[1])