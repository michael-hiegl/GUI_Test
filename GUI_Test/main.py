import tkinter as tk
from turtle import back 

window=tk.Tk()
window.geometry("500x500")
window.title("Gear")
window.config(background="#404040")
photo=tk.PhotoImage(file="gear-icon-13.png")
window.wm_iconphoto(False,photo)

on=tk.PhotoImage(file="toggle_button_left.png")
off=tk.PhotoImage(file="toggle_button_right.png")

def Calculate():
    result=eval(input_field.get())
    input_field.delete(0,tk.END)
    input_field.insert(0,result)

button_state=True
def Toggle():
    global button_state

    if button_state==True:
        print("OFF")
        toggle_button.config(image=off,background="#404040")
        button_state=False

    else:
        print("ON")
        toggle_button.config(image=on,background="#404040")
        button_state=True


toggle_button=tk.Button(window,image=on,border=0,background="#404040",activebackground="#404040",command=Toggle)
toggle_button.grid(row=0,column=2)

calc_button=tk.Button(window,text="Calculate",command=Calculate)
calc_button.grid(row=0,column=1)

input_field=tk.Entry(window)
input_field.grid(row=1,column=1)





window.mainloop()