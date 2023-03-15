def cont_palabras(ruta,palabra):
    
    try:
        with open(ruta,"r",encoding="UTF-8") as archivo:
            contenido = archivo.read().replace("."," ")
            
    except FileNotFoundError:
        error="No se encontro el archivo"
        print(error)
    else:
        
        palabras = contenido.split()
        
        print(palabras.count(palabra))


cont_palabras("archivos\ejemplo.txt", "Lionel")