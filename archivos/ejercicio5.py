def cant_lineas(ruta):
    with open(ruta) as archivo:
        lineas = archivo.readlines()
        for lineas in archivo:
           return len(lineas)-1 
        print(len(lineas))

cant_lineas("archivos\\archivo.txt")
