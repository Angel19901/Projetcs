import tkinter
from tkinter import messagebox
from tkinter import *

ventana = tkinter.Tk()
ventana.geometry("500x600")

etiqueta = tkinter.Label(ventana, text="Log in")
etiqueta.pack()
etiqueta.config(fg="black", font=("BERNARD MT CONDENSED", 24))

etiqueta = tkinter.Label(ventana, text="Usuario")
etiqueta.pack()
etiqueta.config(fg="black", font=("ARIAL", 10))

cajaTexto1 = tkinter.Entry(ventana, bg="light blue")
cajaTexto1.pack()


etiqueta = tkinter.Label(ventana, text="Contraseña")
etiqueta.pack()
etiqueta.config(fg="black", font=("ARIAL",10))

cajaTexto2 = tkinter.Entry(ventana, bg="light blue", show="*")
cajaTexto2.pack()

def insesion():
    C1 = cajaTexto1.get()
    C2 = cajaTexto2.get()
    print(C1)
    print(C2)

    if (cajaTexto1.get()=="" or cajaTexto2.get()=="" ):
        messagebox.showerror("Error!, Llene todos los campos requeridos")
    elif (cajaTexto1.get()=="ABCDEF" and cajaTexto2.get()=="12345" ):
        messagebox.showinfo("Bienvenido!", cajaTexto1.get())
        ventana.destroy()
        ventana2 = tkinter.Tk() #inicio la segunda ventana
        ventana2.geometry("1000x1200")
        ventana2.config(bg = "beige")

        etiqueta = tkinter.Label(ventana2, text="CITAS")
        etiqueta.pack()
        etiqueta.config(fg="black", font=("ARIAL", 20))

        boton1_v2 = tkinter.Button(text="Historial clínico")
        boton1_v2.pack()

        boton2_v2 = tkinter.Button(ventana2, text="Medicamentos")
        boton2_v2.pack()

        boton3_v2 = tkinter.Button(ventana2, text="Resetas")
        boton3_v2.pack()

        boton4_v2 = tkinter.Button(ventana2, text="Usuarios")
        boton4_v2.pack()

    else:
        messagebox.showerror("Error! Datos no válidos")

boton1 = tkinter.Button(ventana, text="Iniciar sesión", command=insesion, bg="light blue")
boton1.pack()

ventana.mainloop()



