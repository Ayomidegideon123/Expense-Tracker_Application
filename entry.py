# function to clear the entries from the entry fields
def clearFields():
'''''This function will clear all the entries from the entry fields'''

# using some global variables
global description, payee, amount, modeOfPayment, dateField, data_table

# defining a variable to store today's date
todayDate = datetime.datetime.now().date()

# setting the values in entry fields back to initial
description.set('') ; payee.set('') ; amount.set(0.0) ; modeOfPayment.set('Cash'), dateField.set_date(todayDate)
# removing the specified item from the selection
data_table.selection_remove(*data_table.selection())
