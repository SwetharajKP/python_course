""" Dictionary : dictionaries are used to store data values in key:value pairs
                 1. mutable
                 2. ordered
                 3. indexed
                 4. no duplicate(key)     """
# # Create and print a dictionary :
# dict1 = {"brand": "ford", "model": "mustang", "year": 1964}
# print(dict1)

"""Dictionary Item : items are presented in key:value pairs, and can be referred by using the key name. """
# # Print the "brand" value of the dictionary:
# dict1 = {"brand": "ford", "model": "mustang", "year": 1964}
# print(dict1["brand"])

""" Duplicates NOT Allowed : dictionaries cannot have two items with same key :"""
# # Duplicate values will overwrite existing values :
# dict1 = {"brand": "ford", "model": "mustang", "year": 1964, "year": 2020}
# print(dict1["year"])

""" Dictionary length : To determine how many items a dictionary has, use the len()function """
# dict1 = {"brand": "ford", "model": "mustang", "year": 1964}
# print(len(dict1))

""" Dictionary Item - Data Types : The values in dictionary items can be of any data type: """
# # string,int,boolean,and list data types:
# dict1 = {"brand": "ford", "electric": False, "year": 1964, "colors": ["red", "white", "blue"]}
# print(dict1)
# print(type(dict1))

""" Accessing Items : You can access the items of a dictionary by referring to its key name."""
# # Get the value of the "model" key
# dict1 = {"brand": "ford", "model": "mustang", "year": 1964}
# print(dict1["model"])
# # There is also a method called get() that will give you the same result :
# x = dict1.get("model")
# print(x)

""" Get Keys : The keys() method will return a list of all the keys in the dictionary. """
# dict1 = {"brand": "ford", "model": "mustang", "year": 1964}
# x = dict1.keys()
# print(x)

# Any change done to dictionary will be reflected in the keys list.
# dict1 = {"brand": "ford", "model": "mustang", "year": 1964}
# x = dict1.keys()
# print(x) # before the change
# dict1["color"] = "white"
# print(x) # after the change

""" Get values : The values() method will return a list of all the values in the dictionary"""
# dict1 = {"brand": "ford", "model": "mustang", "year": 1964}
# x = dict1.values()
# print(x)
# # Make a change in the original dictionary, and see that the values list gets updated as well :
# dict1 = {"brand": "ford", "model": "mustang", "year": 1964}
# x = dict1.values()
# print(x) # before the change
# dict1["year"] = 2020
# print(x) # after the change

""" Get Items : The items() method will return each item in a dictionary, as tuples in a list."""
# dict1 = {"brand": "ford", "model": "mustang", "year": 1964}
# x = dict1.items()
# print(x)

""" Check if Key Exists : To determine if a specified key is present in a dictionary use the "in" keyword. """
# dict1 = {"brand": "ford", "model": "mustang", "year": 1964}
# if "model" in dict1:
#     print("Yes, 'model' is one of the keys in the dict1 dictionary")

""" Change dictionary items :"""
""" change values : you can change the value of a specific item by referring to its key name: """
# dict1 = {"brand": "ford", "model": "mustang", "year": 1964}
# dict1["year"] = 2018
# print(dict1)

""" Update Dictionary : The argument must be a dictionary, or an iterable object with key:value pairs."""
# # update the year by using update() method :
# dict1 = {"brand": "ford", "model": "mustang", "year": 1964}
# dict1.update({"year": 2020})
# print(dict1)

""" Remove Dictionary Items : There are several methods to remove items from a dictionary"""
# # The pop() method removes the item with the specified key name :
# dict1 = {"brand": "ford", "model": "mustang", "year": 1964}
# dict1.pop("model")
# print(dict1)

# # The del() keyword removes the item with the specified key name :
# dict1 = {"brand": "ford", "model": "mustang", "year": 1964}
# del dict1["model"]
# print(dict1)

# The clear() method empties the dictionary
# dict1 = {"brand": "ford", "model": "mustang", "year": 1964}
# dict1.clear()
# print(dict1)

""" Loop Dictionaries :"""
""" Loop through a dictionaries : you can loop through a dictionary by using a for loop.
when looping through a dictionary, the return values are the keys of the dictionary, 
but there are methods to return the values as well.                         """
# # print all key name in the dictionary , one by one :
# dict1 = {"brand": "ford", "model": "mustang", "year": 1964}
# for x in dict1:
#     print(x)
# # print all values in the dictionary one by one :
# dict1 = {"brand": "ford", "model": "mustang", "year": 1964}
# for x in dict1:
#     print(dict1[x])

# loop through both keys and values,by using the items() method :
# dict1 = {"brand": "ford", "model": "mustang", "year": 1964}
# for x, y in dict1.items():
#     print(x, y)

""" Copy Dictionaries :
you can not copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference
to dict1, and changes made in dict1 will automatically also be made in dict2.
There are ways to make a copy,one way is to use the built-in dictionary method copy().            """
# # Make a copy of a dictionary with the copy() method :
# dict1 = {"brand": "ford", "model": "mustang", "year": 1964}
# dict2 = dict1.copy()
# dict2["color"] = "white"
# print(dict1)
# print(dict2)

# Another way to make a copy is to use the built-in function dict() :
# dict1 = {"brand": "ford", "model": "mustang", "year": 1964}
# dict2 = dict(dict1)
# dict2["color"] = "white"
# print(dict1)
# print(dict2)

""" Nested dictionaries :
A dictionary can contain dictionaries,this is called nested dictionaries."""
# # Create a dictionary that contain three dictionaries :
# dict1 = {
#     "child1": {
#         "name": "Emil",
#         "year": 2004
#     },
#     "child2": {
#         "name": "Tobias",
#         "year": 2007
#     },
#     "child3": {
#         "name": "Linus",
#         "year": 2011
#     },
# }
# print(dict1)

""" Access Items in nested dictionaries : 
You can use the name of the dictionaries,starting with the outer dictionary."""
# # print the name of child2 :
# print(dict1["child2"]["name"])

""" fromkeys() method : The fromkeys() method return a dictionary with the specified keys
 and the specified value.
  syntax : dict.fromkeys(key, value)"""
# # create a dictionary with 3 keys, all with the value 0:
# x = ("key1", "key2", "key3")
# y = 0
# print(x, y)
# dict1 = dict.fromkeys(x, y)
# print(dict1)

# # same example as above, but without specifying the value:
# x = ("key1", "key2", "key3")
# dict1 = dict.fromkeys(x)
# print(dict1)
































