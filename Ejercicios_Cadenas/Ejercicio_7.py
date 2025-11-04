correo = input("Introduce tu correo electrónico: ")
partes = correo.split("@")
nuevocorreo = partes[0] + "@ceu.es"
print("Tu nuevo correo es: ", nuevocorreo)
