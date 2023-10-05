#Program 2 - To display the pattern based on the choice of the pattern given as input

while True:
    print("You can choose to view the following programs:")
    print("A : This will show you a cute pattern of odd numbers from 1 to 9!")
    print("B : This will show you an interesting pattern of the numbers 1 to 5!")
    print("C : This will show you a mind - blowing pattern of the letters from Q to Z!")
    print("Exit: You may exit the program!")
    print()
    pattern_choice = input("Enter the pattern you want to view - a/b/c/Exit: ")


    if pattern_choice.lower() == "a":

        for i in range(1,10,2):
            for j in range(i,0,-2):
                print(j,end=" ")
            print()
        print()


    elif pattern_choice.lower() == "b":

        for i in range(1,6):
            for j in range(1,6):
                if (j <= i):
                   print(i,end=" ")
                else:
                    print(j,end=" ")
            print()
        print()        


    elif pattern_choice.lower() == "c":

        for i in range(90,80,-1):
            for j in range(i,i+1):
                if i==90 or i==88 or i==85:
                    print(chr(i),end="\n")
                else:
                    print(chr(i),end=" ")
        print()
        print()
        

    elif pattern_choice.lower() == "exit":
            print()
            print("The program will end now!")
            print("Thank you!")
            break


    else:
        print("Invalid choice!Please choose again!\n")
        continue


"""You can choose to view the following programs:
A : This will show you a cute pattern of odd numbers from 1 to 9!
B : This will show you an interesting pattern of the numbers 1 to 5!
C : This will show you a mind - blowing pattern of the letters from Q to Z!
Exit: You may exit the program!

Enter the pattern you want to view - a/b/c/Exit: a
1 
3 1 
5 3 1 
7 5 3 1 
9 7 5 3 1 

You can choose to view the following programs:
A : This will show you a cute pattern of odd numbers from 1 to 9!
B : This will show you an interesting pattern of the numbers 1 to 5!
C : This will show you a mind - blowing pattern of the letters from Q to Z!
Exit: You may exit the program!

Enter the pattern you want to view - a/b/c/Exit: b
1 2 3 4 5 
2 2 3 4 5 
3 3 3 4 5 
4 4 4 4 5 
5 5 5 5 5 

You can choose to view the following programs:
A : This will show you a cute pattern of odd numbers from 1 to 9!
B : This will show you an interesting pattern of the numbers 1 to 5!
C : This will show you a mind - blowing pattern of the letters from Q to Z!
Exit: You may exit the program!

Enter the pattern you want to view - a/b/c/Exit: c
Z
Y X
W V U
T S R Q 

You can choose to view the following programs:
A : This will show you a cute pattern of odd numbers from 1 to 9!
B : This will show you an interesting pattern of the numbers 1 to 5!
C : This will show you a mind - blowing pattern of the letters from Q to Z!
Exit: You may exit the program!

Enter the pattern you want to view - a/b/c/Exit: d
Invalid choice!Please choose again!

You can choose to view the following programs:
A : This will show you a cute pattern of odd numbers from 1 to 9!
B : This will show you an interesting pattern of the numbers 1 to 5!
C : This will show you a mind - blowing pattern of the letters from Q to Z!
Exit: You may exit the program!

Enter the pattern you want to view - a/b/c/Exit: exit

The program will end now!
Thank you!
"""
