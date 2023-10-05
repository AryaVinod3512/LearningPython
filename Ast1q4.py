#Choosing options within Question 4

while True:
    print("You can choose to view the following programs:")
    print("A : This will show you the tribonacci series upto the number of terms you input!")
    print("B : This will show you an unique cos series for the number of terms you input!")
    print("C : This will show you the result of an unique series!")
    print("Exit: You may exit the program!")
    print()
    choice = input("Enter the pattern you want to view - a/b/c/Exit: ")
    

    
    #Program 4.a) - The Tribonacci series

    if choice.lower() == "a":

        print()
        n = int(input("Enter the number of terms of the series you want to view: "))

        f1 = 1
        f2 = 1
        f3 = 1

        print("The Tribonacci series upto",n,"terms:")

        print(f1,f2,f3,sep = " ",end = " ")

        for i in range (4,n+1):
            f4 = f1 + f2 + f3
            f1 = f2
            f2 = f3
            f3 = f4
            print(f4, end = " ")
        print()
        print()
        


    #Program 4.b) - The result of the cos series

    elif choice.lower() == "b":

        import math
        print()
        n = int(input("Enter the number of terms of the series you want to view: "))
        x1 = float(input("Enter a value for x in cos(x) in degree measure: "))

        x = (x1 * 3.14) / 180
        print("The angle measures",x,"radians!")
        
        sum1 = 1
        index = -1
        

        for a in range(2,n+1,2):
            factorial = 1
            for j in range (1,a+1):
                factorial *= j
                term = ((x**a)*index)/factorial
                sum1 += term
                index *= -1
        print("The sum of the series upto",n,"terms is",sum1)
        print()
        


    #Program 4.c) - The result of a unique series

    elif choice.lower() == "c":

        print()
        n = int(input("Enter the number of terms of the series you want to view: "))
        a = int(input("Enter an integer number of your choice: "))

        sum2 = 0
        index = 1
        power = 1

        for i in range(1,n+1):
            m = (4*(i - 1)) + 1
            factorial = 1
            for j in range(1,m+1):
                factorial *= m
            sum2 += ((a**power)/factorial)*index
            power += 2
            index *= -1
        print("The sum of the series upto",n,"terms is",sum2)
        print()
        


    elif choice.lower() == "exit":
        print()
        print("The program will end now!")
        print("Thank you!")
        break


    else:
        print("Invalid choice!Please choose again!\n")
        continue

"""OUTPUT:
You can choose to view the following programs:
A : This will show you the tribonacci series upto the number of terms you input!
B : This will show you an unique cos series for the number of terms you input!
C : This will show you the result of an unique series!
Exit: You may exit the program!

Enter the pattern you want to view - a/b/c/Exit: a

Enter the number of terms of the series you want to view: 10
The Tribonacci series upto 10 terms:
1 1 1 3 5 9 17 31 57 105

You can choose to view the following programs:
A : This will show you the tribonacci series upto the number of terms you input!
B : This will show you an unique cos series for the number of terms you input!
C : This will show you the result of an unique series!
Exit: You may exit the program!

Enter the pattern you want to view - a/b/c/Exit: b

Enter the number of terms of the series you want to view: 10
Enter a value for x in cos(x) in degree measure: 180
The angle measures 3.14 radians!
The sum of the series upto 10 terms is -65541.41041614303

You can choose to view the following programs:
A : This will show you the tribonacci series upto the number of terms you input!
B : This will show you an unique cos series for the number of terms you input!
C : This will show you the result of an unique series!
Exit: You may exit the program!

Enter the pattern you want to view - a/b/c/Exit: c

Enter the number of terms of the series you want to view: 10
Enter an integer number of your choice: 5
The sum of the series upto 10 terms is 4.960008065913282

You can choose to view the following programs:
A : This will show you the tribonacci series upto the number of terms you input!
B : This will show you an unique cos series for the number of terms you input!
C : This will show you the result of an unique series!
Exit: You may exit the program!

Enter the pattern you want to view - a/b/c/Exit: d
Invalid choice!Please choose again!

You can choose to view the following programs:
A : This will show you the tribonacci series upto the number of terms you input!
B : This will show you an unique cos series for the number of terms you input!
C : This will show you the result of an unique series!
Exit: You may exit the program!

Enter the pattern you want to view - a/b/c/Exit: exit

The program will end now!
Thank you!
"""




