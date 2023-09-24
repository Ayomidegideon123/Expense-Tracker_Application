# function to add an expense
def addAnotherExpense():
'''''This function will add an expense to the table and database'''

# using some global variables
global dateField, payee, description, amount, modeOfPayment
global dbconnector

# if any of the field is empty, return the message box displaying error
if not dateField.get() or not payee.get() or not description.get() or not amount.get() or not modeOfPayment.get(): 
  mb.showerror('Fields empty!', "Please fill all the missing fields before pressing the add button!")
else:
# executing the SQL INSERT INTO command
dbconnector.execute(

'INSERT INTO ExpenseTracker (Date, Payee, Description, Amount,
ModeOfPayment) VALUES (?, ?, ?, ?, ?)',
(dateField.get_date(), payee.get(), description.get(), amount.get(),
modeOfPayment.get())
)

 dbconnector.commit()

# calling the clearFields() function
clearFields()
# calling the listAllExpenses() function
listAllExpenses()

# returning the message box displaying information
mb.showinfo('Expense added', 'The expense whose details you just entered has been added to the database')
