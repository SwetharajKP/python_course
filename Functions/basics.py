# # 1.
# def hello_function():
#     pass
# print(hello_function())
# # We get none because we're not doing anything with the function yet and doesn't have a return value

# # 2.
# def hello_function():
#     print("Hello function")
# hello_function()
"""
How the code works here :
when we call the function the control program jumps to the function header then the statement
inside the function are executed
"""
# # 3
# def hello_function():
#     return "Hello function"
# hello_function()
""" If we run this, and it doesn't give us any results because it's just a string that we're
not doing anything with but instead we "print", this let me print function and if we run that 
it print out our string"""
# def hello_function():
#     return "Hello function"
# print(hello_function())

# 4
# def hello_function():
#     return "Hello function"
# print(hello_function().upper())
# We were able to use the string method upper on the returns value to uppercase the string

""" Argument :"""
# def greet(name):
#     print("Hello", name)
#     print("How are you ?")
# greet("niki")

""" Return : """
# def greet(name):
#     print("Hello", name)
#     return
#     print("How are you ?")
# greet("niki")
""" You can see only hello niki is printed this is because return statement is encountered
immediately the function terminates and control of the program goes back to the function call"""

""" Passing multiple argument :"""
# def sum(n1, n2):
#     sum = n1+n2
#     print(sum)
# sum(3, 4)
# sum(40, 7)
# # Another method :
# def sum(n1, n2):
#     sum = n1+n2
#     return sum
# print(sum(40, 4))








