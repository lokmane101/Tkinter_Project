from tkinter import * 
from tkinter import ttk
from PIL import Image,ImageTk

window = Tk()
window.geometry("720x720")

frame = Frame(window, width=600, height=400,relief="ridge")

frame.place(anchor='center', relx=0.5, rely=0.5)

# Create an object of tkinter ImageTk-----------------------------------
img = ImageTk.PhotoImage(Image.open("C:\\Users\\lokmane\\Desktop\\Tkinter_project\\vecteezy_abstract-gradient-blue-and-pink-wave-background_.jpg"))
# Create a Label Widget to display the  Image
label = Label(window, image = img)
label.pack()
style = ttk.Style()
style.configure("Transparent.TLabel", background="systemTransparent")

label = ttk.Label(window, text="This is a transparent label", style="Transparent.TLabel",foreground="black")
label.pack()


window.mainloop()