def devolver_palabra(ruta,palabra):
    """funcion que devuelve true si existe una palara en un archivo o false en caso conttrario"""
    with open(ruta,"r",encoding="UTF-8") as archivo:
        try:
            contenido = archivo.read()
            for linea in contenido:
                return palabra in contenido
        
        except FileNotFoundError:
            error="No se encontro el archivo"
            print(error)
        
print(devolver_palabra("archivos\ejemplo.txt", "Lionel"))
