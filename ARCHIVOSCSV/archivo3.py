
import csv
with open (".\\ARCHIVOSCSV\\Libro2.csv", mode="r", encoding="utf-8") as archivo:

    lector = csv.DictReader(archivo,delimiter=";")

    for fila in lector:
        nombre = fila["nombre"]
        edad = fila["Edad"]
        estudia = fila["estudia"]
        
        print(f"Nombre: {nombre}, Edad: {edad}, Estudia: {estudia}")
