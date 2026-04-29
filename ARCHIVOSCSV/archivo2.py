import csv
edad_promedio = 0
with open(".\ARCHIVOSCSV\libro2.csv", "r", encoding="utf-8") as csvfile:
    lector = csv.reader(csvfile, delimiter=";")
    encabezado = next(lector)
    print(encabezado)
    for fila in lector:
        edad_promedio += int(fila[1])
        print(fila)
edad_promedio = edad_promedio/5
print(f"Edad promediode los pasajeros: {edad_promedio} años")