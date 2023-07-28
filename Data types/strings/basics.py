"""  Indexing  """
""" 1. python allows you to store an enumerated set of items and access them by their position 
using index
2. In python, index starts from 0    """
# using index with strings :
# s = "Hello World!"
# This string has 12 characters indexed from 0 to 11 . every character , even space has it own index
# print(s[0])
""" similar to string indexing, items in list/tuple are also indexed"""
# car_makes = ["toyota", "honda", "GM"]
# print(car_makes[0])

""" Negative indexes : python also provides another way of indexing,to access items/chars from
                       the end of the list/string"""
# car_makes = ["toyota", "honda", "GM"]
# print(car_makes[-1])
# for complete reverse:
# print(car_makes[::-1])

# Index() method :
""" But what if we have got the value and want to find index of the value"""
# s = "hello python programmers"
# then, use index() method to find out:
# print(s.index("p"))

""" Slicing """
# If I want to extract the substring "python" from following string :
# s = "hello python programmers"
# print(s[6:12])
# if the start index is not specified : it starts from first index(index = 0)
# print(s[:12])
# if the stop index is not specified : it takes all chars from index start to the end of the string
# print(s[13:])

"""what if you want to take non-consecutive string characters or list items
eg : with the string below, you want to extract the characters: b , c, d """
# s = "a1b2c3d4e5f6"
# s[start:stop:step]
# print(s[2:7:2])
# if you don't specify start and stop parameters,only step parameter like this : s[::2]
# print(s[::2])  # then it will take 2-nd character of the whole string, no range limit

# slicing with negative indexes:
# s = "hello python programmers"
# eg : to extract substring "program" from string below, there are two ways of doing it:
# positive indexing:
# print(s[13:20])
# negative indexing :
# print(s[-11:-4])

# eg : to take only 4 last characters in the string
# s = "hi_my_name_is_Alex"
# print(s[-4:])
# or except 4 last characters
# print(s[:-4])

# list slicing with negative indexes: take everything except last item
# ls = ["python", "java", "c++", "PHP", "javascript"]
# print(ls[:-1])

""" string function : """
"""1. replace() : this method is used to replace a sub string in a string with another sub string. 
                           syntax : string.replace(old,new)                                         """

"""2. split() : this method is used to split/break a string into pieces,these pieces returns a list.
                           syntax : string.split("separator")                                        """

""" 3. join() : this method is used to join strings into one string
                           syntax : "separator".join(string_list)                                    """

""" replace() :"""
# name = "geeky show"
# print(name.replace("geeky", "new"))

""" split() : """
# x = "hello_how_are_you"
# print(x.split("_"))
# x = "hello how are you"
# print(x.split(" "))

""" join() : """
# x = ("hello", "how", "are", "you")
# str1 = " ".join(x)
# print(str1)
# print(" ".join(x))

""" 1. create a string made of the first,middle and last character
        eg : str1 = "james" 
              o/p : "jms"                                          """
# str1 = "james"
# first = str1[0]
# l = len(str1)
# mid = int(l/2)
# first = first + str1[mid] + str1[l-1]
# print("new string :", first)

""" To append the new string into the middle of 1st string
    s1 = "hello"
    s2 = "world"
    o/p : heworldllo           """
# s1 = "hello"
# s2 = "world"
# l = len(s1)
# mid = int(l/2)
# x = s1[:mid]
# print(x)
# x = x + s2
# print(x)
# x = x + s1[mid:]
# print("after appending new str :", x)

""" 3. Arrange string characters such that lowercase letter should come first 
       str1 = "hello world"
       o/p : eorldHLLOW"""
# str1 = "Hello World"
# lower = " "
# upper = " "
# for char in str1:
#     if char.islower():
#         lower += char
#         print(lower)
#     else:
#         upper += char
#         print(upper)
# print("Result :", lower+upper) # not clear

""" Python sort()method and sorted() function 
    how are they different and when to use which ?"""

""" To sort a list in python, there are 2 options you can go for :
    - use sort() method on list object
    - use sorted() function                                         """

""" Sorted() method: the sort method change the list directly and doesn't return any value  
            syntax : lst_name.sort()                                                """
# num_lst = [4, 8, 6, 1, 5, 2]
# num_lst.sort()
# print(num_lst)

# because the sort() method doesn't return any value,so we can only call it and doesn't
# assign like this:
# num_lst = [4, 8, 6, 1, 5, 2]
# new_lst = num_lst.sort()

"""key=len : sorts the strings by length,from shortest to longest"""
# num_lst = ["nikita", "sree", "ayu", "k", "jk"]
# num_lst.sort(key=len)
# print(num_lst)

""" with sort() method,the list is changed directly ,list values are sorted,and we are
NO LONGER  retrieve the original order
so if you want to get the original list order later on in your program, thn use the
other option  """

""" sorted() function:
    it's a built-in function, takes the list as an argument and returns a new sorted list,
     and doesn't change the original list   """
# num_lst = [4, 8, 6, 1, 5, 2]
# new_lst = sorted(num_lst)
# print(num_lst)
# print(new_lst)
# new list is created to store sorted values, and original list remains unchanged

""" if you don't want to assign the sorted list to a variable, you can call the function
directly in a statement or expression """
# num_lst = [4, 8, 6, 1, 5, 2]
# print(sorted(num_lst))
































