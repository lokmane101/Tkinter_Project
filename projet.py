from tkinter import *
from PIL import ImageTk, Image

# Create an instance of tkinter window
window = Tk()

# Define the geometry of the window
window.geometry("700x500")

frame = Frame(window, width=600, height=400,relief="ridge")
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("C:\\Users\\lokmane\\Desktop\\Tkinter_project\\photo-bg.jpg"))
# Create a Label Widget to display the text or Image
label = Label(frame, image = img)
label.pack()
################################################################################################################
# creating a leave button and changing its style                                                               #
# activebackground is color when to kpress on button ############ activeforegroud is color of text when press  #
# bg is color of background ##################################### fg is color of font                          #
leavebutton=Button(window,text="Leave",command=window.quit,bg="#258EF5",fg="white",activebackground="#258EF5", activeforeground="white",font=("Arial",16),padx=0,pady=0, relief="flat")      #
leavebutton.place(x=600, y=450)




window.mainloop()