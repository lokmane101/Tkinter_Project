from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageTk
import subprocess
from dataBase import DataBase

#------------button qui retour en arrière-------------#
def go_back():
        window.destroy()
        subprocess.run(["python",r"c:/Users/us/Desktop/Tkinter_Project/signIn2.py"])

#----pour button valider-----

def valider():
        if generate_err():
                print("apply insertion function......")
                db.insert_data_sign_in_phase3(field_username.get(),passwd_field.get(),section_field.get())
                print("hello importaion des donnnées......")
                print(db.getrow())
                print("enregistrement.....")
                db.valide()
                print("saved")
                window.quit()
#____________________________creation of same util function__________________________________________#


#--------------------create icon---------------------#
def create_icon(icon_path,tuple_size):
        image=Image.open(icon_path)
        image=image.resize(tuple_size,Image.ANTIALIAS)
        icon_image=ImageTk.PhotoImage(image)
        return icon_image




#---------fonction pour lagestion d'erreur------------#
def generate_err():
        ok=True
        if field_username.get()=="":
                Label(window,text="****svp entrer votre username'",fg="red",bg="white").place(x=x_username_entry+350,y=y_username_entry+40)
                ok=False
        else:
                Label(window,text="****svp entrer votre username",fg="white",bg="white").place(x=x_username_entry+350,y=y_username_entry+40)
                
        if passwd_field.get()=="":
                Label(window,text="****svp entrer votre password'",fg="red",bg="white").place(x=x_username_entry+350,y=y_username_entry+200-10)
                ok=False
        else:
                Label(window,text="****svp entrer votre password'",fg="white",bg="white").place(x=x_username_entry+350,y=y_username_entry+200-10)
                
        if section_field.get()=="":
                Label(window,text="****svp entrer votre section'",fg="red",bg="white").place(x=x_username_entry+350,y=y_username_entry+300+40)
                ok=False
        
        else:
                Label(window,text="****svp entrer votre section",fg="white",bg="white").place(x=x_username_entry+350,y=y_username_entry+300+40)
        return ok
                 


#________________________________varaibel a utiliser___________________________________#

x_username_entry=300+100+100
y_username_entry=150

x_username_Label=400+100+100
y_username_Label=100

x_username_icon=350+100+100
y_username_icon=90

x_username_etoile=600+100+100
y_username_etoile=100


icon_size=50


#_____________________________________________creation de la fenêtre_________________________________________________#
window=Tk()
window.geometry("1200x720")
window.config(bg="white")



#-----------------se connecter tout d'abord à la base de donnée------------------#
db= DataBase()



#______________________________________________create the username widget______________________________________#


                

#--------------association of icon picture to the Entry-------------------#

username_icon=create_icon("icons/username_icon.jpg",(45,45))

image_label=Label(window, image=username_icon,padx=0,pady=0,relief="flat")
image_label.place(x=x_username_icon-15,y=y_username_icon)
image_label.config(highlightthickness=0,bd=0)



#-----enter the Entry name field------#
name_txt=StringVar()

field_username=Entry(window, textvariable=name_txt, width=45,bd=0,font=("Arial",15),highlightcolor="#05bcfa",highlightthickness=3,highlightbackground='white',bg="#e1f3ff")
field_username.place(x=x_username_entry,y=y_username_entry)


#-----enter the name Label------#
username=Label(window,text="Entrer votre username : ",fg="black",font=("Helvetica",15,"bold"),bg="white" ,highlightthickness=0)
username.place(x=x_username_Label-10,y=y_username_Label)

necessary_point=Label (window, text="*", fg="red",font=("Arial",15),bg="white" ,highlightthickness=0)
necessary_point.place(x=x_username_etoile+20,y=y_username_etoile)



#_______________________________________________________create the password widget __________________________________________________________#


                                                #----passwd Label-----#
passwd_Label=Label(window,text="Enter Votre mot de passe :",font=("Helvetica",15,"bold"),bg="white")
passwd_Label.place(x=x_username_Label-10,y=y_username_Label+120+30)



#--------creation de l'etoile---------#

passwd_etoile=Label(window, text="*", font=("Arial",15),fg="red",bg="white")
passwd_etoile.place(x=x_username_etoile+50,y=y_username_etoile+120+30)


#---------creation du l'icon
passwd_icon=create_icon("icons/passwd_icon.jpg",(45,45))
image_label=Label(window, image=passwd_icon,padx=0,pady=0,relief="flat",bg="white")
image_label.place(x=x_username_icon-20,y=y_username_icon+120+30)
image_label.config(highlightthickness=0)

passwd_txt=StringVar()
passwd_field=Entry(window, textvariable=passwd_txt,bd=0,width=45,font=("Arial",15),highlightcolor="#05bcfa",highlightthickness=3,highlightbackground='white',bg="#e1f3ff")
passwd_field.place(x=x_username_entry,y=y_username_entry+120+30)



# ________________________________________creation du champ section___________________________________________________#

    
    
#--------------creation du label-------------------#
section_Label=Label(window, text="Entrer votre section :",font=("Halvetica",15,"bold"),bg="white")
section_Label.place(x=x_username_Label,y=y_username_Label+300)



#--------------creation du entry of section------------#

section_txt=StringVar()
section_field=Entry(window,textvariable=section_txt,font=("Avial",15), width=45,bd=0,highlightcolor="#05bcfa",highlightthickness=3,highlightbackground='white',bg="#e1f3ff")
section_field.place(x=x_username_entry,y=y_username_entry+300)

#------------creation de l'étoile--------------#
section_etoile=Label(window, text="*",font=("Halvetica",15,"bold"),fg="red",bg="white")
section_etoile.place(x=x_username_etoile+5,y=y_username_etoile+300)

#---------------craetion de l'icon ----------#
section_icon=create_icon("icons/section_icon.png",(icon_size-10,icon_size-10))
icon_label=Label(window,image=section_icon,bd=0,bg="white")
icon_label.place(x=x_username_icon,y=y_username_icon+306)







#______________________________________________________creation d'un frame/background___________________________________________________#



frame_title =Frame(window,bg="white" )
frame_title.place(x=290,y=0,width=3500,height=60)

frame=Frame(window,bg="blue")
frame.place(x=0,y=0,width=290+100,height=7000)


school_image=create_icon("icons/school1.jpg",(300+100,740))
picture_label=Label(frame,image=school_image)
picture_label.pack()

#--------creation du titre--------#


espace_etudiant=Label(frame_title,text="ESPACE      ETUDIANT", font=("LEMONMILK-Medium",40),bg="white")
espace_etudiant.place(x=150,y=5)



#___________________________________________creation des button_________________________________________#


#----------creation du boutton valider-----------#
button_valider=Button(window, text="valider",fg="white",bg="#258EF5",width=20,activebackground="#15b4ea",activeforeground="blue",font=("Avial",10,"bold"),command=valider)
button_valider.place(x=1000,y=680)

#-----------creartion du button go back----------#
# go_back_icon=create_icon("icons/go_back.jpg",(45,15))
go_back_button=Button(window, text="Précedent",width=20,foreground="white" ,compound="left",bg="#258EF5",font=("Avial",10,"bold"),activebackground="#15b4ea",activeforeground="blue",command=go_back)
go_back_button.place(x=300+100,y=680)

window.mainloop()