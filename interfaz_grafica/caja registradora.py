from tkinter import*
from tkinter import ttk

class Interfaz:
    def __init__(self,ventana):
        self.ventana=ventana
        self.productos=("Galletas-$20","Jugo-$10","Chocolate-$100","Papas-$100")
        self.cantidad = IntVar()
        self.caja_total= IntVar()
        self.total = 0
        self.dibujar_componentes()

    def dibujar_componentes(self):
        self.ventana.title("Caja registradora")
        self.ventana.geometry("670x490")
        Label(self.ventana,text="Selecciona tu producto: ").place(x=10,y=10)
        Label(self.ventana,text="Selecciona cantidad: ").place(x=10,y=70)
        Label(self.ventana,text="El total es: ").place(x=430,y=400)
        self.combo = ttk.Combobox(self.ventana,state="readonly")
        self.combo.place(x=10,y=35)
        self.combo["values"]=self.productos
        self.combo.current(0)
        Entry(self.ventana,textvariable=self.cantidad).place(x=10,y=85)
        Entry(self.ventana,textvariable=self.caja_total).place(x=500,y=400)
        Button(self.ventana,text="Agregar al carrito",command=self.agregar_producto).place(x=10,y=110)

        self.tabla = ttk.Treeview(self.ventana,columns=("Cantidad","Subtotal"))
        self.tabla.heading("#0",text="Producto")
        self.tabla.heading("Cantidad",text="Cantidad")
        self.tabla.heading("Subtotal",text="Subtotal")
        self.tabla.place(x=10,y=150)

    def agregar_producto(self):
        texto = self.combo.get()
        datos = texto.split("-$")
        producto = datos[0]
        precio = datos[1]
        cant = self.cantidad.get()
        subtotal =  int(precio)*int(cant)
        self.tabla.insert("",END,text=producto,values=(cant,"$"+str(subtotal)))
        self.total = self.total + subtotal
        self.caja_total.set("$"+str(self.total))

obj = Interfaz(Tk())
obj.ventana.mainloop()