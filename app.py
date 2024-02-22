# ignoring log in for now balance page and others
import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
#accountDetails = [{}]
root.geometry("1280x720")
root.title("Personal Finance Tracker")
largeFont = ("Roboto", 28)
mediumFont = ("Roboto", 18)
smallFont = ("Roboto", 12)
balance = 0
#add button to show COMPLETE transaction and balance history when clicked later
titleLbl = tk.Label(root, text= "Personal Finance Tracker", font= largeFont)
titleLbl.place(relx=0.5, rely = 0.05, anchor = tk.CENTER)
balanceLbl = tk.Label(root, text="Balance:\n "+ str(balance) + "$" , font=largeFont)
balanceLbl.place(relx=0.5, rely=0.15, anchor=tk.CENTER)
transactionLbl = tk.Label(root, text= "Transaction History", font = mediumFont)
transactionLbl.place(relx=0.6, rely= 0.45, anchor= "center")
balanceHistoryLbl = tk.Label(root, text= "Balance History", font = mediumFont)
balanceHistoryLbl.place(relx=0.4, rely=0.45, anchor="center")


transactionList = tk.Text(root, font=smallFont, state= "disabled", height= 5, width=4, background= "#F0F0F0", border= 0)
transactionList.tag_configure("income", foreground="green", justify = tk.CENTER)
transactionList.tag_configure("expense", foreground="red", justify = tk.CENTER)
transactionList.place(relx=0.6, rely=0.6, anchor=tk.CENTER)
balanceList = tk.Text(root, font=smallFont, state= "disabled", height= 5, width=4, background= "#F0F0F0", border= 0)
balanceList.place(relx=0.4, rely=0.6, anchor=tk.CENTER)



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
transactionHistory = []
balanceHistory = []
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
    global transactionHistory
    global balanceHistory
    incomeEntry.pack_forget()
    submitIncomeButton.pack_forget()
    try:
        balance +=int(incomeEntry.get())
        transactionHistory.append(incomeEntry.get())
        balanceHistory.append(balance)
    except:
        errorMessage()

    updateBalance("income")



def addExpense():
    global balance
    global transactionHistory
    global balanceHistory
    try:
        balance -= int(expenseEntry.get())
        transactionHistory.append(expenseEntry.get())
        balanceHistory.append(balance)
    except:
        errorMessage
    updateBalance("expense")

def updateBalance(transactionType): 
    global balance
    global transactionHistory
    global balanceHistory
    balanceLbl.config(text="Balance:\n "+ str(balanceHistory[-1]))
    textAmmount = str(transactionHistory[-1])
    transactionList.config(state= 'normal')
    balanceList.config(state="normal")
    balanceList.insert(tk.END, balance)
    if transactionType == "income":
        transactionList.insert(tk.END, "+" + textAmmount, "income")  
    else:
        transactionList.insert(tk.END, "-" + textAmmount, "expense") 
    balanceList.insert(tk.END, "\n")
    balanceList.see(tk.END)  
    balanceList.config(state="disabled")

    transactionList.insert(tk.END, "\n")  # Add newline for next transaction
    transactionList.see(tk.END)  
    transactionList.config(state="disabled")
        # addInc = tk.Text(fg = "green")
        # addInc.insert(textAmmount)
addMoneyBtn = tk.Button(root, text = "Report Income", command = showIncomeBox)
addMoneyBtn.place(rely=0.25, relx=0.40, anchor= "center")
submitIncomeButton = tk.Button(root, text="Submit",command=addIncome)  

subMoneyBtn = tk.Button(root, text = "Report Expense", command = showExpenseBox)
subMoneyBtn.place(rely=0.25, relx=0.60, anchor= "center")
submitExpenseButton = tk.Button(root, text="Submit",command=addExpense)  

root.mainloop()