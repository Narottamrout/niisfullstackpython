import mysql.connector

# ---------- Connection ----------
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="tcs"
)

cur = con.cursor()

# ---------- Menu ----------
while True:
    print("\n--- Employee Management ---")
    print("1. Show Employees")
    print("2. Insert Employee")
    print("3. Update Salary")
    print("4. Delete Employee")
    print("5. Exit")

    ch = int(input("Enter choice: "))

    # ---------- Show ----------
    if ch == 1:
        cur.execute("SELECT * FROM employee")
        rows = cur.fetchall()
        for row in rows:
            print(row)

    # ---------- Insert ----------
    elif ch == 2:
        eid = int(input("Enter ID: "))
        name = input("Enter Name: ")
        salary = int(input("Enter Salary: "))
        dept = input("Enter Department: ")

        sql = "INSERT INTO employee VALUES (%s,%s,%s,%s)"
        cur.execute(sql, (eid, name, salary, dept))
        con.commit()

        print("Inserted successfully")

    # ---------- Update ----------
    elif ch == 3:
        eid = int(input("Enter ID to update: "))
        salary = int(input("Enter new salary: "))

        sql = "UPDATE employee SET emp_salary=%s WHERE emp_id=%s"
        cur.execute(sql, (salary, eid))
        con.commit()

        print("Updated successfully")

    # ---------- Delete ----------
    elif ch == 4:
        eid = int(input("Enter ID to delete: "))

        sql = "DELETE FROM employee WHERE emp_id=%s"
        cur.execute(sql, (eid,))
        con.commit()

        print("Deleted successfully")

    # ---------- Exit ----------
    elif ch == 5:
        print("Exiting...")
        break

    else:
        print("Invalid choice")

# ---------- Close ----------
con.close()