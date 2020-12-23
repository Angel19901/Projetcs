import tkinter
from tkinter import messagebox
from tkinter import *

ventana = tkinter.Tk() #Primera ventana llamada "ventana"
ventana.geometry("500x600") #Tamaño de la ventana

etiqueta = tkinter.Label(ventana, text="Log in") #Etiqueta que muestra el texto "Log in"
etiqueta.pack()
etiqueta.config(fg="black", font=("BERNARD MT CONDENSED", 24)) #Color, tipo y tamaño de letra del texto

etiqueta = tkinter.Label(ventana, text="Usuario")  #Etiqueta que muestra el texto "Usuario"
etiqueta.pack()
etiqueta.config(fg="black", font=("ARIAL", 10))  #Color, tipo y tamaño de letra del texto

cajaTexto1 = tkinter.Entry(ventana, bg="light blue")  #Asigno el color azul claro a la caja de texto o campo a llenar de Usuario
cajaTexto1.pack()


etiqueta = tkinter.Label(ventana, text="Contraseña")  #Etiqueta que muestra el texto "Contraseña"
etiqueta.pack()
etiqueta.config(fg="black", font=("ARIAL",10))

cajaTexto2 = tkinter.Entry(ventana, bg="light blue", show="*")  # Asigno el color azul claro a la caja de texto o campo a llenar de Contraseña
cajaTexto2.pack()

def insesion(): # Función de iniciar sesión
    C1 = cajaTexto1.get()  # Inicializo el campo1 a llenar (introducir el Usuario)
    C2 = cajaTexto2.get()  # Inicializo el campo2 a llenar (introducir la Contraseña)
    print(C1) # Imprime en la consola el nombre de usuario introducido (no es necesario solo se puso para verificarlo)
    print(C2) # Imprime en la consola el nombre de usuario introducido (no es necesario solo se puso para verificarlo)

    if (cajaTexto1.get()=="" or cajaTexto2.get()=="" ): # Función condicional que avisa cuando NO se han llenado ambos campos (Contraseña e Usuario)
        messagebox.showerror("Error!, Llene todos los campos requeridos")
    elif (cajaTexto1.get() == "ABCDEF" and cajaTexto2.get()=="12345" ): # De lo contrario, si se han llenado correctamente
        messagebox.showinfo("Bienvenido!", cajaTexto1.get()) # Mensaje que muestra "Bienvenido"
        ventana.destroy() # Función "destroy" que cierra la ventana "ventana"
        ventana2 = tkinter.Tk() # Inicio la segunda ventana "ventana2"
        ventana2.geometry("1000x1200") #Tamaño de la ventana "ventana2"
        ventana2.config(bg = "beige") #Color de fondo de la segunda ventana "ventana2"

        etiqueta = tkinter.Label(ventana2, text="CITAS") # Etiqute que muestra en la segunda ventana el texto "CITAS"
        etiqueta.pack()
        etiqueta.config(fg="black", font=("ARIAL", 20))

        boton1_v2 = tkinter.Button(text="Historial clínico") # Botón "Historial clínico"
        boton1_v2.pack()

        boton2_v2 = tkinter.Button(ventana2, text="Medicamentos") # Botón "Medicamentos"
        boton2_v2.pack()

        boton3_v2 = tkinter.Button(ventana2, text="Resetas") # Botón "Resetas"
        boton3_v2.pack()

        boton4_v2 = tkinter.Button(ventana2, text="Usuarios") # Botón "Usuarios"
        boton4_v2.pack()

    else:
        messagebox.showerror("Error! Datos no válidos") # Se han introducido ambos datos pero incorrectamente

boton1 = tkinter.Button(ventana, text="Iniciar sesión", command=insesion, bg="light blue") # Botón de "Iniciar sesión"
boton1.pack()

ventana.mainloop() #Función mainloop