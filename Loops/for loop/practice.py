""" star pattern :"""

"""  1) Square pattern : """
# n = 5
# for i in range(n):
#     for j in range(n):
#         print("*", end=" ")
#     print()

"""  1) Increasing triangle pattern : """
# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print("*", end=" ")
#     print()

"""  2) decreasing triangle pattern : """
# n = 5
# for i in range(n):
#     for j in range(i, n):
#         print("*", end=" ")
#     print()

"""  3) Right sided triangle pattern : """
# n = 5
# for i in range(n):
#     for j in range(i, n):
#         print(" ", end=" ")
#     for j in range(i+1):
#         print("*", end=" ")
#     print()


"""  4) Right sided triangle pattern : """
# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print(" ", end=" ")
#     for j in range(i, n):
#         print("*", end=" ")
#     print()

"""  4) hill pattern : """
# n = 5
# for i in range(n):
#     for j in range(i, n):
#         print(" ", end=" ")
#     for j in range(i):
#         print("*", end=" ")
#     for j in range(i+1):
#         print("*", end=" ")
#     print()

"""  5) Reverse hill pattern : """
# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print(" ", end=" ")
#     for j in range(i, n-1):
#         print("*", end=" ")
#     for j in range(i, n):
#         print("*", end=" ")
#     print()

"""  Diamond pattern : """
# n = int(input("enter the number of rows: "))
# for i in range(n-1):
#     for j in range(i, n):
#         print(" ", end=" ")
#     for j in range(i):
#         print("*", end=" ")
#     for j in range(i+1):
#         print("*", end=" ")
#     print()
# for i in range(n):
#     for j in range(i+1):
#         print(" ", end=" ")
#     for j in range(i, n-1):
#         print("*", end=" ")
#     for j in range(i, n):
#         print("*", end=" ")
#     print()

""" full pyramid """
# n = int(input("enter the rows : "))
# for i in range(n):
#     for j in range(i,n):
#         print(" ", end="")
#     for j in range(i+1):
#         print("* ", end="")
#     print()

""" Reverse full pyramid """
# n = int(input("enter the rows : "))
# for i in range(n):
#     for j in range(i+1):
#         print(" ", end="")
#     for j in range(i,n):
#         print("* ", end="")
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

""" hour glass """
# n = int(input("enter the rows : "))
# for i in range(n-1):
#     for j in range(i+1):
#         print(" ", end="")
#     for j in range(i,n):
#         print("* ", end="")
#     print()
# for i in range(n):
#     for j in range(n-i):
#         print(" ", end="")
#     for j in range(i+1):
#         print("* ", end="")
#     print()

""" ascci values :
 A - 65 to Z - 90 ; a - 97 to z - 122  """
# to print A to Z :
# for i in range(65,91):
#     print(chr(i), " ", end="")
# to print a to z :
# for i in range(97, 123):
#     print(chr(i), " ", end="")

""" Hollow star patterns :"""
""" Basic of indexes :
first row : i = 0
last row : i = n-1
first column : j = 0
last column : j = n-1
middle row or column : n//2
major diagonal : i == j
left diagonal : i+j == n-1     """

""" Hollow square pattern : """
# n = 5
# for i in range(n):
#     for j in range(n):
#         if i == 0 or j == 0 or i == n-1 or j == n-1:
#             print("* ", end=" ")
#         else:
#             print("  ", end=" ")
#     print()

""" Hollow increasing triangle pattern : """
# n = 5
# for i in range(n):
#     for j in range(i+1):
#         if i == n-1 or j == 0 or j == i:
#             print("* ", end=" ")
#         else:
#             print("  ", end=" ")
#     print()

""" Hollow decreasing triangle pattern : """
# n = 5
# for i in range(n):
#     for j in range(i, n):
#         if i == 0 or j == i or j == n-1:
#             print("* ", end=" ")
#         else:
#             print("  ", end=" ")
#     print()

""" Hollow hill pattern : """
# n = 5
# for i in range(n):
#     for j in range(i, n):
#         print(" ", end=" ")
#     for j in range(i):
#         if i == n-1 or j == 0:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     for j in range(i+1):
#         if i == n-1 or j == i:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#     print()

""" hollow full pyramid """
# n = 5
# for i in range(n):
#     for j in range(i, n):
#         print(" ", end="")
#     for j in range(i+1):
#         if i == n-1 or j == 0 or j == i:
#             print("* ", end="")
#         else:
#             print("  ", end="")
#     print()
"""  Reverse hollow full pyramid """
# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print(" ", end="")
#     for j in range(i, n):
#         if i == 0 or j == i or j == n-1:
#             print("* ", end="")
#         else:
#             print("  ", end="")
#     print()

""" hollow diamond """
# n = 5
# for i in range(n-1):
#     for j in range(i, n):
#         print(" ", end="")
#     for j in range(i+1):
#         if j == 0 or j == i:
#             print("* ", end="")
#         else:
#             print("  ", end="")
#     print()
# for i in range(n):
#     for j in range(i+1):
#         print(" ", end="")
#     for j in range(i, n):
#         if j == i or j == n-1:
#             print("* ", end="")
#         else:
#             print("  ", end="")
#     print()

""" Hollow hour glass """
# n = 5
# for i in range(n-1):
#     for j in range(i+1):
#         print(" ", end="")
#     for j in range(i, n):
#         if i == 0 or j == i or j == n-1:
#             print("* ", end="")
#         else:
#             print("  ", end="")
#     print()
# for i in range(n):
#     for j in range(i, n):
#         print(" ", end="")
#     for j in range(i+1):
#         if i == n-1 or j == 0 or j == i:
#             print("* ", end="")
#         else:
#             print("  ", end="")
#     print()

""" Heart shape pattern """
# n = int(input("enter the rows :"))
# m = int(input("enter the rows :"))
# for i in range(n-1):
#     for j in range(i, n):
#         print(" ", end="")
#     for j in range(i+1):
#         print("*", end=" ")
#     for j in range(2*(n-i-1)):  # we need twice the space for 2nd triangle than the first triangle and instead of (i,n) : n-i-1
#         print(" ", end="")
#     for j in range(i+1):
#         print("*", end=" ")
#     print()
# for i in range(m):
#     for j in range(i+1):
#         print(" ", end="")
#     for j in range(i, m):
#         print("*", end=" ")
#     print()

""" Hollow heart pattern """
# n = int(input("enter the rows : "))
# m = int(input("enter the rows: "))
# for i in range(n-1):
#     for j in range(i, n):
#         print(" ", end="")
#     for j in range(i+1):
#         if j == 0 or j == i:
#             print("* ", end="")
#         else:
#             print("  ", end="")
#     for j in range(2*(n-i-1)):
#         print(" ", end="")
#     for j in range(i+1):
#         if j == 0 or j == i:
#             print("* ", end="")
#         else:
#             print("  ", end="")
#     print()
# for i in range(m):
#     for j in range(i+1):
#         print(" ", end="")
#     for j in range(i, m):
#         if j == i or j == m-1:
#             print("* ", end="")
#         else:
#             print("  ", end="")
#     print()

""" Number pattern program : """
# n = 5
# for i in range(n):
#     for j in range(i+1):
#         print("1", end=" ")
#     print()
# 2)
# n = 5
# p = 1
# for i in range(n):
#     for j in range(i+1):
#         print(p, end=" ")
#     p += 1
#     print()
# 3)
# n = 5
# p = 5
# for i in range(n):
#     for j in range(i+1):
#         print(p, end=" ")
#     p -= 1
#     print()
# 4) Increasing triangle with increment of 2
# n = 5
# p = 0
# for i in range(n):
#     for j in range(i+1):
#         print(p, end=" ")
#     p += 2
#     print()
# 5) two repeated values at even and odd row example
# n = 5
# p = 1
# for i in range(n):
#     for j in range(i+1):
#         if i % 2 == 0:
#             print(p, end=" ")
#         else:
#             print(2, end=" ")
#     print()
# 6) Diamond pattern
# n = 5
# p = 1
# for i in range(n-1):
#     for j in range(i, n):
#         print(" ", end="")
#     for j in range(i+1):
#         print(p, end=" ")
#     p += 1
#     print()
# p = 1
# for i in range(n):
#     for j in range(i+1):
#         print(" ", end="")
#     for j in range(i, n):
#         print(p, end=" ")
#     p += 1
#     print()
""" column increment """
# # 1) increasing triangle
# n = 5
# for i in range(n):
#     p = 1
#     for j in range(i+1):
#         print(p, end=" ")
#         p += 1
#     print()
# 2) Decreasing triangle
# n = 5
# for i in range(n):
#     p = 1
#     for j in range(i+1):
#         print(" ", end=" ")
#     for j in range(i, n):
#         print(p, end=" ")
#         p += 1
#     print()
# 3) Hill pattern
# n = 5
# for i in range(n):
#     p = 1
#     for j in range(i, n):
#         print(" ", end=" ")
#     for j in range(i):
#         print(p, end=" ")
#         p += 1
#     for j in range(i+1):
#         print(p, end=" ")
#         p += 1
#     print()
# 4) Diamond pattern
# n = 5
# for i in range(n-1):
#     p = 1
#     for j in range(i, n):
#         print(" ", end="")
#     for j in range(i+1):
#         print(p, end=" ")
#         p += 1
#     print()
# for i in range(n):
#     p = 1
#     for j in range(i+1):
#         print(" ", end="")
#     for j in range(i, n):
#         print(p, end=" ")
#         p += 1
#     print()
# 5) Decreasing triangle with different starting values
# n = 5
# k = 5
# for i in range(n):
#     p = k
#     for j in range(i+1):
#         print(" ", end=" ")
#     for j in range(i, n):
#         print(p, end=" ")
#         p -= 1
#     k -= 1
#     print()
# 6) Hill pattern
# n = 5
# for i in range(n):
#     p = 1
#     for j in range(i, n):
#         print(" ", end=" ")
#     for j in range(i):
#         print(p, end=" ")
#         p += 1
#     for j in range(i+1):
#         print(p, end=" ")
#         p -= 1
#     print()
# Floyd triangle
# n = 5
# p = 1
# for i in range(n):
#     for j in range(i+1):
#         print(p, end=" ")
#         p += 1
#     print()
