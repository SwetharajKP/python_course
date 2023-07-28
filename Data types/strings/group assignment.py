""" python program to count unique values inside a list
    eg : lst = [10,20,10,30,20,10,50,50,40,10,40]
        unique values from A = [10,20,30,40,50]          """
# lst = [10, 20, 10, 30, 20, 10, 50, 50, 40, 10, 40]
# unique_lst = []
# for i in lst:
#     if i not in unique_lst:
#         unique_lst.append(i)
# print(unique_lst)

""" write a python program to get the largest number from a list """
# lst = [10, 20, 4, 45, 99]
# lst.sort()
# print(lst)
# print("The largest number is :", lst[-1])
# # And for 2nd largest number:
# print("The second largest number is :", lst[-2])

""" write a python program to count the number of strings from a given list of strings.
    The string length is 2 or more and the first and last characters are the same.
    eg : lst = ["abc","xyz","aba",1221]
         expected result : 2                                                               """

# lst = ["abc", "xyz", "aba", "1221", "343", "def"]
# c = 0
# for i in lst:
#     if len(i) > 1 and i[0] == i[-1]:
#         print(i)
#         c += 1
# print("No. of string are in lst :", c)

""" write a python function that takes two lists and returns true if they have at least one common member"""
# lst1 = [1, 2, 3, 4, 5]
# lst2 = [5, 6, 7, 8, 9]
# for i in lst1:
#     for j in lst2:
#         if i == j:
#             print("True")

""" python program to sort list according to the length of the elements"""
# num_lst = ["nikita", "sree", "ayu", "k", "jk"]
# num_lst.sort(key=len)
# print(num_lst)

""" Python program to swap the first and last value of a list"""
# lst = [4, 8, 5, 9]
# pos1, pos2 = 0, 3
# lst[pos1], lst[pos2] = lst[pos2], lst[pos1]
# print(lst)

""" write a program to add 7000 after 6000 in the following python list
                     lst1 = [10,20[300,400,[5000,6000],500],30,40]
    expected output:  lst1 = [10,20[300,400,[5000,6000,7000],500],30,40]      """
# lst1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# lst1[2][2].append(7000)
# print(lst1)





















