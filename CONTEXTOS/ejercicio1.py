nombre_archivo = input("Nombra tu nuevo archivo (ej: diario.txt): ")
nombre_archivo += ".txt"


# Contexto de escritura
with open(nombre_archivo, 'w+') as archivo:
    datos = input("Escribe tu primer secreto: ")
    archivo.write(datos)
    archivo.seek(0) # Volvemos al inicio del archivo para escribir más datos
    print("\n--- Leyendo tu archivo ---")
    print(archivo.read())

# Contexto de lectura
#with open(nombre_archivo, 'r') as archivo:
#    print("\n--- Leyendo tu archivo ---")
#    print(archivo.read())