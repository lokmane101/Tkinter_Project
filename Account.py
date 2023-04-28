from tkinter import *
import mysql.connector 
import subprocess
from io import BytesIO
from PIL import Image,ImageTk
import os
import webbrowser
def emploi():
    url = 'https://drive.google.com/file/d/1Nz6Mu8ZliD2G_Hn4mM5zV0aJuBbOOar5/view?usp=sharing'
    webbrowser.open_new_tab(url)
current_path=os.getcwd()
account=Tk()
account.geometry("1200x720")
account.config(bg="white")
iconsbarr=Frame(account,width=155,height=1440,bg="#15b4ea",)
iconsbarr.place(x=0,y=0)

def personel():
    personel=Tk()
    personel.geometry=("1200x720")
    personel.config(bg="white")
def get_username():
    logfile=open("fichierlog.txt",'r')
    users=logfile.read().split("\n")
    username=users[-2]
    cursorr.execute("SELECT nom from Etudiant where Cne='"+username+"';")
    result=cursorr.fetchall()
    return result[0][0]
def get_user_second_name():
    logfile=open("fichierlog.txt",'r')
    users=logfile.read().split("\n")
    username=users[-2]
    cursorr.execute("SELECT prenom from Etudiant where Cne='"+username+"';")
    result=cursorr.fetchall()
    return result[0][0]
def log_out():
    account.destroy()
    subprocess.run(["python",current_path+"\\Luncher.py"])
def get_user_first_name():
    logfile=open("fichierlog.txt",'r')
    users=logfile.read().split("\n")
    username=users[-2]
    print(username)
    cursorr.execute("SELECT nom from Etudiant where Cne='"+username+"';")
    result=cursorr.fetchall()
    return result[0][0]
def get_filiere():
    logfile=open("fichierlog.txt",'r')
    users=logfile.read().split("\n")
    username=users[-2]
    cursorr.execute("SELECT filière from Etudiant where Cne='"+username+"';")
    result=cursorr.fetchall()
    return result[0][0]

def get_user_picture():
    logfile=open("fichierlog.txt",'r')
    users=logfile.read().split("\n")
    username=users[-2]
    print(username)
    cursorr.execute("SELECT image from Etudiant where Cne='"+username+"';")
    result=cursorr.fetchall()
    photo_in_byte=result[0][0]
    picture=imporicon(BytesIO(photo_in_byte),(200,200))
    return picture

def get_user_CNE():
    logfile=open("fichierlog.txt",'r')
    users=logfile.read().split("\n")
    username=users[-2]
    cursorr.execute("SELECT CNE from Etudiant where Cne='"+username+"';")
    result=cursorr.fetchall()
    cne=result[0][0]
    return cne

def get_user_CIN():
    logfile=open("fichierlog.txt",'r')
    users=logfile.read().split("\n")
    username=users[-2]
    cursorr.execute("SELECT CIN from Etudiant where Cne='"+username+"';")
    result=cursorr.fetchall()
    cin=result[0][0]
    return cin

def imporicon(path,size_tuple):
    icon=Image.open(path)
    icon=icon.resize(size_tuple, Image.ANTIALIAS)
    icon=ImageTk.PhotoImage(icon)
    return icon

#--------------subprocesses-------------------------------------
def person():
    account.destroy()
    subprocess.run(["python", current_path+"\\info_pers.py"])
def description():
    account.destroy()
    subprocess.run(["python", current_path+"\\Description_filière.py"])
def accueil():
    account.destroy()
    subprocess.run(["python", current_path+"\\Account.py"])
def cours():
    account.destroy()
    subprocess.run(["python", current_path+"\\Cours.py"])


#------------------------------------------partie SQL-------------------------------------------------------------------------------------------------------#

#------------------------connect to the database------------------------------------    
database = mysql.connector.connect(host='localhost',
                                database='projet',
                                user='root',
                                password='root')
#------------------------create cursor---------------------------------------------
cursorr=database.cursor()

#-----------------------------import icons----------------------------------------

person_icon=imporicon(current_path+"\\icons\\person_icon1.png",(80,80))
person_button=Button(iconsbarr,text="PROFIL",image=person_icon,command=person,compound="top" ,font=("Louis George Cafe",20),padx=0,pady=0,relief="flat",bg="#15b4ea",activebackground="#15b4ea",fg="white",activeforeground="white",highlightcolor="white")
person_button.place(x=18,y=0)


school_icon=imporicon(current_path+"\\icons\\school.png",(80,80))
school_icon_button=Button(iconsbarr,image=school_icon,padx=0,pady=0,command=accueil,relief="flat",bg="#15b4ea",activebackground="#15b4ea",compound="top" ,font=("Louis George Cafe",20),text="ACCUEIL",fg="white",activeforeground="white")
school_icon_button.place(x=10,y=115)

paper=imporicon(current_path+"\\icons\\paper1.png",(70,70))
paper_button=Button(iconsbarr,bg="#15b4ea",padx=0,pady=0, relief="flat",command=description,image=paper,activebackground="#15b4ea",compound="top" ,font=("Louis George Cafe",20),text="DESCRIPT°",fg="white",activeforeground="white")
paper_button.place(x=0,y=230)

book_icon=imporicon(current_path+"\\icons\\book.png",(70,70))
book_icon_button=Button(iconsbarr,bg="#15b4ea",padx=0,pady=0, relief="flat",command=cours,image=book_icon,activebackground="#15b4ea",compound="top" ,font=("Louis George Cafe",18),text="COURS",fg="white",activeforeground="white")
book_icon_button.place(x=25,y=335)


agenda_icon=imporicon(current_path+"\\icons\\agenda.png",(60,60))
agenda_icon_button=Button(iconsbarr,bg="#15b4ea",padx=0,pady=0, relief="flat",command=emploi, image=agenda_icon,activebackground="#15b4ea",compound="top" ,font=("Louis George Cafe",15),text="EMPLOI DU \n DU TEMPS",fg="white",activeforeground="white")
agenda_icon_button.place(x=10,y=460)

support_icon=imporicon(current_path+"\\icons\\support.png",(70,70))
button=Button(iconsbarr,image=support_icon,padx=0,pady=0,relief="flat",bg="#15b4ea",activebackground="#15b4ea")
button.place(x=30,y=630)


#-------------------------------body----------------------------------------------------------------------------
# hello=Label(text="HELLO\t"+get_user_second_name(),font=("Arial",30),fg="#258EF5",bg="white")
# hello.place(x=700,y=30)
#------------------------------personal data frame------------------------------------------------------------------
body_frame=Frame(account,bg="#B5EFFF",width=1000,height=530,relief="flat")
body_frame.place(x=240,y=100)
#-------------------- personal picture import ----------------------------------------------------------
photo=get_user_picture()
photo_label=Label(body_frame,image=photo)
photo_label.place(x=0,y=0)
#----------------------show other data ----------------------------------------------------------------------
username_label=Label(body_frame,text="NOM D'UTILISATEUR:",bg="#B5EFFF",fg="#0073e6",font=("Arila",35))
username_label.place(x=220,y=0)
username_label2=Label(body_frame,text=get_username(),bg="#B5EFFF",fg="white",font=("Arila",35))
username_label2.place(x=700,y=50)

firstName_label=Label(body_frame,text="NOM:",bg="#B5EFFF",fg="#0073e6",font=("Arila",35))
firstName_label.place(x=220,y=100)
firstName_label2=Label(body_frame,text=get_user_first_name(),bg="#B5EFFF",fg="white",font=("Arila",35))
firstName_label2.place(x=700,y=150)

second_Name_label=Label(body_frame,text="PRENOM:",bg="#B5EFFF",fg="#0073e6",font=("Arila",35))
second_Name_label.place(x=220,y=200)
second_Name_label2=Label(body_frame,text=get_user_second_name(),bg="#B5EFFF",fg="white",font=("Arila",35))
second_Name_label2.place(x=700,y=250)

CNE_label=Label(body_frame,text="CNE:",bg="#B5EFFF",fg="#0073e6",font=("Arila",35))
CNE_label.place(x=220,y=300)
CNE_label2=Label(body_frame,text=get_user_CNE(),bg="#B5EFFF",fg="white",font=("Arila",35))
CNE_label2.place(x=700,y=350)

filier_label=Label(body_frame,text="FILIERE:",bg="#B5EFFF",fg="#0073e6",font=("Arila",35))
filier_label.place(x=220,y=400)
filier_label2=Label(body_frame,text=get_filiere(),bg="#B5EFFF",fg="white",font=("Arila",35))
filier_label2.place(x=700,y=450)

#--------------------------leave button-------------------------------------------
leavebutton=Button(account,text="Quitter",command=account.quit,bg="#258EF5",fg="white",activebackground="#258EF5", activeforeground="white",font=("Arial",16),padx=0,pady=0, relief="flat")      #
leavebutton.place(x=1200, y=660)
#--------------------------logout button--------------------------------------------
logout=Button(account,text="Partir",command=log_out,bg="#258EF5",fg="white",activebackground="#258EF5", activeforeground="white",font=("Arial",16),padx=0,pady=0, relief="flat")      #
logout.place(x=280, y=660)
account.mainloop()