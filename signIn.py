from tkinter import *
from tkinter import font
from PIL import Image,ImageTk

#--------------------------------------#
#                                      #
#                                      #
#                                      #
#                                      #
#                                      #
# ------------------------------------ #

x_nom_entry=500+70
y_nom_entry=150

x_nom_Label=285+70
y_nom_Label=100+40

x_non_icon=500+70
y_non_icon=50+50

x_nom_etoile=465+70
y_nom_etoile=94+30


icon_size=50

#__________________________________________some function ___________________________________________#


                        #------------placehoder------------#

                        #event argument is to detect if I ckliked on the field or not

def focus_In(event):
        if date_de_naissan_field.get()=="DD-MM-YYY":
                date_de_naissan_field.delete(0,END)
                

def focus_out(event):
        if date_de_naissan_field.get()=="":
                date_de_naissan_field.insert(0,"DD-MM-YYY")
                date_de_naissan_field.configure(foreground="gray",font="bold")




                        #--------create icon-----------#
def create_icon(icon_path,tuple_size):
        image=Image.open(icon_path)
        image=image.resize(tuple_size)
        icon_image=ImageTk.PhotoImage(image)
        return icon_image







#_____________________________________________creation de la fenêtre_________________________________________________#
window=Tk()
window.geometry("1200x720")
window.config(bg="white")



# image=Image.open("R.jpg")
# image=image.resize((1000,700))
# background_image=ImageTk.PhotoImage(image)

# im_bg=Label(window,image=background_image)
# im_bg.place(x=200,y=0)






#______________________________________________create the non widget______________________________________#


                

                #--------------association of icon picture to the Entry-------------------#

personel_icon=create_icon("person_icon.png",(45,45))

image_label=Label(window, image=personel_icon,padx=0,pady=0,relief="flat",bg="white")
image_label.place(x=x_non_icon,y=y_non_icon)
image_label.config(highlightthickness=0)



                                #-----enter the Entry name field------#
name_txt=StringVar()

field_nom=Entry(window, textvariable=name_txt, width=45,bd=4,font=("Arial",12))
field_nom.place(x=x_nom_entry,y=y_nom_entry)



                            #-----enter the name Label------#
nom=Label(window,text="Entrer votre nom  : ",fg="black",font=("Helvetica",15,"bold"),bg="white" ,highlightthickness=0)
nom.place(x=x_nom_Label,y=y_nom_Label)

necessary_point=Label (window, text="*", fg="red",font=("Arial",15),bg="white" ,highlightthickness=0)
necessary_point.place(x=x_nom_etoile-15,y=y_nom_etoile+7)





#_______________________________________________________create a prenom widget __________________________________________________________#


                                                #----prenom Label-----#
prenom_Label=Label(window,text="Entrer votre Prenom  :",font=("Helvetica",15,"bold"),bg="white")
prenom_Label.place(x=x_nom_Label-30,y=y_nom_Label+70)



                                         #--------creation de l'etoile---------#

prenom_etoile=Label(window, text="*", font=("Arial",15),fg="red",bg="white")
prenom_etoile.place(x=x_nom_etoile-15,y=y_nom_etoile+70)


prenom_txt=StringVar()
prenom_field=Entry(window, textvariable=prenom_txt,bd=4,width=45,font=("Arial",13))
prenom_field.place(x=x_nom_entry,y=y_nom_entry+70)











# ________________________________________creation du champ email___________________________________________________#

    
    
        #--------------creation du label-------------------#
email_Label=Label(window, text="Entrer votre email  :",font=("Halvetica",15,"bold"),bg="white")
email_Label.place(x=x_nom_Label-15,y=y_nom_Label+140)



        #--------------creation du entry of email------------#

email_txt=StringVar()
email_field=Entry(window,textvariable=email_txt,font=("Avial",13), width=45,bd=4)
email_field.place(x=x_nom_entry,y=y_nom_entry+140)

        #------------creation de l'étoile--------------#

email_etoile=Label(window, text="*",font=("Halvetica",15,"bold"),fg="red",bg="white")
email_etoile.place(x=x_nom_etoile-25,y=y_nom_etoile+140)

        #---------------craetion de l'icon ----------#

email_icon=create_icon("email_icon.png",(icon_size-10,icon_size-10))


icon_label=Label(window,image=email_icon,bd=0,bg="white")
icon_label.place(x=x_non_icon,y=y_non_icon+146)








#_______________________________creation du numero de telephone________________________#



    #--------------creation du label-------------------#
phone_Label=Label(window, text="Entrer votre phone  :",font=("Halvetica",15,"bold"),bg="white")
phone_Label.place(x=x_nom_Label-30,y=y_nom_Label+230)



        #--------------creation du entry of phone------------#

phone_txt=StringVar()
phone_field=Entry(window,textvariable=phone_txt,font=("Avial",13), width=45,bd=4)
phone_field.place(x=x_nom_entry,y=y_nom_entry+230)

        #------------creation de l'étoile--------------#

phone_etoile=Label(window, text="*",font=("Halvetica",15,"bold"),fg="red",bg="white")
phone_etoile.place(x=x_nom_etoile-30,y=y_nom_etoile+230)

        #---------------craetion de l'icon ----------#

phone_icon=create_icon("phone_icon.png",(icon_size-10,icon_size-10))


icon_label=Label(window,image=phone_icon,bd=0,bg="white")
icon_label.place(x=x_non_icon,y=y_non_icon+236)




#_____________________________creation de date de naissance______________________________________#


    #--------------creation du label-------------------#
date_de_naissan_Label=Label(window, text="Entrer la date_de_naissance  :",font=("Halvetica",15,"bold"),bg="white")
date_de_naissan_Label.place(x=x_nom_Label-120,y=y_nom_Label+320)



        #--------------creation du entry of date_de_naissan------------#

date_de_naissan_txt=StringVar()
date_de_naissan_field=Entry(window,textvariable=date_de_naissan_txt,font=("Avial",13), width=45,bd=4)
date_de_naissan_field.place(x=x_nom_entry,y=y_nom_entry+320)

date_de_naissan_field.insert(0,"DD-MM-YYY")
date_de_naissan_field.configure(fg="gray")
date_de_naissan_field.bind("<FocusIn>",focus_In)
date_de_naissan_field.bind("<FocusOut>",focus_out)

        #------------creation de l'étoile--------------#

date_de_naissan_etoile=Label(window, text="*",font=("Halvetica",15,"bold"),fg="red",bg="white")
date_de_naissan_etoile.place(x=x_nom_etoile-30,y=y_nom_etoile+320)

        #---------------craetion de l'icon ----------#

date_de_naissan_icon=create_icon("date_de_naissance_icon.png",(icon_size-15,icon_size-15))


icon_label=Label(window,image=date_de_naissan_icon,bd=0,bg="white")
icon_label.place(x=x_non_icon,y=y_non_icon+330)












#_______________________________________creation de l'adress__________________________________________#

                #--------------creation du label-------------------#
adress_Label=Label(window, text="Entrer votre adress  :",font=("Halvetica",15,"bold"),bg="white")
adress_Label.place(x=x_nom_Label-37,y=y_nom_Label+400)



                #--------------creation du entry of adress------------#

adress_txt=StringVar()
adress_field=Entry(window,textvariable=adress_txt,font=("Avial",13), width=45,bd=4)
adress_field.place(x=x_nom_entry,y=y_nom_entry+400)


        #------------creation de l'étoile--------------#

adress_etoile=Label(window, text="*",font=("Halvetica",15,"bold"),fg="red",bg="white")
adress_etoile.place(x=x_nom_etoile-30,y=y_nom_etoile+400)

        #---------------craetion de l'icon ----------#

adress_icon=create_icon("adress_icon.jpg",(icon_size-15,icon_size-15))


icon_label=Label(window,image=adress_icon,bd=0,bg="white")
icon_label.place(x=x_non_icon,y=y_non_icon+410)












#______________________________________________________creation d'un frame___________________________________________________#

frame=Frame(window,bg="blue")
frame.place(x=0,y=0,width=150,height=7000)


frame_title =Frame(window,bg="#22003b" )
frame_title.place(x=150,y=0,width=3500,height=40)

                                #--------creation du titre--------#

titre_label=Label(frame_title,text="Sign up",font=("Halvetica",15,"bold"),fg="white",bg="#22003b")
titre_label.place(x=500,y=2)


                                #-----------creartion du button go back----------#

#---------prepararion de l'icon


go_back_icon=create_icon("go_back.jpg",(15,15))
go_back_button=Button(frame,image=go_back_icon)
go_back_button.place(x=20,y=10)



#------preparationd de Label

go_back_Label=Label(frame,text="go back",fg="white",bg="blue",font=("Halvetica",10,"bold"))
go_back_Label.place(x=50,y=8)

#______________________________________________________creation d'une image dy background___________________________________________________#


                                #----------label de --------------#






window.mainloop()