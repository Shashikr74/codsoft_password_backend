# file: password_gui.py

import tkinter as tk
from tkinter import messagebox
from password_backend import generate_password

def generate():
    try:
        length = int(length_entry.get())
        password = generate_password(
            length,
            upper_var.get(),
            lower_var.get(),
            digit_var.get(),
            symbol_var.get()
        )
        result_entry.delete(0, tk.END)
        result_entry.insert(0, password)
    except:
        messagebox.showerror("Error", "Invalid input")

# GUI setup
root = tk.Tk()
root.title("Password Generator")

tk.Label(root, text="Password Length").pack()
length_entry = tk.Entry(root)
length_entry.pack()

upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digit_var = tk.BooleanVar(value=True)
symbol_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Uppercase", variable=upper_var).pack()
tk.Checkbutton(root, text="Lowercase", variable=lower_var).pack()
tk.Checkbutton(root, text="Digits", variable=digit_var).pack()
tk.Checkbutton(root, text="Symbols", variable=symbol_var).pack()

tk.Button(root, text="Generate Password", command=generate).pack(pady=10)

result_entry = tk.Entry(root, width=40)
result_entry.pack(pady=5)

root.mainloop()
