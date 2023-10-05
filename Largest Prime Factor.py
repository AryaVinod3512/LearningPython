#Prime number - A number which has only 2 factors, i.e., one and itself only are called prime numbers
#Composite number - A number which has more than 2 factors, i.e., other than one and itself are called composite numbers
#1 has only 1 factor, i.e., itself and hence, is neither prime nor composite
#0 multiplied by any number gives 0 and hence, is neither prime nor composite
#negative natural numbers are just additive inverses of positive natural numbers and hence, they are not considered for classification into prime and composite
choice = input("Do you want to calculate largest prime factor of an integer(Y/N)? ")

#Creating a menu-driven code where menu is yes or no
while True:
    if choice.upper() == "Y":
        #Read from user
        num = float(input("Enter an integer number: "))
        n = int(num)

        #Checking if n is positive, negative or zero
        
        if n > 0:

            #Checking if the input number is 1
            if n == 1:
                print("1 is neither a prime nor composite number!")
                
            #Compute max prime factor of input number
            else:
                max_PF = 1

                #computing MAX factor of input number 
                while n%2 == 0:
                    max_PF = n
                    n = n/2

                #computing max PRIME factor of input number
                stop_val = int(n**0.5)
                for i in range(3, stop_val+1, 2):
                    while n%i == 0:
                        max_PF = i
                        n = n/i

                #for prime numbers greater than 2 the max prime factor is itself
                #checking for prime input number greater than 2
                if n >= 2:
                    max_PF = n
                    
                print("The maximum Prime Factor of ",int(num),"is:",int(max_PF))

            #Providing option to find max prime factor for more numbers without running the code again
            choice = input("\nGo again?(Y/N) ")
            continue
        
        elif n == 0:
            print("Zero is neither a prime nor a composite number!")
            choice = input("\nGo again?(Y/N) ")
            continue

        elif n < 0:
            print("Prime factors exist for only positive integers!")
            choice = input("\nGo again?(Y/N) ")
            continue

    #Option to exit the program
    elif choice.upper() == "N":
        print("The program will end now! Thank you!")
        break
    
    #Option to exit or continue program without abruptly stopping the program due to wrong input from user 
    else:
        print("Enter a correct choice!")
        choice = input("\nGo again?(Y/N) ")
        continue

"""OUTPUT:
Do you want to calculate largest prime factor of an integer(Y/N)? y
Enter an integer number: 1
1 is neither a prime nor composite number!

Go again?(Y/N) y
Enter an integer number: 2
The maximum Prime Factor of  2 is: 2

Go again?(Y/N) y
Enter an integer number: 6
The maximum Prime Factor of  6 is: 3

Go again?(Y/N) y
Enter an integer number: 77
The maximum Prime Factor of  77 is: 11

Go again?(Y/N) y
Enter an integer number: 0
Zero is neither a prime nor a composite number!

Go again?(Y/N) y
Enter an integer number: -1
Prime factors exist for only positive integers!

Go again?(Y/N) pig latin
Enter a correct choice!

Go again?(Y/N) n
The program will end now! Thank you!
"""
