def mostrar_contenido(ruta):
    with open(ruta,"r") as archivo:
        todo_el_contenido = archivo.read()
        print(todo_el_contenido)

mostrar_contenido("archivos\\archivo.txt")                       
