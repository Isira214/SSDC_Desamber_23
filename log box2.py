import tkinter as tk
from tkinter import ttk
from tkinter import font

root = tk.Tk()
root.title("Login")
root.geometry("550x250")
root.resizable(True,True)

style1 = ttk.Style().configure("text.TButton",font=("Times new Roman",20),justify="center",forground="black")

unLabel = ttk.Label(root,text="User Name : ",font=("Times new Roman",20),justify="left")
unInput = ttk.Entry(root,font=("Times new Roman",20),justify="center")

pwLabel = ttk.Label(root,text="User Name : ",font=("Times new Roman",20),justify="left")
pwInput = ttk.Entry(root,font=("Times new Roman",20),justify="center")

button1 = ttk.Button(root,text="Submit",width=10,style="text.TButton")

unLabel.grid(row=1,column=2,padx=30,pady=(30,10))
unInput.grid(row=1,column=3)
pwLabel.grid(row=2,column=2,pady=(30,20) )
pwInput.grid(row=2,column=3)
button1.grid(row=3,column=3,sticky=tk.E)

root.mainloop()