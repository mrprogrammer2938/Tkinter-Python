from tkinter import * # python -m pip install tk-tools
from time import strftime
root = Tk()
root.title('Clock')

def time():
    time_zone = strftime("%H:%M:%S %p")
    label.configure(text=time_zone)
    label.after(1000,time)
label = Label(root,foreground='cyan',background='black',font=("dis-digital",80))
label.pack()
time()

photo = PhotoImage(file = './Scr/clock-logo.png') # .png | .jpg 
root.iconphoto(True,photo)
root.resizable(0,0)
root.mainloop()