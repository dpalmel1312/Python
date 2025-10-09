cantinicial = float(input("Introduce la cantidad a invertir (€): "))
interes_anualP = float(input("Introduce el interés anual (en %): "))
num_años = int(input("Introduce el número de años: "))

interes_anualD = interes_anualP / 100
capital_final = cantinicial * (1 + interes_anualD) ** num_años

print(f"\nEl capital obtenido tras {num_años} años será de: {capital_final:.2f} €")
