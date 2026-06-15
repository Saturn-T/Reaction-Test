import tkinter as tk
import random

app = tk.Tk()
app.title("Reactietijd Test")
app.geometry("500x400")
app.configure(bg="red")

canvas = tk.Canvas(app, width=500, height=400, bg="red")
canvas.pack()

def change_color():
    waitTime = random.randint(2000, 5000)  # Random wait time between 2 and 5 seconds
    app.after(waitTime, color_change)

def color_change():
    canvas.configure(bg="green")
    
change_color()  # Start the color change process
app.mainloop()