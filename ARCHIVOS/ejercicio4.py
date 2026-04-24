archivo = open(".\\ARCHIVOS\\log.txt", "a")
texto = input("Ingrese una frase:")
edad = int(input("Ingrese su edad:"))
estatura = float(input("Ingrese su estatura:"))
archivo.write(texto)
archivo.write("\n") # Salto de línea
archivo.write(str(edad)) 
archivo.write("\n") # Salto de línea    
archivo.write(str(estatura))
archivo.write("\n") # Salto de línea
archivo.close()