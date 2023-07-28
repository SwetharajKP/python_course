""" python for loops : for loop is used for iterating over a sequence ( that is either a list,a tuple,a dictionary,
    a set, or a string )

    syntax
    --------
    for value in sequence :
    print(value)                  """

""" sequence datatype : list , string , tuple , dictionary , set ."""

""" main python datatype : number , list , string , tuple , dictionary , set , boolean """

""" python datatypes are divided into two group : 
    1) mutable datatype and 2) immutable datatype 
    
    1) mutable datatype : changeable 
    list , dictionary , set
    
    2) immutable datatype : unchangeable
    number,string,tuples,set ( set can be mutable or immutable depends on the value )
    
1) list : list are used to store multiple items in single variable 
          list are created using square brackets [] :
          list items are ordered , changeable .

2) tuple : tuple are used to store multiple items in a single variable
           tuple are created using round brackets ():
           tuple items are ordered , changeable
        
3) set : set are used to store multiple items in a single variable
         set are created using curly bracket {} :
         set items are unordered and unchangeable

4) dictionaries : are used to store data values in " key : value" pairs
                  are written with curly brackets {} and have keys and values
                  items are ordered and changeable                                  """


""" range function"""
""" to print 1 to 10 """
# for i in range(1, 11):
#     print(i)
""" to print 10 to 1 (descending order)"""
# for i in range(10, 0, -1):
#     print(i)
""" to print even number 1 to 10 """
# for i in range(2, 11, 2):
#     print(i)
""" to print even number 10 to 1 """
# for i in range(10, 1, -2):
#     print(i)
""" to print odd number 1 to 10"""
# for i in range(1, 10, 2):
#     print(i)

""" to print odd number 10 to 1 ( descending order) """
# for i in range(9, 0, -2):
#     print(i)

""" to find the sum of n natural numbers  done by conditional statement method """
# # Natural numbers are the numbers which are positive integers which includes numbers 1 to infinity
#
# n = int(input("enter the number :"))
# sum = 0 # initial value
# if n > 0: # condition
#     sum = n*(n + 1)/2  #statement
#     print(sum)
# else:
#     print("no value")

""" to find the sum of n natural numbers  done by for loop method """
# n = int(input("enter the number :"))
# sum = 0
# for i in range(1, n+1):
#     sum += i # sum = sum + i
#     print(sum)

""" break , continue and pass """
# # break : it helps to come out of the loop once the condition is met
# for i in range(1, 11):
#     if i == 5:
#         break
#     print(i)

# Exit the loop when x is "banana" :
# fruits = ["apple", "banana", "cherry"]
# for i in fruits:
#     print(i)
#     if i == "banana":
#         break

# # Exit the loop when x is "banana", but this time the break comes before the print :
# fruits = ["apple", "banana", "cherry"]
# for i in fruits:
#     if i == "banana":
#         break
#     print(i)

# # continue :
# for i in range(1, 11):
#     if i == 5:
#         continue
#     print(i)

# pass
# for i in range(1, 10):
#     pass