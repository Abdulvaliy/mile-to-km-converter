from tkinter import *

def button_clicked():
    kilometres = int(int(input.get())*1.609)
    output.config(text=kilometres)


window = Tk()
window.title("Mile to Km converter")
window.minsize(width=280, height=120)
window.config(padx=30, pady=30)


input = Entry(width=10)
input.grid(column=1 ,row=0)
input.focus()


text_0 = Label(text="Miles")
text_0.config(padx=5, pady=5)
text_0.grid(column=2 ,row=0)

text_1 = Label(text="is equal to")
text_1.grid(column=0 ,row=1)

output = Label(text="0")
output.config(padx=5, pady=5)
output.grid(column=1 ,row=1)

text_2 = Label(text="Km")
text_2.grid(column=2 ,row=1)

button = Button(text="calculate", command=button_clicked)
button.grid(column=1 ,row=2)


window.mainloop()
