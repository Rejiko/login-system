from tkinter import *


def login():
    logged_in = False
    name = enter_name.get()
    password = enter_password.get()
    file = open("user_details.txt", "r")
    for line in file:
        a, b = line.split(',')
        b = b.strip()
        if name == a and password == b:
            logged_in = True
            file.close()
            break
    if logged_in:
        Label(text="Logged in!", width=22).grid(row=2, column=1, sticky=W)
    else:
        Label(text="Incorrect name or password", width=22).grid(row=2, column=1, sticky=W)


def register():
    name_len = False
    pass_len = False
    taken = False
    name = enter_name.get()
    password = enter_password.get()
    file = open("user_details.txt", "r")
    for line in file:
        a, b = line.split(',')
        b = b.strip()
        if len(name) < 4:
            name_len = True
            file.close()
            break
        if len(password) < 4:
            pass_len = True
            file.close()
            break
        if name == a:
            taken = True
            file.close()
            break
    if name_len:
        Label(text="Username is too short", width=22).grid(row=2, column=1, sticky=W)
    elif pass_len:
        Label(text="Password is too weak!", width=22).grid(row=2, column=1, sticky=W)
    elif taken:
        Label(text="Username already taken", width=22).grid(row=2, column=1, sticky=W)
    else:
        Label(text="Account Registered!", width=22).grid(row=2, column=1, sticky=W)
        file = open("user_details.txt", "a")
        file.write("\n" + name + "," + password)


def exit_here():
    window.destroy()
    exit()


# Window
window = Tk()
window.title("Login System")
window.configure(background="black")

# Labels
label = Label(text="Enter Username", bg="black", fg="white").grid(row=0, column=0, sticky=W)
label2 = Label(text="Enter Password", bg="black", fg="white").grid(row=1, column=0, sticky=W)

# Buttons
button = Button(text="Login", command=login).grid(row=2, column=0, sticky=W)
button2 = Button(text="Register", command=register).grid(row=3, column=0, sticky=W)
exit_btn = Button(text="EXIT", command=exit_here).grid(row=4, column=3, sticky=W)

# Text Entries
enter_name = Entry()
enter_password = Entry()
enter_name.grid(row=0, column=1, sticky=W)
enter_password.grid(row=1, column=1, sticky=W)

window.mainloop()
