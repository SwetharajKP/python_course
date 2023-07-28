"""  reverse a tuple  """
# tuple1 = ("apple", "orange", "banana")
# print(tuple1[::-1]) # slicing
# # Another method :
# lst = list(tuple1)
# lst.reverse()
# print(lst)
# tuple1 = tuple(lst)
# print(tuple1)

""" Access values 20 from the tuple  """
# tuple1 = ("apple", [10, 20, 30], (5, 12, 25))
# print(tuple1[1][1])

""" Swap tuple """
# tuple1 = (11, 22)
# tuple2 = (10, 40)
# tuple1, tuple2 = tuple2, tuple1
# print("tuple1 :", tuple1)
# print("tuple2 :", tuple2)

""" Unpack """
# tuple1 = ("apple", [10, 20, 30], (5, 12, 25))
# (x, y, z) = tuple1
# print(x)
# print(y)
# print(z)
# # Another example :
# (x, *y) = tuple1
# print(x)
# print(y) # here its print everything after x , because it's o/p is in list
# print(tuple(y)) # Therefore we used tuple function to convert list into tuple

""" Write a program to check whether an element exist within a tuple
         tuple1 = ("apple", [10, 20, 30], (5, 12, 25))             """
# tuple1 = ("apple", [10, 20, 30], (5, 12, 25))
# print("apple" in tuple1) # Membership operator
# # check 20 :
# x = tuple1[1]
# print(x)
# print(x in tuple1)

""" convert tuple into string """
# tuple1 = ("s", "t", "r", "i", "n", "g")
# print("".join(tuple1))
# print(type(tuple1))
# # so we need to assign a variable then do the same process
# x = "".join(tuple1)
# print(x)
# print(type(x))

""" Corresponding index of each element  """
# tuple1 = ("s", "t", "r", "i", "n", "g")
# x = enumerate(tuple1)
# print(tuple(x))
# # print(list(x))

""" zip
    map
    filter
    reduce   """
















