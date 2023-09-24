 # function to edit the details of an expense
def editExpense():
'''''This function will allow user to edit the details of the selected expense'''

# using some global variables
global data_table

# defining a nested to update the details of the selected expense
def editExistingExpense():
'''''This function will update the details of the selected expense in the database and table'''

# using some global variables
global dateField, amount, description, payee, modeOfPayment
global dbconnector, data_table

# collecting the data from the selected row in dictionary format
currentSelectedExpense = data_table.item(data_table.focus())

# defining a variable to store the values from the collected data in list
content = currentSelectedExpense['values']

 # executing the SQL UPDATE command to update the record in database table
dbconnector.execute(
'UPDATE ExpenseTracker SET Date = ?, Payee = ?, Description = ?, Amount = ?, ModeOfPayment = ? WHERE ID = ?'
  (dateField.get_date(), payee.get(), description.get(), amount.get(), modeOfPayment.get(), content[0])
)
dbconnector.commit()

# calling the clearFields() function
clearFields()

# calling the listAllExpenses() function
listAllExpenses()
# returning a message box displaying the message
mb.showinfo('Data edited', 'We have updated the data and stored in the database as you wanted')
# destroying the edit button
editSelectedButton.destroy()

# returning a message box displaying error if no record is selected
if not data_table.selection():
mb.showerror('No expense selected!', 'You have not selected any expense in the table for us to edit; please do that!')
return

#calling the viewExpenseInfo() method
viewExpenseInfo()

#adding the Edit button to edit the selected record
editSelectedButton = Button(
frameL3,
  text = "Edit Expense",
font = ("Bahnschrift Condensed", "13"),
width = 30,
bg = "#90EE90",
fg = "#000000",

relief = GROOVE,
activebackground = "#008000",
activeforeground = "#98FB98",
command = editExistingExpense
)

# using the grid() method to set the position of the above button on the main window screen
editSelectedButton.grid(row = 0, column = 0, sticky = W, padx = 50, pady = 10)
