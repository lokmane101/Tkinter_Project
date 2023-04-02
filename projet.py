from tkinter import *
from PIL import ImageTk, Image

# Create an instance of tkinter window
window = Tk()

# Define the geometry of the window
window.geometry("700x500")

frame = Frame(window, width=600, height=400)
frame.pack()
frame.place(anchor='center', relx=0.5, rely=0.5)

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("C:\\Users\\lokmane\\Desktop\\lokmane\\ID-1-S2\\python-scripts\\photo-1553095066-5014bc7b7f2d.jpg"))
leavebutton=Button(window,text="leave",command=window.quit)
leavebutton.pack()

# Create a Label Widget to display the text or Image
label = Label(frame, image = img)
label.pack()

window.mainloop()