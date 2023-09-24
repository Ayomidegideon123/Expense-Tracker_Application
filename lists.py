# --------------------- defining functions ---------------------

# function to list all the expenses

def listAllExpenses():
'''''This function will retrieve the data from the database and insert it to the tkinter data table'''
# using some global variables
global dbconnector, data_table
# clearing the table
data_table.delete(*data_table.get_children())
# executing the SQL SELECT command to retrieve the data from the database table
all_data = dbconnector.execute('SELECT * FROM ExpenseTracker')
# listing the data from the table
data = all_data.fetchall()
# inserting the values iteratively in the tkinter data table
for val in data:
data_table.insert('', END, values = val
