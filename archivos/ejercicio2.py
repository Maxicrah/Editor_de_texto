def nueva_linea(ruta,contenido):
    with open(ruta,"a") as archivo:
        archivo.write(contenido)

nueva_linea("archivos\\archivo.txt","\nNueva linea")        