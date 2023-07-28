""" Function :
         A function is a block of code which only runs when it is called.
         In python a function is defined using the def keyword :
         1. User defined
         2. Builtin
         3. lambda    """

""" Difference b/w args and parameters :
A parameter is the variable listed inside the parentheses in the function definition.
An argument is the value that is sent to the function when it is called.
"""

# # Example :
# def my_function():
#     print("Hello from a function")

""" Calling a function : To call a function, use the function name followed by parenthesis :"""
# def my_function():
#     print("Hello from a function")
# my_function()

# Example 1 :
# def sum():
#     a = 12    # a and b are called local variable because it's inside the function
#     b = 13
#     c = a+b
#     print(c)
# sum()

#
# a = 12  # Here a and b are called global variable because it's outside the function
# b = 13
# def sum():
#     c = a+b
#     print(c)
# sum()

""" Arbitrary Arguments, *args :
If you do not know how many arguments that will be passed into your function, add a * before
the parameter name in the function definition.
This way the function will receive a tuple of arguments, and can access the items accordingly:"""

# # If the number of keyword arguments is unknown, a * before the parameter name :
# def my_function(*kids):
#     print("The youngest child is " + kids[0])
# my_function("Emil", "Tobias", "Linus")

# def my_function(*names):
#     print("Hi", names, "How are you ?")
# my_function("niki", "sreehari", "sanju")

""" Keyword Arguments :
You can also send arguments with the key=value syntax.
This way the ordered of the arguments does not matter.     """
# def my_function(child3, child2, child1):
#     print("The youngest child is ", child3)
# my_function(child3="Linus", child2="Tobias", child1="Emil")

""" Arbitrary keyword Arguments, **kwargs :
If you do not know how many keyword arguments that will be passed into your function, add 
two asterisk: ** before the parameter name in the function definition.
This way the function will receive a dictionary of arguments, and can access the items
accordingly :"""

# # If the number of keyword arguments is unknown, add ** before the parameter name :
# def my_function(**name):
#     print("The last name is " + name["lname"])
# my_function(fname="Swetha", lname="KP")

# # Another example :
# def student_info(**student):
#     print("Highest Qualification of swetha is " + student["college"])
# student_info(school="secondary", high_school="Higher secondary", college="B.tech graduation")

""" Default parameter value :
The following example shows how to use a default parameter value.
If we call the function without arguments, it uses the default value :"""
# def nationality(country="India"):
#     print("I am from " + country)
# nationality()
# nationality("south korea")  # Can add other argument's
# nationality("America")

# # Example :
# def food_items(food):
#     for x in food:
#         print(x)
# food = ["yuppie", "maggie", "chips", "chicken"]
# food_items(food)

# # Another way to do it :
# def food_items(food):
#     for x in food:
#         print(x)
#     return x
# food = ["yuppie", "maggie", "chips", "chicken"]
# food_items(food)

# # What happens if we use "return" before print :
# def food_items(food):
#     for x in food:
#         return x
# food = ["yuppie", "maggie", "chips", "chicken"]
# print(food_items(food))
# # Here return x immediately terminates after its first iteration and go back to function call

"""  define a function which counts vowels and consonant in a word """
# def count(str1):
#     str2 = str1.lower()
#     vowel = 0
#     consonant = 0
#     for x in range(len(str2)):
#         if str2[x] in ["a", "e", "i", "o", "u"]:
#             vowel += 1
#         else:
#             consonant += 1
#     print("The count of vowel = ", vowel)
#     print("The count of consonant = ", consonant)
# str1 = input("Enter the string : ")
# count(str1)
""" range(len()) : allows you to iterate across a iterable/sequence to access each item with
the help of its index."""

# Another method :
# def count(str1):
#     vowels = 0
#     consonant = 0
#     str2 = "AEIOUaeiou"
#     for x in str1:
#         if x in str2:
#             vowels += 1
#         else:
#             consonant += 1
#     print("The count of vowels =", vowels)
#     print("The count of consonant =", consonant)
# str1 = input("Enter the string : ")
# count(str1)

""" Function that accept two numbers as arguments and returns the sum"""
# def function(n,m):
#     sum = n+m
#     return sum
# n = int(input("Enter the number : "))
# m = int(input("Enter the number : "))
# print(function(n, m))

""" A function that accept different values as a parameter and return a list."""
# def food_items(*food):
#     return list(food)
# print(food_items("yuppie", "maggie", "chips", "chicken"))

""" A function that accepts dictionary as a parameter"""
# def fav_idols(**idol):
#     return idol
# print(fav_idols(fav1="jk", fav2="haechan", fav3="heeseung"))

""" Nested function :
A nested function is simply a function within another function :"""

""" How to define a nested function ?
In order to define nested function, just initialize another function within a function
by using the def keyword :
                          def outer_function():
                               def inner function():"""
# # Example 1 :
# def outer_function():
#     print("This is a outer function")
#     def inner_function():
#         print("This is an inner function")
#     inner_function()
# outer_function()

""" Variables in nested function"""
# a = 100    # global variable
# def outer_function():
#     b = 200       # non-local variable
#     print("This is a outer function")
#     def inner_function():
#         c = 300    # local variable
#         print("This is an inner function")
#     inner_function()
# outer_function()
""" Here we can access the variable a and b in the inner function :"""
# a = 100
# def outer_function():
#     b = 200
#     print("This is a outer function")
#     def inner_function():
#         c = 300
#         print(a)
#         print(b)
#         print(c)
#         print("This is an inner function")
#     inner_function()
# outer_function()

""" Why use nested function ?"""
# # 1. Helper function :
# def name(first, last):
#     def fullname():
#         return first + " " + last
#     print("Hi" + " " + fullname())
# name("swetha", "KP")
""" Here def fullname() function is a helper function for def name() function 
Here helper function is helping in concatenating first and last name.       """

# 2. Data privacy :
""" Here we can only access fullname() function inside the name() function and 
If we try to call the fullname() function as global, it will show Name-error.
So its not a global function but a local function which you can't call somewhere else."""

""" class problems :"""
# Example 1:
# def outer_function():
#     def inner_function():
#         print("Have a good day")
#     inner_function()
# outer_function()

# Example 2:
# def increment(number):
#     def inner_increment():
#         return number+1
#     return inner_increment()
# print(increment(10))
# # OR :
# def increment(number):
#     def inner_increment():
#         print(number+1)
#     inner_increment()
# increment(10)

# example 3 :
# def function1():
#     p = "hello guys"
#     def function2():
#         print(p)
#     function2()
# function1()

""" Local Variable :"""
""" What are local variable :
   The variables which are declared inside a function are called as local variables.
   The scope of local variable is limited to that function where it is declared.
   The local variable is available only in the function, not outside the function   """

# def demo():
#     a = 100
#     print(a)
# demo()
# # If I tried to access the variable "a" outside the demo() function than we will get Name-error
# print(a)
# # The parameters are also considered as local variable of the particular function

""" Global variable : 
Variables declared outside the function are called as global variable. """
# a = 500
# def demo(c):
#     print(a)
#     b = 100
#     sum = b+c
#     print(sum)
# demo(200)
# print(a)
# # here c,b,sum are the local variables of function demo() and a is global variable
# # The scope of "a" variable is everything below it

# a = 10
# def demo():
#     b = a+5
#     print(b)
# demo()

""" Global keyword : """
# a = 10
# def demo():
#     a =a+5
#     print(a)
# demo()
""" If we run this program, we get unbound-local-error : local variable 'a' referenced before assigned
Here due to the assignment operator ( = ) the python interpreter will think its a local variable,
instead of a global variable by updating a=10   """

# a = 10
# def demo():
#     global a
#     a = a+5
#     print(a)
# demo()
# print(a)  # 15

""" Return statement in python :"""
# Example : simple interest program :
# p = 10000          # principle
# n = 3              # number of years
# r = 12.25          # rate of interest
# def simple_interest(p,n,r):
#     si = (p*n*r)/100
#     print("simple interest is", si)
# simple_interest(p,n,r)
# If I run this code, I will get the o/p : simple interest is 3675.0

# Here "si" is a local variable, but we want to access it outside the function :
# p = 10000
# n = 3
# r = 12.25
# def simple_interest(p,n,r):
#     si = (p*n*r)/100
#     print("simple interest is", si)
#     return si
# si = simple_interest(p,n,r)
# print(si)
# # due to return "si" its value will be assigned to function call
# total_pay = p+si
# print("Total payment :", total_pay)

""" 1. Can we return multiple values : """
# def function(a,b):
#     sum = a+b
#     sub = a-b
#     return sum,sub
# result = function(2,3)
# print(result)
# print(type(result))

# # unpacking tuple :
# def function(a,b):
#     sum = a+b
#     sub = a-b
#     return sum,sub
# sum,sub = function(2,3)
# print(sum)
# print(sub)

""" 2. return statement must at last in function  """
""" 3. return keyword is only used in function    """
""" 4. datatype of return value can be anything : """

# def demo():
#     return "hello"
# print(demo())

# def demo():
#     return [1,2,3]
# print(demo())

""" 5. If no return values, it return 'none' by default :"""
# def demo():
#     print("Have a nice day")
# print(demo())

""" Recursion : When a function call itself, then that function is called as recursive function
and the process is called recursion. """
# def demo():
#     print("Hello")
#     demo()
# demo()
""" Here 'Hello' is printed many times and we get 'Recursion-Error : Maximum recursion depth
 exceeded while calling a python object"""

""" Recursion limit :"""
# import sys
# print(sys.getrecursionlimit())
# sys.setrecursionlimit(200)
# count = 0
# def demo():
#     global count
#     count = count+1
#     print("Hello", count)
#     demo()
# demo()

""" Write a python program for printing n to 1 sequence :
expected o/p : 10,9,8,7,6,5,4,3,2,1  """
# so here 1 is the stopping range as recursion can go infinite times

""" recursion syntax :
    def function():
       base condition/terminating condition :
           return 
       code
       return (recursion calls)
    function()"""

# n = int(input("Enter the value : "))
# def function(n):
#     if n == 0:
#         return 1
#     print(n, end=" ")
#     return function(n-1)
# function(n)

""" Write a python program for factorial of a number using recursion """
# def factorial(n):
#     if n == 0:
#         return 1
#     return n*factorial(n-1)
# print(factorial(5))

""" Write your name 10 times without using loop and manually """
# count = 1
# def function(name):
#     global count
#     if count <= 10:
#         print(name, count)
#         count += 1
#         function(name)
# function("swetha")

""" Write a python program for sum of n natural numbers """
# def sum(n):
#     if n == 1:
#         return 1
#     return n+sum(n-1)
# print(sum(5))

""" Write a python program for fibonacci series by using recursion"""
# def fibonacci_series(n):
#     if n == 1:
#         return 0
#     if n == 2:
#         return 1
#     return fibonacci_series(n-2) + fibonacci_series(n-1)
# n = int(input("Enter the value : "))
# print(fibonacci_series(n))

""" Python program for counting number of digits in given number use recursion"""
# def counting_numbers(n):
#     if n < 10:
#         return 1
#     return 1+counting_numbers(n//10)
# print(counting_numbers(12345))

""" Write a python program for checking number is prime or not use recursion"""
# def prime_number(n, i):
#     if i == 1:
#         return 1
#     if n%i == 0:
#         return 0
#     return prime_number(n, i-1)
# n = int(input("Enter the number : "))
# prime = prime_number(n, n-1)
# if prime == 1:
#     print(n, "its a prime number")
# if prime == 0:
#     print(n, "its not a prime number")

""" Write a python program to find power of a given number using recursion"""
# def function(number, power):
#     if power == 0:
#         return 1
#     return number*function(number, power-1)
# print(function(2,5))




















































