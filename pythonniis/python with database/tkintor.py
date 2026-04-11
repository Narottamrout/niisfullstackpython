# from tkinter import*
# def add():
# 	n1=int(e1.get())
# 	n2=int(e2.get())
# 	n3=int(e3.get())
# 	result=n1+n2+n3
# 	lbl.config(text="Result="+str(result))
# root=Tk()
# root.title("addition app")
# root.geometry("300x200")
# Label(root,text="enter first number").pack()
# e1=Entry(root)
# e1.pack()
# Label(root,text="enter second number").pack()
# e2=Entry(root)
# e2.pack()
# Label(root,text="enter third number").pack()
# e3=Entry(root)
# e3.pack()
# Button(root,text="add",command=add).pack()
# lbl=Label(root,text="")
# lbl.pack()
# root.mainloop()
import tkinter as tk

# Create window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

# Entry box
entry = tk.Entry(root, width=25, font=("Arial", 18), borderwidth=5)
entry.grid(row=0, column=0, columnspan=4)

# Function to insert numbers
def click(num):
    entry.insert(tk.END, num)

# Function to clear
def clear():
    entry.delete(0, tk.END)

# Function to calculate
def equal():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Buttons
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('C',4,1), ('=',4,2), ('+',4,3)
]

# Create buttons
for (text, row, col) in buttons:
    if text == "C":
        btn = tk.Button(root, text=text, width=5, height=2, command=clear)
    elif text == "=":
        btn = tk.Button(root, text=text, width=5, height=2, command=equal)
    else:
        btn = tk.Button(root, text=text, width=5, height=2, command=lambda t=text: click(t))
    
    btn.grid(row=row, column=col)

# Run app
root.mainloop()
