fp = open(".\\ARCHIVOS\\ejercicio3.txt", "r", encoding="utf-8")
datos_1 = fp.readlines()
for i in datos_1:
    print(i[0])



