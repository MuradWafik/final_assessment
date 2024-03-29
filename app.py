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

root.geometry("1280x720")
root.title("Personal Finance Tracker")

notebook = ttk.Notebook(root)
notebook.pack(pady=5, expand= True, fill ='both')
greeting_page = ttk.Frame(notebook, width= 1280, height = 720)
greeting_page.pack(expand= True, fill= "both")
home_page = ttk.Frame(notebook, width= 1280, height = 720)
home_page.pack(expand=True, fill="both")
pie_chart_page = ttk.Frame(notebook, width= 1280, height = 720)
pie_chart_page.pack(expand=True, fill="both")

bar_graph_page = ttk.Frame(notebook, width = 1280, height= 720)
bar_graph_page.pack(expand= True, fill = "both")

full_history_page = ttk.Frame(notebook, width= 1280, height= 720)
full_history_page.pack(expand=True, fill="both")

delete_transaction_page = ttk.Frame(notebook, width= 1280, height = 720)

# page for recording transactions 
transaction_page = ttk.Frame(root, width = 1280, height= 720)

# transaction_page.pack(expand= True, fill= "both")
notebook.add(greeting_page, text = "Greeting")
notebook.add(home_page, text = "Home")
notebook.add(pie_chart_page, text = "Pie Chart")
notebook.add(bar_graph_page, text= "Bar Chart")
notebook.add(full_history_page, text = "Full Transaction History")
notebook.add(transaction_page, text="Report Transactions")
notebook.add(delete_transaction_page, text = "Delete Transaction")

notebook.hide(1)
notebook.hide(2)
notebook.hide(3)
notebook.hide(4)
notebook.hide(5)
notebook.hide(6)

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

def showHomePage(): # after they enter name, leave that page and show the rest
    notebook.add(home_page, text = "Home")
    notebook.add(pie_chart_page, text = "Pie Chart")
    notebook.add(bar_graph_page, text = "Bar Chart")

    notebook.add(full_history_page, text = "Full Transaction History")
    notebook.select(1)


def showName():
    userName = nameEntry.get()
    nameHome = tk.Label(home_page, font = smallFont )
    if len(userName) != 0: # if the entry for user name is empty
        nameHome.config(text = userName + "'s personal finance tracker",)
    else:
        nameHome.config(text = "Your personal finance tracker") # no name, just say this
    
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
transactionLbl.place(relx=0.75, rely= 0.45, anchor= "center")
payeeAndSourceLbl = tk.Label(home_page, text= "Payee / Source", font = mediumFont)
payeeAndSourceLbl.place(relx=0.2, rely=0.45, anchor="center")
transactionIdLbl = tk.Label(home_page, text= "Transaction ID", font = ["Roboto", 14] )
transactionIdLbl.place(relx=0.9, rely= 0.45, anchor= "center")



# list for transaction and balance
# since its tk.text i disable so user cant change but allows program to add to it and change color
# such as red color if withdrawl or green if deposit
transactionTextBox = tk.Text(home_page, font=smallFont, state= "disabled", height= 5, width = 40,  border= 0, background= "#F0F0F0")


transactionTextBox.place(relx=0.75, rely=0.6, anchor=tk.CENTER)
payeeAndSourceList = tk.Text(home_page, font=smallFont, state= "disabled", height= 5, width= 40, border= 0, background= "#F0F0F0")
payeeAndSourceList.place(relx=0.2, rely=0.6, anchor=tk.CENTER)


transHistoryList = tk.Text(home_page, font = smallFont, state= "disabled",height= 5, width = 10, border= 0 ,background= "#F0F0F0" )
transHistoryList.place(relx=0.9, rely=0.6, anchor=tk.CENTER)


incomeEntry = tk.Entry(transaction_page, font= mediumFont, justify= "center")
expenseEntry = tk.Entry(transaction_page, width=10, font= mediumFont)


incomeGained = {}
# blank dicts for income and expenses to only show categories once the user uses them in chart
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

tablePageLbl = tk.Label(full_history_page, font = ("Roboto", 16), height= 2, width= 84, borderwidth= 0, background= "#F0F0F0")
tablePageLbl.place(relx= 0.5, rely = 0.1, anchor= tk.CENTER)
# just putting the specific spaces so it shows right, no reason for their own text boxes since it wont change
tablePageLbl.config(text=  "Transaction Id   Transaction Type   Transaction Value        Category            Date               Source/Payee")
tranIDText = tk.Text(full_history_page, font = mediumFont, height = 20, width= 14)
tranTypeText = tk.Text(full_history_page, font = mediumFont, height = 20, width= 14)
tranValueText = tk.Text(full_history_page, font = mediumFont, height = 20, width= 14)
categoryText = tk.Text(full_history_page, font = mediumFont, height = 20, width= 14)
dateText = tk.Text(full_history_page, font = mediumFont, height = 20, width= 14)
sourcePayeeText = tk.Text(full_history_page, font = mediumFont, height = 20, width= 14)

tranIDText.place(relx= 0.175, rely = 0.55, anchor= tk.CENTER)
tranTypeText.place(relx = 0.3, rely = 0.55, anchor= tk.CENTER)
tranValueText.place(relx = 0.425, rely = 0.55, anchor= tk.CENTER)
categoryText.place(relx = 0.575, rely = 0.55, anchor = tk.CENTER)
dateText.place(relx= 0.7, rely = 0.55, anchor = tk.CENTER)
sourcePayeeText.place(relx= 0.825, rely = 0.55, anchor= tk.CENTER)


transactionTextBox.tag_configure("income", foreground="green", justify = tk.CENTER)
transactionTextBox.tag_configure("expense", foreground="red", justify = tk.CENTER)
payeeAndSourceList.tag_configure("basic", justify=tk.CENTER) # basic is just a default tag i made to center the text
transHistoryList.tag_configure("basic", justify=tk.CENTER)
tranIDText.tag_configure("basic", justify=tk.CENTER)
tranTypeText.tag_configure("basic", justify=tk.CENTER)
tranValueText.tag_configure("basic", justify=tk.CENTER)
categoryText.tag_configure("basic", justify=tk.CENTER)
dateText.tag_configure("basic", justify=tk.CENTER)
sourcePayeeText.tag_configure("basic", justify=tk.CENTER)


# storing all tk.Texts in list since same actions always apply on them so i can just loop
tableTextBoxes = [tranIDText, tranTypeText, tranValueText, categoryText, dateText, sourcePayeeText,payeeAndSourceList, transHistoryList, transactionTextBox]
def disableTables(): # makes the textboxes for full tables not editable by user
    for widget in tableTextBoxes:
        widget.config(state= tk.DISABLED)
disableTables() # calls one it first time so user cant edit right away


def clearTables(): # if u just insert the text will always duplicate, must clear then add
    # also just make them available to edit
    for widget in tableTextBoxes:
        widget.config(state= tk.NORMAL)
        widget.delete(1.0, tk.END)

def updateBarGraph():
    figure2 = plt.figure()
    canvas2 = FigureCanvasTkAgg(figure2, bar_graph_page )

    canvas2.get_tk_widget().place(relx= 0.5, rely = 0.5, anchor= tk.CENTER) # place the canvas as a tkinter widget

    plt.subplot(1,2,1) # where the graph will be placed on it

    barIncLabels = list(incomeGained.keys())
    # barIncLabels = []
    barIncSizes = list(incomeGained.values())
    plt.bar(barIncLabels, barIncSizes)
    plt.title("Income Bar Graph")

    plt.subplot(1,2,2)
    barExpLabels = list(expenseSpent.keys())
    barExpSizes = list(expenseSpent.values())
    plt.bar(barExpLabels, barExpSizes)

def updatePieChart(): # updates both no matter what so they both always show
    fig = plt.figure() # has to remake from scratch so they dont just draw them over eachother 
    canvas = FigureCanvasTkAgg(fig, pie_chart_page)

    canvas.get_tk_widget().place(relx=0.5, rely=0.5, anchor= tk.CENTER)
    plt.subplot(1,2,1)
    pieIncLabels = list(incomeGained.keys())
    pieIncLizes = list(incomeGained.values())
    plt.pie(pieIncLizes, labels=pieIncLabels, autopct='%1.1f%%', startangle=90)
    plt.title("Income Pie Chart")
    plt.subplot(1,2,2)
    pieExpLabels = list(expenseSpent.keys())
    pieExpSizes = list(expenseSpent.values())
    plt.pie(pieExpSizes, labels=pieExpLabels, autopct='%1.1f%%', startangle=90)
    plt.title("Expense Pie Chart")

    # date list should type should be converted then can be sorted by python built in
    convertedDateList = [] 
    for transactionDate in fullDatesList:
        convertedDateList.append(datetime.datetime.strptime(transactionDate,"%m/%d/%y"))
    sorted_dates = sorted(convertedDateList)

    # minimum and max dates from first and last index of sorted list
    min_date = sorted_dates[0]
    max_date = sorted_dates[-1]

    # place and add the slider
    slider_ax = fig.add_axes([0.20, 0.1, 0.60, 0.03])
    slider = RangeSlider(slider_ax, "Date Range", 0, len(sorted_dates) - 1, valinit=(0, len(sorted_dates) - 1))

    # not sure exactly but adds labels
    slider_labels = [str(date) for date in sorted_dates]
    slider.set_val((0, len(sorted_dates) - 1))
    slider.valtext.set_text(f'{min_date} - {max_date}')




def showIncomeBox(): # function for button to add income,  calls the entry box and button to submit
    noTransactionTypeBtn.place_forget() # hides the default message saying there is no transaction type
    transactionTypeReportingLbl.config(text= "Reporting Income")
    transactionTypeReportingLbl.place(rely = 0.2, relx = 0.5, anchor= tk.CENTER)
    incomeEntry.place(rely = 0.35, relx = 0.50, anchor= "center", width= 100)
    submitIncomeButton.place(rely = 0.625, relx = 0.50, anchor = "center")
    incomeDropdown.place(rely = 0.35, relx = 0.70, anchor = tk.CENTER)
    incomeDate.place(relx = 0.35, rely = 0.35, anchor = tk.CENTER)
    incomeDateLbl.place(relx = 0.35, rely = 0.315, anchor= tk.CENTER)
    incomeSourceEntry.place(relx = 0.5, rely = 0.55, anchor = tk.CENTER)
    incomeSourceLbl.place(relx = 0.5, rely = 0.5, anchor= tk.CENTER)

def errorMessage(): # if an error arises this function is called, ie a string inputted instead of int
    messagebox.showerror('Invalid Input', "Please enter a valid input")

def showExpenseBox(): # function for button to add income,  calls the entry box and button to submit
    noTransactionTypeBtn.place_forget()
    transactionTypeReportingLbl.config(text= "Reporting Expense")
    transactionTypeReportingLbl.place(rely = 0.2, relx = 0.5, anchor= tk.CENTER)
    expenseEntry.place(rely = 0.35, relx = 0.50, anchor= "center", width= 100)
    submitExpenseButton.place(rely = 0.625, relx = 0.50, anchor = "center")
    expenseDropdown.place(rely = 0.35, relx = 0.70, anchor = tk.CENTER)
    expenseDate.place(relx = 0.35, rely = 0.35, anchor = tk.CENTER )
    expenseDateLbl.place(relx = 0.35, rely = 0.315, anchor= tk.CENTER)
    expensePayeeEntry.place(relx = 0.5, rely = 0.55, anchor= tk.CENTER)
    expensePayeeLbl.place(relx= 0.5, rely = 0.5, anchor = tk.CENTER)

usedIDS = set() # how to ensure ids are unique
def generateRandomID():
    global usedIDS
    idToAdd = random.randint(1000,9999)
    if idToAdd not in usedIDS:
        usedIDS.add(idToAdd)
        return idToAdd
    return generateRandomID()

def addIncome(): # once income is added new balance is calculated
    global balance

    incType = incomeOptionChosen.get() # type for the dictionary ie from salary, pension ...
    source = incomeSourceEntry.get()
    if incType not in incomeTypes or incomeEntry.get().isnumeric() == False or not source: 
        # if they didnt pick a type from options possible like the default value, or didnt put a number, or didnt put a source
        errorMessage()
    else:
        if incType not in incomeGained:
            incomeGained.update( {incType : int(incomeEntry.get())} ) # adds category if it does not exist yet
        else:
            incomeGained[incType]+= int(incomeEntry.get())  # updates dictionary for that type 

        balance +=int(incomeEntry.get()) # regular balance update and adding  to history
        transactionID = generateRandomID() # gets a random id for the transaction id

        incomeSubmittedDate = incomeDate.get()
        tempIncomeDict = {"transaction_id": transactionID, "transaction_type": "income", "transaction_value": incomeEntry.get(), # adds info to dict
                          "category": incType, "date": incomeSubmittedDate, "payee/source": source}

        fullTransactionData.append(tempIncomeDict)
        fullDatesList.append(incomeSubmittedDate)

        noTransactionTypeBtn.place(relx = 0.5, rely = 0.3, anchor= tk.CENTER)
        notebook.select(1)
        notebook.hide(5)
        updateBalance() # updates visual balance on top and history lists since they dont auto change

def addExpense(): # same as income but expense
    global balance
    expType = expenseOptionChosen.get()
    payee = expensePayeeEntry.get()
    if expType not in expenseTypes or expenseEntry.get().isnumeric() == False or not payee:
        errorMessage()
    else:
        if expType not in expenseSpent:
            expenseSpent.update( {expType : int(expenseEntry.get())} ) # adds category if it does not exist yet
        else:
            expenseSpent[expType]+= int(expenseEntry.get()) # should it be a negative or positive in expense category dictionary

        balance += -int(expenseEntry.get())
        transactionID = random.randint(1000,9999)

        expenseSubmittedDate = expenseDate.get()
        tempExpenseDict = {"transaction_id": transactionID, "transaction_type": "expense", "transaction_value": expenseEntry.get(),
                            "category": expType, "date": expenseSubmittedDate, "payee/source": payee}
        fullTransactionData.append(tempExpenseDict)
        fullDatesList.append(expenseSubmittedDate)

        noTransactionTypeBtn.place(relx = 0.5, rely = 0.3, anchor= tk.CENTER)
        notebook.select(1)
        notebook.hide(5)
        updateBalance()
 
def updateBalance(): 
    updateBarGraph()
    updatePieChart() # updates graphs with it

    print(fullTransactionData)
    global balance
    balanceLbl.config(text="Balance:\n "+ str(balance)+"$", justify = tk.CENTER) # the balance at the top is updated with new value
 
    clearTables() # makes all text boxes blank so they can be added to again
    for dictionary in fullTransactionData: 
        # adds the values for each index at the full history table
        tranIDText.insert(tk.END, str(dictionary["transaction_id"])+ "\n", "basic")
        tranTypeText.insert(tk.END, dictionary["transaction_type"]+ "\n","basic")
        tranValueText.insert(tk.END, str(dictionary["transaction_value"])+ "\n","basic")
        categoryText.insert(tk.END, dictionary["category"] + "\n", "basic")
        dateText.insert(tk.END, str(dictionary["date"])+ "\n", "basic")
        sourcePayeeText.insert(tk.END, dictionary["payee/source"] + "\n", "basic")
        # above is table page, below is home page

        payeeAndSourceList.insert(tk.END, dictionary["payee/source"] + "\n", "basic")
        transHistoryList.insert(tk.END, str(dictionary["transaction_id"]) + "\n", "basic")
        if dictionary["transaction_type"] == "income":
            transactionTextBox.insert(tk.END, "+" + dictionary["transaction_value"] + "\n", dictionary["transaction_type"])  # income tag so its green
        else:  
            transactionTextBox.insert(tk.END, "-" + dictionary["transaction_value"] + "\n", dictionary["transaction_type"])  # income tag so its green
    disableTables() # disables the status of tables so user cant edit them

def submissionRemove(tType):
    if tType == "increase": # clears the income widgets
        submitIncomeButton.place_forget()
        incomeEntry.delete(0,tk.END)
        incomeEntry.place_forget()
        incomeOptionChosen.set("Select Income Type")
        incomeDropdown.place_forget()
        incomeDate.place_forget()
        incomeDateLbl.place_forget()
        incomeSourceEntry.delete(0, tk.END)
        incomeSourceEntry.place_forget()
        incomeSourceLbl.place_forget()

    else: # clears the expense widgets 
        submitExpenseButton.place_forget()
        expenseEntry.delete(0,tk.END)
        expenseEntry.place_forget()
        expenseOptionChosen.set("Select Expense Type")
        expenseDropdown.place_forget()
        expenseDate.place_forget()
        expenseDateLbl.place_forget()
        expensePayeeEntry.delete(0, tk.END)
        expensePayeeEntry.place_forget()
        expensePayeeLbl.place_forget()


# buttons to report income starting actions, and submit button, each with functions
def showTransactionPageType(event):
    notebook.add(transaction_page, text="Report Transactions")
    notebook.select(5)
    if transactionChosen.get() == "Income":
        showIncomeBox()
    elif transactionChosen.get() == "Expense":
        showExpenseBox()
    transactionChosen.set("Select Transaction Type")


def showDeleteTransactionPage():
    notebook.add(delete_transaction_page, text = "Delete Transaction")
    notebook.select(6)
    deleteTransactionPageLbl.place(relx = 0.5, rely = 0.05, anchor= tk.CENTER)
    deletingDescriptionLbl.place(relx = 0.5, rely =0.25, anchor= tk.CENTER)
    deleteTransactionIDEntry.place(relx = 0.5, rely = 0.4, anchor= tk.CENTER)
    submitDeletionBtn.place(relx = 0.5, rely = 0.5 , anchor = tk.CENTER)


def showDeleteStatus(status):
    if status == "success":
        messagebox.showinfo("Sucess", "Sucessfully Deleted Transaction")
    elif status == "failure":
        messagebox.showinfo("Unsucsessful", "Unable to Find Transaction")
def deleteTransaction():
    global fullTransactionData
    global balance
    global incomeGained
    global expenseSpent # delete from these so the graphs look right too
    transactionIDToDelete = deleteTransactionIDEntry.get()
    if len(transactionIDToDelete) !=4: # can only check length on string
        errorMessage()

    transactionIDToDelete = int(transactionIDToDelete) # convert entry to int for filtering dictionary
    hasFoundSolution = False
    for dictionary in fullTransactionData:
        dictCategory = dictionary["category"]
        if dictionary["transaction_id"] == transactionIDToDelete:
            if dictionary["transaction_type"] == "income":
                    balance-= int(dictionary["transaction_value"]) # if they are deleting an income, subtract balance by that ammount
                    incomeGained[dictCategory] -= int(dictionary["transaction_value"]) # subtract value from the category for charts
                    if incomeGained[dictCategory] == 0:
                        del incomeGained[dictCategory]
            elif dictionary["transaction_type"] == "expense":
                    balance+= int(dictionary["transaction_value"]) # if they are deleting an expense, add balance by that ammount
                    expenseSpent[dictCategory] -= int(dictionary["transaction_value"])
                    if expenseSpent[dictCategory]== 0:
                        del expenseSpent[dictCategory]
            
            print(fullTransactionData, "THIS IS BEFORE")
            fullTransactionData.remove(dictionary)
            print(fullTransactionData, "THIS IS AFTER")
            updateBalance() 
            hasFoundSolution = True
            break
    if(hasFoundSolution):
        showDeleteStatus("success")
    else:
        showDeleteStatus("failure")
    deleteTransactionIDEntry.delete(0,tk.END)
    notebook.select(1) # clears the entry box and goes back to home page

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


submitIncomeButton = tk.Button(transaction_page, font = mediumFont, text="Submit",command=lambda: [addIncome(),submissionRemove("increase")])  
submitExpenseButton = tk.Button(transaction_page,font = mediumFont, text="Submit",command=lambda: [addExpense(), submissionRemove("expense")])


#dropdown menues
incomeOptionChosen = tk.StringVar(value = "Select Income Type")
incomeDropdown = tk.OptionMenu(transaction_page, incomeOptionChosen, *incomeTypes) # like *args, taking in all income types for dropdown from list
incomeDropdown.config(font = mediumFont)


expenseOptionChosen = tk.StringVar(value = "Select Expense Type")
expenseDropdown = tk.OptionMenu(transaction_page, expenseOptionChosen, *expenseTypes)
expenseDropdown.config(font = mediumFont)

incomeDate = DateEntry(transaction_page)
incomeDateLbl = tk.Label(transaction_page,text = "Enter Transaction Date", font = smallFont)

incomeSourceEntry = tk.Entry(transaction_page, font = mediumFont)
incomeSourceLbl = tk.Label(transaction_page, text = "Income Source", font= mediumFont)

expenseDate = DateEntry(transaction_page)
expenseDateLbl = tk.Label(transaction_page, text = "Enter Transaction Date", font = smallFont)

expensePayeeLbl = tk.Label(transaction_page, text = "Expense Payee", font= mediumFont)
expensePayeeEntry = tk.Entry(transaction_page, font = mediumFont)


deleteTransactionLbl = tk.Label(home_page, text= "Put in a wrong Transaction?", font = mediumFont)
deleteTransactionBtn = tk.Button(home_page, text= "Click here to remove a transaction", font= smallFont, command= showDeleteTransactionPage)

deleteTransactionLbl.place(relx= 0.5, rely= 0.65, anchor= tk.CENTER)
deleteTransactionBtn.place(relx = 0.5, rely = 0.70, anchor= tk.CENTER)


deleteTransactionPageLbl = tk.Label(delete_transaction_page, text= "Delete A transaction", font = largeFont)
deletingDescriptionLbl = tk.Label(delete_transaction_page, text= "Enter ID of transaction ", font= mediumFont)
deleteTransactionIDEntry = tk.Entry(delete_transaction_page, font= mediumFont)
submitDeletionBtn = tk.Button(delete_transaction_page, text = "Submit", font= mediumFont, command= deleteTransaction)


pieChartsLbl = tk.Label(pie_chart_page, text = "Pie Charts", font = largeFont)
pieChartsLbl.place(relx= 0.5, rely = 0.05, anchor= tk.CENTER)

barGraphsLbl = tk.Label(bar_graph_page, text = "Bar Gra")
historyLbl = tk.Label(full_history_page, text = "Full Transaction History", font = largeFont)
historyLbl.place(relx = 0.5, rely = 0.05, anchor = tk.CENTER) 


def quitApplication(): # doesnt end runtime by default when closing
    root.quit()
    root.destroy()
root.protocol("WM_DELETE_WINDOW", quitApplication)

# transaction page, changing it from all on the home


root.bind("<Configure>", onResize)  # lets the frames (tabs for diff pages) resize with the window
root.mainloop()