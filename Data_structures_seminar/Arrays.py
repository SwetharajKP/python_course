import array as arr
lst = arr.array('i',[1,2,3,4,5])
while True:
    print('1. Print Array, 2. Add Elements, 3. Delete Elements, 4. Exit')
    choice = int(input('Enter your choice: '))
    if choice == 1:
        print('The array elements are: ')
        for numbers in lst:
            print(numbers)
    elif choice == 2:
        value = int(input('Enter the value: '))
        if isinstance(value,int):
            lst.append(value)
    elif choice == 3:
        value = lst.pop()
        print('The deleted value was: ',value)
    elif choice == 4:
        break
    else:
        print('Enter valid choice')
