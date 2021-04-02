from tkinter import *
from tkinter import messagebox

root = Tk()


def btn_click():
    login = logn.get()
    password = passwd.get()

    info_str = f'Данні: {str(login)}, {str(password)}'
    messagebox.showinfo(title='Результат', message=info_str)


root['bg'] = "White"
root.title("Авторизація")
root.geometry('220x220')
root.resizable(width=False, height=False)

text1 = Label(root, text='Авторизація', bg='white', font=("Arial", 15, "bold"))
text1.place(x=45, y=10)

lab1 = Label(root, text='Логін:', bg='white', font=("Arial", 8, "bold"))
lab1.place(x=20, y=40)
lab2 = Label(root, text='Пароль:', bg='white', font=("Arial", 8, "bold"))
lab2.place(x=110, y=40)

logn = Entry(root, width=10)
logn.place(x=20, y=60)
passwd = Entry(root, width=10)
passwd.place(x=110, y=60)

but1 = Button(root, text="Авторизуватися", command=btn_click)
but1.place(x=60, y=100)

root.mainloop()
