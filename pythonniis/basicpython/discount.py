#Write a Python program to calculate discounted price
price=int(input("enter the price"))
discount=int(input("enter the percentage of discount"))
dis=price*(discount/100)
finalprice=price-dis
print("the final price is=",finalprice)
print("the discount amount is=",dis)