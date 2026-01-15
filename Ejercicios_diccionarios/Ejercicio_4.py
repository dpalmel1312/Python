fecha=input("dime la fecha: ")
fecha=fecha.split("/")
dic={
    '01':'enero',
    '02':'febrero',
    '03':'marzo',
    '04':'abril',
    '05':'mayo',
    '06':'junio',
    '07':'julio',
    '08':'agosto',
    '09':'septiembre',
    '10':'octubre',
    '11':'noviembre',
    '12':'diciembre'
    }

print(f"{fecha[0]} de {dic[fecha[1]]} de {fecha[2]}")
