# . WAP to check whether the given number is positive or negative. 

number = 25

if number > 0:
    print("Positive number")
else:
    print("Negative number")
# 2. WAP to check whether the given number is odd or even. 
if number%2==0:
    print("even  number")
else:
    print("Odd number")
# 3. WAP to find out largest number from given two numbers using simple if and 
# ternary operator. 

a=10
b=20
c=30
largest = a if a > b and a > c else (b if b > c else c)

print("Largest number is:", largest)
# 4. WAP to find out largest number from given three numbers. 
if a > b and a > c:
    print("Largest number is:", a)
elif b > c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)
# 5. WAP to check whether the given year is leap year or not.  
year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")
# 6. WAP to display the name of the day according to the number given by the 
day = int(input("Enter day number (1-7): "))

if day == 1:
    print("Sunday")
elif day == 2:
    print("Monday")
elif day == 3:
    print("Tuesday")
elif day == 4:
    print("Wednesday")
elif day == 5:
    print("Thursday")
elif day == 6:
    print("Friday")
elif day == 7:
    print("Saturday")
else:
    print("Invalid day number")
#    7  WAP to implement simple calculator which performs (addition, subtraction, 
# multiplication and division) of two numbers based on user input
# 
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    print("Addition =", num1 + num2)
elif choice == 2:
    print("Subtraction =", num1 - num2)
elif choice == 3:
    print("Multiplication =", num1 * num2)
elif choice == 4:
    if num2 != 0:
        print("Division =", num1 / num2)
    else:
        print("Division by zero is not possible")
else:
    print("Invalid Choice")

# 8. WAP to read marks of five subjects. Calculate percentage and print class 
# accordingly. Fail below 35, Pass Class between 36 to 45, Second Class between 
# 46 to 60, First Class between 61 to 70, Distinction if more than 70. 

s1= float(input("enter subject 1 marks: "))
s2= float(input("enter subject 2 marks: "))
s3= float(input("enter subject 3 marks: "))
s4= float(input("enter subject 4 marks: "))
s5= float(input("enter subject 5 marks: "))

total_marks=500;
Obtained_marks =s1+s2+s3+s4+s5;


percentage = (Obtained_marks/total_marks)*100

if percentage < 35:
    print("You failed in exam")
elif 36 <= percentage <= 45:
    print("Pass in exam")
elif 46 <= percentage <= 60:
    print("You are in second class")
elif 61 <= percentage <= 70:
    print("You are in first class")
else:
    print("Distinction")

# 9. Three sides of a triangle are entered through the keyboard, WAP to check 
# whether the triangle is isosceles, equilateral, scalene or right-angled triangle. 
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a == b == c:
    print("Equilateral Triangle")
elif a == b or b == c or a == c:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")

sides = sorted([a, b, c])

if sides[0]**2 + sides[1]**2 == sides[2]**2:
    print("Right-Angled Triangle")
# 10. WAP to find the second largest number among three user input numbers. 

a= int (input("enter a value of a : "))
b= int (input("enter a value of b : "))
c= int (input("enter a value of c : "))
num =[a,b,c]
num.sort()
print("second larger number is :" ,num[1])
# 11. WAP to calculate electricity bill based on following criteria. Which takes the 
# unit from the user. 
# i. First 1 to 50 units – Rs. 2.60/unit  
# ii. Next 50 to 100 units – Rs. 3.25/unit 
# iii. Next 100 to 200 units – Rs. 5.26/unita 
# iv. bove 200 units – Rs. 8.45/unit 
units = int(input("Enter units consumed: "))

if units <= 50:
    bill = units * 2.60

elif units <= 100:
    bill = (50 * 2.60) + ((units - 50) * 3.25)

elif units <= 200:
    bill = (50 * 2.60) + (50 * 3.25) + ((units - 100) * 5.26)

else:
    bill = (50 * 2.60) + (50 * 3.25) + (100 * 5.26) + ((units - 200) * 8.45)

print("Electricity Bill = Rs.", bill)