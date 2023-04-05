from tkinter import *
import mysql.connector 
account=Tk()
account.geometry("1200x720")
iconsbarr=Frame(account,width=150,height=1440,bg="#15b4ea",)
iconsbarr.place(x=0,y=0)
def get_user_name():
    logfile=open("fichierlog.txt",'r')
    users=logfile.read().split("\n")
    username=users[-2]
    return username

#------------------------------------------partie SQL-------------------------------------------------------------------------------------------------------#

#------------------------connect to the database------------------------------------    
database = mysql.connector.connect(host='localhost',
                                database='projet',
                                user='root',
                                password='lokmane-SQL-12')
#------------------------create cursor---------------------------------------------
cursorr=database.cursor()

#-----------------------------import icons----------------------------------------
time_icon=PhotoImage(file=r"C:\\Users\\lokmane\\Desktop\\Tkinter_project\\icons\\time1.png")
time_icon_button=Button(iconsbarr,bg="#15b4ea",padx=0,pady=0, relief="flat",image=time_icon,activebackground="#15b4ea")
time_icon_button.place(x=15,y=80)



paper=PhotoImage(file=r"C:\\Users\\lokmane\\Desktop\\Tkinter_project\\icons\\paper1.png")
paper_button=Button(iconsbarr,bg="#15b4ea",padx=0,pady=0, relief="flat",image=paper,activebackground="#15b4ea")
paper_button.place(x=25,y=200)


icon=PhotoImage(file=r"C:\\Users\\lokmane\\Desktop\\Tkinter_project\\icons\\support.png")
button=Button(iconsbarr,image=icon,padx=0,pady=0,relief="flat",bg="#15b4ea",activebackground="#15b4ea")
button.place(x=25,y=620)

person=PhotoImage(file=r"C:\\Users\\lokmane\\Desktop\\Tkinter_project\\icons\\person_icon1.png")
person_button=Button(iconsbarr,image=person,padx=0,pady=0,relief="flat",bg="#15b4ea",activebackground="#15b4ea")
person_button.place(x=18,y=300)



#-------------------------------body----------------------------------------------------------------------------

hello=Label(text="HELLO\t"+get_user_name(),font=("Arial",30),fg="#258EF5")
hello.place(x=500,y=50)




#--------------------------leave button-------------------------------------------
leavebutton=Button(account,text="Leave",command=account.quit,bg="#258EF5",fg="white",activebackground="#258EF5", activeforeground="white",font=("Arial",16),padx=0,pady=0, relief="flat")      #
leavebutton.place(x=1100, y=650)

account.mainloop()