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
transactionLbl.place(relx=0.8, rely= 0.45, anchor= "center")
balanceHistoryLbl = tk.Label(root, text= "Balance History", font = mediumFont)
balanceHistoryLbl.place(relx=0.2, rely=0.45, anchor="center")

# list for transaction and balance
# since its tk.text i disable so user cant change but allows program to add to it and change color
# such as red color if withdrawl or green if deposit
transactionList = tk.Text(root, font=smallFont, state= "disabled", height= 5, width = 40,  border= 0, background= "#F0F0F0")
transactionList.tag_configure("income", foreground="green", justify = tk.CENTER)
transactionList.tag_configure("expense", foreground="red", justify = tk.CENTER)
transactionList.place(relx=0.8, rely=0.6, anchor=tk.CENTER)
balanceList = tk.Text(root, font=smallFont, state= "disabled", height= 5, width= 40, border= 0, background= "#F0F0F0")
balanceList.place(relx=0.2, rely=0.6, anchor=tk.CENTER)
balanceList.tag_configure("basic", justify=tk.CENTER)

incomeEntry = tk.Entry(root, font= smallFont, justify= "center")
expenseEntry = tk.Entry(root, width=10, font= smallFont)
transactionHistory = []
balanceHistory = []
incomeGained = {
    "Salary": 0,
    "Pension": 0,
    "Interest": 0,
    "Others": 0
}

expenseSpent = {
    "Food": 0,
    "Rent": 0,
    "Clothing": 0,
    "Car":0,
    "Health":0, 
    "Others":0
}
incomeTypes = [
    "Salary", 
    "Pension",
    "Interest",
    "Others"
]
expenseTypes = [
    "Food",
    "Rent",
    "Clothing",
    "Car",
    "Health", 
    "Others"
]
def showIncomeBox(): # function for button to add income,  calls the entry box and button to submit
    incomeEntry.place(rely = 0.35, relx = 0.30, anchor= "center", width= 80)
    submitIncomeButton.place(rely = 0.4, relx = 0.30, anchor = "center")
    incomeDropdown.place(rely = 0.35, relx = 0.45, anchor = tk.CENTER)
    #incomeTypeLabel.place(rely = 0.3, relx =0.45, anchor = tk.CENTER)


def errorMessage(): # if an error arises this function is called, ie a string inputted instead of int
    messagebox.showerror('Invalid Input', "Please enter a valid input")


def showExpenseBox(): # function for button to add income,  calls the entry box and button to submit
    expenseEntry.place(rely = 0.35, relx = 0.70, anchor= "center", width= 80)
    submitExpenseButton.place(rely = 0.4, relx = 0.70, anchor = "center")


    expenseDropdown.place(rely = 0.35, relx = 0.85, anchor = tk.CENTER)
    #expenseTypeLabel.place(rely = 0.3, relx =0.85, anchor = tk.CENTER)

def test():
    print(balance)

def addIncome(): # once income is added new balance is calculated
    global balance
    global transactionHistory
    global balanceHistory
    incType = incomeOptionChosen.get() # type for the dictionary ie from salary, pension ...
    if incType not in incomeTypes: # if they didnt pick a type from options possible like the default value
        errorMessage()
    else:
        incomeGained[incType]+= int(incomeEntry.get()) # updates dictionary for that type
        print(incomeGained)

        try:
            balance +=int(incomeEntry.get()) # regular balance update and adding  to history
            transactionHistory.append(incomeEntry.get())
            balanceHistory.append(balance)
        except:
            errorMessage()
    updateBalance("income") # updates visual balance on top and history lists since they dont auto change
    # uses income as entry type so text for transaction is green



def addExpense(): # same as income but expense
    global balance
    global transactionHistory
    global balanceHistory
    expType = expenseOptionChosen.get()
    if expType not in expenseTypes:
        errorMessage()
    else:
        expenseSpent[expType]+= -int(expenseEntry.get())
        try:
            balance += -int(expenseEntry.get())
            transactionHistory.append(expenseEntry.get())
            balanceHistory.append(balance)
        except:
            errorMessage()
    updateBalance("expense")

def updateBalance(transactionType): 
    global balance
    global transactionHistory
    global balanceHistory
    balanceLbl.config(text="Balance:\n "+ str(balanceHistory[-1]), justify = tk.CENTER) # the balance at the top is updated with new value
    textAmmount = str(transactionHistory[-1]) # the last transaction but converted to string
    transactionList.config(state= 'normal')
    balanceList.config(state="normal") # allow the lists to be modified so the latest transactions and balance are added in program
    balanceList.insert(tk.END, balance, "basic")

    if transactionType == "income":
        transactionList.insert(tk.END, "+" + textAmmount, "income")  # income tag so its green
    else:
        transactionList.insert(tk.END, "-" + textAmmount, "expense") # expense tag so its red
    balanceList.insert(tk.END, "\n")
    balanceList.see(tk.END)  
    balanceList.config(state="disabled") # disable after so user cant alter text box

    transactionList.insert(tk.END, "\n")  #  newline for next transaction
    transactionList.see(tk.END)  
    transactionList.config(state="disabled")
        # addInc = tk.Text(fg = "green")
        # addInc.insert(textAmmount)
def submissionRemove(type): # clear entry box and remove buttons after use
    if type == "increase": # clears the income widgets
        submitIncomeButton.place_forget()
        incomeEntry.delete(0,tk.END)
        incomeEntry.place_forget()
        incomeDropdown.place_forget()
        #incomeTypeLabel.place_forget()
    else: # clears the expense widgets 
        submitExpenseButton.place_forget()
        expenseEntry.delete(0,tk.END)
        expenseEntry.place_forget()
        expenseDropdown.place_forget()
        #expenseTypeLabel.place_forget()


        

def categorizeExpense():
    pass

addMoneyBtn = tk.Button(root, text = "Report Income", bg ="#e0dede", font = mediumFont,command = showIncomeBox) # dropdown will show here
addMoneyBtn.place(rely=0.25, relx=0.30, anchor= "center")
submitIncomeButton = tk.Button(root, text="Submit",command=lambda: [addIncome(),submissionRemove("increase")])  

subMoneyBtn = tk.Button(root, text = "Report Expense", bg ="#e0dede",font= mediumFont, command = showExpenseBox)
subMoneyBtn.place(rely=0.25, relx=0.70, anchor= "center")
submitExpenseButton = tk.Button(root, text="Submit",command=lambda: [addExpense(),submissionRemove("expense"),categorizeExpense()])

incomeOptionChosen = tk.StringVar(value = None)
incomeDropdown = tk.OptionMenu(root, incomeOptionChosen, *incomeTypes)
incomeOptionChosen.set("Select Income Type")
#incomeTypeLabel = tk.Label(root, text = "Select Income Type", font = smallFont)

expenseOptionChosen = tk.StringVar(value = "Select Expense Type")
expenseDropdown = tk.OptionMenu(root, expenseOptionChosen, *expenseTypes)

#expenseTypeLabel = tk.Label(root, text ="Select Expense Type", font = smallFont)

root.mainloop()