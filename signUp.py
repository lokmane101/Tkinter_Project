from tkinter import *
from PIL import Image,ImageTk
window=Tk()

# Define the geometry of the window
window.geometry("700x500")

frame = Frame(window, width=600, height=400,relief="ridge")
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

#----------------------------------------------import icons---------------------------------------------------#
width = 20
height = 20

email_icon=Image.open("C:\\Users\\lokmane\\Desktop\\Tkinter_project\\email_icon.png")
email_icon = email_icon.resize((width, height), Image.ANTIALIAS)
person_icon=Image.open("C:\\Users\\lokmane\\Desktop\\Tkinter_project\\person_icon.png")
person_icon=person_icon.resize((width, height), Image.ANTIALIAS)
phone_icon=Image.open("C:\\Users\\lokmane\\Desktop\\Tkinter_project\\phone_icon.png")
phone_icon=phone_icon.resize((width, height), Image.ANTIALIAS)
lock_icon=Image.open("C:\\Users\\lokmane\\Desktop\\Tkinter_project\\lock_icon.png")
lock_icon=lock_icon.resize((width, height), Image.ANTIALIAS)
email_icon=ImageTk.PhotoImage(email_icon)
person_icon=ImageTk.PhotoImage(person_icon)
phone_icon=ImageTk.PhotoImage(phone_icon)
lock_icon=ImageTk.PhotoImage(lock_icon)
#-------------------email label and entry filed-------------------------------


email =Label(window,text="email:",image=email_icon, compound="left")
email.place(x=300,y=40)

email_field=Entry(window)
email_field.place(x=300,y=70)

#-------------------nom label and entry filed-------------------------------

nom=Label(window,text="nom:",image=person_icon, compound="left")
nom.place(x=300,y=90)

nom_field=Entry(window)
nom_field.place(x=300,y=120)

#-------------------prenom label and entry filed-------------------------------

prenom=Label(window,text="prenom:",image=person_icon, compound="left")
prenom.place(x=300,y=140)

prenom_field=Entry(window)
prenom_field.place(x=300,y=170)

#-------------------numero_tele label and entry filed-------------------------------

Numro_tele=Label(window,text="Numero du telephone:",image=phone_icon, compound="left")
Numro_tele.place(x=300,y=190)

Numro_tele_field=Entry(window)
Numro_tele_field.place(x=300,y=220)

#-------------------mot de passe label and entry filed-------------------------------

MotDePass=Label(window,text="Mot de passe:",image=lock_icon, compound="left")
MotDePass.place(x=300,y=240)

MotDePass_field=Entry(window)
MotDePass_field.place(x=300,y=270)

#-------------------confirm mot de passe label and entry filed-------------------------------

confirm_pwd=Label(window,text="confirmer cotre mot de passe:",image=lock_icon, compound="left")
confirm_pwd.place(x=300,y=290)

confirm_pwd_field=Entry(window)
confirm_pwd_field.place(x=300,y=320)


#-------------------check de verification-----------------------

je_suis_sure=IntVar()
sure=Checkbutton(window,text="j'ai rivisé tput les information et je prend la responsabilité de toute defaut possible",variable=je_suis_sure)
sure.place(x=150,y=350)



#-------------------confirm button------------------------------

confirm_button=Button(window,text="confirm",bg="#258EF5",fg="white",activebackground="#258EF5", activeforeground="white",font=("Arial",16),padx=0,pady=0, relief="flat")
confirm_button.place(x=320,y=380)


#-------------------leave button -------------------------------

leave_button=Button(window,text="leave",command=window.quit,bg="#258EF5",fg="white",activebackground="#258EF5", activeforeground="white",font=("Arial",12),padx=0,pady=0, relief="flat")
leave_button.place(x=600,y=450)










window.mainloop()