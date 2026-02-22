#Write a Python program to calculate BMI.
#BMI = weight (kg) / (height (m) × height (m))
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height * height)

print("Your BMI is:", bmi)