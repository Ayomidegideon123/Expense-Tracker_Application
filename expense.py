# function to display the expense details into words before adding it to the table
def expenseToWordsBeforeAdding():
'''''This function will display the details of the expense into words before adding it to the table'''

# using some global variables
global dateField, description, amount, payee, modeOfPayment

# if any of the field is empty, return the message box displaying error
if not dateField.get() or not payee.get() or not description.get() or not amount.get() or not modeOfPayment.get()
mb.showerror('Incomplete data', 'The data is incomplete, meaning fill all the

fields first!')
else:
# defining the message to be displayed in the message box msg = f'Your expense can be read like: \n"You paid {amount.get()} to {payee.get()} for {description.get()} on {dateField.get_date()} via {modeOfPayment.get()}"'

# displaying a message box asking for confirmation
addQuestion = mb.askyesno('Read your record like: ', f'{msg}\n\nShould I add it to the database?')
# if the user say YES, calling the addAnotherExpense() function

 if addQuestion:
addAnotherExpense()
else:
# returning a message box displaying information
mb.showinfo('Ok', 'Please take your time to add this record')
