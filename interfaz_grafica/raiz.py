from tkinter import*

raiz=Tk()
raiz.title("Hola")#titulo ventana
raiz.resizable(1,1)#redimensionar ventana
#raiz.iconbitmap("gato.ico") #cambiar icono
raiz.geometry("650x350")#ventana redimensionar 
raiz.config(bg="pink")#fondo color

def mensaje():
    print("hola mundo")

lbl = Label(raiz, text= "este es un label tkinter")
lbl.pack()

btn = Button(raiz, text="preisona boton", command=mensaje)
btn.pack()

raiz.mainloop()
