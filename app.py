# ignoring log in for now balance page and others
import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
accountDetails = [{}]
root.geometry("1280x720")
root.title("Personal Finance Tracker")
largeFont = ("Roboto", 28)
mediumFont = ("Roboto", 18)
smallFont = ("Roboto", 12)
balance = 0

titleLbl = tk.Label(root, text= "Personal Finance Tracker", font= largeFont)
titleLbl.place(relx=0.5, rely = 0.05, anchor = tk.CENTER)
balanceLbl = tk.Label(root, text="Balance:\n "+ str(balance) + "$" , font=largeFont)
balanceLbl.place(relx=0.5, rely=0.15, anchor=tk.CENTER)


# def transactionHistory(bal, operation, balanceHistory = None,  tranHistory = None): # list to store transaction history that will be displayed

#     if tranHistory == None:
#         tranHistory == [operation]
#     else:
#         tranHistory.append(operation)
    
# def balanceHistory(bal, balHistory = None): # list to store balance history to be displayed
#     if balHistory == None:
#         balHistory = [bal]
#     else:
#         balHistory.appened(bal)
    
    

incomeEntry = tk.Entry(root, font= smallFont, justify= "center")
expenseEntry = tk.Entry(root, width=10, font= smallFont)

def showIncomeBox():
    incomeEntry.place(rely = 0.3, relx = 0.40, anchor= "center", width= 80)
    submitIncomeButton.place(rely = 0.375, relx = 0.40, anchor = "center")
def errorMessage():
    messagebox.showerror('Invalid Input', "Please enter a valid input")


def showExpenseBox():
    expenseEntry.place(rely = 0.3, relx = 0.60, anchor= "center", width= 80)
    submitExpenseButton.place(rely = 0.375, relx = 0.60, anchor = "center")

def test():
    print(balance)
def addIncome():
    global balance
    incomeEntry.pack_forget()
    submitIncomeButton.pack_forget()
    try:
        balance +=int(incomeEntry.get())
    except:
        errorMessage()

    updateBalance()



def addExpense():
    global balance
    try:
        balance -= int(expenseEntry.get())
    except:
        errorMessage
    updateBalance()

def updateBalance():
    global balanceLbl
    global balance
    balanceLbl["text"] ="Balance:\n "+ str(balance) + "$" 

addMoneyBtn = tk.Button(root, text = "Report Income", command = showIncomeBox)
addMoneyBtn.place(rely=0.25, relx=0.40, anchor= "center")
submitIncomeButton = tk.Button(root, text="Submit",command=addIncome)  

subMoneyBtn = tk.Button(root, text = "Report Expense", command = showExpenseBox)
subMoneyBtn.place(rely=0.25, relx=0.60, anchor= "center")
submitExpenseButton = tk.Button(root, text="Submit",command=addExpense)  

root.mainloop()