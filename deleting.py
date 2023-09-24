# function to delete the selected record
def removeExpense():
'''''This function will remove the selected record from the table'''

# returning the message box displaying error if no row is selected
if not data_table.selection():
mb.showerror('No record selected!', 'Please select a record to delete!')
  return

# collecting the data from the selected row in dictionary format
currentSelectedExpense = data_table.item(data_table.focus())

# defining a variable to store the values from the collected data in list
valuesSelected = currentSelectedExpense['values']

# displaying a message box asking for confirmation
confirmation = mb.askyesno('Are you sure?', f'Are you sure that you want to delete the record of {valuesSelected[2]}')

# if the user say YES, executing the SQL DELETE FROM command
if confirmation:
dbconnector.execute('DELETE FROM ExpenseTracker WHERE ID=%d' % valuesSelected[0])
dbconnector.commit()

# calling the listAllExpenses() function
listAllExpenses()

# returning the message box displaying the information
mb.showinfo('Record deleted successfully!', 'The record you wanted to delete has been deleted successfully')
