# main function
if __name__ == "__main__":
# connecting to the Database
  dbconnector = sqlite3.connect("Expense_Tracker.db")
dbcursor = dbconnector.cursor()

# specifying the function to execute whenever the application runs
dbconnector.execute(
'CREATE TABLE IF NOT EXISTS ExpenseTracker (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, Date DATETIME, Payee TEXT, Description TEXT, Amount FLOAT, ModeOfPayment TEXT)'
)
# committing the above command
dbconnector.commit()
