""" python program to sum all the items in a dictionary. """
# dict1 = {"maths": 94, "science": 88, "english": 80, "hindi": 77}
# # Method 1:
# sum = 0
# for i in dict1.values():
#     sum += i
# print(sum)
# # Method 2 :
# print(sum(dict1.values()))

""" python program to multiply all the items in a dictionary"""
# dict1 = {"a": 94, "b": 88, "c": 80, "d": 77}
# value = 1
# for i in dict1.values():
#     value = value * i
# print(value, "is the product of all values in the given dictionary")

""" Write a python program to sort a dictionary by key"""
# dict1 = {"swetha": 94, "niki": 88, "ayu": 80, "sanju": 77}
# lst = sorted(dict1.keys())
# print(lst)
# for k in lst:
#     print(k, ":", dict1[k])
# # Another method :
# lst1 = sorted(dict1.items())
# print(dict(lst1))

""" Write a program to check if a dictionary is empty or not."""
# dict1 = {}
# if not bool(dict1):
#     print("Dictionary is empty")

""" Write a python program to convert a list into nested dictionary of keys"""
# lst = [90, 88, 80, 77]
# dict1 = student = {}
# for name in lst:
#     student[name] = {}
#     student = student[name]
# print(dict1)

""" convert two list into dictionary."""
# lst1 = ["name", "age", "place"]
# lst2 = ["swetha", "23", "kerala"]
# dict1 = dict(zip(lst1, lst2))
# print(dict1)

""" Merge two python dictionaries into one."""
# dict1 = {"name": "swetha", "age": 23, "place": "kerala"}
# dict2 = {"course": "python", "fee": 29500}
# dict1.update(dict2)
# print(dict1)

""" print the value of key "history" from the below dict."""
# sampleDict = {
#     "class": {
#         "student": {
#             "name": "mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }
# print(sampleDict["class"]["student"]["marks"]["history"])

""" Initialize dictionary with default values."""
# student = {"swetha", "niki", "ayu"}
# default = {"designation": "student", "Department": "B.tech"}
# dict1 = dict.fromkeys(student, default)
# print(dict1)

""" Create a dictionary by extracting the keys from a given dictionary"""
# dict1 = {"name": "swetha", "age": 23, "place": "kerala"}
# x = dict.keys(dict1)
# print(x)
# another problem :
# sampleDict = {
#     "class": {
#         "student": {
#             "name": "mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }

""" Delete a list of keys from a dictionary."""
# dict1 = {"name": "swetha", "age": 23, "place": "kerala"}
# lst = ["age", "place"]
# for key in lst:
#     dict1.pop(key)
# print(dict1)
# # For single key delete :
# del dict1["age"]
# print(dict1)

""" Check if values exist in a dictionary."""
# dict1 = {"name": "swetha", "place": "kerala", "Qualification": "B.tech"}
# value = input("Enter the value to be checked : ")
# if value in dict1.values():
#     print(value, "exist in dictionary")
# else:
#     print(value, "doesn't exist in dictionary")

""" Rename key of a dictionary."""
# colors = {
#     1: "purple",
#     2: "black",
#     3: "blue",
#     4: "green",
#     5: "violet"
# }
# print("original Dict :", colors)
# colors[7] = colors.pop(1)
# print("Rename key Dict :", colors)

""" Get the key of a minimum value from the following dictionary."""
# dict1 = {"a": 5, "b": 10, "c": 15, "d": 0.5}
# print(min(dict1, key=dict1.get))

""" Change the value of a key in a nested dictionary."""
# sampleDict = {
#     "class": {
#         "student": {
#             "name": "mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }
# sampleDict["class"]["student"]["marks"]["history"] = 88
# print(sampleDict)

# PART 2
""" Write a code to reverse a number"""
# n = int(input("Enter the number : "))
# n1 = str(n)
# r1 = n1[::-1]
# r2 = int(r1)
# print("reversed number is", r2)
# # Another method :
# n = int(input("Enter the number : "))
# rev = 0
# while n > 0:
#     rev = n % 10
#     n = n//10
#     print(rev, end="")

""" Write a code of greatest common divisor."""
# num1 = int(input("Enter the  first number : "))
# num2 = int(input("Enter the second number : "))
# if num1 > num2:
#     mn = num2
# else:
#     mn = num1
# for i in range(1, mn+1):
#     if num1%i == 0 and num2%i == 0:
#         gdc = i
# print("The greatest common divisor is ", gdc)

""" Write a code to check if two strings are anagram or not."""
# s1 = str(input("enter the string 1 : "))
# s2 = str(input("enter the string 2 : "))
# s1 = s1.replace(" ", " ").lower()
# s2 = s2.replace(" ", " ").lower()
# if len(s1) == len(s2) and sorted(s1) == sorted(s2):
#     print("Anagram")
# else:
#     print("Not anagram")

""" Write code to check if the given string is palindrome or not."""
# s1 = str(input("enter the string : "))
# s2 = s1[::-1]
# if s1 == s2:
#     print("the string is palindrome")
# else:
#     print("the string is not palindrome")

""" Write a code to calculate the frequency of characters in a string."""
# str1 = input("Enter the string : ")
# dict1 = dict()
# for i in str1:
#     if i in dict1:
#         dict1[i] += 1
#     else:
#         dict1[i] = 1
# print(dict1)
# # Modified method :
# str1 = input("Enter the string : ")
# dict1 = dict()
# for i in str1:
#     dict1[i] = dict1.get(i, 0) + 1
# print(dict1)
# # Another method :
# str1 = str(input("Enter the string : "))
# for i in str1:
#     t = str1.count(i)
#     print(i, "occurs", t, "times")

""" Write code to check if two strings match where one string contains wildcard."""

""" Write a code to check whether a given year is leap year or not."""
# year = int(input("Enter the year : "))
# if year%4 == 0 and year%100 != 0 or year%400 == 0:
#     print(year, " is a leap year")
# else:
#     print(year, "is not a leap year")

""" Find non-repeating characters in a string."""
# str1 = input("Enter the string : ")
# str2 = ""
# for i in str1:
#     if str1.count(i)>1:
#         pass
#     else:
#         str2 += i
# print("The non repeating characters in string are:", str2)

""" Write a code to find circular rotation of an array by k position."""

""" Whether a character is a vowel or consonant."""
# char = input("Enter the character : ")
# x = char.lower()
# print(x)
# if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
#     print("The entered character is vowel")
# else:
#     print("The entered character is Consonant")















