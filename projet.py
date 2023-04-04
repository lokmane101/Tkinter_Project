from tkinter import *
from PIL import ImageTk, Image
import subprocess


#---------------------------------------

def signup_button():
    subprocess.run(["python", "C:\\Users\\lokmane\\Desktop\\Tkinter_project\\signUp.py"])

def login_button():
    subprocess.run(["python", "C:\\Users\\lokmane\\Desktop\\Tkinter_project\\LogIn.py"])
#-----------------------------------














# Create an instance of tkinter window----------------------------
window = Tk()

# Define the geometry of the window-------------------------------
window.geometry("1080x720")

frame = Frame(window, width=600, height=400,relief="ridge")
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

# Create an object of tkinter ImageTk-----------------------------------
img = ImageTk.PhotoImage(Image.open("C:\\Users\\lokmane\\Desktop\\Tkinter_project\\vecteezy_abstract-gradient-blue-and-pink-wave-background_.jpg"))
# Create a Label Widget to display the text or Image
label = Label(frame, image = img)
label.pack()







#--------------------------------------------------------------------------------------------------------------#
# creating a leave button and changing its style                                                               #
# activebackground is color when to kpress on button ############ activeforegroud is color of text when press  #
# bg is color of background ##################################### fg is color of font                          #
#--------------------------------------------------------------------------------------------------------------#

leavebutton=Button(window,text="Leave",command=window.quit,bg="#258EF5",fg="white",activebackground="#258EF5", activeforeground="white",font=("Arial",16),padx=0,pady=0, relief="flat")      #
leavebutton.place(x=900, y=650)

#----------------------------welcome label--------------------------------------------
welcome=Label(window,text="wolcome to your shcoolar profil manager!",font=("Arial",20))
welcome.pack()

#--------------------------sign in and sing up buttoms-----------------------------

signIN=Button(window,text=("sign in"),command=login_button,bg="#258EF5",fg="white",activebackground="#258EF5", activeforeground="white",font=("Arial",30),padx=0,pady=0, relief="flat")
signIN.place(x=350,y=200)

signUp=Button(window,text=("sign up"),command=signup_button,bg="#258EF5",fg="white",activebackground="#258EF5", activeforeground="white",font=("Arial",30),padx=0,pady=0, relief="flat")
signUp.place(x=550,y=200)









window.mainloop()