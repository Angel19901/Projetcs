import tkinter as tk
from tkinter import ttk
from datetime import datetime
import Dates as d
from tkinter import messagebox

def Add2(tree):
    root = tk.Tk()
    root.title("Nueva cita")
    root.geometry("450x100")

    tk.Label(root, text= "Nombre", font=(10)).place(x=10, y=0, width=140, height=30)
    name = tk.Entry(root, relief="sunken", borderwidth=2)
    name.place(x=10, y=31, width=140, height=30)


    def getyears():
        date = datetime.now()
        years = []

        for i in range(5):
            years.append(str(date.year + i))

        return years

    def getmonths():
        months = []

        for i in range(12):
            months.append(str(i + 1))
        return months

    def getdays():
        days = []

        for i in range(31):
            days.append(str(i+1))

        return days

    def gethours():
        hours = []

        for i in range(24):
            hours.append(str(i + 1))

        return hours

    def getminutes():
        minutes = []

        for i in range(60):
            if(i<10):
                minutes.append("0" + str(i + 1))
            else:
                minutes.append(str(i + 1))

        return minutes

    def exit():
        root.destroy()

    #Combobox fechas

    #obtención de año
    tk.Label(root, text= "Fecha", font=(10)).place(x=160, y=0, width=150, height=30)
    year = ttk.Combobox(root, state="readonly")
    year.place(x=160, y=31, width=50, height=30)

    years = getyears()

    year['values'] = (years)

    #mes
    month = ttk.Combobox(root, state="readonly")
    month.place(x=211, y=31, width=50, height=30)

    month['values'] = (getmonths())

    #Día
    day = ttk.Combobox(root, state="readonly")
    day.place(x=262, y=31, width=50, height=30)

    day['values'] = (getdays())

    #Hora
    tk.Label(root, text="Hora", font=(10)).place(x=330, y=0, width=100, height=30)

    hour = ttk.Combobox(root, state="readonly")
    hour.place(x=330, y=31, width=40, height=30)

    hour['values'] = (gethours())

    tk.Label(root, text=":", font=("bold",17)).place(x=371, y=28)

    minute = ttk.Combobox(root, state="readonly")
    minute.place(x=385, y=31, width=50, height=30)

    minute['values'] = (getminutes())

    def save():
        prueba = d.Date()
        try:
            nombre = str(name.get())
            dia = str(day.get())
            mes = str(month.get())
            anio = str(year.get())
            hora = str(hour.get())
            minuto = str(minute.get())

            prueba.GetName(nombre)
            prueba.GetDay(int(dia))
            prueba.GetMonth(int(mes))
            prueba.GetYear(int(anio))
            prueba.GetHour(int(hora))
            prueba.GetMinute(int(minuto))

            prueba.Dump()

            prueba = prueba.LoadToday(anio, mes, dia)[len(prueba.LoadToday(anio, mes, dia))-1]
            fecha = str(str(prueba[2]) + "/" + str(prueba[1]) + "/" + str(prueba[0]))
            hora = str(str(prueba[3]) + ":" + str(prueba[4]))

            tree.insert("", 10, text=prueba[5], values=(fecha, hora))
            exit()

        except:
            messagebox.showerror("¡Error!", "Llene todos los campos requeridos")


    Accept = tk.Button(root, text="Aceptar", bg="light blue", command=lambda: save())
    Accept.place(x=160, y=70, width=60, height=25)



    Exit = tk.Button(root, text="Salir", bg="light blue", command=lambda: exit())
    Exit.place(x=250, y=70, width=60, height=25)


    root.mainloop()




