from tkinter import *

creativemode = False

window = Tk()
window.title("No")


canvas = Canvas(window, width=600, height=800, bg='white')
canvas.pack()

#snowman
top = canvas.create_oval(550, 550, 500, 500, fill='white')
bottom = canvas.create_oval(475, 550, 575, 650, fill='white')
#background
canvas.create_rectangle(0, 800, 600, 700, fill='#651200')
canvas.create_rectangle(0, 700, 700, 650, fill='darkgreen')
canvas.create_rectangle(50, 650, 100, 500, fill='#651200')
canvas.create_polygon(15, 500, 140, 500, 75, 400, fill='#006530')
canvas.create_polygon(30, 450, 120, 450, 75, 360, fill='#006530')


#Changing the time
def night():
    canvas.config(bg='#0F024A')

def morning():
    canvas.config(bg='white')

#buttons for changing the time
button = Button(window, text="Change to day", command=morning)
button.pack()

button1 = Button(window, text="Change to night", command=night)
button1.pack()

#moving
def moveleft(event):
    a = canvas.coords(top)[2]
    b = canvas.coords(bottom)[2]
    if a > 50 and b > 50:
        canvas.move(top, -10, 0)
        canvas.move(bottom, -10, 0)

def moveright(event):
    a = canvas.coords(top)[2]
    b = canvas.coords(bottom)[2]
    if a < 600 and b < 600:
        canvas.move(top, 10, 0)
        canvas.move(bottom, 10, 0)


#keybinds for moving
canvas.bind_all('<Left>', moveleft)
canvas.bind_all('<Right>', moveright)


window.mainloop()