import tkinter as tk
from tkinter import ttk
import mysql.connector

# ---------- Database Connection ----------
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="tcs"
    )

# ---------- Show Data ----------
def show_data():
    con = get_connection()
    cur = con.cursor()

    cur.execute("SELECT * FROM employee")
    rows = cur.fetchall()

    # Clear old data
    for item in tree.get_children():
        tree.delete(item)

    # Insert new data
    for row in rows:
        tree.insert("", tk.END, values=row)

    con.close()

# ---------- GUI ----------
root = tk.Tk()
root.title("Employee Management System")
root.geometry("600x400")

# Table (Treeview)
columns = ("emp_id", "emp_name", "emp_salary", "department")

tree = ttk.Treeview(root, columns=columns, show="headings")

# Headings
tree.heading("emp_id", text="ID")
tree.heading("emp_name", text="Name")
tree.heading("emp_salary", text="Salary")
tree.heading("department", text="Department")

# Column width
tree.column("emp_id", width=80)
tree.column("emp_name", width=120)
tree.column("emp_salary", width=120)
tree.column("department", width=150)

tree.pack(pady=20)

# Button
btn = tk.Button(root, text="Show Employees", command=show_data)
btn.pack()

root.mainloop()