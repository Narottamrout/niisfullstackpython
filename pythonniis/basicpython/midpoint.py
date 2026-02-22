#Write a Python program to find midpoint of two points.
print("Enter coordinates of first point:")
x1 = float(input("x1 = "))
y1 = float(input("y1 = "))

print("\nEnter coordinates of second point:")
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))

# Midpoint formula
mx = (x1 + x2) / 2
my = (y1 + y2) / 2

print("\nMidpoint = (", mx, ",", my, ")")