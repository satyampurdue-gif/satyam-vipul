import tkinter as tk
from tkinter import ttk

# This function runs whenever a button is clicked
def button_click(value):
    current = entry_var.get()
    entry_var.set(current + value)

# This function calculates the result
def calculate_result():
    try:
        result = eval(entry_var.get())
        entry_var.set(str(result))
    except:
        entry_var.set("Error")

# Clear the screen
def clear_screen():
    entry_var.set("")

# Create window
window = tk.Tk()
window.title("Calculator")
window.geometry("300x400")

# Entry display
entry_var = tk.StringVar()
entry = ttk.Entry(window, textvariable=entry_var, font=("Arial", 20))
entry.pack(fill="x", padx=10, pady=10)

# Create a frame for buttons
frame = ttk.Frame(window)
frame.pack()

# Button layout
buttons = [
    ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("/", 0, 3),
    ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("*", 1, 3),
    ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("-", 2, 3),
    ("0", 3, 0), ("=", 3, 1), ("C", 3, 2), ("+", 3, 3),
]

for (text, row, col) in buttons:
    if text == "=":
        btn = ttk.Button(frame, text=text, command=calculate_result)
    elif text == "C":
        btn = ttk.Button(frame, text=text, command=clear_screen)
    else:
        btn = ttk.Button(frame, text=text, command=lambda t=text: button_click(t))

    btn.grid(row=row, column=col, ipadx=10, ipady=10, padx=5, pady=5)

window.mainloop()