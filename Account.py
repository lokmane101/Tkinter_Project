from tkinter import *

account=Tk()
account.attributes('-fullscreen',True)
iconsbarr=Frame(account,width=240,height=1440,bg="black",)
iconsbarr.place(x=0,y=0)
# personal_icon=


#--------------------------leave button-------------------------------------------
leavebutton=Button(account,text="Leave",command=account.quit,bg="#258EF5",fg="white",activebackground="#258EF5", activeforeground="white",font=("Arial",16),padx=0,pady=0, relief="flat")      #
leavebutton.place(x=1440, y=800)

account.mainloop()