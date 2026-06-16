import tkinter as tk
import random
import time

app = tk.Tk()
app.title("Reaction Time Test")
app.geometry("500x400")
app.configure(bg="black")

begin_time = None
loop_count = 0
reactions = []

canvas = tk.Canvas(app, width=500, height=400, bg="red")
canvas.pack()
canvas.bind("<Button-1>", lambda event: canvas.focus_set())

label = canvas.create_text(200, 150, justify="center", text="Try 1 van 10", font=("Helvetica", 16), fill="white")

def change_color():
    global begin_time, loop_count
    begin_time = None
    loop_count += 1
    canvas.configure(bg="red")
    waitTime = random.randint(2000, 5000)  # Random wait time between 2 and 5 seconds
    app.after(waitTime, color_change)

def color_change():
    global begin_time
    canvas.configure(bg="green")
    begin_time = time.time()

def on_click(event):
    global loop_count
    
    if begin_time is None:
        print("Too soon! Wait for the color to change.")
        return  # Ignore clicks before the color changes
    
    reaction_time = (time.time() - begin_time) * 1000  # Convert to milliseconds 
    reactions.append(reaction_time)
    
    print(f"reaction_time: {reaction_time:.0f} ms")
    canvas.itemconfig(label, text=f"Try {loop_count + 1} van 10")
    
    if loop_count >= 10:  # Limit the number of rounds
        app.unbind("<space>")
        canvas.configure(bg="gray")
        canvas.itemconfig(label, text=f"Test completed! Average: {sum(reactions)/len(reactions):.0f} ms")
        print(f"\nAll times: {[f'{t:.0f}' for t in reactions]}")
        print(f"Average: {sum(reactions)/len(reactions):.0f} ms")
        return
    
    change_color()

canvas.bind("<space>", on_click)

change_color()  # Start the color change process
app.mainloop()