from tkinter import Tk,Label,Button,Entry,Frame

class Mi_ventana(Frame):

    def __init__(self,master=None):
        super().__init__(master,width=320,height=170)
        self.master
        self.pack()
        self.crear_widgets()


    def suma(self):
        n1 = self.txt1.get()
        n2 = self.txt2.get()
        resultado = int(n1) + int(n2) 
        self.txt3.delete(0,"end")
        self.txt3.insert(0,resultado)
   

    def crear_widgets(self):
        self.lbl1=Label(self,text="Primer numero", bg="pink")
        self.lbl1.place(x=10,y=10,width=100,height=30)

        self.txt1=Entry(self, bg="pink")
        self.txt1.place(x=120,y=10,width=100,height=30)

        self.lbl2=Label(self, text="Segundo numero", bg="pink")
        self.lbl2.place(x=10,y=50,width=100,height=30)
        self.txt2=Entry(self, bg="pink")
        self.txt2.place(x=120,y=50,width=100,height=30)

        self.btn1=Button(self, bg="pink",text="Sumar",command=self.suma)
        self.btn1.place(x=230,y=50,width=80,height=30)

        self.lbl3=Label(self, text="Resultado", bg="pink")
        self.lbl3.place(x=10,y=120,width=100,height=30)
        self.txt3=Entry(self, bg="pink")
        self.txt3.place(x=120,y=120,width=100,height=30)

        



ventana = Tk()
ventana.wm_title("Sumar Numeros")
app = Mi_ventana(ventana)


app.mainloop()
    