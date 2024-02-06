
#importing required libraries
import tkinter as tk
import sqlite3
from tkinter import messagebox
import os
from tkinter import ttk


# Tkinter theme
window = tk.Tk()
window.configure(background="#000d66")

# Set logo to application for macOS
img = tk.Image('photo', file=os.path .join(os.path.dirname(__file__), "DataFlair.png"))
window.tk.call( 'wm','iconphoto', window._w, img)

# Set icon to application for Windows
window.iconbitmap(os.path.join(os.path.dirname(__file__), "DataFlair.ico"))

# Set window size
window.geometry("1280x720")

# Set window title
window.title("DataFlair - School Management System")


# Connect to database
mydb = sqlite3.connect(os.path.join(os.path.dirname(__file__), "Student.db")) 

# Create a cursor to execute SQL commands
cursor = mydb.cursor() 

# Create a table in database if not exists
cursor.execute('''
create table if not exists student (
    Name varchar(50) NOT NULL, 
    ID varchar(20) NOT NULL PRIMARY KEY,
    Grade varchar(10) NOT NULL, 
    Sex varchar(10) NOT NULL, 
    date varchar(5) NOT NULL, 
    Month varchar(5) NOT NULL, 
    Year varchar(6) NOT NULL,
    Degree varchar(10) NOT NULL,
    Stream varchar(50) NOT NULL,
    Phone varchar(20) NOT NULL,
    Email varchar(50) NOT NULL UNIQUE,
    Address varchar(150) NOT NULL
    )
    ''')



var = 0 # Variable for radio button

sex = "none" # Variable for gender 

# If female radio button is selected then
# value of sex variable will be set to "Female"
def female_selected(): 
    global sex
    sex = "Female"
    return sex


# If male radio button is selected then
# value of sex variable will be set to "Male"
def male_selected():
    global sex
    sex = "Male"
    return sex


# Add student information to database
def add_info():
    global sex
    name = Entry_Student_Name.get()
    grade = Entry_Grade.get()
    sex = sex
    id = Entry_Student_ID.get()
    date = Entry_Date.get()
    month = Entry_Month.get()
    year = Entry_Year.get()
    degree = Entry_Degree.get()
    stream = Entry_Stream.get()
    phone = Entry_Phone_Number.get()
    email = Entry_Email.get()
    address = Entry_Address.get(1.0, "end-1c")

    #Here proceedOrNot is a variable which is used to store the return value of askyesno() method
    #askyesno() method is used to display a dialog box with yes and no button
    #If yes button is clicked then it returns 1 else it returns 0
    proceedOrNot = messagebox.askyesno("Student Adding", "Are You Sure add Student \nName = {}\nId = {}\nGrade = {}\nSex = {}\ndate = {}/{}/{}\nDegree = {}\nStream = {}\nPhone = {}\nEmail = {}\nAddress = {}".format(name, id, grade, sex, date, month, year, degree, stream, phone, email, address))

    if proceedOrNot == 1:

        # Inserting data into database
        cursor.execute("insert into student values ('"+name+"', '"+id+"', '"+grade+"', '"+sex+"', '"+date+"', '"+month+"', '"+year+"' , '"+degree+"', '"+stream+"', '"+phone+"', '"+email+"', '"+address+"')")
        
        # Displaying a message box if data is inserted successfully
        messagebox.showinfo("Student Adding", "Successfully added Student \nName = {}\nId = {}\nGrade = {}\nSex = {}\ndate = {}/{}/{}\nDegree = {}\nStream = {}\nPhone = {}\nEmail = {}\nAddress = {}".format(name, id, grade, sex, date, month, year, degree, stream, phone, email, address))
        
        # Commiting changes to database
        mydb.commit()

    else:

        # Displaying a message box if data is not inserted successfully
        messagebox.showinfo("Unsuccessfull", "Cancelled")
