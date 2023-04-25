import tkinter as tk
from tkinter import *
import _mysql_connector
import subprocess
import os
# GUI for personnel infos----------------------------------------------

root = tk.Tk()
root.title("Modification des infos personnels")
root.geometry("1200x720")
#-----------subprocess-----------
current_path=os.getcwd()
def go_there():
    subprocess.run(["python", current_path+"\\singUp1"])

# Create GUI elements for CIN and CNE input fields
iconsbarr=Frame(root,width=150,height=1440,bg="#15b4ea")
iconsbarr.place(x=0,y=0)
#------------------------------personal data frame------------------------------------------------------------------
body_frame=Frame(root,bg="#B5EFFF",width=1000,height=530,relief="flat")
body_frame.place(x=170,y=100)


nom_label = tk.Label(body_frame, text="Nom:", font=("Arial", 20))
nom_label.place(x=385, y=6)


prenom_label = tk.Label(body_frame, text="Prénom:", font=("Arial", 20))
prenom_label.place(x=385, y=48)


CNE_label = tk.Label(body_frame, text="CNE:", font=("Arial", 20))
CNE_label.place(x=385, y=90)



CIN_label = tk.Label(body_frame, text="CIN:", font=("Arial", 20))
CIN_label.place(x=385, y=132)



Filière_label = tk.Label(body_frame, text="Filière:", font=("Arial", 20))
Filière_label.place(x=385, y=176)


Email_label = tk.Label(body_frame, text="Email:", font=("Arial", 20))
Email_label.place(x=385, y=220)


Adresse_label = tk.Label(body_frame, text="Adresse:", font=("Arial", 20))
Adresse_label.place(x=385, y=264)


Téléphone_label = tk.Label(body_frame, text="Téléphone:", font=("Arial", 20))
Téléphone_label.place(x=385, y=308)



Date_de_naissance_label = tk.Label(body_frame, text="Date de naissance:", font=("Arial", 20))
Date_de_naissance_label.place(x=385, y=352)



password_label = tk.Label(body_frame, text="Mot de passe:", font=("Arial", 20))
password_label.place(x=385, y=396)

verify_button = tk.Button(body_frame, text="Modifier!", bg="blue", fg="white", font=("Arial", 18), command=go_there())
verify_button.place(x=870, y=470)

root.mainloop()
