import csv
peso_total = 0
with open(".\ARCHIVOSCSV\libro1.csv", "r", encoding="utf-8") as csvfile:
    lector = csv.reader(csvfile, delimiter=";")
    encabezado = next(lector)
    for fila in lector:
        peso_total += int(fila[4])
        print(fila)
print(f"Peso total de los aviones: {peso_total} Kg")