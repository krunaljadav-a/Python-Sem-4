# 1. WAP to print “Hello World.!” 

print("hellow world")
# 2. WAP to print addition of two numbers with and without using input().
a=int(input("enter a value of a :")) 
b=int(input("enter a value of b :"))

print("sum of two number is : ",a+b)
# 3. WAP to check the type of the variable.
array =[21,25,12,5,12,5,12,5,1,2,51,2,4,24]
print("array")
print(type(array))
a=25
b="HELLO "
c ='k'
d= True
print(type(a))
print(type(b))
print(type(c))
print(type(d))
 
# 4. WAP to calculate simple interest. 

p=int(float("enter a value of p :"))
r=int(float("enter a value of r :"))
s=int(float("enter a value of s :"))
simple_intrest=float((r*p*s)/100)

print(simple_intrest)

# 5. WAP to calculate area and perimeter of a circle. 

Range = float(input("enter a value of perimeter: "))

import math
pi = math.pi

circle = float(pi*Range*Range)
print(circle)



# 6. WAP to calculate area of a triangle. 


# 7. WAP to compute quotient and remainder. 

    

dividend=input("Enter dividend: ");

divisor=input("Enter divisor: ");
quotient = dividend / divisor;remainder = dividend % divisor;
print("Quotient = ", quotient);print("Remainder = ", remainder);

# 8. WAP to convert degree into Fahrenheit and vice versa.# Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Fahrenheit =", fahrenheit)

# Fahrenheit to Celsius
fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = (fahrenheit - 32) * 5/9
print("Celsius =", celsius)
 
# 9. WAP to find the distance between two points in 2-D space. 
import math

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print("Distance =", distance)
# 10. WAP to print sum of n natural numbers. 
n = int(input("Enter n: "))

sum = n * (n + 1) // 2

print("Sum =", sum)
# 11. WAP to print sum of square of n natural numbers. 
n = int(input("Enter n: "))

sum_square = n * (n + 1) * (2 * n + 1) // 6

print("Sum of squares =", sum_square)
# 12. WAP to concate the first and last name of the student. 
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

full_name = first_name + " " + last_name

print("Full Name =", full_name)
# 13. WAP to swap two numbers. 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a, b = b, a

print("After swapping:")
print("a =", a)
print("b =", b)
# 14. WAP to get the distance from user into kilometer, and convert it into meter, feet, inches and centimeter. 
km = float(input("Enter distance in kilometer: "))

meter = km * 1000
centimeter = km * 100000
feet = km * 3280.84
inches = km * 39370.1

print("Meters =", meter)
print("Centimeters =", centimeter)
print("Feet =", feet)
print("Inches =", inches)
# 15. WAP to get day, month and year from the user and print the date in the given 
day = input("Enter day: ")
month = input("Enter month: ")
year = input("Enter year: ")

print(day + "-" + month + "-" + year)
# format: 20-10-2024. 
day = int(input("Enter day: "))
month = int(input("Enter month: "))
year = int(input("Enter year: "))

print(f"{day:02d}-{month:02d}-{year}")
