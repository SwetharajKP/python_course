""" conditional_statement: support for decision-making :
        if ,elif , else"""

""" if case :"""
# a = 33
# b = 200
# if b > a:
#     print("b is greater than a")

"""Elif : means " if the previous conditions were not true , then try this condition """
# a = 33
# b = 33
# if b > a:
#     print("b is greater than a")
# elif a == b:
#     print("a and b are equal")

"""Else : catches anything which isn't caught by the preceding conditions """
# a = 200
# b = 33
# if b > a:
#     print("b is greater than a")
# elif a == b:
#     print(" a and b are equal")
# else:
#     print(" a is greater than b")

""" example"""
# a = int(input("enter the first number :"))
# b = int(input("enter the second number :"))
# c = input("enter the choices(+,-,*,/) : ")
#
# if c == '+':
#     print("the sum is :", a+b)
# elif c == '-':
#     print("the difference :", a-b)
# else:
#     print("invalid syntax")

"""write a python program to find those numbers which are divisible by 7 and multiple of 5 """
# num = int(input("enter the number :"))
# if num%7 == 0 and num%5 == 0:
#     print(num, " is divisible by 7 and multiple of 5")
# else:
#     print(num, "is not divisible by 7 and multiple of 5")

# """ take three int value from user and print greatest among them """
# num1 = int(input("enter the first number :"))
# num2 = int(input("enter the second number :"))
# num3 = int(input("enter the third number:"))
# if num1 > num2 and num1 > num3:
#     print(" num1 is greater than num2 and num3")
# elif num2 > num1 and num2 > num3:
#     print("num2 is greater than num1 and num3")
# elif num3 > num1 and num3 > num2:
#     print("num3 is greater than num1 and num2")
# elif num1 == num2 and num1 > num3:
#     print("num1 and num2 are greater than num3")
# elif num2 == num3 and num2 > num1:
#     print("num2 and num3 are greater than num1")
# elif num3 == num1 and num3 > num2:
#     print("num3 and num1 are greater than num2")
# else:
#     print("all are equal")

""" Nested if: you can have if statements inside if statements, this is called nested if statements """
# x = 40
# if x > 10:
#     print("above ten")
#     if x > 20:
#         print("and also above 20! ")
#     else:
#         print(" but not above 20")
