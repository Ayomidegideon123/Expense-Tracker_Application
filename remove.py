# function to delete all the entries
def removeAllExpenses():
'''''This function will remove all the entries from the table'''

# displaying a message box asking for confirmation
confirmation = mb.askyesno('Are you sure?', 'Are you sure that you want to delete all the expense items from the database?', icon='warning')

# if the user say YES, deleting the entries from the table and executing the SQL

DELETE FROM command to delete all the entries
if confirmation:
  data_table.delete(*data_table.get_children())

  dbconnector.execute('DELETE FROM ExpenseTracker')
  dbconnector.commit()

# calling the clearFields() function
clearFields()

# calling the listAllExpenses() function
listAllExpenses()

# returning the message box displaying the information

mb.showinfo('All Expenses deleted', 'All the expenses were successfully deleted')
else:
# returning the message box, if the operation is aborted
mb.showinfo('Ok then', 'The task was aborted and no expense was deleted!')
