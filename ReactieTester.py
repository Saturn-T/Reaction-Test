# 1. Imports
import tkinter as tk
import random
import time
import pandas as pd
import matplotlib.pyplot as plt


# 2. App configuration
app = tk.Tk()
app.title("Reaction Time Test")
app.geometry("500x400")
app.configure(bg="black")


# 3. State variables
begin_time = None
loop_count = 0
reactions = []


# 4. UI elements
canvas = tk.Canvas(app, width=500, height=400, bg="red")
canvas.pack()
canvas.bind("<Button-1>", lambda _: canvas.focus_set())  # ensure canvas has focus when clicked

label = canvas.create_text(200, 150, justify="center", text="Try 1 van 10", font=("Helvetica", 16), fill="white")


# 5. Core functions
def change_color():
    """#5.1 Start a new round: set red and schedule green after random delay."""
    global begin_time, loop_count
    begin_time = None
    loop_count += 1
    canvas.configure(bg="red")
    waitTime = random.randint(2000, 5000)  # Random wait time between 2 and 5 seconds
    app.after(waitTime, color_change)


def color_change():
    """#5.2 Turn green and record the start time."""
    global begin_time
    canvas.configure(bg="green")
    begin_time = time.time()


def on_click(event):
    """#5.3 Handle user click (space key binding). Record reaction if green, otherwise ignore."""
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
        results()
        return
    else:
        change_color()


def results():
    """#5.4 Show summary and schedule plotting."""
    canvas.configure(bg="gray")
    canvas.itemconfig(label, text=f"Test completed! Average: {sum(reactions)/len(reactions):.0f} ms")
    print(f"\nAll times: {[f'{t:.0f}' for t in reactions]}")
    print(f"Average: {sum(reactions)/len(reactions):.0f} ms")
    app.after(1000, make_plot)


def make_plot():
    """#5.5 Save CSV and show a matplotlib plot of the reaction times."""
    # Pandas
    df = pd.DataFrame({
        "Tries": range(1, len(reactions) + 1),
        "Reaction Time (ms)": reactions
    })
    df.to_csv("reactiontimes.csv", index=False)
    print(df)

    # Matplotlib
    plt.figure(figsize=(8, 5))
    plt.plot(df["Tries"], df["Reaction Time (ms)"], marker="o", color="steelblue", linewidth=2)
    plt.axhline(df["Reaction Time (ms)"].mean(), color="red", linestyle="--", label=f"Average: {df['Reaction Time (ms)'].mean():.0f} ms")
    plt.title("Your reaction times")
    plt.xlabel("Tries")
    plt.ylabel("Reaction Time (ms)")
    plt.xticks(df["Tries"])
    plt.legend()
    plt.tight_layout()
    plt.savefig("reactiontimes.png")
    plt.show()

    app.destroy()


# 6. Bindings and start
canvas.bind("<space>", on_click)

change_color()  # Start the color change process
app.mainloop()