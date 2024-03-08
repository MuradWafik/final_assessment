# ignoring log in for now balance page and others
import tkinter as tk
from tkinter import messagebox, ttk 
import random # random transaction id
import matplotlib.pyplot as plt # regular graphs
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg # to show on tkinter
from tkcalendar import DateEntry # for date of transaction
from matplotlib.widgets import RangeSlider  # slider for dates when filtering graphs gonna add
import datetime # helps filter the dates
root = tk.Tk()
#accountDetails = [{}]
root.geometry("1280x720")
root.title("Personal Finance Tracker")
# no notebook, fra es
notebook = ttk.Notebook(root)
notebook.pack(pady=5, expand= True, fill ='both')
greeting_page = ttk.Frame(notebook, width= 1280, height = 720)
greeting_page.pack(expand= True, fill= "both")
home_page = ttk.Frame(notebook, width= 1280, height = 720)
home_page.pack(expand=True, fill="both")
summary_page = ttk.Frame(notebook, width= 1280, height = 720)
summary_page.pack(expand=True, fill="both")
full_history_page = ttk.Frame(notebook, width= 1280, height= 720)
full_history_page.pack(expand=True, fill="both")

# page for recording transactions 
transaction_page = ttk.Frame(root, width = 1280, height= 720)

# transaction_page.pack(expand= True, fill= "both")
notebook.add(greeting_page, text = "Greeting")
notebook.add(home_page, text = "Home")
notebook.add(summary_page, text = "Summary")
notebook.add(full_history_page, text = "Full Transaction History")
notebook.add(transaction_page, text="Report Transactions")

notebook.hide(1)
notebook.hide(2)
notebook.hide(3)
notebook.hide(4)

largestFont = ("Roboto", 36)
largeFont = ("Roboto", 28)
mediumFont = ("Roboto", 18)
smallFont = ("Roboto", 12)
balance = 0
welcomeLbl = tk.Label(greeting_page, text = "Welcome to the\nPersonal Finance Tracker", font = largestFont)
welcomeLbl.place(relx=0.5, rely = 0.1, anchor= tk.CENTER)

def onResize(event): # makes the tabs change size with window
    curWidth = event.width
    curHeight = event.height
    notebook.config(width=curWidth, height=curHeight)

def showHomePage():
    notebook.add(home_page, text = "Home")
    notebook.add(summary_page, text = "Summary")
    notebook.add(full_history_page, text = "Full Transaction History")
    notebook.select(1)


def showName():
    userName = nameEntry.get()
    # enterNameLbl.config(text= "Welcome " + userName)
    # nameEntry.place_forget()
    # submitName.place_forget()

    nameHome = tk.Label(home_page, font = smallFont )
    if len(userName) != 0: # if the entry for user name is empty
        nameHome.config(text = userName + "'s personal finance tracker",)
    else:
        nameHome.config(text = "Your personal finance tracker")
    
    nameHome.place(relx = 0.0125, rely = 0.025, anchor= "w") # anchored west since some names are longer so it always shows the name
enterNameLbl = tk.Label(greeting_page, text = "Enter your name ", font = largeFont)
enterNameLbl.place(relx=0.5, rely = 0.3, anchor= tk.CENTER)

nameEntry = tk.Entry(greeting_page, font = mediumFont)
nameEntry.place(relx = 0.5, rely = 0.45, anchor = tk.CENTER)

submitName = tk.Button(greeting_page, text= "Submit Name", font = smallFont, width = 16, command = lambda: [showHomePage(), showName(), notebook.hide(0)] )
submitName.place(relx=0.65, rely = 0.45, anchor= tk.CENTER)

submitName.place(relx=0.5, rely = 0.55, anchor= tk.CENTER)

# for some reason if input is wrong like being string it now shows error but adds repeats the previous value to list instead cancelling despite the try and except
titleLbl = tk.Label(home_page, text= "Home Page", font= largeFont)
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

incomeEntry = tk.Entry(transaction_page, font= mediumFont, justify= "center")
expenseEntry = tk.Entry(transaction_page, width=10, font= mediumFont)


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
fullDatesList = [] # will contain the dates to be sorted for the range, for slider when filtering charts
coloumnTitles = ["Transaction Id", "Transaction Type", "Transaction Value", "Category", "Date"]
rawData = []

def updateTableShown(rows, columns):
    # remove label since it messes up with placement for some reason
    historyLbl.grid_remove()

    # makes columns take up entire space, also allows the history label to span them all again
    for col in range(columns):
        full_history_page.grid_columnconfigure(col, weight=1)

    # place it again
    historyLbl.grid(row=0, column=0, columnspan=columns, sticky="n")

    # putting table data
    for row1 in range(rows + 1):
        for column1 in range(columns):
            if row1 == 0: # gives the titles for the columns
                text = coloumnTitles[column1]
            else:
                # adds to it to move the the different entries, idk why this is the exact formula
                text = str(rawData[(row1 - 1) * columns + column1]) 

            # add the text
            tablePosition = tk.Entry(full_history_page)
            tablePosition.config(state="normal")
            tablePosition.insert(tk.END, text)
            tablePosition.grid(row=row1 + 1, column=column1, sticky="nsew")  # sticky for covering entire page

            # disabled so user cant edit
            tablePosition.config(state="disabled", disabledforeground="#000000")




def updateGraph(hideGraphs = True): # updates both no matter what so they both always show
    fig = plt.figure() # has to remake from scratch so they dont just draw them over eachother 
    canvas = FigureCanvasTkAgg(fig, summary_page)

    canvas.get_tk_widget().place(relx=0.5, rely=0.5, anchor= tk.CENTER)
    plt.subplot(1,2,1)
    labels = list(incomeGained.keys())
    sizes = list(incomeGained.values())
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title("Income Pie Chart")
    plt.subplot(1,2,2)
    labels = list(expenseSpent.keys())
    sizes = list(expenseSpent.values())
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title("Expense Pie Chart")
    if hideGraphs == False:
        fig.set_visible(False)
    else:
        fig.set_visible(True)

# sliderLeftValue = tk.DoubleVar(value= 0)
# sliderRightValue = tk.DoubleVar(value = 1)
# dateSlider = RangeSliderH( summary_page , [sliderLeftValue, sliderRightValue], padX= 11)
# dateSlider.place(relx = 0.7, rely = 0.6, anchor= tk.CENTER)

    slider_ax = fig.add_axes([0.20, 0.1, 0.60, 0.03])
    slider = RangeSlider(slider_ax, "Date Range", 0, 1234)
    canvas.draw()  # redraw so visuals are right




def showIncomeBox(): # function for button to add income,  calls the entry box and button to submit
    noTransactionTypeBtn.place_forget() # hides the default message saying there is no transaction type
    transactionTypeReportingLbl.config(text= "Reporting Income")
    transactionTypeReportingLbl.place(rely = 0.2, relx = 0.5, anchor= tk.CENTER)
    incomeEntry.place(rely = 0.35, relx = 0.50, anchor= "center", width= 100)
    submitIncomeButton.place(rely = 0.425, relx = 0.50, anchor = "center")
    incomeDropdown.place(rely = 0.35, relx = 0.70, anchor = tk.CENTER)
    incomeDate.place(relx = 0.35, rely = 0.35, anchor = tk.CENTER)
    incomeDateLbl.place(relx = 0.35, rely = 0.315, anchor= tk.CENTER)

def errorMessage(): # if an error arises this function is called, ie a string inputted instead of int
    messagebox.showerror('Invalid Input', "Please enter a valid input")


def showExpenseBox(): # function for button to add income,  calls the entry box and button to submit
    noTransactionTypeBtn.place_forget()
    transactionTypeReportingLbl.config(text= "Reporting Expense")
    transactionTypeReportingLbl.place(rely = 0.2, relx = 0.5, anchor= tk.CENTER)
    expenseEntry.place(rely = 0.35, relx = 0.50, anchor= "center", width= 100)
    submitExpenseButton.place(rely = 0.425, relx = 0.50, anchor = "center")
    expenseDropdown.place(rely = 0.35, relx = 0.70, anchor = tk.CENTER)
    expenseDate.place(relx = 0.35, rely = 0.35, anchor = tk.CENTER )
    expenseDateLbl.place(relx = 0.35, rely = 0.315, anchor= tk.CENTER)




def addIncome(): # once income is added new balance is calculated
    global balance
    global transactionHistory
    global balanceHistory
    incType = incomeOptionChosen.get() # type for the dictionary ie from salary, pension ...
    if incType not in incomeTypes or incomeEntry.get().isnumeric() == False: 
        # if they didnt pick a type from options possible like the default value, or didnt put a number
        errorMessage()
    else:
        if incType not in incomeGained:
            incomeGained.update( {incType : int(incomeEntry.get())} ) # adds category if it does not exist yet
        else:
            incomeGained[incType]+= int(incomeEntry.get())  # updates dictionary for that type 

        balance +=int(incomeEntry.get()) # regular balance update and adding  to history
    
        transactionHistory.append(incomeEntry.get())
        transactionID = random.randint(1000,9999)
        latestTransaction = transactionHistory[-1]
        transactionDict.update({latestTransaction: transactionID})
        balanceHistory.append(balance)
        # print(transactionDict)
        # print(incomeGained)
        incomeSubmittedDate = incomeDate.get()
        tempIncomeDict = {"transaction_id": transactionID, "transaction_type": "income", "transaction_value": incomeEntry.get(), # adds info to dict
                          "category": incType, "date": incomeSubmittedDate}
        dataValues =[transactionID, "income", incomeEntry.get(), incType, incomeSubmittedDate]
        rawData.extend(dataValues) # append for multiple values
        fullTransactionData.append(tempIncomeDict)
        fullDatesList.append(incomeSubmittedDate)

        noTransactionTypeBtn.place(relx = 0.5, rely = 0.3, anchor= tk.CENTER)
        notebook.select(1)
        notebook.hide(4)
        updateTableShown(columns= 5, rows = len(fullTransactionData))
        updateBalance("income") # updates visual balance on top and history lists since they dont auto change
        updateGraph() # updates the visual graphs

        


    noTransactionTypeBtn.place(relx = 0.5, rely = 0.3, anchor= tk.CENTER)

    # uses income as entry type so text for transaction is green



def addExpense(): # same as income but expense
    global balance
    global transactionHistory
    global balanceHistory
    expType = expenseOptionChosen.get()
    if expType not in expenseTypes or expenseEntry.get().isnumeric() == False:
        errorMessage()
    else:
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
                            "category": expType, "date": expenseSubmittedDate}
        fullTransactionData.append(tempExpenseDict)
        fullDatesList.append(expenseSubmittedDate)
        expenseValues = [transactionID, "expense", expenseEntry.get(), expType, expenseSubmittedDate]

        rawData.extend(expenseValues)
            
        noTransactionTypeBtn.place(relx = 0.5, rely = 0.3, anchor= tk.CENTER)
        notebook.select(1)
        notebook.hide(4)
        updateTableShown(columns= 5, rows = len(fullTransactionData))
        updateBalance("expense")
        updateGraph()

def updateBalance(transactionType): 
    print(fullTransactionData)
    global balance
    global transactionHistory
    global balanceHistory
    global transactionDict
    balanceLbl.config(text="Balance:\n "+ str(balanceHistory[-1])+"$", justify = tk.CENTER) # the balance at the top is updated with new value
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

def showTransactionPageType(event):
    notebook.add(transaction_page, text="Report Transactions")
    notebook.select(4)
    if transactionChosen.get() == "Income":
        showIncomeBox()
    elif transactionChosen.get() == "Expense":
        showExpenseBox()
    
    transactionChosen.set("Select Transaction Type")

reportTransactionLbl = tk.Label(home_page, text= "Report Transaction:", font = largeFont)
reportTransactionLbl.place(relx = 0.5, rely = 0.3, anchor= tk.CENTER)
        
transactionChosen = tk.StringVar(value = "Select Transaction Type")
transactionTypes = ["Income", "Expense"]
transactionDropdown = tk.OptionMenu(home_page, transactionChosen, *transactionTypes, command=showTransactionPageType)
transactionDropdown.config(font = mediumFont)
transactionDropdown.place(relx = 0.5, rely = 0.375, anchor= tk.CENTER)


transactionPageTitle = tk.Label(transaction_page, text = "Transaction Page", font = largestFont)
transactionPageTitle.place(relx= 0.5, rely = 0.05, anchor= tk.CENTER)

# if on report income it just titles the page such and same for expense
transactionTypeReportingLbl = tk.Label(transaction_page, font = largeFont)


noTransactionTypeBtn = tk.Button(transaction_page, text = "It seems like you don't have a transaction type chosen\n Click here to go to home page",
                                 font = largeFont, borderwidth=0, command= lambda: notebook.select(1))
noTransactionTypeBtn.place(relx = 0.5, rely = 0.3, anchor= tk.CENTER)


submitIncomeButton = tk.Button(transaction_page, font = mediumFont, text="Submit",command=lambda: [addIncome(),submissionRemove("increase")])  
submitExpenseButton = tk.Button(transaction_page,font = mediumFont, text="Submit",command=lambda: [addExpense(), submissionRemove("expense")])


#dropdown menues
incomeOptionChosen = tk.StringVar(value = "Select Income Type")
incomeDropdown = tk.OptionMenu(transaction_page, incomeOptionChosen, *incomeTypes) # like *args, taking in all income types for dropdown
incomeDropdown.config(font = mediumFont)


expenseOptionChosen = tk.StringVar(value = "Select Expense Type")
expenseDropdown = tk.OptionMenu(transaction_page, expenseOptionChosen, *expenseTypes)
expenseDropdown.config(font = mediumFont)

incomeDate = DateEntry(transaction_page)
incomeDateLbl = tk.Label(transaction_page,text = "Enter Transaction Date", font = smallFont)

expenseDate = DateEntry(transaction_page)
expenseDateLbl = tk.Label(transaction_page, text = "Enter Transaction Date", font = smallFont)










#2ND PAGE PLT
dashLbl = tk.Label(summary_page, text = "Dashboard", font = largeFont)
dashLbl.place(relx= 0.5, rely = 0.05, anchor= tk.CENTER)
# dashLbl.grid(row = 1, column= 1, columnspan= 10, rowspan= 3, sticky = "ew")
# dashLbl.grid_rowconfigure(1, weight=1)
# dashLbl.grid_columnconfigure(1, weight=1)

historyLbl = tk.Label(full_history_page, text = "Full Transaction History", font = largeFont)
# historyLbl.place(relx = 0.5, rely = 0.05, anchor= tk.CENTER)
historyLbl.grid(row=0, column=0, columnspan=3, sticky="n")

# Configure the columns in the grid to expand
full_history_page.grid_columnconfigure(0, weight=1)  # Allow the first column to expand
full_history_page.grid_columnconfigure(1, weight=1)  # Allow the second column to expand
full_history_page.grid_columnconfigure(2, weight=1)  # Allow the third column to expand
def quitApplication(): # doesnt end runtime by default when closing
    root.quit()
    root.destroy()
root.protocol("WM_DELETE_WINDOW", quitApplication)

# transaction page, changing it from all on the home


root.bind("<Configure>", onResize)  # lets the frames (tabs for diff pages) resize with the window
root.mainloop()