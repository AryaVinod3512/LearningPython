#Q4.Accept a single dimension list of n elements and do the following processes

while True:
    print("You have the following options to choose from:")
    print("A : You can see a 2D list from the 1D input list in an unique format! ")
    print("B : You can see the transpose of the 2D list generated in option A! ")
    print("Exit: You may exit the program!")
    choice = input("\nEnter your choice(A/B/Exit): ")


#Q4.(a) - Create a 2D list from the 1D list in an unique format
    if choice == "a" or choice == "A":

        L = []
        n = int(input("Enter number of list elements: "))

        for i in range(n):
            x = int(input("Enter an element: "))
            L.append(x)
        print ("The 1D list you input is: ",L)

        matrix = []
        for i in range(n):
           matrix.append([])
           for j in range(n):
               if j<i:
                   matrix[i].append(0)
               else:
                   a=L[j-i]
                   matrix[i].append(a)

        print()
        print("The resultant 2D list is: ")
        for i in range(n):
           print()
           for j in range(n):
                print(matrix[i][j], end = " ")      #printing the list
        print()
        print()
        continue

#Q4.(b) - Create a transpose of the 2D list generated in option A
    elif choice == "b" or choice == "B":

        trans = []
        for i in range(n-1,-1,-1):
           trans.append([])
           for j in range(n-1,-1,-1):
               a = matrix[i][j]                    #interchanging the position of the elements
               trans[n-i-1].append(a)
        print()
        print("The transposed 2D list is: ", )
        for i in range(n):
           print()
           for j in range(n):
                print(trans[i][j], end = " ")
        print()
        print()
        continue

    elif choice == "Exit" or choice == "exit" or choice == "EXIT":
        print()
        print("The program will end now!")
        print("Thank you!")
        break


    else:
        print("Invalid choice!Please choose again!\n")
        continue

"""OUTPUT:
You have the following options to choose from:
A : You can see a 2D list from the 1D input list in an unique format! 
B : You can see the transpose of the 2D list generated in option A! 
Exit: You may exit the program!

Enter your choice(A/B/Exit): a
Enter number of list elements: 4
Enter an element: 1
Enter an element: 2
Enter an element: 3
Enter an element: 4
The 1D list you input is:  [1, 2, 3, 4]
The resultant 2D list is: 

1 2 3 4 
0 1 2 3 
0 0 1 2 
0 0 0 1 

You have the following options to choose from:
A : You can see a 2D list from the 1D input list in an unique format! 
B : You can see the transpose of the 2D list generated in option A! 
Exit: You may exit the program!

Enter your choice(A/B/Exit): b

The transposed 2D list is: 

1 0 0 0 
2 1 0 0 
3 2 1 0 
4 3 2 1 

You have the following options to choose from:
A : You can see a 2D list from the 1D input list in an unique format! 
B : You can see the transpose of the 2D list generated in option A! 
Exit: You may exit the program!

Enter your choice(A/B/Exit): EXIT

The program will end now!
Thank you!
"""
