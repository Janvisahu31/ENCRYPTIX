import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(event=None):
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Length must be positive")
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid positive integer for length")

def copy_to_clipboard():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()  # Now it stays on the clipboard after the window is closed
        messagebox.showinfo("Success", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy!")

root = tk.Tk()
root.title("Password Generator")

font_settings = ("Arial", 12)

length_label = tk.Label(root, text="Length of Password:",font=font_settings)
length_label.grid(row=0, column=0, padx=10, pady=10)

length_entry = tk.Entry(root, width=30,font=font_settings)
length_entry.grid(row=0, column=1, padx=20, pady=20)
length_entry.bind("<Return>", generate_password) 

generate_button = tk.Button(root, text="Generate Password", command=generate_password,font=font_settings)
generate_button.grid(row=1, column=0,columnspan=2, padx=10, pady=10)

password_label = tk.Label(root, text="Generated Password:",font=font_settings)
password_label.grid(row=2, column=0, padx=10, pady=10)

password_entry = tk.Entry(root, width=30,font=font_settings)
password_entry.grid(row=2, column=1, padx=20, pady=20)



copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard,font=font_settings)
copy_button.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
