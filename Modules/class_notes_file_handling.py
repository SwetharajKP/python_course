""" what is handling ?"""

""" write : """
# f = open("hello.txt",mode="w")
# f.write("hello guys\nWelcome to program classes")
# f.close()

# # if I try to print write :
# print(f.write("hello guys\nWelcome to program classes"))
# # It won't be printing content but the number of characters of the content

""" read : """
# f = open("hello.txt",mode="r")
# print(f.read())
# f.close()

""" If the file is located in different location, you will have to specify the file path :"""
# f = open("C:/Users/user/PycharmProjects/pythoncourse/operators/sample.txt",mode="r")
# print(f.read())
# f.close()

""" Read only parts of the file :
By default the read() method returns the whole text, but you can also specify how many characters 
you want to return : """
# f = open("C:/Users/user/PycharmProjects/pythoncourse/operators/sample.txt",mode="r")
# print(f.read(5))
# f.close()

""" Read Line : returns one line by using the readline() method :"""
# f = open("C:/Users/user/PycharmProjects/pythoncourse/operators/sample.txt",mode="r")
# print(f.readline())
# f.close()

# # By calling readline() two times, you can read the two first lines :
# f = open("C:/Users/user/PycharmProjects/pythoncourse/operators/sample.txt",mode="r")
# print(f.readline(),end="")
# print(f.readline(),end="")
# f.close()

# # By looping through the lines of the file, you can read the whole file line by line :
# f = open("C:/Users/user/PycharmProjects/pythoncourse/operators/sample.txt",mode="r")
# for line in f:
#     print(line,end="")
# f.close()

""" Write to an Existing File : 
"a" : Append - will append to the end of the file.
"w" : write - will overwrite any existing content."""

# # Example :
# f = open("C:/Users/user/PycharmProjects/pythoncourse/operators/sample.txt",mode="a")
# f.write("\nNow the file has more content!")
# f.close()

""" append : """
# f = open("hello.txt",mode="a")
# f.write("\nHave a nice day")
# f.close()

""" Delete a File : 
To delete a file,you must import the os module, and run its os.remove() function """
import os
# os.remove("C:/Users/user/PycharmProjects/pythoncourse/operators/sample.txt")

""" Check if File exist : To avoid getting an error, you might want to check
 if the file exist before you try to delete it """
# sample_path = "C:/Users/user/PycharmProjects/pythoncourse/operators/sample.txt"
# if os.path.exists(sample_path):
#     os.remove(sample_path)
# else:
#     print("The file does not exist")

""" getsize() : """
# # file to check :
# hello_path = "C:/Users/user/PycharmProjects/pythoncourse/Modules/hello.txt"
# size = os.path.getsize(hello_path)
# print(size)

# hello_path = r'C:/Users/user/PycharmProjects/pythoncourse/Modules/hello.txt'
# size = os.path.getsize(hello_path)
# print(size)

""" delete lines from a file : didn't get """














































