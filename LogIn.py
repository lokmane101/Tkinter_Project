from tkinter import *
import subprocess
from PIL import Image ,ImageTk


#----------------------defintion des fonctions des buttons---------------------------------
def forgoten_password():
    subprocess.run(["python", "C:\\Users\\lokmane\\Desktop\\Tkinter_project\\forgottenPwd.py"])

def pass_to_account():
    subprocess.run(["python","C:\\Users\\lokmane\\Desktop\\Tkinter_project\\Account.py"])
login=Tk()
login.attributes('-fullscreen',True)
frame = Frame(login, width=600, height=400,relief="ridge")
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

# Create an object of tkinter ImageTk-----------------------------------
img = ImageTk.PhotoImage(Image.open("C:\\Users\\lokmane\\Desktop\\Tkinter_project\\vecteezy_abstract-gradient-blue-and-pink-wave-background_.jpg"))
# Create a Label Widget to display the text or Image
label = Label(frame, image = img)
label.pack()


width = 20
height = 20
#---------------------------nom label and entry field-------------------------------
nom=Label(login,text="nom complet:",font=("Arial",14))
nom.place(x=350,y=200)

nomfield=Entry(login)
nomfield.place(x=350,y=230)
nomfield.config(width=40)
#--------------------------password label and entry field----------------------------
password=Label(login,text="mot de passe:",font=("Arial",14))
password.place(x=350,y=270)

passwordfield=Entry(login)
passwordfield.config(width=40)
passwordfield.place(x=350,y=300)

#-------------------------forgot password -----------------------------------------------


forgot_password=Button(login,text=("password forgoten"),command=forgoten_password,bg="#258EF5",fg="white",activebackground="#258EF5", activeforeground="white",font=("Arial",14),padx=0,pady=0, relief="flat")
forgot_password.place(x=350,y=360)
#--------------------------leave button-------------------------------------------
leavebutton=Button(login,text="Leave",command=login.quit,bg="#258EF5",fg="white",activebackground="#258EF5", activeforeground="white",font=("Arial",16),padx=0,pady=0, relief="flat")      #
leavebutton.place(x=1440, y=800)
#------------------------contact support ------------------------------------------------
framei = Frame(login, width=200, height=200,relief="ridge")
framei.place(x=400,y=600)
icon=PhotoImage(file=r"C:\\Users\\lokmane\\Desktop\\Tkinter_project\\support.png")
button=Button(framei,image=icon,padx=0,pady=0,relief="flat")
button.pack()


















login.mainloop()