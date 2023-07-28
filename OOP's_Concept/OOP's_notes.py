""" Python Classes and Objects :
Python is an object-oriented programming language.
Almost everything in python is an object, with its properties and methods.

A class is like an object constructor, or a blueprint for creating objects."""

# x = 100
# print(type(x))   # O/P : <class 'int'>

# x = [1,2,3]
# print(type(x))

# def demo():
#     print("hello guys !")
# print(type(demo))     # O/P : <class 'function'>

""" Creating class and objects : 
class class_name:
      # attributes
      # methods
obj1 = class_name([args])
obj2 = class_name ([args])       """

# class Email:
#     pass
# e1 = Email()
# e2 = Email()
# print(type(e1))

# class Employee:     # class
#     def __init__(self,name,age):
#         self.name = name      # attributes
#         self.age = age
#     def display(self):        # method
#         print(self.name)
# e1 = Employee("swetha",23)
# e2 = Employee("niki",24)

""" Constructor and types of constructor :"""
# # Example :
# class Employee:
#     def __init__(self):
#         self.salary = 40000
#         self.age = 23
# e1 = Employee()
# e2 = Employee()
# # If we want to see the content of e1 and e2:
# print("e1 =",e1.__dict__)
# print("e2 =", e2.__dict__)
# # __dict__ is special attribute through which we can see the content of object

""" Types of constructor : """
# # 1) Non-parameterized constructor :
# class Employee:
#     def __init__(self):
#         self.salary = 40000
#         self.age = 23
# e1 = Employee()
# e2 = Employee()
# print(e1.__dict__)
# print(e2.__dict__)
# # Because in this constructor we didn't pass any other parameter than "self" that's y it's called Non-parameterized constructor

# # 2) Parameterized constructor :
# class Employee:
#     def __init__(self,salary,age):
#         self.salary = salary
#         self.age = age
# e1 = Employee(40000,23)
# e2 = Employee(40000,24)
# print(e1.__dict__)
# print(e2.__dict__)

# # 3) Default constructor :
# class Employee:
#     pass
# e1 = Employee()
# e2 = Employee()
# print(e1.__dict__)
# print(e2.__dict__)
# # Without constructor, object can not be created

""" Working of oop :
1. Memory allocation for object
2. Memory reference returned to the object
3. Memory reference automatically passed inside the constructor
4. Constructor creates/initialize variables at that memory reference  """

""" What is self :
Self parameter is a reference to the current instance of the class, and is used to
access variables that belongs to the class."""

""" How to access class members :
Class members : Attributes(variables)+Actions(methods)
we can access these variables using object outside the class"""
# class Employee:
#     def __init__(self,salary,age):
#         self.salary = salary
#         self.age = age
#
#     def display(self):
#         print(f"salary is {self.salary} and age is {self.age}")
# e1 = Employee(40000,23)
# e2 = Employee(40000,24)
# # Accessing attribute outside the class :
# print(e1.salary)
# e1.salary = 45000    # Updating attribute
# print(e1.salary)
# # # How to access display method :
# e2.display()
# e1.display()

""" Built-in functions : 
1. getattr(object_name, attribute_name)
2. setattr(object_name, attribute_name,new_name)
3. delattr(object_name, attribute_name)
4. hasattr(object_name,attribute_name )"""
# hasattr() checks whether the object has that attribute if yes thn it returns True else False

# # Example :
# class Employee:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
# e1 = Employee("swetha",23)
# e2 = Employee("niki",24)
# # getattr() :
# print(getattr(e1,"age"))
# # setattr() :
# setattr(e2,"age",25)
# print(e2.__dict__)
# # delattr() :
# delattr(e2,"age")
# print(e2.__dict__)
# # hasattr():
# print(hasattr(e2,"age"))
# print(hasattr(e1,"age"))

""" Built-in class attribute :
1. __dict__ : Dictionary containing class's namespace.
2. __doc__ : Clas documentation string.
3. __name__ : Class name.
4. __module__ : Module name in which class is defined.
5. __base__ : List of base classes."""

# class Employee:
#     """This is employee class for maintaining employee data"""
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
# e1 = Employee("swetha",23)
# e2 = Employee("niki",24)
# print(Employee.__doc__)
# print(Employee.__dict__)
# print(Employee.__name__)
# print(Employee.__module__)

""" isinstance(object_name,class_name) function :"""
# class Demo:
#     pass
# d1 = Demo()
#
# class Employee:
#     """This is employee class for maintaining employee data"""
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def display(self):
#         print(f"name is{self.name} and age is {self.age}")
#
# e1 = Employee("swetha",23)
# e2 = Employee("niki",24)
# print(isinstance(e1,Employee))
# print(isinstance(d1,Employee))
# # use in operation :
# # if isinstance(object_name,class_name):
# #     pass

""" Types of variables(object oriented variable):
1.Instance Variables
2.Class Variables"""

# # Instance variables :
# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#
# std1 = Student('swetha',84)
# std2 = Student('niki',94)
# std3 = Student('ayu',91)

""" Instance variable :
1. Variable made of particular instance.
2. separate copy is created for every object.
3. Values of variable differs from object to object.
4. Modification in one object won't effect other objects. """

# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#
# std1 = Student('swetha',84)
# std2 = Student('niki',94)
# std3 = Student('ayu',91)
# # If I want to add a variable outside the class :
# std1.age = 23
# # So here "age" is an instance variable created for std1
# print(std1.__dict__)
# print(std2.__dict__)
# # delete :
# del std3.marks
# print(std3.__dict__)

""" Creating instance variables :
1. Using constructor
2. Using instance method
3. outside class                 """

# 2. Using instance method :
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(f"name is{self.name}")

std1 = Student('swetha',84)
std2 = Student('niki',94)
std3 = Student('ayu',91)



