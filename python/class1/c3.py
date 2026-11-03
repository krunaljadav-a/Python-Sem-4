# 1. WAP to print 1 to 10.
# i=1
# for i in range(1, 11):
#     print(i)
# # 2. WAP to print 1 to n.
# n= int(input("enter a number: "))

# for i in range(1,n+1):
#     print(i)


# # 3. WAP to print odd numbers between 1 to n.
# n= int(input("enter a to print odd number : "))
# for i in range(1,n+1):
#     if i%2!=0:
#         print(i)

# # 4. WAP to print numbers between two given numbers which is divisible by 2 but
# # not divisible by 3.
# n= int(input("enter a  : "))
# m= int(input("enter b  : "))

# for i in range(n,m):
#     if i%2!=1 and i%3!=0:
#         print(i)

# 5. WAP to print sum of 1 to n numbers.
# number = int(input("Enter a number: "))

# sum = 0

# for i in range(1, number + 1):
#     sum += i

# print("sum of number ", sum)


# # 6. WAP to print sum of series 1 + 4 + 9 + 16 + 25 + 36 + ...n.
# for i in range(1,number+1):
#     series = i**2
#     print(series ,end=" \n")

# # 7. WAP to print multiplication table of given number.
# for i in range(1 ,11):
#     table=number*i
#     print(number,"x",i,"=",table)
# 8. WAP to print sum of series 1 – 2 + 3 – 4 + 5 – 6 + 7 ... n.

# sum = 0
# for i in range(1, number + 1):
#     if i % 2 == 0:
#         sum -= i
#     else:
#         sum += i


# print(sum)
# 9. WAP to find factorial of the given number.

# factorial = 1

# for i in range(1, number + 1):
#     factorial *= i

# print("Factorial =", factorial)
# # 10. WAP to find whether the given number is prime or not.

# num = int(input("Enter a number: "))
# count = 0

# for i in range(1, num + 1):
#     if num % i == 0:
#         count += 1

# if count == 2:
#     print("Prime Number")
# else:
#     print("Not Prime Number")
# 11. WAP to find factors of a given number.
# num = int(input("Enter your number : "))
# factorial=1;
# for i in range(1,num+1):
#     factorial*=i

# print(f"factorial of {num} is : ",factorial)

# # 12. WAP to print sum of digits of given number.
# num = int(input("Enter your number : "))
# temp=num
# sum=0
# while temp>0:
#     digit = temp%10
#     sum+=digit
#     temp//=10


# print("sum of digits =", f"{sum:.2f}")


# 13. WAP to find GCD of the given two numbers.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

while b != 0:
    a, b = b, a % b

print("GCD =", a)
# 14. WAP to check whether the given number is palindrome or not.
# num = int(input("Enter your number : "))
# temp = num
# count = 0
# reversed = 0
# while temp > 0:
#     count += 1
#     temp //= 10

# print(count)
# temp = num

# while temp > 0:
#     digit = temp % 10
#     reversed = reversed * 10 + digit
#     temp //= 10

# if num == reversed:
#     print("your number is palindrome ")
# else:
#     print("not palindrome")
