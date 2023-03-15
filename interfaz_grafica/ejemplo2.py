import tkinter as tk
from tkinter import filedialog

class EditorTexto:
    def __init__(self, master):
        self.master = master
        self.master.title("Editor de Texto")
        
        # Crear el área de texto
        self.texto = tk.Text(self.master, undo=True)
        self.texto.pack(expand=True, fill="both")
        
        # Crear el menú
        menu_bar = tk.Menu(self.master)
        
        # Menú Archivo
        archivo_menu = tk.Menu(menu_bar, tearoff=0)
        archivo_menu.add_command(label="Abrir", command=self.abrir_archivo)
        archivo_menu.add_command(label="Guardar", command=self.guardar_archivo)
        archivo_menu.add_separator()
        archivo_menu.add_command(label="Salir", command=self.salir)
        menu_bar.add_cascade(label="Archivo", menu=archivo_menu)
        
        # Menú Editar
        editar_menu = tk.Menu(menu_bar, tearoff=0)
        editar_menu.add_command(label="Deshacer", command=self.texto.edit_undo)
        editar_menu.add_command(label="Rehacer", command=self.texto.edit_redo)
        menu_bar.add_cascade(label="Editar", menu=editar_menu)
        
        self.master.config(menu=menu_bar)
    
    def abrir_archivo(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "r") as archivo:
                contenido = archivo.read()
                self.texto.delete("1.0", tk.END)
                self.texto.insert("1.0", contenido)
    
    def guardar_archivo(self):
        file_path = filedialog.asksaveasfilename()
        if file_path:
            with open(file_path, "w") as archivo:
                contenido = self.texto.get("1.0", tk.END)
                archivo.write(contenido)
    
    def salir(self):
        self.master.quit()

root = tk.Tk()
editor = EditorTexto(root)
root.mainloop()
