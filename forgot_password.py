import tkinter as tk
import mysql.connector
from PIL import Image,ImageTk
#----------------------placeholder in birtthday----------------------------
def on_entry_click(event):
    """Function to handle click event on Entry widget"""
    if date_de_naissance_entry.get() == 'YYYY-MM-DD':
       date_de_naissance_entry.delete(0, tk.END)  # Delete the placeholder text

#-------------------------click number function---------------------------
global num_clicks
num_clicks = 0
max_clicks = 4
#------------first one------------------------
def verify_with_limit1():
    global num_clicks
    num_clicks += 1
    if num_clicks > max_clicks:
        root.after(350, root.destroy)
    else:
        verify_user_info()
#-------------second one-------------------
def verify_with_limit2():
    global num_clicks
    num_clicks += 1
    if num_clicks > max_clicks:
        reset_root.after(350, reset_root.destroy)
    else:
        update_password()

#------------------------------Function to verify user information in the MySQL database-------------------------------

def verify_user_info():
    # Get user input from the GUI fields
    global cne
    cin = cin_entry.get()
    cne= cne_entry.get()
    date_de_naissance = date_de_naissance_entry.get()

    # Connect to MySQL database
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="lokmane-SQL-12", 
        database="projet"
    )
    mycursor = mydb.cursor()

    # Execute the MySQL query to verify user information
    query = "SELECT * FROM projet.etudiant WHERE cin = %s AND cne = %s AND date_de_naissance = %s "
    values = (cin, cne, date_de_naissance)
    mycursor.execute(query, values)
    result = mycursor.fetchone()

    # Check if the result is indicating valid user information
    if result:
        # Close the MySQL connection
        mycursor.close()
        mydb.close()

        # Open the password reset GUI
        open_password_reset_gui()
    else:
        # Update the main interface with error message
        error_label = tk.Label(root, text="Error")
        error_label.config(text="Les informations saisies sont incorrectes", font=("Arial", 18, "bold"), fg="red")
        error_label.place(x=700, y=580)
        error_label.after(2000, error_label.destroy) # this message will be deleted after 3s



# -----------------------------Function to open the password reset GUI--------------------------------------------

def open_password_reset_gui():
    # Close the main GUI window
    root.destroy()

    # Create a new GUI window for password reset
    global reset_root
    reset_root = tk.Tk()
    reset_root.title("Réinitialisation du mot de passe")
    reset_root.geometry("1200x720")
    welcome=tk.Label(reset_root,text="ESPACE     ÉTUDIANT ",font=("Arial",65),fg="blue")
    welcome.place(x=155,y=10)
    global entry1
    global entry2

    # Add labels, entry fields, and buttons

    label1 = tk.Label(reset_root, text="Enterez le nouveau mot de passe:", font=("Arial", 20))
    label1.place(x=700, y=200)

    entry1 = tk.Entry(reset_root, show="*", width=20, font=("Arial", 14),highlightthickness=3, highlightcolor='blue',highlightbackground='black') 
    entry1.place(x=700, y=250)



    label2 = tk.Label(reset_root, text="confirmez le mot de passe:", font=("Arial", 20))
    label2.place(x=700, y=300)

    entry2 = tk.Entry(reset_root, show="*",  width=20, font=("Arial", 14),highlightthickness=3, highlightcolor='blue',highlightbackground='black')  
    entry2.place(x=700, y=350)

    button = tk.Button(reset_root, text="Confirmez! ", bg="green",font=("Arial",18), relief="flat",command=verify_with_limit2)
    button.place(x=700,y=415)

    # Main GUI window loop
    reset_root.mainloop()

#-----------------------------update_password----------------------------------------------------------

def update_password():
  mydb = mysql.connector.connect(
      host="127.0.0.1",
      user="root",
      password="Mohamed-123+", 
      database="projet"
  )
  mycursor = mydb.cursor()
  # Retrieve password input from entry fields
  new_password = entry1.get()
  confirm_password = entry2.get()

  # Validate that new password and confirm password match
  if new_password != confirm_password:
    error_label1 = tk.Label(reset_root, text="Error")
    error_label1.config(text="les mots de passes ne correspondent pas! ",  font=("Arial", 18, "bold"), fg="red")  
    error_label1.place(x=700, y=480)
    error_label1.after(3000, error_label1.destroy)
    return 
  # Update password in the database
  mycursor.execute("UPDATE projet.etudiant SET password = %s WHERE cne= %s", (new_password, cne))
  # Commit changes to the database
  mydb.commit()

  # Show confirmation message
  error_label2 = tk.Label(reset_root, text="Error")
  error_label2.config(text="mise à jour du mot de passe réussie!",  font=("Arial", 18, "bold"), fg="red")  
  error_label2.place(x=700, y=480)  
  reset_root.after(3500, reset_root.destroy) 

#---------------------------main_function------------------------------------------------ 


root = tk.Tk()
root.title("Vérification des informations d'utilisateur")
root.geometry("1200x720")
root.config(bg="white")
imagee=(Image.open("C:\\Users\\lokmane\\Desktop\\Tkinter_project\\icons\\password2.jpg"))
imagee=imagee.resize((430,800))
sidepicture = ImageTk.PhotoImage(imagee)
#----------------Create a Label Widget to display the  Image-----------------
label = tk.Label(root, image = sidepicture,padx=0,pady=0, relief="flat")
label.grid(row=0,column=0)
welcome=tk.Label(root,text="ESPACE     ETUDIANT ",font=("Arial",54),bg="white")
welcome.place(x=435,y=0)

# Create GUI elements for CIN and CNE input fields
cin_label = tk.Label(root, text="Entrez votre CIN:", font=("Arial",35),bg="white")
cin_label.place(x=600,y=150)

cin_entry = tk.Entry(root,width=20,font=("Arial",30),relief="flat",bg="#e9eaef",highlightcolor="#041777",highlightthickness=3,highlightbackground='white')
cin_entry.place(x=580,y=220)

cne_label = tk.Label(root, text="Entrez votre CNE:", font=("Arial",35),bg="white")
cne_label.place(x=600,y=280)

cne_entry = tk.Entry(root,width=20,font=("Arial",30),relief="flat",bg="#e9eaef",highlightcolor="#041777",highlightthickness=3,highlightbackground='white')
cne_entry.place(x=580,y=340)

birthday_label=tk.Label(root, text="Entrez votre date de naissance:", font=("Arial", 20),bg="white")
birthday_label.place(x=580, y=425)

date_de_naissance_entry = tk.Entry(root, width=20,font=("Arial",30),relief="flat",bg="#e9eaef",highlightcolor="#041777",highlightthickness=3,highlightbackground='white')
date_de_naissance_entry.insert(0, 'YYYY-MM-DD')  # Set the placeholder text
date_de_naissance_entry.bind('<FocusIn>', on_entry_click)  # Bind the click event to the function
date_de_naissance_entry.place(x=580, y=460)

verify_button = tk.Button(root, text="Vérifiez!",bg="#32a2cd",fg="white",activebackground="#32a2cd", activeforeground="white",font=("Arial",20),padx=0,pady=0, relief="flat",width=27,command=verify_with_limit1)
verify_button.place(x=580, y=570)

root.mainloop()





