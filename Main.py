import random
import tkinter as tk
# Python final project at kaplan
print("Welcome to Personal Finance Tracker")
main_window = tk.Tk()
main_window.geometry("400x300")
main_window.title("Personal Finance Tracker")

greeting = tk.Label(main_window, text= "Welcome to our website", font=("calibri", 14))
greeting.grid(row = 0, column=  0)
username = tk.Label(main_window, text= "Username", font=("calibri", 14))
username.grid(row = 1, column=  0)
password = tk.Label(main_window, text= "Password", font=("calibri", 14))
password.grid(row = 2, column=  0)

user_entry = tk.Entry(main_window, font=("calibri", 14))
user_entry.grid(row = 1, column= 1)

pass_entry = tk.Entry(main_window, font=("calibri", 14), show = "*")
pass_entry.grid(row = 2, column= 1)

def check_pass():
    if user_entry.get() == "MuradWafik" and pass_entry.get() == "123456":
        print("Login Successful")
    else:
        print("Invalid Username or Password")

submit_btn = tk.Button(main_window, text = "Submit", font=("calibri", 14), command= check_pass)
submit_btn.grid(row =3, column= 0)

def clear_all():
    user_entry.delete(0, "end")
    pass_entry.delete(0, "end")
clear_btn = tk.Button(main_window, text = "Clear", font =("calibri", 14), command= clear_all)
clear_btn.grid(row = 3, column= 1)
main_window.mainloop()
