import tkinter as tk


print("Welcome to Personal Finance Tracker")
root = tk.Tk()
accountDetails = [{}]
root.geometry("1280x720")
root.title("Personal Finance Tracker")
largeFont = ("Roboto", 28)
mediumFont = ("Roboto", 18)
smallFont = ("Roboto", 12)


# Login page
logInPage = tk.Frame(root)

greeting = tk.Label(logInPage, text="Personal Finance Tracker", font=largeFont, pady=5)
greeting.grid(row=0, column=3, columnspan=3, rowspan=1)
username = tk.Label(logInPage, text="Username")
username.grid(row=3, column=2, padx=(10, 0))
password = tk.Label(logInPage, text="Password")
password.grid(row=4, column=2, padx=(10, 0))

user_entry = tk.Entry(logInPage)
user_entry.grid(row=3, column=3)

pass_entry = tk.Entry(logInPage, show="*")
pass_entry.grid(row=4, column=3)


def show_page(page_to_show, page_to_hide):
    page_to_hide.pack_forget()  # Hide the current page
    page_to_show.pack()  #which page to show 
def check_pass():
    if user_entry.get() == "MuradWafik" and pass_entry.get() == "123456":
        print("Login Successful")
    else:
        print("Invalid Username or Password")





submitButton = tk.Button(logInPage, text="Submit",command=check_pass)  # Let's move the command to the button
submitButton.grid(row=5, column=2)


def clear_all():
    user_entry.delete(0, "end")
    pass_entry.delete(0, "end")

clearButton = tk.Button(logInPage, text="Clear", command=clear_all)
clearButton.grid(row=5, column=3)

signUpButton = tk.Button(logInPage, text="Don't have an account? Click here to sign up", command=lambda: show_page(signUpPage, logInPage), fg="#18171c")
signUpButton.grid(row=6, column=2, columnspan=3)
signUpButton.configure(borderwidth=0)

# Sign-up page
signUpPage = tk.Frame(root)



# Pack both frames
logInPage.pack()
signUpPage.pack()

# Initially show the login page
logInPage.tkraise()



root.mainloop()




# expensePieChart = plt.subplot(0,1,1)
    #     expText = list(expenseSpent.items())
    #     expFinal = []
    #     for expense in expText:
    #         end = str(expense)
    #         end = end.replace("(", "")
    #         end = end.replace(")", "") # its saved as a tuple such as ("name", amount) so we need to remove these
    #         end = end.replace("'","")
    #         end += "$"

    #         expFinal.append(end)
    #     expLabels = expFinal
    #     sizes = list(expenseSpent.values())
    #     expensePieChart.clear()  # Clear the previous plot
    #     expensePieChart.pie(sizes, labels=expLabels, autopct='%1.1f%%', startangle=90)
    #     expensePieChart.axis('equal')
    #     expensePieChart.set_title("Expense pie chart")
    #     expensePieChart.set_position([0, 0.6, 0.4, 0.4])
    # if graphType =="income":
    #     incomePieChart = fig.add_subplot(1,2,2)
    #     incText = list(incomeGained.items())
    #     incFinal = []
    #     for income in incText:
    #         end1 = str(income)
    #         end1 = end1.replace("(", "")
    #         end1 = end1.replace(")", "") # its saved as a tuple such as ("name", amount) so we need to remove these
    #         end1 = end1.replace("'","")
    #         end1 += "$"
    
    #         incFinal.append(end)
    #     incLabels = incFinal
    #     sizes = list(incomeGained.values())
    #     incomePieChart.clear()  # Clear the previous plot
    #     incomePieChart.pie(sizes, labels=incLabels, autopct='%1.1f%%', startangle=90)
    #     incomePieChart.axis('equal')
    #     incomePieChart.set_title("Income pie chart")
    #     incomePieChart.set_position([0.6, 0.6, 0.4, 0.4])


# extra stuff in case to draw pie charts