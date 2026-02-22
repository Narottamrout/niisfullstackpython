#Write a Python program to calculate net salary.
basic = float(input("Enter basic salary: "))
hra = float(input("Enter HRA: "))
da = float(input("Enter DA: "))
pf = float(input("Enter PF deduction: "))
tax = float(input("Enter tax deduction: "))

gross = basic + hra + da
net_salary = gross - (pf + tax)

print("Gross Salary =", gross)
print("Net Salary =", net_salary)