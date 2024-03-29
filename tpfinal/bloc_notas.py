import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
root=tk.Tk()
class App(ttk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.parent=parent
        parent.title("Editor de texto")
        #asignar menu ventana principal
        self.menu=tk.Menu(self.parent)
        #cuadro texto
        self.cuadro_texto=tk.Text(self.parent)
        self.cuadro_texto.grid(row=1, column=1, pady=10, padx=10, sticky=tk.NSEW)
        #creando menu archivo
        self.menu_arch = tk.Menu(self.menu,tearoff=0)
        self.menu_arch.add_command(label="ABRIR",command=self.abrir_arch)
        self.menu_arch.add_command(label="GUARDAR",command=self.guardar_arch)
        self.menu.add_separator()
        self.menu_arch.add_command(label="SALIR",command=self.salir_arch)
        self.menu.add_cascade(label="Archivo", menu=self.menu_arch)
        #creando menu edicion
        self.menu_edit = tk.Menu(self.menu, tearoff=0)
        self.menu_edit.add_command(label="CORTAR",command=self.cortar)
        self.menu_edit.add_command(label="COPIAR",command=self.copiar)
        self.menu_edit.add_command(label="PEGAR",command=self.pegar) 
        self.menu.add_cascade(label="Edicion", menu=self.menu_edit)
        #creando menu ayuda
        self.menu_ayuda = tk.Menu(self.menu, tearoff=0)
        self.menu_ayuda.add_command(label="Acerca de...", command=self.mostrar_acerca_de)
        self.menu.add_cascade(label="Ayuda", menu=self.menu_ayuda)
        #agregar menu a ventana principal
        self.parent.config(menu=self.menu)


    def abrir_arch(self):
        """funcion paraa abrir un archivo.txt"""
        
        nombre_archivo = filedialog.askopenfilename(title="Abrir", initialdir="C:/", filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])
        #usamos el is not para comparar dos objetos y que no sean lo mismo en este caso comparamos el nombre del archivo con otro objeto "None" (inexistente)
        if nombre_archivo is not None:
            with open(nombre_archivo,"r",encoding="UTF-8") as archivo:
                contenido = archivo.read()
            self.cuadro_texto.delete("1.0","end")    
            self.cuadro_texto.insert("end",contenido)    

    def guardar_arch(self):
        """funcion que guarda un archivo"""
        
        nombre_archivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])
        
        if nombre_archivo is not None:
            contenido = self.cuadro_texto.get("1.0", tk.END)
            with open(nombre_archivo, "w") as archivo:
                archivo.write(contenido)
        else:
            contenido = self.texto.get("1.0", tk.END)
            with open(self.archivo_actual, "w") as archivo:
                archivo.write(contenido)

    def salir_arch(self):
        """metodo para salir de la app"""    
        self.parent.quit()
    

    def cortar(self):
        """metodo para cortar lo seleccionado en el texto"""
        self.cuadro_texto.event_generate("<<Cut>>")
    
    def copiar(self):
        """metodo paraa copiar lo seleccionado del texto"""
        self.cuadro_texto.event_generate("<<Copy>>")
    
    def pegar(self):
        """metodo para pegar fuera o adentro del texto"""
        self.cuadro_texto.event_generate("<<Paste>>")

    def mostrar_acerca_de(self):
        """metodo para mostrar informacion del desarrollador"""
        self.acerca_de=tk.Toplevel(self.parent)
        self.acerca_de.title("Acerca de...")
        ttk.Label(self.acerca_de, text="Editor de Texto\nDesarrollado por Maximiliano Ramiro Flores").grid()


editor_de_texto = App(root).grid()
root.mainloop()