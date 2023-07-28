""" write a python program that prints all the numbers from 0 to 6 except 3 and 6 """
# for x in range(0,7):
#     if x == 3 or x == 6:
#         continue
#     print(x)
# or
# for x in range(0,7):
#     if x == 3:
#         continue
#     if x == 6:
#         continue
#     print(x)
# or
# for x in range(6):
#     if x == 3:
#         continue
#     print(x)

"""write a python program to get the fibonacci series between 0 to 50 """
# n1 = 0
# n2 = 1
# sum = 0
# for x in range(0,51):
#     print(sum,end=" ")
#     n1 = n2
#     n2 = sum
#     sum = n1 + n2


""" write a program to print multiplication table of given number """
# n = int(input("enter the number :"))
# for x in range(1,11):
#     print(n,"*",x,"=",n*x)

"""display numbers from -10 to -1 using for loop """
# for x in range(-10,0):
#     print(x)

"""write a program to display all prime numbers within a range """
# n = int(input("enter the lower interval : "))
# m = int(input("enter the upper interval : "))
# for x in range(n,m+1):
#     if n > 1:
#         for i in range(2,x):
#             if x%i==0:
#                 break
#         else:
#             print(x)

""" to calculate factorial of 5! # 5! = 5*4*3*2*1"""
# num = int(input(" enter the number :"))
# fact = 1
# for x in range(1,num+1):
#     fact = fact * x
#     print(fact)
# print("factorial of",num,"is",fact)

""" write a program to check whether a number is prime or not """
# num = int(input("enter the number :"))
# if num > 1:
#     for x in range(2, num):
#         if num % x == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")
# else:
#     print(num, "is not a prime number")
# or
# num = int(input(" enter the number :"))
# c = 0
# for x in range(1, n+1):
#     if num % x == o:
#         c += num
#


""" write a program to display product of the digits of a number accepted from the user """ # eg : 234 = 2*3*4 = 24
# num = int(input(" enter the number :"))
# a = num % 10
# b = num // 10
# print('product of the digit is', a * b)

""" accept 10 numbers from the user and display their average"""
# sum = 0
# for x in range(1,11):
#     num = int(input("enter the number :"))
#     sum += num
#     avg = sum/10
# print("average =", avg)

""" write a program to display all the numbers which are divisible by 11 but not by 2 between 100 and 500"""
# for x in range(100, 501):
#     if x % 11 == 0 and x % 2 != 0:
#         print(x, end=" ")



