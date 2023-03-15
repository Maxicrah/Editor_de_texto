
def solicitar_cadenas(ruta):
 continuar = True
 while continuar:   
        cad=str(input("ingrese cadena: "))
        with open(ruta,"a") as archivo:
            archivo.write(cad + "\n")
            print("Desea seguir añadiendo cadenas?")
            print("1.SI")
            print("2.NO")
            x=int(input("Ingrese una opcion: "))
            if x == 2:
                continuar=False
            else:
                print("ingrese una opcion valida")

solicitar_cadenas("archivospt2\\cad.txt")