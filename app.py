# ignoring log in for now balance page and others
import tkinter as tk
from tkinter import messagebox, ttk
import random
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkcalendar import DateEntry
root = tk.Tk()
#accountDetails = [{}]
root.geometry("1280x720")
root.title("Personal Finance Tracker")

notebook = ttk.Notebook(root)
notebook.pack(pady=5, expand= True)
home_page = ttk.Frame(notebook, width= 1280, height = 720)
home_page.pack(expand=True, fill="both")
summary_page = ttk.Frame(notebook, width= 1280, height = 720)
summary_page.pack(expand=True, fill="both")
notebook.add(home_page, text = "Home")
notebook.add(summary_page, text = "Summary")
largeFont = ("Roboto", 28)
mediumFont = ("Roboto", 18)
smallFont = ("Roboto", 12)
balance = 0

# for some reason if input is wrong like being string it now shows error but adds repeats the previous value to list instead cancelling despite the try and except
titleLbl = tk.Label(home_page, text= "Personal Finance Tracker", font= largeFont)
titleLbl.place(relx=0.5, rely = 0.05, anchor = tk.CENTER)
balanceLbl = tk.Label(home_page, text="Balance:\n "+ str(balance) + "$" , font=largeFont)
balanceLbl.place(relx=0.5, rely=0.15, anchor=tk.CENTER)
transactionLbl = tk.Label(home_page, text= "Transaction History", font = mediumFont)
transactionLbl.place(relx=0.7, rely= 0.45, anchor= "center")
balanceHistoryLbl = tk.Label(home_page, text= "Balance History", font = mediumFont)
balanceHistoryLbl.place(relx=0.2, rely=0.45, anchor="center")
transactionIdLbl = tk.Label(home_page, text= "Transaction ID", font = ["Roboto", 14] )
transactionIdLbl.place(relx=0.9, rely= 0.45, anchor= "center")

# list for transaction and balance
# since its tk.text i disable so user cant change but allows program to add to it and change color
# such as red color if withdrawl or green if deposit
transactionTextBox = tk.Text(home_page, font=smallFont, state= "disabled", height= 5, width = 40,  border= 0, background= "#F0F0F0")
transactionTextBox.tag_configure("income", foreground="green", justify = tk.CENTER)
transactionTextBox.tag_configure("expense", foreground="red", justify = tk.CENTER)

transactionTextBox.place(relx=0.7, rely=0.6, anchor=tk.CENTER)
balanceList = tk.Text(home_page, font=smallFont, state= "disabled", height= 5, width= 40, border= 0, background= "#F0F0F0")
balanceList.place(relx=0.2, rely=0.6, anchor=tk.CENTER)
balanceList.tag_configure("basic", justify=tk.CENTER)

transHistoryList = tk.Text(home_page, font = smallFont, state= "disabled",height= 5, width = 10, border= 0 ,background= "#F0F0F0" )
transHistoryList.place(relx=0.9, rely=0.6, anchor=tk.CENTER)
transHistoryList.tag_configure("basic", justify=tk.CENTER)

incomeEntry = tk.Entry(home_page, font= smallFont, justify= "center")
expenseEntry = tk.Entry(home_page, width=10, font= smallFont)


transactionHistory = [] # last index will be used when adding new transactions
transactionDict = {} # will have the transaction and id
balanceHistory = [] # last index will be used in balance history displayed 1 by 1

incomeGained = {}
# blank dicts for income and expenses to only show categories once the user uses them 
expenseSpent = {}

fullTransactionData = [] # list of dictionaries, key is id, shows  all data about a specific transction
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
def updateIncomeGraph():
    
    plt.subplot(1,2,1)
    labels = list(incomeGained.keys())
    sizes = list(incomeGained.values())
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title("Income Pie Chart")

def updateExpenseGraph():

    plt.subplot(1,2,2)
    labels = list(expenseSpent.keys())
    sizes = list(expenseSpent.values())
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title("Expense Pie Chart")
def updateGraph(graphType):
    if graphType == "income":
        updateIncomeGraph()
    elif graphType == "expense":
        updateExpenseGraph()
    canvas.draw()  # redraw so visuals are right


fig = plt.figure()
canvas = FigureCanvasTkAgg(fig, summary_page)
canvas.get_tk_widget().place(relx=0.25, rely=0.25)



def showIncomeBox(): # function for button to add income,  calls the entry box and button to submit
    incomeEntry.place(rely = 0.35, relx = 0.30, anchor= "center", width= 80)
    submitIncomeButton.place(rely = 0.4, relx = 0.30, anchor = "center")
    incomeDropdown.place(rely = 0.35, relx = 0.45, anchor = tk.CENTER)
    #incomeTypeLabel.place(rely = 0.3, relx =0.45, anchor = tk.CENTER)
    incomeDate.place(relx = 0.15, rely = 0.35, anchor = tk.CENTER)
    incomeDateLbl.place(relx = 0.15, rely = 0.315, anchor= tk.CENTER)

def errorMessage(): # if an error arises this function is called, ie a string inputted instead of int
    messagebox.showerror('Invalid Input', "Please enter a valid input")


def showExpenseBox(): # function for button to add income,  calls the entry box and button to submit
    expenseEntry.place(rely = 0.35, relx = 0.70, anchor= "center", width= 80)
    submitExpenseButton.place(rely = 0.4, relx = 0.70, anchor = "center")


    expenseDropdown.place(rely = 0.35, relx = 0.55, anchor = tk.CENTER)
    expenseDate.place(relx = 0.85, rely = 0.35, anchor = tk.CENTER )
    expenseDateLbl.place(relx = 0.85, rely = 0.315, anchor= tk.CENTER)
    #expenseTypeLabel.place(rely = 0.3, relx =0.85, anchor = tk.CENTER)



def addIncome(): # once income is added new balance is calculated
    global balance
    global transactionHistory
    global balanceHistory
    incType = incomeOptionChosen.get() # type for the dictionary ie from salary, pension ...
    if incType not in incomeTypes: # if they didnt pick a type from options possible like the default value
        errorMessage()
    else:
        if incType not in incomeGained:
            incomeGained.update( {incType : int(incomeEntry.get())} ) # adds category if it does not exist yet
        else:
            incomeGained[incType]+= int(incomeEntry.get())  # updates dictionary for that type 
        try:
            balance +=int(incomeEntry.get()) # regular balance update and adding  to history
        
            transactionHistory.append(incomeEntry.get())
            transactionID = random.randint(1000,9999)
            latestTransaction = transactionHistory[-1]
            transactionDict.update({latestTransaction: transactionID})
            balanceHistory.append(balance)
            # print(transactionDict)
            # print(incomeGained)

            incomeSubmittedDate = incomeDate.get()
            tempIncomeDict = {"transaction_id": transactionID, "transaction_type": "income", "transaction_value": incomeEntry.get(),
                              "income_category": incType, "income_date": incomeSubmittedDate}
            fullTransactionData.append(tempIncomeDict)
            
            

        except:
            errorMessage()
    updateBalance("income") # updates visual balance on top and history lists since they dont auto change
    updateGraph("income") # updates the visual graphs
    # uses income as entry type so text for transaction is green



def addExpense(): # same as income but expense
    
    global balance
    global transactionHistory
    global balanceHistory
    expType = expenseOptionChosen.get()
    if expType not in expenseTypes:
        errorMessage()
    else:
        try:
            if expType not in expenseSpent:
                expenseSpent.update( {expType : int(expenseEntry.get())} ) # adds category if it does not exist yet
            else:
                expenseSpent[expType]+= int(expenseEntry.get()) # should it be a negative or positive in expense category dictionary

        
            balance += -int(expenseEntry.get())
            transactionHistory.append(expenseEntry.get())
            balanceHistory.append(balance)
            transactionID = random.randint(1000,9999)
            latestTransaction = transactionHistory[-1]
            transactionDict.update({latestTransaction: transactionID})
            print(transactionDict)
            print(expenseSpent)

            expenseSubmittedDate = expenseDate.get()
            tempExpenseDict = {"transaction_id": transactionID, "transaction_type": "expense", "transaction_value": expenseEntry.get(),
                              "income_category": expType, "income_date": expenseSubmittedDate}
            fullTransactionData.append(tempExpenseDict)

        except:
            errorMessage()
    updateBalance("expense")
    updateGraph("expense")

def updateBalance(transactionType): 
    print(fullTransactionData)
    global balance
    global transactionHistory
    global balanceHistory
    global transactionDict
    balanceLbl.config(text="Balance:\n "+ str(balanceHistory[-1]), justify = tk.CENTER) # the balance at the top is updated with new value
    textAmmount = str(transactionHistory[-1]) # the last transaction but converted to string
    transactionTextBox.config(state= 'normal')
    balanceList.config(state="normal") # allow the lists to be modified so the latest transactions and balance are added in program
    balanceList.insert(tk.END, balance, "basic")

    transHistoryList.config(state="normal")
    transHistoryList.insert(tk.END, transactionDict[transactionHistory[-1]], "basic")

    if transactionType == "income":
        transactionTextBox.insert(tk.END, "+" + textAmmount, "income")  # income tag so its green
    else:
        transactionTextBox.insert(tk.END, "-" + textAmmount, "expense") # expense tag so its red
    balanceList.insert(tk.END, "\n")
    balanceList.see(tk.END)  
    balanceList.config(state="disabled") # disable after so user cant alter text box

    transactionTextBox.insert(tk.END, "\n")  #  newline for next transaction
    transactionTextBox.see(tk.END)  
    transactionTextBox.config(state="disabled")

    transHistoryList.insert(tk.END, "\n")  #  newline for next transaction
    transHistoryList.see(tk.END)  
    transHistoryList.config(state="disabled")

def submissionRemove(type): # clear entry box and remove buttons after use
    if type == "increase": # clears the income widgets
        submitIncomeButton.place_forget()
        incomeEntry.delete(0,tk.END)
        incomeEntry.place_forget()
        incomeOptionChosen.set("Select Expense Type")
        incomeDropdown.place_forget()
        incomeDate.place_forget()
        incomeDateLbl.place_forget()

        #incomeTypeLabel.place_forget()
    else: # clears the expense widgets 
        submitExpenseButton.place_forget()
        expenseEntry.delete(0,tk.END)
        expenseEntry.place_forget()
        expenseOptionChosen.set("Select Expense Type")
        expenseDropdown.place_forget()
        expenseDate.place_forget()
        expenseDateLbl.place_forget()
        #expenseTypeLabel.place_forget()      

# buttons to report income starting actions, and submit button, each with functions
addMoneyBtn = tk.Button(home_page, text = "Report Income", bg ="#e0dede", font = mediumFont,command = showIncomeBox) # dropdown will show here
addMoneyBtn.place(rely=0.25, relx=0.30, anchor= "center")
submitIncomeButton = tk.Button(home_page, text="Submit",command=lambda: [addIncome(),submissionRemove("increase")])  

subMoneyBtn = tk.Button(home_page, text = "Report Expense", bg ="#e0dede",font= mediumFont, command = showExpenseBox)
subMoneyBtn.place(rely=0.25, relx=0.70, anchor= "center")
submitExpenseButton = tk.Button(home_page, text="Submit",command=lambda: [addExpense(),submissionRemove("expense")])

#dropdown menues
incomeOptionChosen = tk.StringVar(value = None)
incomeDropdown = tk.OptionMenu(home_page, incomeOptionChosen, *incomeTypes)
incomeOptionChosen.set("Select Income Type")
#incomeTypeLabel = tk.Label(root, text = "Select Income Type", font = smallFont)

expenseOptionChosen = tk.StringVar(value = "Select Expense Type")
expenseDropdown = tk.OptionMenu(home_page, expenseOptionChosen, *expenseTypes)

incomeDate = DateEntry(home_page)

incomeDateLbl = tk.Label(home_page,text = "Enter Transaction Date", font = smallFont)




expenseDate = DateEntry(home_page)

expenseDateLbl = tk.Label(home_page, text = "Enter Transaction Date", font = smallFont)


#expenseTypeLabel = tk.Label(root, text ="Select Expense Type", font = smallFont)




#2ND PAGE PLT
dashLbl = tk.Label(summary_page, text = "Dashboard", font = largeFont)
dashLbl.place(relx= 0.5, rely = 0.1, anchor= tk.CENTER)
def quitApplication(): # doesnt end runtime by default when closing
    root.quit()
    root.destroy()
root.protocol("WM_DELETE_WINDOW", quitApplication)
root.mainloop()