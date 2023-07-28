""" Why Module ?
In any project, we have to write big programs. Its become difficult to manage
and organize programs.
   So, we break down the big programs into small manageable and organized files
having same logic. These files are nothing but modules.
It provides reusability to our code  """

""" What are modules in python ?
A file containing python code is called as python modules.
Modules contains functions definitions, class definitions, variables, runnable code,
python statements you want to include in your python main file.  
            Example.py('example' is name of the module.) """

""" 'import' is a keyword used to import external files into our current program file
after writing import we have to write the Filename . Then in the next line again
we have to write Filename.add(arg,arg) [here add is the function name]
dot(.)operator is used to access members of modules.  """
# import Example
# Example.add(3,5)

# # import with renaming :by using "as" *keyword
# import Example as Ex
# Ex.add(3, 5)
# # Here after renaming we can't use Example as filename, it will show error

""" From the Example file, If only add function I have to import :
 syntax for IF its from same dictionary :
  from filename import function
  syntax for IF its from different dictionary :
  from dictionary.filename import function"""

# from Example import add
# add(13,4)

# # importing all (*) :
# from Example import *
# add(5,6)
# sub(6,7)

# # How to import multiple attributes :
# from Example import sub,add
# add(1,3)
# sub(9,8)

""" There are two types of modules :
1. User defined modules : modules created by us
2. Built in modules : modules given by python """

""" math : This module provides access to the mathematical functions """
# import math
# print(math.factorial(5))
# print(dir(math))
# # dir() will return all the properties and methods, even built-in properties which are default for all object

"""The module search path :
1.when a module named math is imported, the interpreter first searches for 
built in modules with that name.
2.If not found, it then searches for a file named math.py in a current directory.
3.If not found, it then searches in directories mentioned in sys.path"""

# NOTE : never give filename as built-in functions, if math is given as filename then it will import built-in math and not the module math file-named

# # To know about built-in modules :
# help("modules")
# # Enter any module name to get more help. or, type "modules spam" to search for modules whose name or summary contain in the string "spam"
# # or we can just browse "python documentation " search and click on global modules index

""" Built-in Modules :
There are several built-in modules in python, which we can import whenever we like :"""
# import and use the platform module :
import platform
# x = platform.system()
# print(x)

""" Using the dir() Function :
There is a built-in function to list all the function names(or variable names)in a module
   The dir() function : """
# import platform
# print(dir(platform))




















