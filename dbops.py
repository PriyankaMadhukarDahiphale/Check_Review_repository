
# Function to update student information
def delete_student():

    # Getting id of student to delete
    id = Entry_Student_ID.get()

    #Here proceedOrNot is a variable which is used to store the return value of askyesno() method
    proceedOrNot = messagebox.askyesno("Student Information", "Delete Student ?\nId = {} ".format(id))

    if proceedOrNot == 1:

        # Deleting student information from database
        cursor.execute(" delete from student where id = '"+id+"' ")

        # Commiting changes to database
        mydb.commit()

        # Displaying a message box if data is deleted successfully
        messagebox.showinfo("Deleting Student", "Successfully deleted Student \n Id = {}".format(id))
    else:

        # Displaying a message box if data is not deleted successfully
        messagebox.showinfo("Unsuccessfully", "Canceled")


# Function to reset all fields
def reset_info():
    Entry_Student_ID.delete(0, 40)
    Entry_Student_Name.delete(0,40)
    Entry_Grade.delete(0, 40)
    Entry_Student_ID.delete(0, 40)
    Entry_Date.delete(0, 40)
    Entry_Month.delete(0, 40)
    Entry_Year.delete(0, 40)
    Entry_Degree.delete(0, 40)
    Entry_Stream.delete(0, 40)
    Entry_Phone_Number.delete(0, 40)
    Entry_Email.delete(0, 40)
    Entry_Address.delete(1.0, "end-1c")


# Function to update student informations displayed in treeview
def refresh_info():
    # Deleting previous data from treeview
    tree.delete(*tree.get_children())

    # Fetching data from database
    cursor.execute("select * from student")

    for i in cursor:
        #inserting data into treeview. Start from 0
        tree.insert("", 0, text=i[0], values=(i[1], i[2], i[3], i[4]+" - "+i[5]+" - "+i[6], i[7], i[8], i[9], i[10], i[11]))


# Function to search student information from database
def search_info():
    id = Entry_Student_ID.get()
    name = Entry_Student_Name.get()
    email = Entry_Email.get()

    # Deleting previous data from treeview
    if tree2.get_children() != ():
        tree2.delete(*tree2.get_children())

    # Fetching data from database
    cursor.execute("select * from student where id = '"+id+"' or Email = '"+email+"' or name like '"+name+"%' ")

    for i in cursor:
        #inserting data into treeview. Start from 0
        tree2.insert("", 0, text=i[0], values=(i[1], i[2], i[3], i[4]+" - "+i[5]+" - "+i[6], i[7], i[8], i[9], i[10], i[11]))
