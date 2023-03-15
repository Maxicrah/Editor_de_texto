class Archivo:
    def __init__(self,ruta):
        self.ruta=ruta
        
    def crear_archivo(self,contenido):
        with open(self.ruta,"w") as archivo:
            contenido=archivo.write(contenido)
            print(contenido)

    def agregar_contenido(self,cont):
        with open(self.ruta, "a") as archivo:
            archivo.write(cont)

    def mostrar_contenido(self):
        with open(self.ruta) as archivo:
            mostrar_todo=archivo.read()
            print(mostrar_todo)

    def __len__(self):
        with open(self.ruta, "r") as archivo:
            contenido = archivo.read()
            return len(contenido.replace('\n', ''))
            
    @property
    def cant_lineas(self):
        with open(self.ruta,"r") as archivo:
            lineas = archivo.readlines()
            for lineas in archivo:
                return len(lineas)-1 
            

archivo1 = Archivo("archivos\\clase.txt")
archivo1.crear_archivo("Hola soy Maxi")
archivo1.agregar_contenido("\nEsta es otra linea")
archivo1.mostrar_contenido()  
print(len(archivo1))
print(archivo1.cant_lineas)
                        