""" Set : set are used to store multiple items in a single variable.
          1. A set is a collection which is unordered, unchangeable and unindexed.
          2. sets are written with {}
          3. set items do not allow duplicate values
          4. set items are unchangeable, but you can remove items and add new items."""

""" Duplicate values will be ignored :   """
# set1 = {"apple", "banana", "cherry", "apple", 1, True}
# print(set1)
# # The values of True and 1 are considered the same values in set and treated as duplicates.

""" Length of a set : To determine how many items a set has, use the len() function . """
# # Get the number of items in a set :
# set1 = {"apple", "banana", "cherry", "apple", 1, True}
# print(len(set1))

""" Set items - Data Types : set items can be of any data type """
# # string,int and boolean data types :
# set1 = {"apple", "banana", "cherry"}
# print(set1)
# set2 = {1, 2, 3, 4, 5}
# print(set2)
# set3 = {True, False, False}
# print(set3)

# # A set with strings,int and boolean values :
# set1 = {"abc", 34, True, 40, "male"}
# print(set1)

""" Access set items : 
you can't access items in a set by referring to an index or a key.
But you can loop through the set items using a "for loop", or ask if a specified value is
presented in a set by using the "in" keyword. """
# # Loop through the set, and print the values:
# set1 = {"apple", "banana", "cherry"}
# for i in set1:
#     print(i)

# Check if "banana" is present in the set :
# set1 = {"apple", "banana", "cherry"}
# print("banana" in set1)

""" Add items to a set :
Once a set is created, you can't change its items, but you can add new items.
To add one item to a set use the add() method. """
# # Add an item to a set, using add() method :
# set1 = {"apple", "banana", "cherry"}
# set1.add("orange")
# print(set1)

""" Add sets : 
To add items from one set into the current set, use the update() method."""
# set1 = {"apple", "banana", "cherry"}
# set2 = {"pineapple", "mango", "papaya"}
# set1.update(set2)
# print(set1)

""" Add Any Iterable :
The object in the update() method does not have to be a set, it can be any iterable object
(tuple,dictionaries,list,etc) """
# set1 = {"apple", "banana", "cherry"}
# lst = ["kiwi", "orange"]
# set1.update(lst)
# print(set1)

""" Remove item : 
To remove an item in a set, use the remove(), or the discard() method. """
# # Remove "banana" by using the remove() method :
# set1 = {"apple", "banana", "cherry"}
# set1.remove("banana")
# print(set1)
# # If the item to remove does not exist, remove() will raise an error.

# # Remove "banana" using the discard() method :
# set1 = {"apple", "banana", "cherry"}
# set1.discard("banana")
# print(set1)
# # If the item to remove does not exist, discard() method does NOT raise an error.

"""You can also use the pop() method to remove an item, but this method will remove a random
item, so you cannot be sure what item that gets removed."""
# # Remove a random item by using pop() method :
# set1 = {"apple", "banana", "cherry"}
# x = set1.pop()
# print(x)
# print(set1)

# # Clear() method : Empties the set
# set1 = {"apple", "banana", "cherry"}
# set1.clear()
# print(set1)

# # The del keyword will delete the set completely :
# set1 = {"apple", "banana", "cherry"}
# del set1
# print(set1)
# # This will raise an error because the set no longer exists

""" Loop Items :
You can loop through the set items by using a "for loop". """
# # Loop through the set, and print the values :
# set1 = {"apple", "banana", "cherry"}
# for i in set1:
#     print(i)

""" Join Two Set :
There are several ways to join two or more sets in python.
You can use the Union() method that returns a new set containing all items from both sets,
or the Update() method that inserts all the items from one set into another : """

# # Union() method : It returns a new set with all items from both sets :
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = set1.union(set2)
# print(set3)

# # Update() method : Inserts the items of set2 into set1 :
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set1.update(set2)
# print(set1)
# # Both union() and update() will exclude any duplicate items.

""" Keep ONLY the Duplicates : """
""" intersection_update() method will keep only the items that are presented in both sets."""
# # Eg : keep the items that exist in both x and y set.
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# x.intersection_update(y)
# print(x)

""" intersection() method :
It will return a new set, that only contains items that are present in both sets."""
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# z = x.intersection(y)
# print(z)

""" Keep All, but Not the duplicates :"""
""" Symmetric_difference_update() method will keep only the elements that are NOT present 
    in both sets."""
# # Keep the items that are not present in both sets :
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# x.symmetric_difference_update(y)
# print(x)

""" Symmetric_difference() method will return a new set, that contains only the elements
that are NOT present in both sets. """
# x = {"apple", "banana", "cherry"}
# y = {"google", "microsoft", "apple"}
# z = x.symmetric_difference(y)
# print(z)

""" Exercise :"""
# # Check if "apple" is present in the fruits set.
# fruits = {"apple", "banana", "cherry"}
# print("apple" in fruits)

# # use the add method to add "orange" to the fruits set.
# fruits = {"apple", "banana", "cherry"}
# fruits.add("orange")
# print(fruits)

# # use the correct method to add multiple items (more_fruits) to the fruits set.
# fruits = {"apple", "banana", "cherry"}
# more_fruits = {"orange", "mango"}
# fruits.update(more_fruits)
# print(fruits)

# # remove"banana" from the fruits set.
# fruits = {"apple", "banana", "cherry"}
# fruits.remove("banana")
# print(fruits)
# # Another method :
# fruits.discard("banana")
# print(fruits)

""" Running notes of class :"""
# set1 = {1, 2, 5, 6, "baa"}
# # we have to check if it is existing
# print(5 in set1)
# # set is unchangeable once it's created, but we can add element
# # add() :
# set1.add("apple")
# print(set1)
# # Update():
# set2 = {"orange", "pineapple", "grape"}
# set1.update(set2)
# print(set1)
# If we want to add only one element in set
# set1 = {1, 2, 5, 6, "baa"}
# set1.update("kiwi")
# print(set1) # o/p : 1,2,5,6,baa,k,w,i

# Update set by list
# set1 = {1, 2, 5, 6, "baa"}
# lst = ["cars", "jeeps", "lorry"]
# set1.update(lst)
# print(set1)

# # remove():
# set1.remove("baa")
# print(set1)


























