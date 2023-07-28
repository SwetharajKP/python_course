""" Multiply all the numbers in a list using function"""
# def multiply(lst):
#     mul = 1
#     for i in lst:
#         mul *= i
#     return mul
# lst = [1, 2, 3, 4, 5]
# print(" Product of all numbers in list is :", multiply(lst))

""" Write a python program to reverse a string.
         sample string :"123abcd"
       expected output :dcba321"      """
# def reverse(str1):
#     return str1[::-1]
# str1 = input("enter the string : ")
# print("The reversed string is :", reverse(str1))

""" Write a python function to calculate the factorial of a number (a non-negative integer).
The function accepts the number as an argument."""
# def fact(n):
#     f = 1
#     for i in range(1,n+1):
#         f *= i
#     return f
# n = int(input("Enter the number : "))
# print("factorial of", n, "is :", fact(n))

""" Write a python function that takes a number as a parameter and check the number
 is prime or not"""
# def prime(n):
#     for i in range(2,n+1):
#         if n%i == 0:
#             print(n, "is not prime")
#             break
#         else:
#             print(n, "is a prime")
#             break
# n = int(input("Enter the number : "))
# prime(n)

""" Generate a  python list of all the even numbers between 4 to 30
expected o/p : [4,6,8,10,12,14,16,18,20,22,24,26,28]  """
# def even(lst):
#     lst = []
#     for i in range(4, 30, 2):
#         if i%2 == 0:
#             lst.append(i)
#     print(lst)
# even(list)

""" Write a python function to create and print a list where the values are
 square of numbers b/w 1 and 30 (both included)    """
# def values():
#     lst = []
#     for x in range(1, 31):
#         lst.append(x**2)
#     print(lst)
# values()

""" Write a python function that accepts a string and calculate the number of upper
case letter and lower case letter."""
# def count_upper_lower(str1):
#     upper_case = 0
#     lower_case = 0
#     for char in str1:
#         if char.isupper():
#             upper_case += 1
#         else:
#             if char.islower():
#                 lower_case += 1
#     print("count of upper case is ", upper_case)
#     print("count of lower case is ", lower_case)
# str1 = input("Enter the string : ")
# count_upper_lower(str1)

""" Write a python function that checks whether a passed string is palindrome or not."""
# def palindrome(str):
#     str1 = str.lower()
#     str2 = str1[::-1]
#     if str1 == str2:
#         print(str, "is a palindrome")
#     else:
#         print(str, "is not a palindrome")
# str = input("Enter the string : ")
# palindrome(str)

"""  Write a python function that takes a list and returns a new list with
unique element of the first list."""
# def unique(lst):
#     lst1 = []
#     for x in lst:
#         if x not in lst1:
#             lst1.append(x)
#     print("Unique list =", lst1)
# lst = [1, 2, 3, 4, 1, 2, 3, 4, 5, 6, 7, 7]
# unique(lst)

""" Write a python function to check whether a number is perfect or not."""
# def perfect_number(n):
#     sum = 0
#     for i in range(1, n):
#         if n%i == 0:
#             sum += i
#     if sum == n:
#         print(n, "is a perfect number")
#     else:
#         print(n, "is not a perfect number")
# n = int(input("Enter the number : "))
# perfect_number(n)

















