from tkinter import *
import mysql.connector 
import subprocess
from PIL import Image,ImageTk
account=Tk()
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
    subprocess.run(["python","C:\\Users\\lokmane\\Desktop\\Tkinter_project\\Luncher.py"])
def get_user_first_name():
    logfile=open("fichierlog.txt",'r')
    users=logfile.read().split("\n")
    username=users[-2]
    cursorr.execute("SELECT nom from Etudiant where CIN='"+username+"';")
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

def get_user_CIN():
    logfile=open("fichierlog.txt",'r')
    users=logfile.read().split("\n")
    username=users[-2]
    cursorr.execute("SELECT CIN from Etudiant where CIN='"+username+"';")
    result=cursorr.fetchone()
    cin=result[0]
    return cin

def imporicon(path,size_tuple):
    icon=Image.open(path)
    icon=icon.resize(size_tuple, Image.ANTIALIAS)
    icon=ImageTk.PhotoImage(icon)
    return icon

#------------------------------------------partie SQL-------------------------------------------------------------------------------------------------------#

#------------------------connect to the database------------------------------------    
database = mysql.connector.connect(host='localhost',
                                database='projet',
                                user='root',
                                password='lokmane-SQL-12')
#------------------------create cursor---------------------------------------------
cursorr=database.cursor()

#-----------------------------import icons----------------------------------------

person_icon=imporicon("C:\\Users\\lokmane\\Desktop\\Tkinter_project\\icons\\person_icon1.png",(110,110))
person_button=Button(iconsbarr,image=person_icon,padx=0,pady=0,relief="flat",bg="#15b4ea",activebackground="#15b4ea")
person_button.place(x=18,y=30)


school_icon=imporicon("C:\\Users\\lokmane\\Desktop\\Tkinter_project\\icons\\school.png",(90,90))
school_icon_button=Button(iconsbarr,image=school_icon,padx=0,pady=0,relief="flat",bg="#15b4ea",activebackground="#15b4ea")
school_icon_button.place(x=25,y=140)

paper=imporicon("C:\\Users\\lokmane\\Desktop\\Tkinter_project\\icons\\paper1.png",(80,80))
paper_button=Button(iconsbarr,bg="#15b4ea",padx=0,pady=0, relief="flat",image=paper,activebackground="#15b4ea")
paper_button.place(x=30,y=250)

book_icon=imporicon("C:\\Users\\lokmane\\Desktop\\Tkinter_project\\icons\\book.png",(90,90))
book_icon_button=Button(iconsbarr,bg="#15b4ea",padx=0,pady=0, relief="flat",image=book_icon,activebackground="#15b4ea")
book_icon_button.place(x=20,y=350)


agenda_icon=imporicon("C:\\Users\\lokmane\\Desktop\\Tkinter_project\\icons\\agenda.png",(70,70))
agenda_icon_button=Button(iconsbarr,bg="#15b4ea",padx=0,pady=0, relief="flat",image=agenda_icon,activebackground="#15b4ea")
agenda_icon_button.place(x=35,y=460)

support_icon=imporicon("C:\\Users\\lokmane\\Desktop\\Tkinter_project\\icons\\support.png",(70,70))
button=Button(iconsbarr,image=support_icon,padx=0,pady=0,relief="flat",bg="#15b4ea",activebackground="#15b4ea")
button.place(x=30,y=630)


#-------------------------------body----------------------------------------------------------------------------
hello=Label(text="HELLO\t"+get_user_second_name(),font=("Arial",30),fg="#258EF5",bg="white")
hello.place(x=500,y=30)
#------------------------------personal data frame------------------------------------------------------------------
body_frame=Frame(account,bg="#B5EFFF",width=1000,height=530,relief="flat")
body_frame.place(x=170,y=100)
#-------------------- personal picture import ----------------------------------------------------------
photo=imporicon(get_user_picture(),(200,200))
photo_label=Label(body_frame,image=photo)
photo_label.place(x=0,y=0)
#----------------------show other data ----------------------------------------------------------------------
CIN_label=Label(body_frame,text="CIN:",bg="#B5EFFF",fg="black",font=("Arila",35))
CIN_label.place(x=220,y=240)
CIN_label2=Label(body_frame,text=get_user_CIN(),bg="#B5EFFF",fg="black",font=("Arila",35))
CIN_label2.place(x=500,y=240)

CNE_label=Label(body_frame,text="CNE:",bg="#B5EFFF",fg="black",font=("Arila",35))
CNE_label.place(x=220,y=310)
CNE_label2=Label(body_frame,text=get_user_CNE(),bg="#B5EFFF",fg="black",font=("Arila",35))
CNE_label2.place(x=500,y=310)

firstName_label=Label(body_frame,text="NOM:",bg="#B5EFFF",fg="black",font=("Arila",35))
firstName_label.place(x=220,y=380)
firstName_label2=Label(body_frame,text=get_user_first_name(),bg="#B5EFFF",fg="black",font=("Arila",35))
firstName_label2.place(x=500,y=380)

second_Name_label=Label(body_frame,text="PRENOM:",bg="#B5EFFF",fg="black",font=("Arila",35))
second_Name_label.place(x=220,y=450)
second_Name_label2=Label(body_frame,text=get_user_second_name(),bg="#B5EFFF",fg="black",font=("Arila",35))
second_Name_label2.place(x=500,y=450)

#--------------------------leave button-------------------------------------------
leavebutton=Button(account,text="Quitter",command=account.quit,bg="#258EF5",fg="white",activebackground="#258EF5", activeforeground="white",font=("Arial",16),padx=0,pady=0, relief="flat")      #
leavebutton.place(x=1100, y=660)
#--------------------------logout button--------------------------------------------
logout=Button(account,text="log out",command=log_out,bg="#258EF5",fg="white",activebackground="#258EF5", activeforeground="white",font=("Arial",16),padx=0,pady=0, relief="flat")      #
logout.place(x=180, y=660)
account.mainloop()