import tkinter as tk
from tkinter import filedialog

class TextEditor:

    def __init__(self, master):
        self.master = master
        master.title("Editor de texto plano")

        # Crear menús
        self.menu_bar = tk.Menu(master)
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.help_menu = tk.Menu(self.menu_bar, tearoff=0)

        # Configurar menú Archivo
        self.file_menu.add_command(label="Abrir", command=self.open_file)
        self.file_menu.add_command(label="Guardar", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Salir", command=self.master.quit)
        self.menu_bar.add_cascade(label="Archivo", menu=self.file_menu)

        # Configurar menú Edición
        self.edit_menu.add_command(label="Cortar", command=self.cut)
        self.edit_menu.add_command(label="Copiar", command=self.copy)
        self.edit_menu.add_command(label="Pegar", command=self.paste)
        self.menu_bar.add_cascade(label="Edición", menu=self.edit_menu)

        # Configurar menú Ayuda
        self.help_menu.add_command(label="Acerca de...", command=self.about)
        self.menu_bar.add_cascade(label="Ayuda", menu=self.help_menu)

        # Configurar textarea
        self.textarea = tk.Text(master)
        self.textarea.pack(fill=tk.BOTH, expand=True)

        # Variables para guardar archivo actual
        self.file_path = None
        self.file_content = ""

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            with open(file_path, "r") as file:
                self.file_path = file_path
                self.file_content = file.read()
                self.textarea.delete(1.0, tk.END)
                self.textarea.insert(tk.END, self.file_content)

    def save_file(self):
        if not self.file_path:
            file_path = filedialog.asksaveasfilename(defaultextension=".txt")
            if file_path:
                self.file_path = file_path
        if self.file_path:
            self.file_content = self.textarea.get(1.0, tk.END)
            with open(self.file_path, "w") as file:
                file.write(self.file_content)

    def cut(self):
        self.textarea.event_generate("<<Cut>>")

    def copy(self):
        self.textarea.event_generate("<<Copy>>")

    def paste(self):
        self.textarea.event_generate("<<Paste>>")

    def about(self):
        about_window = tk.Toplevel(self.master)
        about_window.title("Acerca de...")
        about_label = tk.Label(about_window, text="Desarrollado por [nombre del desarrollador]")
        about_label.pack()

root = tk.Tk()
text_editor = TextEditor(root)
root.config(menu=text_editor.menu_bar)
root.mainloop()
