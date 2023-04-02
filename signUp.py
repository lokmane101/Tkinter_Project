from tkinter import *
window=Tk()

# Define the geometry of the window
window.geometry("700x500")

frame = Frame(window, width=600, height=400,relief="ridge")
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)


#-------------------email label and entry filed-------------------------------


email =Label(window,text="email:")
email.place(x=300,y=80)

email_field=Entry(window)
email_field.place(x=300,y=100)

#-------------------nom label and entry filed-------------------------------

nom=Label(window,text="nom:")
nom.place(x=300,y=120)

nom_field=Entry(window)
nom_field.place(x=300,y=140)

#-------------------prenom label and entry filed-------------------------------

prenom=Label(window,text="prenom:")
prenom.place(x=300,y=160)

prenom_field=Entry(window)
prenom_field.place(x=300,y=180)

#-------------------numero_tele label and entry filed-------------------------------

Numro_tele=Label(window,text="Numero du telephone:")
Numro_tele.place(x=300,y=200)

Numro_tele_field=Entry(window)
Numro_tele_field.place(x=300,y=220)

#-------------------mot de passe label and entry filed-------------------------------

MotDePass=Label(window,text="Mot de passe:")
MotDePass.place(x=300,y=240)

MotDePass_field=Entry(window)
MotDePass_field.place(x=300,y=260)

#-------------------confirm mot de passe label and entry filed-------------------------------

confirm_pwd=Label(window,text="confirmer cotre mot de passe:")
confirm_pwd.place(x=300,y=280)

confirm_pwd_field=Entry(window)
confirm_pwd_field.place(x=300,y=300)


#-------------------check de verification-----------------------

je_suis_sure=IntVar()
sure=Checkbutton(window,text="j'ai rivisé tput les information et je prend la responsabilité de toute defaut possible",variable=je_suis_sure)
sure.place(x=150,y=320)



#-------------------confirm button------------------------------

confirm_button=Button(window,text="confirm",bg="#258EF5",fg="white",activebackground="#258EF5", activeforeground="white",font=("Arial",16),padx=0,pady=0, relief="flat")
confirm_button.place(x=320,y=360)


#-------------------leave button -------------------------------

leave_button=Button(window,text="leave",command=window.quit,bg="#258EF5",fg="white",activebackground="#258EF5", activeforeground="white",font=("Arial",12),padx=0,pady=0, relief="flat")
leave_button.place(x=600,y=450)










window.mainloop()