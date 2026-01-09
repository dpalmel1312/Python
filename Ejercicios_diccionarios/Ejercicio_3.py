dic={
    'Plátano': 1.35,
    'Manzana': 0.80,
    'Pera' : 0.85,
    'Naranja' : 0.70
}

pre=input("Dime una fruta")
kilos=print("Dime los kilos que quieres")
if pre in dic:
    ktotal=dic[pre]*kilos
    print(f"El precio es {ktotal}")
else:
    print("Te has inventado la fruta payaso")

