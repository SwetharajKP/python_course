# sum of n natural numbers
# num = int(input("enter the number :"))
# sum = 0
# i = 0
# while i <= num:
#     sum += i
#     i += 1
# print(sum)

# to print even numbers 1 to 10

"""convert a for loop into while loop.
for i in range(25,500,25):
    print(i)                      """
# i = 25  # initialization
# while i < 25: # check condition
#     print(i) # body of the loop : block of code to execute
#     i += 25  # increment

"""convert a for loop into while loop.
for i in range(10):
    for j in range(i):
        print("$",end="")
    print()                  """
# i = 0
# while i < 10:
#     for j in range(i):
#         print("$", end=" ")
#     print()
#     i += 1
# same question for inner loop :
# i = 0
# while i < 10:
#     j = 0
#     for j in range(i):
#         print("$", end=" ")
#         j += 1
#     print()
#     i += 1

""" convert a while loop into for loop
i = 15
while i >= 8:
    print(i)
    i -= 1                                """
# for i in range(15,7,-1):
#     print(i)


