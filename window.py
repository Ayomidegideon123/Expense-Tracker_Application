# creating the main window of the application

# creating an instance of the Tk() class
main_win = Tk()
# setting the title of the application
main_win.title("EXPENSE TRACKER - JAVATPOINT")
# setting the size and position of the window
main_win.geometry("1415x650+400+100")
# disabling the resizable option for better UI
main_win.resizable(0, 0)
# configuring the background color to #FFFAF0
main_win.config(bg = "#FFFAF0")
# setting the icon of the application
main_win.iconbitmap("./piggyBank.ico"
