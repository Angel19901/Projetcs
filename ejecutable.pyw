from tkinter import *
import Login

def main():
    # ----------------- ROOT DECLARATION ------------------
    root = Tk()
    root.title('Mi consultorio virtual')
    root.configure(bg = "#53CDB8")
    root.geometry("300x250")
    root.resizable(0, 0)
    root.config(bd= 15)

    Login.login(root)
    root.mainloop()

if __name__ == "__main__":
    main()