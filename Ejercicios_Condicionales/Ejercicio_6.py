nom = input("Dime tu nombre")
sex = input("Dime tu sexo")
if (sex == "mujer" and nom < "m") or (sex == "hombre" and nom  > "n"):
    print("Grupo A")
else:
    print("Grupo B")