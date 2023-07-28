"""  1) Square pattern : """
# n = 5
# for i in range(n):
#     for j in range(n):
#         print("*",end=' ')
#     print()

"""  1) Increasing triangle pattern : """
# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

"""  2) decreasing triangle pattern : """
# n = 5
# for i in range(n):
#     for j in range(i,n):
#         print("*",end=" ")
#     print()

"""  3) Right sided triangle pattern : """
# n = 5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

"""  4) hill pattern : """
# n = 5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

"""  5) Reverse hill pattern : """
# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n-1):
#         print("*",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     print()

"""  Diamond pattern : """
# n = int(input("enter the number: "))
# for i in range(n-1):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n-1):
#         print("*",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     print()

""" full pyramid """
# n = int(input("enter the number : "))
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end="")
#     for j in range(i+1):
#         print("* ",end="")
#     print()

""" Reverse full pyramid """
# n = int(input("enter the number: "))
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end="")
#     for j in range(i,n):
#         print("* ",end="")
#     print()

""" Diamond pattern : """
# n = int(input("enter the number: "))
# for i in range(n-1):
#     for j in range(i+1):
#         print(" ",end="")
#     for j in range(i,n):
#         print("* ",end="")
#     print()
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end="")
#     for j in range(i+1):
#         print("* ",end="")
#     print()