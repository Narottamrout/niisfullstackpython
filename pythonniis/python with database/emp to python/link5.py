import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

# ---------- Database Connection ----------
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="tcs"
    )

# ---------- Insert Data ----------
def insert_data():
    eid = id_entry.get()
    name = name_entry.get()
    salary = salary_entry.get()
    dept = dept_entry.get()

    if eid == "" or name == "" or salary == "" or dept == "":
        messagebox.showerror("Error", "All fields are required")
        return

    con = get_connection()
    cur = con.cursor()

    sql = "INSERT INTO employee VALUES (%s,%s,%s,%s)"
    cur.execute(sql, (eid, name, salary, dept))

    con.commit()
    con.close()

    messagebox.showinfo("Success", "Inserted successfully")

    show_data()  # refresh table

# ---------- Show Data ----------
def show_data():
    con = get_connection()
    cur = con.cursor()

    cur.execute("SELECT * FROM employee")
    rows = cur.fetchall()

    # clear table
    for item in tree.get_children():
        tree.delete(item)

    # insert rows
    for row in rows:
        tree.insert("", tk.END, values=row)

    con.close()

# ---------- GUI ----------
root = tk.Tk()
root.title("Employee Management System")
root.geometry("650x500")

# Labels + Entries
tk.Label(root, text="ID").place(x=50, y=20)
tk.Label(root, text="Name").place(x=50, y=60)
tk.Label(root, text="Salary").place(x=50, y=100)
tk.Label(root, text="Department").place(x=50, y=140)

id_entry = tk.Entry(root)
id_entry.place(x=150, y=20)

name_entry = tk.Entry(root)
name_entry.place(x=150, y=60)

salary_entry = tk.Entry(root)
salary_entry.place(x=150, y=100)

dept_entry = tk.Entry(root)
dept_entry.place(x=150, y=140)

# Buttons
tk.Button(root, text="Insert", command=insert_data).place(x=150, y=180)
tk.Button(root, text="Show", command=show_data).place(x=230, y=180)

# Table
columns = ("emp_id", "emp_name", "emp_salary", "department")

tree = ttk.Treeview(root, columns=columns, show="headings")

tree.heading("emp_id", text="ID")
tree.heading("emp_name", text="Name")
tree.heading("emp_salary", text="Salary")
tree.heading("department", text="Department")

tree.place(x=50, y=230, width=550, height=200)

root.mainloop()