from tkinter import *
import subprocess
from PIL import Image ,ImageTk
def forgoten_password():
    subprocess.run(["python", "C:\\Users\\lokmane\\Desktop\\Tkinter_project\\forgottenPwd.py"])

login=Tk()
login.geometry("1080x720")

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

# #------------------------contact support ------------------------------------------------
framei = Frame(login, width=200, height=200,relief="ridge")
framei.place(x=400,y=600)
icon=PhotoImage(file=r"C:\\Users\\lokmane\\Desktop\\Tkinter_project\\support.png")
button=Button(framei,image=icon,padx=0,pady=0,relief="flat")
button.pack()


















login.mainloop()