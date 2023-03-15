def crear_archivo(ruta,contenido):
    with open(ruta, "w") as archivo:
        contenido = archivo.write(contenido)
        print(contenido)

crear_archivo("archivos\\archivo.txt","Hola Mundo")

    