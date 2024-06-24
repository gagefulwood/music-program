import tkinter as tk
from tkinter import StringVar, OptionMenu, Label

def on_dropdown_change(*args):
    selected_value = dropdown_var.get()
    label.config(text=f"Selected: {selected_value}")

# Create the main window
root = tk.Tk()
root.title("Dropdown Change Example")

# Create a StringVar to hold the value of the dropdown menu
dropdown_var = StringVar()
dropdown_var.set("Option 1")  # Set the default value

# Trace the StringVar to detect changes
dropdown_var.trace("w", on_dropdown_change)

# Create the dropdown menu
options = ["Option 1", "Option 2", "Option 3"]
dropdown = OptionMenu(root, dropdown_var, *options)
dropdown.pack(padx=10, pady=10)

# Create a label to display the selected option
label = Label(root, text="Selected: Option 1")
label.pack(padx=10, pady=10)

# Run the main loop
root.mainloop()
