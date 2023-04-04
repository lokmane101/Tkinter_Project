from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
account=Tk()
account.attributes('-fullscreen',True)
iconsbarr=Frame(account,width=240,height=1440,bg="black",)
iconsbarr.place(x=0,y=0)
# personal_icon=


frame = Frame(account, width=600, height=400,relief="ridge")

frame.place(anchor='center', relx=0, rely=0)

# Create an object of tkinter ImageTk-----------------------------------
img = ImageTk.PhotoImage(Image.open("C:\\Users\\lokmane\\Desktop\\Tkinter_project\\vecteezy_abstract-gradient-blue-and-pink-wave-background_.jpg"))
# Create a Label Widget to display the  Image
label = Label(account, image = img)
label.pack()
style = ttk.Style()
style.configure("TLabel", background=account[img], foreground=account[img])  # set background and foreground to be the same as the parent widget

label = ttk.Label(account, text="This is a transparent label",foreground="black")
label.pack()


#--------------------------leave button-------------------------------------------
leavebutton=Button(account,text="Leave",command=account.quit,bg="#258EF5",fg="white",activebackground="#258EF5", activeforeground="white",font=("Arial",16),padx=0,pady=0, relief="flat")      #
leavebutton.place(x=1440, y=800)

account.mainloop()