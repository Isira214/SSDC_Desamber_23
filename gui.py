import tkinter as tk
from cProfile import label

from tkinter import ttk
from tkinter import font

root = tk.Tk()
root.title("GUI")

def center():
    width,height = 300,500
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = int(screen_width/2 - width /2)
    y = int(screen_height/2 - height /2)
    root.geometry(f"{width}x{height}+{x}+{y}")

    text_var = tk.StringVar()
    text_var.set('test')
    font1 = font.Font(family="times new roman",size=50,weight="bold")
    user_name = ttk.Entry(root,width=50,foreground='red',font=font1,textvariable=text_var,justify="center")

    label = ttk.Label(root,foreground="blue",font=font1,textvariable=text_var)

    # if 'root' == 'root':
    #     user_name.configure(foreground='green')
    # else:
    #     user_name.configure(foreground='red')
    user_name.pack()
    label.pack()

    style1 = ttk.Style()
    style1.configure( "text.TButton",font=("arial",18,"bold"),forground="pink")

    def test():
        print(text_var.get())

    button1 = ttk.Button(root)
    button1.configure(text="Submit",style="test.TButton",width=7)
    button1.pack()
    # button1.configure(text="submit",font = font1)


center()

# root.geometry("400x400")
root.resizable(True,True)
root.mainloop()