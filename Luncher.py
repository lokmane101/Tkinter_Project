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

# Define the geometry of the window-------------------------------
window.attributes('-fullscreen',True)

frame = Frame(window, width=600, height=400,relief="ridge")

frame.place(anchor='center', relx=0, rely=0)

# Create an object of tkinter ImageTk-----------------------------------
img = ImageTk.PhotoImage(Image.open("C:\\Users\\lokmane\\Desktop\\Tkinter_project\\vecteezy_abstract-gradient-blue-and-pink-wave-background_.jpg"))
# Create a Label Widget to display the  Image
label = Label(window, image = img)
label.pack()







#--------------------------------------------------------------------------------------------------------------#
# creating a leave button and changing its style                                                               #
# activebackground is color when to kpress on button ############ activeforegroud is color of text when press  #
# bg is color of background ##################################### fg is color of font                          #
#--------------------------------------------------------------------------------------------------------------#




#----------------------------welcome label--------------------------------------------
welcome=Label(window,text="wolcome to your shcoolar profil manager! ",font=("Arial",62))
welcome.place(x=0,y=0)




width = 20
height = 20
#---------------------------nom label and entry field-------------------------------
nom=Label(window,text="nom complet:",font=("Arial",30))
nom.place(x=550,y=200)

nomfield=Entry(window,width=25,font=("Arial",20))
nomfield.place(x=500,y=280)
#--------------------------password label and entry field----------------------------
password=Label(window,text="mot de passe:",font=("Arial",30))
password.place(x=550,y=360)

passwordfield=Entry(window,width=25,font=("Arial",20))
passwordfield.place(x=500,y=440)
#-------------------confirm button------------------------------

confirm_button=Button(window,text="confirm",command=pass_to_account, bg="#258EF5",fg="white",activebackground="#258EF5", activeforeground="white",font=("Arial",30),padx=0,pady=0, relief="flat")
confirm_button.place(x=600,y=500)

#-------------------------forgot password -----------------------------------------------


forgot_password=Button(window,text=("password forgoten"),command=forgoten_password,bg="#258EF5",fg="white",activebackground="#258EF5", activeforeground="white",font=("Arial",14),padx=0,pady=0, relief="flat")
forgot_password.place(x=600,y=650)


#--------------------------sing up buttom-----------------------------

signUp=Button(window,text=("sign up"),command=signup_button,bg="#258EF5",fg="white",activebackground="#258EF5", activeforeground="white",font=("Arial",14),padx=0,pady=0, relief="flat")
signUp.place(x=800,y=650)

#--------------------------leave button-------------------------------------------
leavebutton=Button(window,text="Leave",command=window.quit,bg="#258EF5",fg="white",activebackground="#258EF5", activeforeground="white",font=("Arial",16),padx=0,pady=0, relief="flat")      #
leavebutton.place(x=1440, y=800)


#------------------------contact support ------------------------------------------------
framei = Frame(window, width=200, height=200,relief="ridge")
framei.place(x=650,y=780)
icon=PhotoImage(file=r"C:\\Users\\lokmane\\Desktop\\Tkinter_project\\support.png")
button=Button(framei,image=icon,padx=0,pady=0,relief="flat")
button.pack()







window.mainloop()