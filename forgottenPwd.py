from tkinter import *
from PIL import Image,ImageTk

f_Pwd=Tk()
f_Pwd.geometry("700x500")


frame = Frame(f_Pwd, width=600, height=400,relief="ridge")
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

#----------------------------------------------import icons---------------------------------------------------#
width = 20
height = 20


person_icon=Image.open("C:\\Users\\lokmane\\Desktop\\Tkinter_project\\person_icon.png")
person_icon=person_icon.resize((width, height), Image.ANTIALIAS)
school_icon=Image.open("C:\\Users\\lokmane\\Desktop\\Tkinter_project\\school.png")
school_icon=school_icon.resize((width, height), Image.ANTIALIAS)
lock_icon=Image.open("C:\\Users\\lokmane\\Desktop\\Tkinter_project\\lock_icon.png")
lock_icon=lock_icon.resize((width, height), Image.ANTIALIAS)

person_icon=ImageTk.PhotoImage(person_icon)
school_icon=ImageTk.PhotoImage(school_icon)
lock_icon=ImageTk.PhotoImage(lock_icon)


#-------------------nom label and entry filed-------------------------------

nom=Label(f_Pwd,text="nom:",image=person_icon, compound="left")
nom.place(x=300,y=190)

nom_field=Entry(f_Pwd)
nom_field.place(x=300,y=220)

#-------------------prenom label and entry filed-------------------------------

prenom=Label(f_Pwd,text="prenom:",image=person_icon, compound="left")
prenom.place(x=300,y=140)

prenom_field=Entry(f_Pwd)
prenom_field.place(x=300,y=170)

#-------------------CIN label and entry filed-------------------------------

Numro_tele=Label(f_Pwd,text="CIN",image=school_icon, compound="left")
Numro_tele.place(x=300,y=90)

Numro_tele_field=Entry(f_Pwd)
Numro_tele_field.place(x=300,y=120)
#-------------------CNE label and entry filed-------------------------------


email =Label(f_Pwd,text="CNE:",image=school_icon, compound="left")
email.place(x=300,y=40)

email_field=Entry(f_Pwd)
email_field.place(x=300,y=70)



#-------------------mot de passe label and entry filed-------------------------------

MotDePass=Label(f_Pwd,text="Neauvou Mot de passe:",image=lock_icon, compound="left")
MotDePass.place(x=300,y=240)

MotDePass_field=Entry(f_Pwd)
MotDePass_field.place(x=300,y=270)

#-------------------confirm mot de passe label and entry filed-------------------------------

confirm_pwd=Label(f_Pwd,text="confirmer votre mot de passe:",image=lock_icon, compound="left")
confirm_pwd.place(x=300,y=290)

confirm_pwd_field=Entry(f_Pwd)
confirm_pwd_field.place(x=300,y=320)


#-------------------check de verification-----------------------

je_suis_sure=IntVar()
sure=Checkbutton(f_Pwd,text="j'ai rivisé tput les information et je prend la responsabilité de toute defaut possible",variable=je_suis_sure)
sure.place(x=150,y=350)



#-------------------confirm button------------------------------

confirm_button=Button(f_Pwd,text="confirm",bg="#258EF5",fg="white",activebackground="#258EF5", activeforeground="white",font=("Arial",16),padx=0,pady=0, relief="flat")
confirm_button.place(x=320,y=380)


#-------------------leave button -------------------------------

leave_button=Button(f_Pwd,text="leave",command=f_Pwd.quit,bg="#258EF5",fg="white",activebackground="#258EF5", activeforeground="white",font=("Arial",12),padx=0,pady=0, relief="flat")
leave_button.place(x=600,y=450)

f_Pwd.mainloop()