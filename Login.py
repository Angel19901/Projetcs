import tkinter
from tkinter import messagebox
import citas

class login():
    def __init__(self, root):
        self.window = root

        etiqueta = tkinter.Label(root, text="Iniciar sesión")
        etiqueta.pack()
        etiqueta.config(fg="black",bg = "#53CDB8", font=("Arial Baltic", "28"))

        etiqueta = tkinter.Label(root, text="Usuario")
        etiqueta.pack()
        etiqueta.config(fg="black",bg = "#53CDB8", font=("Arial Baltic",12))

        cajaTexto1 = tkinter.Entry(root, borderwidth=3 , bg="white", font=("Arial Baltic", 10))
        cajaTexto1.pack()
        cajaTexto1.insert(0,"@nombre")


        etiqueta = tkinter.Label(root, text="Contraseña")
        etiqueta.pack()
        etiqueta.config(fg="black", bg = "#53CDB8", font=("Arial Baltic",12))
        etiqueta.config()

        cajaTexto2 = tkinter.Entry(root, borderwidth=3, bg="white", show= "*")
        cajaTexto2.pack()

        def insesion():
            user = cajaTexto1.get()
            password = cajaTexto2.get()

            if password == "daf":
                root.destroy()
                citas.firstwindow(user)

            else:
                messagebox.showwarning("Wrong...","Contraseña incorrecta")

        separate = tkinter.Label(root, bg = "#53CDB8", text="      ")
        separate.pack()

        boton1 = tkinter.Button(root, text="Aceptar", command=insesion, bg="light blue")
        boton1.pack()
