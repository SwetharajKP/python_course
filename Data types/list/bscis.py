""" List : list are used to store multiple items in a single variable.
list items are ordered , changeable , and allow duplicate values      """
# List allow duplicate value :
# lst = ["apple", "banana", "cherry", "apple", "cherry"]
# print(lst)

""" List length : To determine how many items a list has, use the len() function:     """
# lst = ["apple", "banana", "cherry", "apple", "cherry"]
# print(len(lst))

""" List items- Data types : List items can be of any data type          """
# string,int and boolean data types:
# lst1 = ["apple", "banana", "cherry"]
# lst2 = [1, 2, 3, 4, 5]
# lst3 = [True, False, False]
# print(lst1)
# print(lst2)
# print(lst3)

# A list can contain different data types :
# eg : A list with strings,integers and boolean values :
# lst = ["abc", 34, True, 40, "male"]
# print(lst)

# 1. Remove 'r' from the following string :
# str1 = "priya"
# lst = list(str1)
# print(lst)
# lst.remove("r")
# print(lst)
# print("".join(lst))

# checking if indexing is possible in list :
# items = ["apple", 123, "orange", 9.1, True]
# print(items[4])
# Let see if slicing is possible : we want o/p from apple to orange
# print(items[:3])

""" 1. Append() : this method is used to add an element at the end of the existing list
       syntax : lst_name.append(new_element)                             """
# items = ["apple", 123, "orange", 9.4, "kiwi", True]
# items_names.append("grapes")
# print(items_names) # here only one element at a time can be added
# items.append(["grapes", "banana", 2345])
# print(items)

""" 2. extend() : """
# item = ["apple", 123, "orange", 9.4, "kiwi", True]
# lst = ["ford", "volvo"]
# item.extend(lst)
# print(item)

""" 3. insert() : This method is used to insert an element in a particular position of
                  the existing list.
      syntax : list_name.insert(position_number,new_element)       """
# name_lst = ["niki", "ayu", "sana"]
# I want to insert mina after ayu :
# name_lst.insert(2, "mina")
# print(name_lst)

# If we want to remove an item :
# item = ["apple", 123, "orange", 9.4, "kiwi", True]
# item.pop(2)
# print(item)
# Here we have to just say the position of element which we have to remove
# item.remove("apple")
# print(item)
# And here we have to just mention the element we have to remove

# Default pop :
# item = ["apple", 123, "orange", 9.4, "kiwi", True]
# item.pop()
# print(item)
# End of the element will be removed






















