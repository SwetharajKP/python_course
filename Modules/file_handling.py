""" Need of file handling : to save the data permanently"""
# age = input("Enter your age : ")
# file = open("data.txt","w")
# file.write(age)
# file.close()

# file = open("data.txt","r")
# print(file.read())
# file.close()

""" Opening File : 
Python provides an in-built function 'open()' to open a file.
syntax :
f = open(filename,mode="r",buffering,encoding=None,error=None,newline=None,closedfd=True)
f = open(filename,mode="r")  """

# f = open("hello.txt")
# if f:
#     print("file successfully opened")

# f = open("hello.txt",mode="w")
# if f:
#     print("file is successfully opened")
# print(type(f))

# f = open("hello.txt",mode="r",buffering=10,encoding="utf-8")
# if f:
#     print("open")
# print(f)

""" File Object Variables :
  name : name of specified file.
  mode : mode of specified file.
  closed : has boolean value. shows file is closed or not
  encoding : has encoding name.

syntax :
        file_object.variable_name     """
# f = open("hello.txt", mode="r", encoding="utf-8")
# print("file name is:",f.name)
# print("encoding is:",f.encoding)
# print("mode is:", f.mode)
# print("is file closed?:",f.closed)
# f.close()
# print("is file closed?:",f.closed)

# f = open("hello.txt", mode="w")
# print("mode is:",f.mode)
# print("encoding is:",f.encoding)   # here default encoding will be the o/p

""" File Object Method :
1. readable() : 
This method is used to check whether file is readable or not.
true : if file is readable.
false : if file is not readable.

2. writable() :
This method is used to check whether file is writable or not.
true : if file is writable.
false : if file is not writable.     """

# f = open("hello.txt",mode="r")
# if f.readable():
#     print("file is readable")
# f.close()

# f = open("hello.txt",mode="r")
# print(f.readable())
# print(f.writable())
# f.close()
# # mode= w+ can perform both thus both will be true

""" Check file exist or not :
isfile() :
-This method is used to check if file exist or not.
-This method belongs to 'path module' which is sub-module of OS module.
- Return true if file exist else false.
syntax :
       import os
       os.path.isfile(filename)       """
import os
# print(os.path.isfile("hello.txt"))
# # The file should be in the same directory

# # User input :
# filename = input("Enter the filename : ")
# if os.path.isfile(filename):
#     f = open(filename)
#     print("file exist")
#     f.close()
# else:
#     print("file not exist ")

""" Mode of opening file : 
When you open a file for operations, you have to specify mode.
mode specify the purpose of opening file . There are two types of modes :
1. Text mode 
2. Binary mode                """

""" Text mode : """
# f = open("hello.txt",mode="r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()

""" Binary mode : """
# f = open("hello.txt",mode="rb")
# data1 = f.read()
# print(data1)
# print(type(data1))
# f.close()
# # Here data is not encode

""" Reading data from file : 
To read content of file, we have following three methods :
1. read()
2.readline()
3.readlines()            """

""" 1. read() : This method is used to read data/content from a file returns as a 
string in text mode and bytes in binary mode.
syntax : 
        file_object.read(size) # here size is optional
size : It represents the number of characters to be read in text mode.        """
# f = open("hello.txt",mode="r")
# data = f.read()
# print(data)
# f.close()

# # if I gave size :
# f = open("hello.txt",mode="r")
# data = f.read(14)
# print(data)
# f.close()
# # here at the end of each line , there is by default '\n' which takes one space

# # if I gave size 2 times  :
# f = open("hello.txt",mode="r")
# data = f.read(14)
# data1 = f.read(4)
# print(data)
# print(data1)
# f.close()

""" 2.readline() : This function is used to read single line from a file.
syntax :
        file_object.readline(size)
size : number of characters to read from line."""
# f = open("hello.txt",mode="r")
# data = f.readline()
# print(data)
# f.close()

# f = open("hello.txt",mode="r")
# data = f.readline()
# data1 = f.readline()
# print(data)
# print(data1)
# f.close()
# # But here we can see space b/w two lines that is because of '/n' after print so to avoid it :
# f = open("hello.txt",mode="r")
# data = f.readline()
# data1 = f.readline()
# print(data,end="")
# print(data1,end="")
# f.close()

# # If we are give size :
# f = open("hello.txt",mode="r")
# data = f.readline(3)
# data1 = f.readline()
# print(data,end="")
# print(data1,end="")
# f.close()
# # here 'hel' will be printed by data and rest by data1 of that line

# f = open("hello.txt",mode="r")
# data = f.readline(3)
# data1 = f.readline(4)
# print(data,end="")
# print(data1,end="")
# f.close()

""" 3.readlines() : This method is used to read all lines from a file and
returns a list of lines.
syntax : 
        file_object.readlines()        """
# f = open("hello.txt",mode="r")
# data = f.readlines()
# print(data)
# f.close()
#
# # If we want to iterate :
# f = open("hello.txt",mode="r")
# data = f.readlines()
# for line in data:
#     print(line)
# f.close()
# # here we have space b/w two line that is new line due to "/n" so to avoid it :
# f = open("hello.txt",mode="r")
# data = f.readlines()
# for line in data:
#     print(line,end="")
# f.close()

""" Important methods :
 1. tell() : This method is used to find the current position of a file pointer from the
beginning of file. Position starts from 0 just like indexing in the string 
syntax :
        file_object.tell()          """
# f = open("hello.txt",mode="r")
# print(f.tell())   # Here we didn't start operation so its at 0
# f.read(3)
# print(f.tell())
# f.read()
# print(f.tell())
# f.close()

""" Seek() : This method is used to change the position of the file pointer.
Remember,file pointer is always counted from the beginning.
syntax :
        file_object.seek(position)      """
# f = open("hello.txt",mode="r")
# print(f.tell())
# print(f.read(3))
# f.seek(0)
# print(f.read())
# f.close()

""" number of words,number of characters and number of lines :"""
# f = open("hello.txt",mode="r")
# number_of_lines = 0
# number_of_chars = 0
# number_of_words = 0
# for line in f:
#     number_of_lines += 1
#     line = line.strip("\n")
#     number_of_chars += len(line)
#     lst = line.split()
#     number_of_words += len(lst)
# f.close()
# print("number of lines :", number_of_lines)
# print("number of chars :", number_of_chars)
# print("number of words :", number_of_words)

""" Writing in a file :  "w" mode :  
1. write() :                          """
# # It overwrites the data in a file :
# f = open("hello.txt",mode="w")
# # f.write("hello\nworld")
# f.write("hello guys\nhave a nice day")
# # n = f.write("hello guys\nhave a nice day")
# # print(n)
# f.close()

""" Copy Content of one file into Another file using python : """
# first = open("first.txt",mode="r",encoding="utf-8")
# f = open("hello.txt",mode="w",encoding="utf-8")
# for line in first:
#     f.write(line)
# first.close()
# f.close()

""" Writing in a file : "w"mode :
2.writelines() : This method is used to write a group of lines of string into
the file represented by a file object.
Group of lines are stored in list/tuple/set.
syntax :
        file_object.writelines(list/tuple/set)     """
# f = open("hello.txt",mode="w")
# line_lst = ["swetha\n","niki\n","sanju\n","ayu\n"]
# f.writelines(line_lst)
# f.close()

""" X mode :
Used to write data in file.
note : It write only in a new file due to which we don't loss the data of existing file"""
# data = "Swetha KP"
# f = open("hello.txt",mode="x")
# f.write(data)
# f.close()
# # Here we will get "file Exist Error : 'hello.txt' and thus we won't lose the data of hello.txt

""" Merging multiple text file using python :"""
























































































































































