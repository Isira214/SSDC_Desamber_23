import tkinter as tk
from tkinter import ttk
from tkinter import font

root = tk.Tk()
root.title("GUI")
root.geometry("400x300")
root.resizable(True,True)

login = tk.StringVar()
login.set('Log In')
unLabel = tk.StringVar()
unLabel.set('User Name')
pwLabel = tk.StringVar()
pwLabel.set('Password')
un = tk.StringVar()
un.set('')
pw = tk.StringVar()
pw.set('')
style1 = ttk.Style()
style1.configure("text.TButton", font=("arial", 18, "bold"), forground="black")
font1 = font.Font(family="times new roman",size=20,weight="bold")
label1 = ttk.Label(root,foreground="black",font=font1,textvariable=login)
unLabel1 = ttk.Label(root,foreground="black",font=font1,textvariable=unLabel,justify="left")
pwLabel1 = ttk.Label(root,foreground="black",font=font1,textvariable=pwLabel,justify="left")
unInput = ttk.Entry(root,width=50,foreground='black',font=font1,textvariable=un,justify="left")
pwInput = ttk.Entry(root,width=50,foreground='black',show="*",font=font1,textvariable=pw,justify="left")

def check():
    if(un.get()=="root"):
        unInput.configure(foreground="green")
    else:
        unInput.configure(foreground="red")
    if(pw.get()=="pass"):
        pwInput.configure(foreground="green")
    else:
        pwInput.configure(foreground="red")

button1 = ttk.Button(root,width=7,style="text.TButton",command=check ,text="Submit")
label1.pack()
unLabel1.pack()
unInput.pack()
pwLabel1.pack()
pwInput.pack()
button1.pack()

root.mainloop()