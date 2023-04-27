# from tkinter import *
# from tkinter import filedialog
# from re import *
# import mysql.connector as sc

# # root = Tk()

# # # Fonction pour ouvrir la boîte de dialogue de sélection de fichier
# # def open_file_dialog():
# #     file_path = filedialog.askopenfilename()
# #     picture_path_entry.delete(0, END)
# #     picture_path_entry.insert(0, file_path)

# # # Créer un champ pour afficher le chemin d'accès de la photo sélectionnée
# # picture_path_entry = Entry(root, width=50)

# # # Créer un bouton "Parcourir" pour ouvrir la boîte de dialogue de sélection de fichier
# # browse_button = Button(root, text="Parcourir", command=open_file_dialog)

# # # Pack les widgets
# # picture_path_entry.pack()
# # browse_button.pack()

# # root.mainloop()







# # nom,prenom,email=("rida","bentouh","m@gmial.com")
# # args=[("nom",nom),("prenom",prenom),("email",email)]
# # file=open("data.txt","a+")
# # for key,value in args:
# #     file.write(key+f":{value}\n")
# # file.close()

# # mydata={}
# # file=open("data.txt","r")
# # data=file.read().split("\n")
# # data.remove("")
# # print(data)
# # for line in data:
# #     items=line.split(":")
# #     mydata[items[0]]=items[1]



# # print(mydata)

# database=sc.connect(
#             user="root",
#             passwd="root",
#             host="localhost",
#             database="projet"

#         )
# print("connected")

# cursor=databa
import mysql.connector
from io import BytesIO
from PIL import Image,ImageTk
import re

# Connect to the database

database = mysql.connector.connect(
    user="root",
    passwd="root",
    host="localhost",
    database="projet"
)

# cursor = database.cursor()
# def convertToBinary(file):
#     with open(file,"rb") as f:
#         bd=f.read()
#     return bd

# sql="UPDATE ETUDIANT SET IMAGE=%s WHERE ID=1"
# data=(convertToBinary("'C:/Users/us/Pictures/mercedes.jpg'".replace("'","")),)

# cursor.execute(sql,data)
# database.commit()
# print("cheked")




# Create a cursor object
cursor = database.cursor()

# Execute the SELECT query to retrieve the image data
sql = "SELECT IMAGE FROM ETUDIANT WHERE ID=2"
cursor.execute(sql)

# Fetch the image data from the database
# image_data = cursor.fetchone()[0]

# print(image_data)
# Convert the image data to a PIL Image object
# image = Image.open(BytesIO(image_data))
# image=image.resize((500,500),Image.ANTIALIAS)
# image=ImageTk.PhotoImage(image)

# Display the image
# image.show()

# email=re.match(r"\w+\.?\w+@\w+\.\w{2,}","ridagmai.com")
# print(bool(email))
# r"2\d{3}-[0-1]?\d-[0-2]?\d|3[0-1]"
# date = re.match(r"2\d{3}-[0-1]?\d-[0-2]?\d|3[0-1]","2003-1-31")
# print(bool(date))

# phone=re.match(r"\+212(6|7)\d{8}","+212655675768")
# print(bool(phone))

# print(bool(re.match(r"[A-Z]{1}/d{10}","S2346383923")))

# print("<_io.TextIOWrapper name='C:/Users/us/Pictures/mercedes.jpg' mode='r' encoding='cp65001'>".split(" ")[1].split("=")[1].replace("'",""))

# print(bool(re.match(r"^0(6|7)\d{8}$","0655675876")))

import tkinter as tk

# Créer une fenêtre
window = tk.Tk()

# Créer une liste de choix
choices = ["Choix 1l ", "Choix 2", "Choix 3", "Choix 2", "Choix 3", "Choix 2", "Choix 3", "Choix 2", "Choix 3", "Choix 2", "Choix 3", "Choix 2", "Choix 3", "Choix 2", "Choix 3", "Choix 2", "Choix 3", "Choix 2", "Choix 3", "Choix 2", "Choix 3", "Choix 2", "Choix 3", "Choix 2", "Choix 3", "Choix 2", "Choix 3", "Choix 2", "Choix 3", "Choix 2", "Choix 3", "Choix 2", "Choix 3", "Choix 2", "Choix 3"]

# Créer un widget Listbox
listbox = tk.Listbox(window)

# Ajouter les choix à la liste
for choice in choices:
    listbox.insert(tk.END, choice)

# Créer un bouton pour afficher ou masquer la liste de choix
button = tk.Button(window, text="Afficher/Masquer", command=lambda: listbox.place_forget() if listbox.winfo_ismapped() else listbox.place(x=40,y=90))

# Afficher le bouton
button.place(x=40,y=70)

# Démarrer la boucle principale
# window.mainloop()

# cursor1=database.cursor()

# requete="CREATE TABLE FILIERE ( NOM varchar(50)"

# for i in range(1,12):
#     requete=requete +f",module{i} varchar(50)"

# requete=requete+")"

# print(requete)

# cursor1.execute(requete)
# with open(r"fichierLog.txt","r") as fL:
#         cne=fL.readlines()[0].replace("\n","")
# requete="SELECT NOM,PRENOM,filière FROM ETUDIANT WHERE CNE=%s"
# cursor.execute(requete,(cne,))
# nom_prenom_fil=cursor.fetchall()
# print(nom_prenom_fil[0])

# cursor.execute("SELECT IMAGE FROM ETUDIANT WHERE CIN='R1587899633'")
# print(cursor.fetchone())
raise "contacter l'addministration"
print(3)