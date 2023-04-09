from tkinter import *
from tkinter import filedialog

# root = Tk()

# # Fonction pour ouvrir la boîte de dialogue de sélection de fichier
# def open_file_dialog():
#     file_path = filedialog.askopenfilename()
#     picture_path_entry.delete(0, END)
#     picture_path_entry.insert(0, file_path)

# # Créer un champ pour afficher le chemin d'accès de la photo sélectionnée
# picture_path_entry = Entry(root, width=50)

# # Créer un bouton "Parcourir" pour ouvrir la boîte de dialogue de sélection de fichier
# browse_button = Button(root, text="Parcourir", command=open_file_dialog)

# # Pack les widgets
# picture_path_entry.pack()
# browse_button.pack()

# root.mainloop()
nom,prenom,email=("rida","bentouh","m@gmial.com")
args=[("nom",nom),("prenom",prenom),("email",email)]
file=open("data.txt","a+")
for key,value in args:
    file.write(key+f":{value}\n")
file.close()

mydata={}
file=open("data.txt","r")
data=file.read().split("\n")
data.remove("")
print(data)
for line in data:
    items=line.split(":")
    mydata[items[0]]=items[1]


    

print(mydata)