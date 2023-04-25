import tkinter as tk
import mysql.connector
from PIL import Image,ImageTk
import subprocess
MAX_TRIES = 5
def on_entry_click(event):
    """Function to handle click event on Entry widget"""
    if date_de_naissance_entry.get() == 'YYYY-MM-DD':
        date_de_naissance_entry.delete(0, tk.END)  # Delete the placeholder text

def verify():
    """Function to verify user information"""
    global cne
    cne = cne_entry.get()
    cin = cin_entry.get()
    ddn = date_de_naissance_entry.get()

    # Verify user information in database
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="lokmane-SQL-12",
        database="projet"
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM etudiant WHERE cne=%s AND cin=%s AND date_de_naissance=%s", (cne, cin, ddn))
    result = cursor.fetchone()

    if result:
        root.destroy()
        subprocess.run(["python","C:\\Users\\lokmane\\Desktop\\Tkinter_project\\forgot_password2.py"])
    else:
        global MAX_TRIES
        MAX_TRIES -= 1
        if MAX_TRIES == 0:
            error_label = tk.Label(root, text="Error")
            error_label.config(text="Les informations saisies sont incorrectes", font=("Arial", 18, "bold"), fg="red")
            error_label.place(x=700, y=580)
            error_label.after(2000, root.destroy) # this message will be deleted after 3s
        else:
            error_label = tk.Label(root, text="Error")
            error_label.config(text="Les informations saisies sont incorrectes", font=("Arial", 18, "bold"), fg="red")
            error_label.place(x=700, y=580)
            error_label.after(2000, error_label.destroy)
def get_user_name():
    logfile=open("fichierlog.txt",'r')
    users=logfile.read().split("\n")
    username=users[-2]
    return username
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
welcome=tk.Label(root,text="ESPACE     ETUDIANT ",font=("LEMONMILK-Medium",54),bg="white")
welcome.place(x=435,y=0)

# Create GUI elements for CIN and CNE input fields
cin_label = tk.Label(root, text="CIN:", font=("Louis George Cafe Bold",35),bg="white")
cin_label.place(x=580,y=150)

cin_entry = tk.Entry(root,width=20,font=("Arial",30),relief="flat",bg="#e9eaef",highlightcolor="#041777",highlightthickness=3,highlightbackground='white')
cin_entry.place(x=580,y=220)

cne_label = tk.Label(root, text="CNE:", font=("Louis George Cafe Bold",35),bg="white")
cne_label.place(x=580,y=280)

cne_entry = tk.Entry(root,width=20,font=("Arial",30),relief="flat",bg="#e9eaef",highlightcolor="#041777",highlightthickness=3,highlightbackground='white')
cne_entry.place(x=580,y=340)

birthday_label=tk.Label(root, text="Date de naissance:", font=("Louis George Cafe Bold", 35),bg="white")
birthday_label.place(x=580, y=400)

date_de_naissance_entry = tk.Entry(root, width=20,font=("Arial",30),relief="flat",bg="#e9eaef",highlightcolor="#041777",highlightthickness=3,highlightbackground='white')
date_de_naissance_entry.insert(0, 'YYYY-MM-DD')  # Set the placeholder text
date_de_naissance_entry.bind('<FocusIn>', on_entry_click)  # Bind the click event to the function
date_de_naissance_entry.place(x=580, y=465)

verify_button = tk.Button(root, text="Vérifiez!",bg="#32a2cd",fg="white",activebackground="#32a2cd", activeforeground="white",font=("Arial",20),padx=0,pady=0, relief="flat",width=27,command=verify)
verify_button.place(x=580, y=570)
#--------------------------leave button--------------------------------------------------------------------------
leavebutton=tk.Button(root,text="Quitter",command=root.quit,bg="#258EF5",fg="white",activebackground="#258EF5", activeforeground="white",font=("Arial",16),padx=0,pady=0, relief="flat")      #
leavebutton.place(x=1100, y=660)

root.mainloop()






