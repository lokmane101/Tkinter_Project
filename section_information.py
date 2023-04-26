from tkinter import *
from PIL import Image,ImageTk
from os import *


#------------------------focntions utiles----------------------#
def imporicon(path,icon_size):
    icon=Image.open(path)
    icon=icon.resize(icon_size)
    icon=ImageTk.PhotoImage(icon)
    return icon

#-----------------variables a utiliser----------------------------------------#
current_path=getcwd()





#_____________________________________________creation de la fenêtre_________________________________________________#
account=Tk()
account.geometry("1200x720")
account.config(bg="white")






#______________________________creation du frame des icons_______________________________________#
iconsbarr=Frame(account,width=150,height=1440,bg="#15b4ea")
iconsbarr.place(x=0,y=0)

#-----------------------------import icons----------------------------------------

person_icon=imporicon(current_path+"\\icons\\person_icon1.png",(80,80))
person_button=Button(iconsbarr,text="PROFIL",image=person_icon,compound="top" ,font=("Louis George Cafe",20),padx=0,pady=0,relief="flat",bg="#15b4ea",activebackground="#15b4ea",fg="white",activeforeground="white",highlightcolor="white")
person_button.place(x=18,y=0)


school_icon=imporicon(current_path+"\\icons\\school.png",(80,80))
school_icon_button=Button(iconsbarr,image=school_icon,padx=0,pady=0,relief="flat",bg="#15b4ea",activebackground="#15b4ea",compound="top" ,font=("Louis George Cafe",20),text="text ici",fg="white",activeforeground="white")
school_icon_button.place(x=25,y=115)

paper=imporicon(current_path+"\\icons\\paper1.png",(70,70))
paper_button=Button(iconsbarr,bg="#15b4ea",padx=0,pady=0, relief="flat",image=paper,activebackground="red",compound="top" ,font=("Louis George Cafe",20),text="text ici",fg="white",activeforeground="green")
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


account.mainloop()