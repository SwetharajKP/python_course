""" Python program to count the number of vowels present in a string using sets."""
# str1 = input("enter the string : ")
# c = 0
# vowels = set("aeiou")
# for x in str1:
#     if x in vowels:
#         c += 1
# print("number of vowels in the given string :", c)

""" Python program to check common letters in two input strings"""
# str1 = input("enter the 1st string : ")
# str2 = input("enter the 2nd string : ")
# set1 = set(str1)
# set2 = set(str2)
# print(set1)
# print(set2)
# set3 = set1.intersection(set2)
# print("common letters :", set3)

""" Python program that display which letter are in the first string but not in the second"""
# str1 = input("enter the 1st string : ")
# str2 = input("enter the 2nd string : ")
# set1 = set(str1)
# set2 = set(str2)
# set3 = set1.difference(set2)
# print("The letters present in first string and not in the second string :", set3)

""" Python program that displays which letters are presented in both the strings"""
# str1 = input("enter the 1st string : ").split()
# str2 = input("enter the 2nd string : ").split()
# print(str1)
# print(str2)
# set1 = set(str1)
# set2 = set(str2)
# set3 = set1.union(set2)
# print("The letters present in both string :", set3)

""" Python program that display which letters are in the two strings but not in both"""
# str1 = input("enter the 1st string : ").split()
# str2 = input("enter the 2nd string : ").split()
# set1 = set(str1)
# set2 = set(str2)
# set3 = set1.symmetric_difference(set2)
# print("Letters which are in two string but not in both :", set3)

""" Write a python program to create an intersection of sets. """
# set1 = set(input("enter the items : ").split())
# print(set1)
# set2 = set(input("enter the items : ").split())
# print(set2)
# set3 = set1.intersection(set2)
# print("Common letter :", set3)

""" Write a python program to create a union of sets. """
# set1 = set(input("enter the items : ").split())
# print(set1)
# set2 = set(input("enter the items : ").split())
# print(set2)
# set3 = set1.union(set2)
# print(set3)

""" Write a python program to create set difference"""
# set1 = set(input("enter the items : ").split())
# print(set1)
# set2 = set(input("enter the items : ").split())
# print(set2)
# set3 = set1.difference(set2)
# print(set3)

""" Write a python program to create a symmetric_difference """
# set1 = set(input("enter the items : ").split())
# print(set1)
# set2 = set(input("enter the items : ").split())
# print(set2)
# set3 = set1.symmetric_difference(set2)
# print(set3)

""" Write a python program to check if a set is a subset of another set"""
# set1 = set(input("enter the items : ").split())
# print(set1)
# set2 = set(input("enter the items : ").split())
# print(set2)
# set3 = set1.issubset(set2)
# print(set3)
# # The issubset() method returns true if all items in a set exists in the specified set, otherwise it returns false

""" Create a set of values that are in all of these sets. """
# set1 = {1, 2, 3}
# set2 = {2, 3, 4}
# set3 = {3, 4, 5}
# set4 = set1.intersection(set2, set3)
# print(set4)

""" Create a set of values which are not in all of these sets"""
# set1 = {1, 2, 3}
# set2 = {2, 3, 4}
# set3 = {3, 4, 5}
# set4 = set1.difference(set2, set3)
# print(set4)

""" We have a list which has some duplicates and we want to remove those. """
# lst = [1, 2, 3, 1, 2, 3]
# lst1 = list(set(lst))
# print(lst1)
# # So the inner function set removes the duplicate and the outer function cast it back to a list

# 1.
# employees = ["corey", "jim", "steven", "april", "judy", "jenn", "john", "jane"]
# gym_members = ["april", "john", "corey"]
# developers = ["judy", "corey", "steven", "jene", "april"]
# # common employees from gym_members and developers :
# result1 = set(gym_members).intersection(developers)
# print(result1)
# # employees who are neither gym_members and  developers :
# result2 = set(employees).difference(gym_members, developers)
# print(result2)

""" When we use the assign operator (=), it only create a new variable that shares the reference of the 
original object. In order to create "real copies" of these objects, we can use the copy module in python.
   syntax of Deep copy : copy.deepcopy(x)
   syntax of shallow copy : copy.copy(x)        """

""" Write a python program to create a shallow copy of set."""
# set1 = {"apple", "banana", "cherry"}
# set2 = copy.copy(set1)
# print(set1)
# print(set2)

""" Write a python program to clear a set"""
# set1 = {"apple", "banana", "cherry"}
# set1.clear()
# print(set1)

""" Write a python program to use of frozen-sets"""
# x = frozenset([1, 2, 3, 4, 5])
# y = frozenset([3, 4, 5, 6, 7])
# # use isdisjoint() : returns true if the set has no element in common with other
# print(x.isdisjoint(y))
# # use difference() :
# print(x.difference(y))
# # new set with elements from both x and y
# print(x | y)

" Write a python program to find maximum and minimum values in a set"
# num = {45, 78, 12, 46, 98, 66, 53, 21, 63, 87, 89, 91}
# print("maximum value =", max(num))
# print("minimum value =", min(num))

""" Write a python to find the length of a set"""
# num = {45, 78, 12, 46, 98, 66, 53, 21, 63, 87, 89, 91}
# print("length of the given set =", len(num))

""" Write a python program to check if a given value is present in a set or not"""
# num = {45, 78, 12, 46, 98, 66, 53, 21, 63, 87, 89, 91}
# n = int(input("enter the value : "))
# if n in num:
#     print(n, "is present in the set")
# else:
#     print(n, "is not present in the set ")

""" Write a python program to check if two given sets have no common elements"""
# set1 = {1, 2, 3, 4}
# set2 = {5, 6, 7, 8}
# x = set1.isdisjoint(set2)
# print(x)























