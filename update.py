from tkinter import *
import mysql.connector 
import subprocess
from PIL import Image,ImageTk
import os
import webbrowser
from tkinter import messagebox

current_path=os.getcwd()
account=Tk()
account.title("Modification des infos personnels")
account.geometry("1200x720")
account.config(bg="white")
iconsbarr=Frame(account,width=150,height=1440,bg="#15b4ea",)
iconsbarr.place(x=0,y=0)

def personel():
    personel=Tk()
    personel.geometry=("1200x720")
    personel.config(bg="white")
def get_user_second_name():
    logfile=open("fichierlog.txt",'r')
    users=logfile.read().split("\n")
    username=users[-2]
    cursorr.execute("SELECT prenom from Etudiant where CIN='"+username+"';")
    result=cursorr.fetchone()
    return result[0]
def log_out():
    account.destroy()
    subprocess.run(["python",current_path+"\\Luncher.py"])
def get_user_first_name():
    logfile=open("fichierlog.txt",'r')
    users=logfile.read().split("\n")
    username=users[-2]
    cursorr.execute("SELECT nom from Etudiant where CIN='"+username+"';")
    result=cursorr.fetchone()
    return result[0]
def get_filiere():
    logfile=open("fichierlog.txt",'r')
    users=logfile.read().split("\n")
    username=users[-2]
    cursorr.execute("SELECT filiere from Etudiant where CIN='"+username+"';")
    result=cursorr.fetchone()
    return result[0]

def get_user_picture():
    logfile=open("fichierlog.txt",'r')
    users=logfile.read().split("\n")
    username=users[-2]
    cursorr.execute("SELECT photo from Etudiant where CIN='"+username+"';")
    result=cursorr.fetchone()
    photo_path=result[0]
    return photo_path
def get_user_CNE():
    logfile=open("fichierlog.txt",'r')
    users=logfile.read().split("\n")
    username=users[-2]
    cursorr.execute("SELECT CNE from Etudiant where CIN='"+username+"';")
    result=cursorr.fetchone()
    cne=result[0]
    return cne

def get_user_picture():
    logfile=open("fichierlog.txt",'r')
    users=logfile.read().split("\n")
    username=users[-2]
    cursorr.execute("SELECT photo from Etudiant where CIN='"+username+"';")
    result=cursorr.fetchone()
    photo_path=result[0]
    return photo_path
def get_user_CNE():
    logfile=open("fichierlog.txt",'r')
    users=logfile.read().split("\n")
    username=users[-2]
    cursorr.execute("SELECT CNE from Etudiant where CIN='"+username+"';")
    result=cursorr.fetchone()
    cne=result[0]
    return cne

def get_user_CIN():
    logfile=open("fichierlog.txt",'r')
    users=logfile.read().split("\n")
    username=users[-2]
    cursorr.execute("SELECT CIN from Etudiant where CIN='"+username+"';")
    result=cursorr.fetchone()
    cin=result[0]
    return cin
def get_password():
    logfile=open("fichierlog.txt",'r')
    users=logfile.read().split("\n")
    username=users[-2]
    cursorr.execute("SELECT mot_de_passe from Etudiant where cne='"+username+"';")
    result=cursorr.fetchone()
    mot_de_passe=result[0]
    return mot_de_passe
def get_téléphone():
    logfile=open("fichierlog.txt",'r')
    users=logfile.read().split("\n")
    username=users[-2]
    cursorr.execute("SELECT téléphone from Etudiant where cne='"+username+"';")
    result=cursorr.fetchone()
    téléphone=result[0]
    return téléphone

def get_email():
    logfile=open("fichierlog.txt",'r')
    users=logfile.read().split("\n")
    username=users[-2]
    cursorr.execute("SELECT email from Etudiant where cne='"+username+"';")
    result=cursorr.fetchone()
    email=result[0]
    return email

def get_date_de_naissance():
    logfile=open("fichierlog.txt",'r')
    users=logfile.read().split("\n")
    username=users[-2]
    cursorr.execute("SELECT date_de_naissance from Etudiant where cne='"+username+"';")
    result=cursorr.fetchone()
    date_de_naissance=result[0]
    return date_de_naissance
def get_adress():
    logfile=open("fichierlog.txt",'r')
    users=logfile.read().split("\n")
    username=users[-2]
    cursorr.execute("SELECT id from Etudiant where cne='"+username+"';")
    id=cursorr.fetchone()
    cursorr1.execute("SELECT num, rue, ville from adress where id_Etud='"+id+"';")
    result =cursorr1.fetch()
    adress=result[0]+"-"+result[1]+"-"+result[2]
    return adress
    

def imporicon(path,size_tuple):
    icon=Image.open(path)
    icon=icon.resize(size_tuple, Image.ANTIALIAS)
    icon=ImageTk.PhotoImage(icon)
    return icon

def emploi():
    logfile=open("fichierlog.txt",'r')
    users=logfile.read().split("\n")
    username=users[-2]
    cursorr.execute("SELECT filiere from Etudiant where CIN='"+username+"';")
    result=cursorr.fetchone()
    filier=result[0]
    cursorr.execute("SELECT link from emploidutemps where filier='"+filier+"';")
    print(filier)
    url =cursorr.fetchone() 
    link=url[0]
    print(link)
    webbrowser.open_new_tab(link)
def support():
    messagebox.showinfo(title="SUPPORT", message="CONTACTER UN DES ADMINS :\n\n\nAFKIR MOHAMED \t email\n\n\nAKKOUH LOKMANE \t lokmaneakkouh10@gmail.com\n\n\n BEN TOUHAMI MOHAMED RIDA \t email")

#------------------------------------------partie SQL-------------------------------------------------------------------------------------------------------#

#------------------------connect to the database ETUDIANT------------------------------------    
database = mysql.connector.connect(host="127.0.0.1",
      user="root",
      password="lokamne-sql-12", 
      database="projet")
#------------------------create cursor---------------------------------------------
cursorr=database.cursor()
#------------------------connect to the database ADRESSE------------------------------------    
database = mysql.connector.connect(host="127.0.0.1",
      user="root",
      password="lokmane-sql-12", 
      database="projet")
#------------------------create cursor---------------------------------------------
cursorr1=database.cursor()

#-----------------------------import icons----------------------------------------

person_icon=imporicon(current_path+"\\icons\\person_icon1.png",(80,80))
person_button=Button(iconsbarr,text="PROFIL",image=person_icon,compound="top" ,font=("Louis George Cafe",20),padx=0,pady=0,relief="flat",bg="#15b4ea",activebackground="#15b4ea",fg="white",activeforeground="white",highlightcolor="white")
person_button.place(x=18,y=0)


school_icon=imporicon(current_path+"\\icons\\school.png",(80,80))
school_icon_button=Button(iconsbarr,image=school_icon,padx=0,pady=0,relief="flat",bg="#15b4ea",activebackground="#15b4ea",compound="top" ,font=("Louis George Cafe",20),text="text ici",fg="white",activeforeground="white")
school_icon_button.place(x=25,y=115)

paper=imporicon(current_path+"\\icons\\paper1.png",(70,70))
paper_button=Button(iconsbarr,bg="#15b4ea",padx=0,pady=0, relief="flat",image=paper,activebackground="#15b4ea",compound="top" ,font=("Louis George Cafe",20),text="text ici",fg="white",activeforeground="white")
paper_button.place(x=24,y=230)

book_icon=imporicon(current_path+"\\icons\\book.png",(70,70))
book_icon_button=Button(iconsbarr,bg="#15b4ea",padx=0,pady=0, relief="flat",image=book_icon,activebackground="#15b4ea",compound="top" ,font=("Louis George Cafe",18),text="COURS",fg="white",activeforeground="white")
book_icon_button.place(x=25,y=335)


agenda_icon=imporicon(current_path+"\\icons\\agenda.png",(60,60))
agenda_icon_button=Button(iconsbarr,bg="#15b4ea",padx=0,pady=0, relief="flat",command=emploi, image=agenda_icon,activebackground="#15b4ea",compound="top" ,font=("Louis George Cafe",15),text="EMPLOI DU \n DU TEMPS",fg="white",activeforeground="white")
agenda_icon_button.place(x=10,y=460)

support_icon=imporicon(current_path+"\\icons\\support.png",(70,70))
button=Button(iconsbarr,command=support,image=support_icon,padx=0,pady=0,relief="flat",bg="#15b4ea",activebackground="#15b4ea")
button.place(x=30,y=630)


#-------------------------------body----------------------------------------------------------------------------
# hello=Label(text="HELLO\t"+get_user_second_name(),font=("Arial",30),fg="#258EF5",bg="white")
# hello.place(x=700,y=30)
#------------------------------personal data frame------------------------------------------------------------------
body_frame=Frame(account,bg="#B5EFFF",width=1000,height=530,relief="flat")
body_frame.place(x=170,y=100)
#-------------------- personal picture import ----------------------------------------------------------
photo=imporicon(get_user_picture(),(200,200))
photo_label=Label(body_frame,image=photo)
photo_label.place(x=0,y=0)
#----------------------show other data ----------------------------------------------------------------------


firstName_label=Label(body_frame,text="NOM:",bg="#B5EFFF",fg="#0073e6",font=("Arila",20))
firstName_label.place(x=180,y=110)
firstName_label2=Label(body_frame,text=get_user_first_name(),bg="#B5EFFF",fg="white",font=("Arila",20))
firstName_label2.place(x=600,y=110)

second_Name_label=Label(body_frame,text="PRENOM:",bg="#B5EFFF",fg="#0073e6",font=("Arila",20))
second_Name_label.place(x=180,y=200)
second_Name_label2=Label(body_frame,text=get_user_second_name(),bg="#B5EFFF",fg="white",font=("Arila",20))
second_Name_label2.place(x=600,y=200)

CNE_label=Label(body_frame,text="CNE:",bg="#B5EFFF",fg="#0073e6",font=("Arila",20))
CNE_label.place(x=180,y=250)
CNE_label2=Label(body_frame,text=get_user_CNE(),bg="#B5EFFF",fg="white",font=("Arila",20))
CNE_label2.place(x=600,y=250)


CIN_label=Label(body_frame,text="CIN:",bg="#B5EFFF",fg="#0073e6",font=("Arila",20))
CIN_label.place(x=180,y=300)
CIN_label2=Label(body_frame,text=get_user_CIN(),bg="#B5EFFF",fg="white",font=("Arila",20))
CIN_label2.place(x=600,y=300)


filiere_label=Label(body_frame,text="FILIERE:",bg="#B5EFFF",fg="#0073e6",font=("Arila",20))
filiere_label.place(x=180,y=350)
filiere_label2=Label(body_frame,text=get_filiere(),bg="#B5EFFF",fg="white",font=("Arila",20))
filiere_label2.place(x=600,y=400)



EMAIL_label=Label(body_frame,text="EMAIL:",bg="#B5EFFF",fg="#0073e6",font=("Arila",20))
EMAIL_label.place(x=180,y=300)
EMAIL_label2=Label(body_frame,text=get_email(),bg="#B5EFFF",fg="white",font=("Arila",20))
EMAIL_label2.place(x=600,y=300)


TELEPHONE_label=Label(body_frame,text="TELEPHONE:",bg="#B5EFFF",fg="#0073e6",font=("Arila",20))
TELEPHONE_label.place(x=180,y=300)
TELEPHONE_label2=Label(body_frame,text=get_téléphone(),bg="#B5EFFF",fg="white",font=("Arila",20))
TELEPHONE_label2.place(x=600,y=300)


DATE_DE_NAISSANCE_label=Label(body_frame,text="DATE DE NAISSANCE:",bg="#B5EFFF",fg="#0073e6",font=("Arila",20))
DATE_DE_NAISSANCE_label.place(x=180,y=300)
DATE_DE_NAISSANCE_label2=Label(body_frame,text=get_date_de_naissance(),bg="#B5EFFF",fg="white",font=("Arila",20))
DATE_DE_NAISSANCE_label2.place(x=600,y=300)


ADRESSE_label=Label(body_frame,text="TELEPHONE:",bg="#B5EFFF",fg="#0073e6",font=("Arila",20))
ADRESSE_label.place(x=180,y=300)
ADRESSE_labe2=Label(body_frame,text=get_adress(),bg="#B5EFFF",fg="white",font=("Arila",20))
ADRESSE_labe2.place(x=600,y=300)

#---------------------------- masquer le mot de passe----------------------

def show_password(event):
    """Cette fonction est appelée lorsque l'utilisateur clique sur le Label du mot de passe."""
    password_label.config(show="")
    password_label.unbind("<Button-1>")
    password_label.bind("<Button-1>", hide_password)

def hide_password(event):
    """Cette fonction est appelée lorsque l'utilisateur clique à nouveau sur le Label du mot de passe."""
    password_label.config(show="*")
    password_label.unbind("<Button-1>")
    password_label.bind("<Button-1>", show_password)

# Création du champ de mot de passe sécurisé
password_label = Label(body_frame, text=get_password(), show="*", bg="#B5EFFF", fg="white", font=("Arial", 20))
password_label.place(x=600, y=300)

# Ajout d'un événement de clic au Label pour afficher/masquer le mot de passe
password_label.bind("<Button-1>", show_password)


MOT_DE_PASSE_label=Label(body_frame,text="MOT_DE_PASSE:",bg="#B5EFFF",fg="#0073e6",font=("Arila",20))
MOT_DE_PASSE_label.place(x=180,y=300)

#------------------modification button: go to script singUP1 of Rida----------------------------

#-----------subprocess-----------
def go_there():
    subprocess.run(["python", current_path+"\\singUp1"])

verify_button = account.Button(body_frame, text="Modifier!", bg="blue", fg="white", font=("Arial", 18), command=go_there())
verify_button.place(x=870, y=470)


#--------------------------leave button-------------------------------------------
leavebutton=Button(account,text="Quitter",command=account.quit,bg="#258EF5",fg="white",activebackground="#258EF5", activeforeground="white",font=("Arial",16),padx=0,pady=0, relief="flat")      #
leavebutton.place(x=1100, y=660)
#--------------------------logout button--------------------------------------------
logout=Button(account,text="Partir",command=log_out,bg="#258EF5",fg="white",activebackground="#258EF5", activeforeground="white",font=("Arial",16),padx=0,pady=0, relief="flat")      #
logout.place(x=180, y=660)
account.mainloop()



