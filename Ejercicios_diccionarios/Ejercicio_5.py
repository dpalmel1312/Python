dic={'Matemáticas': 6, 'Física': 4, 'Química': 5}
totalcre=int(0)

for asig in dic.keys():
    credits=int(dic[asig])
    totalcre=totalcre + credits
    print(f"{asig} tiene {credits} creditos")

print(f"Total de creditos son {totalcre}")
