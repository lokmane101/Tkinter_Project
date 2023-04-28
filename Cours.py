from tkinter import *
import mysql.connector 
import subprocess
from PIL import Image,ImageTk
import os
import webbrowser
from tkinter import messagebox

current_path=os.getcwd()
account=Tk()
account.title("LES COURS")
account.geometry("1200x720")
account.config(bg="white")
iconsbarr=Frame(account,width=150,height=1440,bg="#15b4ea",)
iconsbarr.place(x=0,y=0)
#------------------------------------------partie SQL-------------------------------------------------------------------------------------------------------#
#------------------------connect to the database------------------------------------    
database = mysql.connector.connect(host='localhost',
                                database='projet',
                                user='root',
                                password='root')
#------------------------create cursor---------------------------------------------
cursorr=database.cursor()
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
def log_out():
    account.destroy()
    subprocess.run(["python",current_path+"\\Luncher.py"])
def imporicon(path,size_tuple):
    icon=Image.open(path)
    icon=icon.resize(size_tuple, Image.ANTIALIAS)
    icon=ImageTk.PhotoImage(icon)
    return icon

def emploi():
    logfile=open("fichierlog.txt",'r')
    users=logfile.read().split("\n")
    username=users[-2]
    cursorr.execute("SELECT filière from Etudiant where CNE='"+username+"';")
    result=cursorr.fetchone()
    filier=result[0]
    cursorr.execute("SELECT link from emploidutemps where filier='"+filier+"';")
    print(filier)
    url =cursorr.fetchone() 
    link=url[0]
    print(link)
    webbrowser.open_new_tab(link)
def support():
    messagebox.showinfo(title="SUPPORT", message="CONTACTER UN DES ADMINS :\n\n\nAFKIR MOHAMED \t mohammedafk002@gmail.com\n\n\nAKKOUH LOKMANE \t lokmaneakkouh10@gmail.com\n\n\n BEN TOUHAMI MOHAMED RIDA \t bentouhamimohamedrida@gmail.com")


#-----------------------------import icons----------------------------------------

person_icon=imporicon(current_path+"\\icons\\person_icon1.png",(80,80))
person_button=Button(iconsbarr,text="PROFIL",command=person, image=person_icon,compound="top" ,font=("Louis George Cafe",20),padx=0,pady=0,relief="flat",bg="#15b4ea",activebackground="#15b4ea",fg="white",activeforeground="white",highlightcolor="white")
person_button.place(x=18,y=0)


school_icon=imporicon(current_path+"\\icons\\school.png",(80,80))
school_icon_button=Button(iconsbarr,image=school_icon,padx=0,pady=0, command=accueil,relief="flat",bg="#15b4ea",activebackground="#15b4ea",compound="top" ,font=("Louis George Cafe",20),text="ACCUEIL",fg="white",activeforeground="white")
school_icon_button.place(x=25,y=115)

paper=imporicon(current_path+"\\icons\\paper1.png",(70,70))
paper_button=Button(iconsbarr,bg="#15b4ea",padx=0,pady=0,command=description, relief="flat",image=paper,activebackground="#15b4ea",compound="top" ,font=("Louis George Cafe",20),text="Description",fg="white",activeforeground="white")
paper_button.place(x=24,y=230)

book_icon=imporicon(current_path+"\\icons\\book.png",(70,70))
book_icon_button=Button(iconsbarr,bg="#15b4ea",padx=0,pady=0,command=cours, relief="flat",image=book_icon,activebackground="#15b4ea",compound="top" ,font=("Louis George Cafe",18),text="COURS",fg="white",activeforeground="white")
book_icon_button.place(x=25,y=335)


agenda_icon=imporicon(current_path+"\\icons\\agenda.png",(60,60))
agenda_icon_button=Button(iconsbarr,bg="#15b4ea",padx=0,pady=0, relief="flat",command=emploi, image=agenda_icon,activebackground="#15b4ea",compound="top" ,font=("Louis George Cafe",15),text="EMPLOI DU \n DU TEMPS",fg="white",activeforeground="white")
agenda_icon_button.place(x=10,y=460)

support_icon=imporicon(current_path+"\\icons\\support.png",(70,70))
button=Button(iconsbarr,command=support,image=support_icon,padx=0,pady=0,relief="flat",bg="#15b4ea",activebackground="#15b4ea")
button.place(x=30,y=630)
#--------------------------leave button-------------------------------------------
leavebutton=Button(account,text="Quitter",command=account.quit,bg="#258EF5",fg="white",activebackground="#258EF5", activeforeground="white",font=("Arial",16),padx=0,pady=0, relief="flat")      #
leavebutton.place(x=1100, y=675)
#--------------------------logout button--------------------------------------------
logout=Button(account,text="Partir",command=log_out,bg="#258EF5",fg="white",activebackground="#258EF5", activeforeground="white",font=("Arial",16),padx=0,pady=0, relief="flat")      #
logout.place(x=180, y=675)
#----------------------Les cours----------------------------------


def username():
    logfile=open("fichierlog.txt",'r')
    users=logfile.read().split("\n")
    username=users[-2]
    return username
def cours_acces(i):
    cursorr.execute("SELECT filière from Etudiant where CNE='"+username()+"';")
    result=cursorr.fetchone()
    filiere=result[0]
    cursorr.execute("SELECT link from modules where filière='"+filiere+"';")
    url =cursorr.fetchall() 
    link=url[i][0]
    webbrowser.open_new_tab(link)

#----------------------Les cours----------------------------------

body_frame=Frame(account,bg="#B5EFFF", width=940,height=640,relief="flat")
body_frame.place(x=200,y=30)
cursorr.execute("SELECT filière from Etudiant where CNE='"+username()+"';")
result=cursorr.fetchone()
filiere=result[0]
cursorr.execute("select module from modules where filière = '"+filiere+"';")
re1=cursorr.fetchall()
cursorr.execute("select link from modules where filière = '"+filiere+"';")
re2=cursorr.fetchall()
re1 = [elem[0].replace('(', '').replace(')', '').replace(',', '') for elem in re1]
re2=[elem[0].replace('(', '').replace(')', '').replace(',', '') if elem[0] is not None else None for elem in re2]
dy=20
for i in range(0, len(re1)):
    if re2[i] is None or re2[i].lower() == 'none':
        l1=Label(body_frame,text=str(re1[i])+": ",bg="#B5EFFF",fg="#0073e6",font=("Arila",20))
        l1.place(x=40,y=dy) 
        l2=Label(body_frame, text='Pas de cours',bg="#B5EFFF",fg="#BC5294",font=("Arila",20))
        l2.place(x=735,y=dy)
    else:
        l1=Label(body_frame,text=re1[i]+": ",bg="#B5EFFF",fg="#0073e6",font=("Arila",20))
        l1.place(x=40,y=dy)
        cours_lien=Button(body_frame,bg="#15b4ea",padx=0,pady=0, relief="flat",command=lambda i=i:cours_acces(i),activebackground="#15b4ea",compound="top" ,font=("Louis George Cafe",15),text="Clique ici",fg="#F9F871",activeforeground="white")
        cours_lien.place(x=735,y=dy)
    dy=dy+47



account.mainloop()


