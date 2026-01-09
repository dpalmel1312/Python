dic={'Euros':'€','Dollar':'$', 'Yen':'¥'}
pre=input("Dime la divisa: ")
if pre in dic:
    print(dic[pre])
else:
    print("La divisa es incorrecta o no esta en el diccionario")


