import tkinter as tk
from tkinter import messagebox


def login():
    username = entry_username.get()
    password = entry_password.get()

    # Here you can add your authentication logic
    if username == "admin" and password == "password":
        messagebox.showinfo("Login Successful", "Welcome!")
        root.destroy()  # Close the dialog
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")


# Create the main window
root = tk.Tk()
root.title("Login Dialog")

# Create and place the username label and entry
label_username = tk.Label(root, text="Username:")
label_username.pack(pady=5)

entry_username = tk.Entry(root)
entry_username.pack(pady=5)

# Create and place the password label and entry
label_password = tk.Label(root, text="Password:")
label_password.pack(pady=5)

entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

# Create and place the login button
button_login = tk.Button(root, text="Login", command=login)
button_login.pack(pady=20)

# Start the GUI event loop
root.mainloop()