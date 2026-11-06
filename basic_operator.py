#1. Add Two Numbers
#Ask the user to enter two numbers. Print their sum.
"""
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = num1 + num2

print("Sum =", result)
"""

#2. Basic Calculator
#Ask the user to enter two numbers. Print their sum, difference, product, and quotient.
"""
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result1 = num1 + num2
result2 = num1 - num2
result3 = num1 * num2
result4 = num1 / num2

print("Sum =", result1)
print("Difference =", result2)
print("Product =", result3)
print("Quotient =", result4)
"""

#4. Even or Odd
#Ask the user to enter an integer. Print the remainder when the number is divided by 2.
"""
num = int(input("Enter first number: "))
print(num%2)
"""

#5. Integer Division
#Ask the user to enter two integers. Print the quotient using integer division.
"""
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(num1//num2)
"""

#6. Find the Remainder
#Ask the user to enter two integers. Print the remainder after division.
"""
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num=num1%num2
print(num)
"""

#7. Convert Minutes
#Ask the user to enter a number of minutes. Convert it into hours and remaining minutes.
"""
min = int(input("Enter min: "))
hr=min//60
remaining_min=min%60
print(hr)
print(remaining_min)
"""

#8. Area of a Rectangle
#Ask the user to enter the length and width. Calculate the area.
"""
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area=length*width
print(area)
"""

#9. Average of Three Numbers
#Ask the user to enter three numbers. Calculate their average.
"""
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
avg=(num1+num2+num3)/3
print(avg)
"""

#10. Swap Two Numbers
#Ask the user to enter two numbers. Swap their values and print the results.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Before swamping",num1,num2)
temp=num1
num1=num2
num2=temp
print("After swamping",num1,num2)
