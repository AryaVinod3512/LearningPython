''' Consider a sequence of numbers with some missing values. Write a python
    program for inserting the missing values, remove some of the values
    and add a few more values to the existing sequence. '''

print("This program performs manipulations on a sequence of integers")

# Create the Empty List
numbers = []

# Read the Size of the List
n = int(input("\nEnter Size of the List: "))

# Reading the List Elements
while n > 0:
    i = int(input("Enter an element of your choice: "))
    numbers.append(i)
    n = n-1

# Printing the Content of the List
print("\nThe list of numbers is: ",end = " ")
for j in numbers:
    print(j,end = " ")
    

# Performing the List Operation
while True:
    
    print("\n\nA - Inserting at Specific Position \nB - Remove the Values from the List \nC - Adding the Elements to the List\nE - Exit\n")
    choice = input("\nEnter your Choice: ")
    
    if choice.upper() == "A":
        
        position = int(input("Enter the position to insert an element: "))
        ele = int(input("Enter the element to insert at the given position: "))
        if (position - 1) > len(numbers):
            print("The list is not long enouh to insert an element at given position!")
        elif (position - 1) <= len(numbers): 
            numbers.insert(position+1, ele)

        print(numbers)
        continue

    elif choice.upper() == "B":

        position = int(input("Enter the position at which element is to be deleted: "))
        numbers.pop(position-1)

        print(numbers)
        continue
    
    elif choice.upper() == "C":

        item = int(input("Enter an element to add: "))
        numbers.append(item)

        print(numbers)
        continue
        
    elif choice.upper() == "E":

        print("The program will end now! Thank you!")
        break

    else:
        print("\nEnter a correct choice!")
        continue

"""OUTPUT:
This program performs manipulations on a sequence of integers

Enter Size of the List: 3
Enter an element of your choice: 1
Enter an element of your choice: 2
Enter an element of your choice: 3

The list of numbers is:  1 2 3 

A - Inserting at Specific Position 
B - Remove the Values from the List 
C - Adding the Elements to the List
E - Exit


Enter your Choice: a
Enter the position to insert an element: 3
Enter the element to insert at the given position: 4
[1, 2, 3, 4]


A - Inserting at Specific Position 
B - Remove the Values from the List 
C - Adding the Elements to the List
E - Exit


Enter your Choice: b
Enter the position at which element is to be deleted: 3
[1, 2, 4]


A - Inserting at Specific Position 
B - Remove the Values from the List 
C - Adding the Elements to the List
E - Exit


Enter your Choice: c
Enter an element to add: 8
[1, 2, 4, 8]


A - Inserting at Specific Position 
B - Remove the Values from the List 
C - Adding the Elements to the List
E - Exit


Enter your Choice: d

Enter a correct choice!


A - Inserting at Specific Position 
B - Remove the Values from the List 
C - Adding the Elements to the List
E - Exit


Enter your Choice: e
The program will end now! Thank you!
"""
