import os
# print(dir(os))
# # here in o/p whatever with double underscore are classes and others are functions.

""" 1. System functionalities : """

""" system(cmd) : It is a function which execute shell based function. here cmd is a string """
# cdm = "time"
# print(os.system(cdm))

# n = "date"
# print(os.system(n))

# cdm = "notepad"
# print(os.system(cdm))

# cdm = "calc"
# print(os.system(cdm))

""" cpu_count() : return the number of cpu's in the system """
# print(os.cpu_count())

""" getlogin() : returns the name of the user logged-in"""
# print(os.getlogin())

""" 2.Directory based function (folder related) :"""
np = "D:/"
# path = "D:/swetha"
""" getcwd() : returns the current working directory """
# print(os.getcwd())

""" chdir(path) : change the directory """
# os.chdir(np)
# print(os.getcwd())

""" listdir(path) : returns list of all files, folder in the given directory"""
# print(os.listdir(np))
# print(os.listdir(path))

""" mkdir(path) : create a new directory
path = "D:/swetha/name the folder you want to create    """
# path = "D:/sample"
# os.mkdir(path)

""" rmdir(path) : remove a directory """
# os.rmdir("D:/sample")

""" walk(path) : prints the names of all files and folder inside a folder"""
# for dir_path, dir_name,filenames in os.walk("C:/Users/user/PycharmProjects"):
#     print("current path",dir_path)
#     print("current folder", dir_name)
#     print("current filenames", filenames)
#     print()

""" rename(path, new filename) :"""
# path = "C:/Users/user/PycharmProjects/pythoncourse/Modules/sample.txt"
# os.rename(path,"python.txt")
# os.remove("C:/Users/user/PycharmProjects/pythoncourse/Modules/python.txt")
