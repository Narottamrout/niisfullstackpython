salary = int(input("enter basic salary: "))
da=0
hra=0
if salary >= 5000:
    da = salary * 30 / 100
    hra = salary * 20 / 100


total = salary + da + hra

print("HRA =", hra)
print("DA =", da)
print("Total Salary =", total)