nom=input("Dime tu nombre: ")
edad=int(input("Dime tu edad: "))
direc=input("Dime tu direccion: ")
telf=input("dime tu telefono: ")

dic={'nombre':nom,'edad':edad,'direc':direc,'telf':telf}

print(dic['nombre']," tiene ",dic['edad']," años, vive en ",dic['direc']," y su nomero de telefono es ",dic['telf'])