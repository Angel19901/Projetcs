from tkinter import *
from time import localtime, asctime

#def able_date():


#def Add_date():

   # cajaTexto1.insert(0, "@nombre")



class firstwindow():
    def __init__(self,user):
        root = Tk()

        root.config(bd=15, bg="#53CDB8")
        root.title('Mi consultorio virtual')

        # ------FRAMES-----

        title_frame = LabelFrame(root, bg="#53CDB8", relief=FLAT)
        title_frame.grid(row=0, column=1)

        photo_frame = LabelFrame(root, bg="#53CDB8", relief=FLAT)
        photo_frame.grid(row=0, column=2)

        buttons1_frame = LabelFrame(root, bg="#53CDB8")
        buttons1_frame.grid(row=1, column=0)

        tableau_frame = LabelFrame(root, bg="#53CDB8", relief=FLAT)
        tableau_frame.grid(row=1, column=1)

        buttons2_frame = LabelFrame(root, bg="#53CDB8")
        buttons2_frame.grid(row=2, column=1)

        # -----WIDGETS------
        Label(title_frame, text='CITAS', bg="#53CDB8", font=("Comic Sans MS", "28", "normal")).grid(row=0, column=0)

        expedientes_button = Button(buttons1_frame, text='Historiales Clínicos', width=20)
        expedientes_button.configure(bg="light pink", cursor='hand2', font=("Comic Sans MS", "10", "normal"))
        expedientes_button.grid(row=0, column=0, padx=2, pady=3, sticky=W + E)

        Label(buttons1_frame, bg="#53CDB8").grid(row=2, column=0)

        medicine_button = Button(buttons1_frame, text='Medicamentos', width=20)
        medicine_button.configure(bg="light pink", cursor='hand2', font=("Comic Sans MS", "10", "normal"))
        medicine_button.grid(row=3, column=0, padx=2, pady=3, sticky=W + E)

        Label(buttons1_frame, bg="#53CDB8").grid(row=4, column=0)

        prescription_button = Button(buttons1_frame, text='Recetar', width=20)
        prescription_button.configure(bg="light pink", cursor='hand2', font=("Comic Sans MS", "10", "normal"))
        prescription_button.grid(row=5, column=0, padx=2, pady=3, sticky=W + E)

        Label(buttons1_frame, bg="#53CDB8").grid(row=6, column=0)

        users_button = Button(buttons1_frame, text='Usuarios', width=20)
        users_button.configure(bg="light pink", cursor='hand2', font=("Comic Sans MS", "10", "normal"))
        users_button.grid(row=7, column=0, padx=2, pady=3, sticky=W + E)

        # ------TABLA DE CITAS------
        Label(tableau_frame, text="Paciente", relief=RAISED, font=("Comic Sans MS", 11), bg="light gray").grid(row=0,
                                                                                                               column=0,
                                                                                                               sticky=NSEW)
        Label(tableau_frame, text="Fecha", relief=RAISED, font=("Comic Sans MS", 11), bg="light gray").grid(row=0,
                                                                                                            column=1,
                                                                                                            sticky=NSEW)
        Label(tableau_frame, text="Hora", relief=RAISED, font=("Comic Sans MS", 11), bg="light gray").grid(row=0,
                                                                                                           column=2,
                                                                                                           sticky=NSEW)

        for i in range(8):
            for j in range(3):
                l = Entry(tableau_frame, text='', relief=GROOVE, font=("Comic Sans MS", 10), state=DISABLED).grid(row=i + 2, column=j,
                                                                                                  sticky=NSEW)

        # ------Foto/Fecha y hora------
        time= asctime(localtime())
        Label(photo_frame, text= user + "\n" + asctime(localtime()), bg="#53CDB8").grid(row=0, column=0)

        # ---botones add_date, delete_date, exit---
        add_date_button = Button(buttons2_frame, text='Agregar cita', width=20)
        add_date_button.configure(bg="light pink", cursor='hand2', font=("Comic Sans MS", "10", "normal"))
        add_date_button.grid(row=0, column=0, padx=2, pady=3, sticky=W + E)

        delete_date_button = Button(buttons2_frame, text='Recetar', width=20)
        delete_date_button.configure(bg="light pink", cursor='hand2', font=("Comic Sans MS", "10", "normal"))
        delete_date_button.grid(row=0, column=1, padx=2, pady=3, sticky=W + E)

        exit_button = Button(buttons2_frame, text='Salir', width=20)
        exit_button.configure(bg="light pink", cursor='hand2', font=("Comic Sans MS", "10", "normal"))
        exit_button.grid(row=0, column=2, padx=2, pady=3, sticky=W + E)


        root.mainloop()