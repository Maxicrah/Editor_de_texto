import tkinter as tk
from tkinter import ttk
class App(ttk.Frame):
 
 def __init__(self, parent):
    super().__init__(parent)
    
    etiqueta = ttk.Label(parent, text="Hola")
    etiqueta.bind("<ButtonPress-1>", self.click_etiqueta)

 def click_etiqueta(self):
    print("Se hizo click izquierdo en la etiqueta")

root = tk.Tk()
App(root).grid()
root.mainloop()