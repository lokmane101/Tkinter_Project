from tkinter import *
from PIL import ImageTk, Image
import subprocess


#---------------------------------------definition des commands des buttons------------------------

def signup_button():
    subprocess.run(["python", "C:\\Users\\lokmane\\Desktop\\Tkinter_project\\signUp.py"])

def window_button():
    subprocess.run(["python", "C:\\Users\\lokmane\\Desktop\\Tkinter_project\\window.py"])

def forgoten_password():
    subprocess.run(["python", "C:\\Users\\lokmane\\Desktop\\Tkinter_project\\forgottenPwd.py"])

def pass_to_account():
    subprocess.run(["python","C:\\Users\\lokmane\\Desktop\\Tkinter_project\\Account.py"])
#---------------------------------------------------------------------------------------------------














# Create an instance of tkinter window----------------------------
window = Tk()

# Define the geometry of the window (full screen)-------------------------------

window.attributes('-fullscreen',True)
#-------------define sceen color----------------------------------------------
window.config(bg="white")
#-------------import picture---------------------------------------------------
imagee=(Image.open("C:\\Users\\lokmane\\Desktop\\Tkinter_project\\school.jpg"))
imagee=imagee.resize((600,900))
sidepicture = ImageTk.PhotoImage(imagee)
#----------------Create a Label Widget to display the  Image-----------------
label = Label(window, image = sidepicture,padx=0,pady=0, relief="flat")
label.grid(row=0,column=0)


#--------------------------------------------------------------------------------------------------------------#
# creating a leave button and changing its style                                                               #
# activebackground is color when to kpress on button ############ activeforegroud is color of text when press  #
# bg is color of background ##################################### fg is color of font                          #
#--------------------------------------------------------------------------------------------------------------#




#----------------------------welcome label--------------------------------------------
welcome=Label(window,text="ESPACE     ETUDIANT ",font=("Arial",65),bg="white")
welcome.place(x=605,y=0)

#---------------------------nom label and entry field--------------------------------
nom=Label(window,text="User Name:",font=("Arial",40),bg="white")
nom.place(x=950,y=150)

nomfield=Entry(window,width=25,font=("Arial",30),relief="flat",bg="#e1f3ff")
nomfield.place(x=850,y=250)
#--------------------------password label and entry field----------------------------
password=Label(window,text="mot de passe:",font=("Arial",40),bg="white")
password.place(x=950,y=350)

passwordfield=Entry(window,width=25,font=("Arial",30),relief="flat",bg="#e1f3ff")
passwordfield.place(x=850,y=450)
#-------------------confirm button---------------------------------------------------

confirm_button=Button(window,text="confirm",command=pass_to_account, bg="#258EF5",fg="white",activebackground="#258EF5", activeforeground="white",font=("Arial",20),padx=0,pady=0, relief="flat",width=35)
confirm_button.place(x=850,y=550)

#-------------------------forgot password -------------------------------------------


forgot_password=Button(window,text=("password forgoten"),command=forgoten_password,bg="white",fg="#258EF5",activebackground="white", activeforeground="#258EF5",font=("Arial",14),padx=0,pady=0, relief="flat")
forgot_password.place(x=850,y=620)


#--------------------------sing up buttom--------------------------------------------

signUp=Button(window,text=("sign up"),command=signup_button,bg="white",fg="#258EF5",activebackground="white", activeforeground="#258EF5",font=("Arial",14),padx=0,pady=0, relief="flat")
signUp.place(x=1350,y=620)

#--------------------------leave button---------------------------------------------
leavebutton=Button(window,text="Leave",command=window.quit,bg="#258EF5",fg="white",activebackground="#258EF5", activeforeground="white",font=("Arial",16),padx=0,pady=0, relief="flat")      #
leavebutton.place(x=1440, y=800)


#------------------------contact support -------------------------------------------
framei = Frame(window, width=200, height=200,relief="ridge")
framei.place(x=650,y=780)
icon=PhotoImage(file=r"C:\\Users\\lokmane\\Desktop\\Tkinter_project\\support.png")
button=Button(framei,image=icon,padx=0,pady=0,relief="flat",bg="white")
button.pack()







window.mainloop()