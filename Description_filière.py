from tkinter import *
from PIL import Image,ImageTk
from os import *
from dataBase import DataBase
import subprocess


#------------------------focntions utiles----------------------#
def imporicon(path,icon_size):
    icon=Image.open(path)
    icon=icon.resize(icon_size)
    icon=ImageTk.PhotoImage(icon)
    return icon
def go_to_personel():
    account.destroy()
    subprocess.run(["python",current_path+"\\info_pers.py"])

def go_to_accueil():
    account.destroy()
    subprocess.run(["python",current_path+"\\Account.py"])


#-----------------variables a utiliser----------------------------------------#
current_path=getcwd()
db=DataBase()



#_____________________________________________creation de la fenêtre_________________________________________________#
account=Tk()
account.geometry("1200x720")
account.config(bg="white")






#______________________________creation du frame des icons_______________________________________#
iconsbarr=Frame(account,width=150,height=1440,bg="#15b4ea")
iconsbarr.place(x=0,y=0)

#-----------------------------import icons----------------------------------------

person_icon=imporicon(current_path+"\\icons\\person_icon1.png",(80,80))
person_button=Button(iconsbarr,text="PROFIL",image=person_icon,compound="top" ,font=("Louis George Cafe",20),padx=0,pady=0,relief="flat",bg="#15b4ea",activebackground="#15b4ea",fg="white",activeforeground="white",highlightcolor="white",command=go_to_personel)
person_button.place(x=18,y=0)


school_icon=imporicon(current_path+"\\icons\\school.png",(80,80))
school_icon_button=Button(iconsbarr,image=school_icon,padx=0,pady=0,relief="flat",bg="#15b4ea",activebackground="#15b4ea",compound="top" ,font=("Louis George Cafe",20),text="text ici",fg="white",activeforeground="white",command=go_to_accueil)
school_icon_button.place(x=25,y=115)

paper=imporicon(current_path+"\\icons\\paper1.png",(70,70))
paper_button=Button(iconsbarr,bg="#15b4ea",padx=0,pady=0, relief="flat",image=paper,activebackground="#15b4ea",compound="top" ,font=("Louis George Cafe",20),text="text ici",fg="white",activeforeground="white")
paper_button.place(x=24,y=230)

book_icon=imporicon(current_path+"\\icons\\book.png",(70,70))
book_icon_button=Button(iconsbarr,bg="#15b4ea",padx=0,pady=0, relief="flat",image=book_icon,activebackground="#15b4ea",compound="top" ,font=("Louis George Cafe",18),text="COURS",fg="white",activeforeground="white")
book_icon_button.place(x=25,y=335)


agenda_icon=imporicon(current_path+"\\icons\\agenda.png",(60,60))
agenda_icon_button=Button(iconsbarr,bg="#15b4ea",padx=0,pady=0, relief="flat", image=agenda_icon,activebackground="#15b4ea",compound="top" ,font=("Louis George Cafe",15),text="EMPLOI DU \n DU TEMPS",fg="white",activeforeground="white")
agenda_icon_button.place(x=10,y=460)

support_icon=imporicon(current_path+"\\icons\\support.png",(70,70))
button=Button(iconsbarr,image=support_icon,padx=0,pady=0,relief="flat",bg="#15b4ea",activebackground="#15b4ea")
button.place(x=30,y=630)
#-------------frame (Nom filière et nom d'étudiant)-------------- 

Student_frame=Frame(account,bg="#5CECAE")
Student_frame.place(x=220,y=10, height=150,width=1100)


nom,prenom,filière=db.getStudent()

Student_fil=Label(Student_frame,text=filière,font=("LEMONMILK-Medium",50),fg="white",bg="#5CECAE")
Student_fil.place(x=170,y=25)

Student_nom_prenom=Label(Student_frame,text="Mr(s)."+nom+" "+prenom,font=("LEMONMILK-Medium",15),fg="white",bg="#5CECAE")
Student_nom_prenom.place(x=780,y=120)

#-------------------frame (des professeurs)---------------------

modules_frame=Frame(account,bg="#5CECAE" )
modules_frame.place(x=160,y=180, height=550,width=1200)

# def create_listBox()
modules_profs=db.get_Modules_Profs()
print(modules_profs)
dx=10
dy=5
l_listbox=[]
l_button=[]


def show_listbox(index):
    if l_listbox[index].winfo_ismapped():
        l_listbox[index].place_forget()
    else:
        l_listbox[index].place(x=l_button[index]["dx"]-10,y=l_button[index]["dy"]+45)

#-----------creation des listes boxes----------------#
for module,prof in modules_profs:
    listbox=Listbox(modules_frame,width=30,height=6,relief="flat")
    listbox.insert(END,"                  Titre: ")
    if "/" in module: 
        module=module.split("/")
        listbox.insert(END,module[0])
        listbox.insert(END,module[1])
        
    if "&" in module: 
        module=module.split("&")
        listbox.insert(END,module[0])
        listbox.insert(END,module[1])

    elif " et " in module:
        module=module.split(" et ")
        listbox.insert(END,module[0])
        listbox.insert(END,module[1])
    else:
        listbox.insert(END,module)

    listbox.configure(fg="white",bg="#3C8E82",font=("LEMONMILK-Medium",12,"bold"),bd=3)

    listbox.insert(END," ")
    listbox.insert(END,"              Enseignant(e):")
    listbox.insert(END,prof)

    l_listbox.append(listbox)

    

#-----------creation des boutton-----------------------------#
for index in range(len(modules_profs)):
    button=Button(modules_frame,relief="flat",text=f"module{index+1}",width=20,height=2,command=lambda index=index: show_listbox(index),bg="#15b4ea",fg="#F9F871",font=("LEMONMILK-Medium",9,"bold"))
    if index+1==13:
        button.place(x=dx,y=dy-30)
        l_button.append({"button":button,"dx":dx,"dy":dy-30})
    else:
        l_button.append({"button":button,"dx":dx,"dy":dy})
        button.place(x=dx,y=dy)
    dx+=200   
    if len(l_button)%6==0:
        dx=10
        dy+=210
    







account.mainloop()