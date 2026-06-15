import tkinter as tk
import random
import time

app = tk.Tk()
app.title("Reactietijd Test")
app.geometry("500x400")
app.configure(bg="red")

begin_time = None

canvas = tk.Canvas(app, width=500, height=400, bg="red")
canvas.pack()
canvas.bind("<Button-1>", lambda event: canvas.focus_set())


def change_color():
    global begin_time
    begin_time = None
    canvas.configure(bg="red")
    waitTime = random.randint(2000, 5000)  # Random wait time between 2 and 5 seconds
    app.after(waitTime, color_change)

def color_change():
    global begin_time
    canvas.configure(bg="green")
    begin_time = time.time()

def on_click(event):
    if begin_time is None:
        print("Too soon! Wait for the color to change.")
        return  # Ignore clicks before the color changes
    if begin_time is not None:
        reaction_time = (time.time() - begin_time) * 1000  # Convert to milliseconds 
        print(f"Reactietijd: {reaction_time:.3f} ms")
        change_color()  # Reset for the next round

canvas.bind("<space>", on_click)

change_color()  # Start the color change process
app.mainloop()