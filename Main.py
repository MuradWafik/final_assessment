import random
import tkinter as tk
# Python final project at kaplan
print("Welcome to Personal Finance Tracker")
root = tk.Tk()
accountDetails = [{}]
root.geometry("1280x720")
root.title("Personal Finance Tracker")
largeFont =("Roboto", 28)
mediumFont = ("Roboto", 18)
smallFont = ( "Roboto", 12)
root.configure(bg="#18171c") # default window background color
root.option_add("*Label.Background", "#18171c") # background color for all labels
root.option_add("*Font", smallFont) # default font
root.option_add("*foreground", "white")  # text color
root.option_add("*Button.Background", "#36343d") # button background color
root.option_add("*Entry*Background", "#36343d")

greeting = tk.Label(root, text= "Personal Finance Tracker", font = largeFont, pady=5)
greeting.grid(row = 0, column=  3, columnspan= 3, rowspan= 1)
username = tk.Label(root, text= "Username")
username.grid(row = 3, column=  2, padx= (10,0))
password = tk.Label(root, text= "Password")
password.grid(row = 4, column=  2, padx = (10,0))

user_entry = tk.Entry(root)
user_entry.grid(row = 3, column= 3)

pass_entry = tk.Entry(root, show = "*")
pass_entry.grid(row = 4, column= 3)


def checkPass(): # checks if password is correct
    if user_entry.get() == "MuradWafik" and pass_entry.get() == "123456":
        print("Login Successful")
    else:
        print("Invalid Username or Password")

submitButton = tk.Button(root, text = "Submit", command= checkPass)
submitButton.grid(row =5, column= 2)

def clearAll():
    user_entry.delete(0, "end")
    pass_entry.delete(0, "end")
clearButton = tk.Button(root, text = "Clear", command= clearAll)
clearButton.grid(row = 5, column= 3)

def signUpPage():
    pass

signUpButton = tk.Button(root, text = "Dont have an account? Click here to sign up", command = signUpPage, bg = "#18171c")
signUpButton.grid(row = 6, column= 2, columnspan= 3)
signUpButton.configure(borderwidth=0)


root.mainloop()
