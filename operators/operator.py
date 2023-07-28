"""  PYTHON OPERATORS:
     Operators are used to perform operations on variables and values.
     python  divides the operators in the following group :        """

""" 1) python Arithmetic operators :
         Arithmetic operators are used with numerical values to perform common mathematical operations :

1) Addition (+) : x+y """
# x = 5
# y = 3
# print( x+y)

""" 2) subtraction (-) : x-y  """
# x = 5
# y = 3
# print(x-y)

""" 3) multiplication (*) : x*y  """
# x = 5
# y = 3
# print(x*y)

""" 4) division (/) : x/y  """
# x = 12
# y = 3
# print(12/3)

""" 5) modulus (%) : x%y ( its the reminder of x%Y ) """
# x = 5
# y = 2
# print(x % y)

""" exponential ( ** ) : ( x**y ) """
# x = 2
# y = 5
# print(x ** y)  # same as 2*2*2*2*2

""" floor division (//) : (x//y)  """
# x = 15
# y = 2
# print(x//y) # rounds the results

"""   += : x += 3 (x = x +3)     """
# x = 5
# x += 3
# print(x)

"""  -= : x -= 3 (x=x-3)"""
# x = 5
# x -= 3
# print(x)

"""  *= : x *= 3 (x = x*3)  """
# x = 5
# x *= 3
# print(x)

""" /= : x /= 3 (x = x/3)   """
# x = 5
# x /= 3
# print(x)


""" %= : x %=3 (x = x%3)   """
# x = 5
# x %= 3
# print(x)

""" //= : x//=3 (x = x//3)  """
# x = 5
# x //= 3
# print(x)

""" 2) python comparison operators : comparison operators are used to compare two values """
""" i) equal (==) : (x == y) """
# x = 5
# y = 3
# print(x == y) # returns false because 5 is not equal to 3

""" ii) not equal ( != ): ( x != y) """
# x = 5
# y = 3
# print(x != y) # returns true because 5 is not equal to 3

""" iii) greater than ( > ) : (x > y)"""
# x = 5
# y = 3
# print(x > 3) # returns true because 5 is greater than 3

""" iv) less than (<) : (x < y) """
# x = 5
# y = 3
# print(x < y) # returns false because 5 is not less than 3

""" v) greater than or equal to (>=): (x >= y) """
# x = 5
# y = 3
# print(x >= y) # returns true because 5 is greater,or equal to 3

""" vi)less than or equal to (<=): (x <= y) """
# x = 5
# y = 3
# print(x <= y) # returns false because 5 is neither less than,or equal to 3

""" 3) python logical operators : are used to combine conditional statements."""
""" i) and : returns true if both statements are true """
# x = 5
# print(x > 3 and x < 10)

""" ii) or : returns true if one of the statement is true """
# x = 5
# print(x > 3 or x < 4)

""" iii) not : reverse the results """
# x = 5
# print(not(x > 3 and x < 10)) # returns false because not is used to reverse the result

""" 4) python identity operators: are used to compare the objects, not if they are equal but if
they are actually the same object, with same memory location"""

""" i) is : returns true if both the variables are the same object"""
# x = ["apple","banana"]
# y = ["apple","banana"]
# z = x
# print(x is z) # returns true because z is the same object as x
# print(x is y) # returns false because x is not the same object as y, even if they have the same content
# print( x == y) # returns true because x is equal to y

""" 5) python membership operators : are used to test if a sequence is presented in an object"""

""" i) in : returns true if a sequence with the specific value is presented in the object """
# x = ["apple","banana"]
# print("banana" in x)

""" ii) not in : returns true if a sequence with the specified value is not presented in the object"""
# x = ["apple","banana"]
# print("mango" not in x)

""" class_notes_file_handling :"""
# f = open("sample.txt",mode="w")
# f.write("Hello! welcome to sample.txt\nThis file is for testing purpose\nGood Luck!")
# f.close()
