# stack = []
# def empty():
#     if len(stack) == 0:
#         print('stack is empty\n')
#     else:
#         print(stack,'\n')
#
# val1 = 1
# val2 = 2
# val3 = 3
# stack.append(val1)
# stack.append(val2)
# stack.append(val3)
# empty()
# a = stack.pop()
# b = stack.pop()
# c = stack.pop()
# print('The popped elements are :',a,b,c,'\n')
# empty()

stack = []
def push():
    element = input('Enter the element: ')
    stack.append(element)
    print(stack)

def pop_element():
    if not stack:
        print('stack is empty')
    else:
        e = stack.pop()
        print('Removed element: ',e)
        print(stack)

while True:
    print('select the operation 1.push, 2.pop, 3.exit ')
    choice = int(input('Enter the choice: '))
    if choice == 1:
        push()
    elif choice == 2:
        pop_element()
    elif choice == 3:
        break
    else:
        print('Invalid choice')


