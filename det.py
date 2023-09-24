 # function to display the details of selected expense into words
def selectedExpenseToWords():
'''''This function will display the details of the selected expense from the table into words'''

# using some global variables
global data_table

# returning a message box displaying error, if no record is selected from the table
if not data_table.selection():
mb.showerror('No expense selected!', 'Please select an expense from the table for us to read')
return

# collecting the data from the selected row in dictionary format
currentSelectedExpense = data_table.item(data_table.focus())
# defining a variable to store the values from the collected data in list
val = currentSelectedExpense['values']

# defining the message to be displayed in the message box
msg = f'Your expense can be read like: \n"You paid {val[4]} to {val[2]} for {val[3]} on {val[1]} via {val[5]}"

# returning the message box displaying the message
mb.showinfo('Here\'s how to read your expense', msg)
