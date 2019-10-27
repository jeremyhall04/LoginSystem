from tkinter import *
from tkinter import messagebox
from get_users import check_user, create_user


class Screen:
    def login(self):
        print(self.e.get())

    def __init__(self, master):
        username = StringVar(master)
        password = StringVar(master)

        master.geometry("300x250")
        master.title("Login System")

        Label(master, text="Username").pack()
        e = Entry(master, bd="4")
        e.pack()
        e.focus_set()

        Label(master, text="Password").pack()
        password_in = Entry(master, bd="4")
        password_in.pack()

        Button(master, text="Login", height="2", width="15", command=login).pack()
        Button(master, text="Register", height="2", width="15", command=register).pack()


def register():
    print("Registeration initianted")
    scrn = Tk()
    scrn.geometry("300x250")
    scrn.title("Register an account")

    Label(scrn, text="Enter a username").pack()
    new_user = Entry(scrn, bd="4")
    new_user.pack()

    Label(scrn, text="Enter a password").pack()
    new_password = Entry(scrn, bd="4", show="*")
    new_password.pack()
    Label(scrn, text="Re-enter your password").pack()
    re_pw = Entry(scrn, bd="4", show="*")
    re_pw.pack()

    def verify():
        if new_user.get() != "" and new_password.get() != "" and re_pw.get() != "":
            if new_password.get() == re_pw.get():
                print("Passwords match, account being created")
                create_user(new_user.get(), new_password.get())
                messagebox.showinfo(
                    "Account Created",
                    "Congradulations, you're account was successfully created",
                )
                scrn.destroy()

        else:
            print("Please make sure all data-fields are entered")

    Button(scrn, text="Register New Account", command=verify).pack()

    scrn.mainloop()


def send_login():
    username = u.get()
    password = p.get()
    complete = False
    valid_user = False

    while complete != True:

        (valid_user, pw) = check_user(username, valid_user)
        if valid_user == True:
            if pw == password:
                print("Login Successful")
                complete = True
                open_system()
                break
            else:
                messagebox.showinfo("Error", "Password is incorrect")
                break
        else:
            break


def open_system():
    screen1 = Tk()
    screen1.title("Entered The Database")
    screen1.geometry("300x250")

    Label(screen1, text="You suck")
    screen1.mainloop()


def main_screen(screen):
    screen.geometry("300x250")
    screen.title("Login System")

    Label(screen, text="Username").pack()
    username_in = Entry(screen, bd="4")
    username_in.pack()

    Label(screen, text="Password").pack()
    password_in = Entry(screen, bd="4", show="*")
    password_in.pack()

    Button(screen, text="Login", height="2", width="15", command=send_login).pack()
    Button(screen, text="Register", height="2", width="15", command=register).pack()
    return (username_in, password_in)


root = Tk()
username = StringVar()
password = StringVar()
(u, p) = main_screen(root)
root.mainloop()

