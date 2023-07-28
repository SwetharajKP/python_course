""" 1. Remove special symbols/punctuation from a string"""
# str1 = "/* jon is a 2developer & music director"
# str2 = ""
# for i in str1:
#     if i.isalpha() or i.isspace():
#         str2 += i
# print(str2)

"""2. To find if two strings are anagrams or not"""
# s1 = str(input("enter the string 1 : "))
# s2 = str(input("enter the string 2 : "))
# s1 = s1.replace(" ", " ").lower()
# s2 = s2.replace(" ", " ").lower()
# if len(s1) == len(s2) and sorted(s1) == sorted(s2):
#     print("Anagram")
# else:
#     print("Not anagram")

""" 3. To calculate the length of a string without using a library function"""
# str1 = input("enter the string : ")
# count = 0
# for i in str1:
#     count += 1
# print(count)

""" 4. To check if a string is palindrome or not"""
# s1 = str(input("enter the string : "))
# s2 = s1[::-1]
# if s1 == s2:
#     print("the string is palindrome")
# else:
#     print("the string is not palindrome")

""" 5. write a python code to remove all the repeating letters from each words of 
       given sentence"""
# str1 = "let's google the pineapple"
# x1 = ""
# x2 = ""
# for i in str1.split(" "):
#     for j in i:
#         if x1.find(j) == -1:
#             x1 += j
#         else:
#             continue
#     x2 = x2+x1+" "
#     x1 = ""
# print(x2)

""" write a program to separate negative and positive numbers from a given list """
# lst1 = input("enter the numbers :").split()
# lst2 = []
# for i in lst1:
#     lst2.append(int(i))
# print(lst2)
# positive = []
# negative = []
# for i in lst2:
#     if i >= 0:
#         positive.append(i)
#     else:
#         negative.append(i)
# print("positive_lst :", positive)
# print("negative_lst :", negative)

""" write a python program to find the sum of all numbers in a list"""
# lst1 = input("enter the number :").split()
# lst2 = []
# for i in lst1:
#     lst2.append(int(i))
# print(lst2)
# sum = 0
# for i in lst2:
#     sum += i
# print(sum)

""" write a python program to find the largest number in the given list without using max()"""
# lst1 = input("enter the number :").split()
# lst2 = []
# for i in lst1:
#     lst2.append(int(i))
# print(lst2)

# lst = sorted(lst2)
# print(lst)
# print("The largest number is :", lst[-1])

""" write a program to find the common number from the two list"""
# lst1 = [1, 2, 3, 4, 5]
# lst2 = [5, 6, 7, 8, 9]
# lst = []
# for i in lst1:
#     if i in lst2:
#         lst.append(i)
# print("The common number :", lst)
# Another method
# lst1 = [1, 2, 3, 4, 5]
# lst2 = [5, 6, 7, 8, 9]
# lst = []
# for i in lst1:
#     for j in lst2:
#         if i == j:
#             lst.append(i)
# print("The common number :", lst)

""" write a python program to print all even numbers from a given list"""
# lst1 = input("enter the number :").split()
# lst2 = []
# for i in lst1:
#     lst2.append(int(i))
# print(lst2)
# print("Even numbers are")
# for i in lst2:
#     if i % 2 == 0:
#         print(i, end=" ")

""" write a python program to create a list of even numbers and another list of odd numbers
from a given list """
# lst1 = input("enter the number:").split()
# lst2 = []
# for i in lst1:
#     lst2.append(int(i))
# print(lst2)
# even_lst = []
# odd_lst = []
# for i in lst2:
#     if i % 2 == 0:
#         even_lst.append(i)
#     else:
#         odd_lst.append(i)
# print("Even numbers list :", even_lst)
# print("Odd numbers list :", odd_lst)

""" write a python program to remove repeated elements from a given list without using
built-in method
list_to_remove = ["let's","google","the","pineapple","photo","google",photo",""]     """

# lst_to_remove = ["let's", "google", "the", "pineapple", "photo", "google", "photo", ""]
# lst2 = []
# for i in lst_to_remove:
#     if i not in lst2:
#         lst2.append(i)
# print(lst2)

""" [ "www.zframez.com",www.wikipedia.org,"www.asp.net","www.abcd.in"]
write a python program to print website suffixes (com,org,net,in)from this list      """
# lst1 = ["www.zframez.com", "www.wikipedia.org", "www.asp.net", "www.abcd.in"]
# print(lst1[0][-3:])
# print(lst1[1][-3:])
# print(lst1[2][-3:])
# print(lst1[3][-2:])














