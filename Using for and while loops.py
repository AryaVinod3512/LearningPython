'''Programs to perform specific functions and display output in a particular format using for and while loops only'''

##1.a)To display the numbers divisible by 3 or 5, 5 in each line and print their sum and count
##1.b)To print the sum and count of odd multiples of 11 in a specified range taken as input
##2.To display specific patterns of the numbers and the alphabet based on choice input
##3.To generate bus charge fares based on distance travelled and the given tariff


while True:
    print("You can choose to view the following programs:")
    print("A : You can see a format of the numbers in the range 20 and 100 which are divisble by 3 and 5 along wit their count and sum!")
    print("B : If you input a certain range, you can see the sum and count of all the odd multiples of 11 withing that range!")
    print("Exit: You may exit the program!")
    print()
    choice = input("Enter your choice(a/b/Exit): ")




    if choice == "a" or choice == "A":
        
        sum = count = 0         #Initializing
        for i in range(20,101):
            if (i%3 == 0) or (i%5 == 0):
                print(i,end=" ")
                sum += i
                count += 1      #Incrementing the count
                if count%5 == 0:
                    print("\n")
        print("\n\nThe sum of the numbers divisible by 3 and 5 is: ",sum)
        print("The count of the numbers divisible by 3 and 5 is: ",count)
        print()

    


    elif choice  == "b" or choice == "B":
        
        sum = count = 0

        lower_limit = int(input("\n\nEnter a lower limit: "))
        upper_limit = int(input("Enter an upper limit: "))

        for i in range(lower_limit,upper_limit + 1):
            if (i%11 == 0) and (i%2 != 0): #Check for divisibility by 11 and 2
                sum += i
                count += 1

        print("The number of odd multiples of 11 in the specified range is: ",count)        
        print("The sum of the odd multiples of 11 is: ",sum)
        print()


   

    elif choice == "Exit" or choice == "exit" or choice == "EXIT":
        print()
        print("The program will end now!")
        print("Thank you!")
        break


    else:
        print("Invalid choice!Please choose again!\n")
        continue

"""OUTPUT:
You can choose to view the following programs:
A : You can see a format of the numbers in the range 20 and 100 which are divisble by 3 and 5 along wit their count and sum!
B : If you input a certain range, you can see the sum and count of all the odd multiples of 11 withing that range!
Exit: You may exit the program!

Enter your choice(a/b/Exit): A
20 21 24 25 27 

30 33 35 36 39 

40 42 45 48 50 

51 54 55 57 60 

63 65 66 69 70 

72 75 78 80 81 

84 85 87 90 93 

95 96 99 100 

The sum of the particular numbers is:  2340
The count of the particular numbers is:  39

You can choose to view the following programs:
A : You can see a format of the numbers in the range 20 and 100 which are divisble by 3 and 5 along wit their count and sum!
B : If you input a certain range, you can see the sum and count of all the odd multiples of 11 withing that range!
Exit: You may exit the program!

Enter your choice(a/b/Exit): B


Enter a lower limit: 100
Enter an upper limit: 220
The number of odd multiples of 11 in the specified range is:  5
The sum of the odd multiples of 11 is:  825

You can choose to view the following programs:
A : You can see a format of the numbers in the range 20 and 100 which are divisble by 3 and 5 along wit their count and sum!
B : If you input a certain range, you can see the sum and count of all the odd multiples of 11 withing that range!
Exit: You may exit the program!

Enter your choice(a/b/Exit): C
Invalid choice!Please choose again!

You can choose to view the following programs:
A : You can see a format of the numbers in the range 20 and 100 which are divisble by 3 and 5 along wit their count and sum!
B : If you input a certain range, you can see the sum and count of all the odd multiples of 11 withing that range!
Exit: You may exit the program!

Enter your choice(a/b/Exit): EXIT

The program will end now!
Thank you!
"""

