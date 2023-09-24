# function to view an expense information
def viewExpenseInfo():
'''''This function will display the expense information in the data frame'''

# using some global variables
global data_table
global dateField, payee, description, amount, modeOfPayment

# return a message box displaying error if no row is selected from the table
if not data_table.selection():
  mb.showerror('No expense selected', 'Please select an expense from the table to view its details')

# collecting the data from the selected row in dictionary format
currentSelectedExpense = data_table.item(data_table.focus())

# defining a variable to store the values from the collected data in list
val = currentSelectedExpense['values']

# retrieving the date of expenditure from the list
expenditureDate = datetime.date(int(val[1][:4]), int(val[1][5:7]), int(val[1][8:])
