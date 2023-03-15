def mostrar_cant_car(ruta):
    with open(ruta) as archivo:
        cant_car=archivo.read().replace("\n"," ")
        print(cant_car)

mostrar_cant_car("archivos\\archivo.txt")