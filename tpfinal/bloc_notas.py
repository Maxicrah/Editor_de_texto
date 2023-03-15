import tkinter as tk
from tkinter import ttk,Button
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
        
        
        #agregar menu a ventana principal
        self.parent.config(menu=self.menu)

        #archivo actual le asignamos el valor None para que inicialice vacio
        self.archivo_actual=None

    def abrir_arch(self):
        
        """funcion para abrir un archivo.txt"""
        
        nombre_archivo = filedialog.askopenfilename(title="Abrir", initialdir="C:/", filetypes=[("Archivos de texto", "*.txt"), ("Todos los archivos", "*.*")])
        if nombre_archivo:
            self.archivo_actual = nombre_archivo
            with open(nombre_archivo,"r",encoding="UTF-8") as archivo:
                contenido = archivo.read()
            self.cuadro_texto.delete("1.0","end")    
            self.cuadro_texto.insert("end",contenido)    

    
    


    def guardar_arch(self):
        pass

    def salir_arch(self):    
        pass
    
    @staticmethod
    def mensaje(msj='mundo!'):
       pass




editor_de_texto = App(root).grid()
root.mainloop()