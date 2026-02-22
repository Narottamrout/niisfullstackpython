#Write a Python program to calculate acceleration.
#acceleration=finalvelocity-initialvelocity/time
v=int(input("the final velocity"))
u=int(input("the initial velocity"))
t=float(input("enter the time"))
a=(v-u)/t
print("the accleration is",a)
