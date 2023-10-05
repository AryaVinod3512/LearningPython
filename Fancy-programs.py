#Choosing options within Question 5
while True:
    print("You have the following options to choose from:")
    print("A : You can see all the Harshad numbers between 150 and 1000! ")
    print("B : You can see all the Palindromic Prime numbers in the range 200 to 400! ")
    print("C : You can see the binary equivalents of all decimal numbers from 20 to 40! ")
    print("D : Upon the input of two integers, you can see their greatest common divisor! ")
    print("Exit: You may exit the program!")
    print()
    choice = input("Enter your choice - a/b/c/d/Exit: ")
    print()

    #Program 5.a) - To print all the Harshad numbers between 150 and 1000

    if choice == "a" or choice == "A":

        print("The Harshad numbers between 150 and 1000 are:")

        j = 0

        for i in range(150,1001):

            rem = sum = 0       
            num = i  
            while(num > 0):    
                rem = num%10    
                sum = sum + rem    
                num = num//10   
                
             
            if(i%sum == 0):       
                if j < 3:
                    print(i,end=" ")
                    j += 1
                else:
                    print(i,end="\n")
                    j = 0
                    
            else:
                pass

        print()
        print()
        continue


         
    #Program 5.b) - To print all the Palindromic Prime numbers in the range 200 to 400

    elif choice == "b" or choice == "B":

        print("The Paindromic Prime numbers between 200 and 400 are:")
        
        j = 0

        for num in range(200,401):

            rev = 0

            temp1 = num
            while temp1 > 0:
                
                digit = temp1 % 10
                rev = rev*10 + digit
                temp1 //=10

            if rev == num:
                
                
                for i in range(2,num):
                    a = True
                    if (num % i) == 0:
                        a = False
                        break
                if a == True:
                    if j < 4:
                        print(num,end=" ")
                        j += 1
                    else:
                        print(num,end="\n")
                        j = 0

        print()
        print()
        continue




    #Program 5.c) - To print binary equivalents of all decimal numbers from 20 to 40

    elif choice == "c" or choice == "C":
        
        print("The binary equivalents of numbers from 20 to 40 are: ")

        j = 0

        for i in range(20,41):
            x = i
            pos = 1
            binary_number = 0
            while x > 0:
                rem = x % 2
                binary_number = binary_number + rem * pos
                pos *= 10
                x //= 2
                
            if j < 2:
                print(binary_number,end=" ")
                j += 1
            else:
                print(binary_number,end="\n")
                j = 0

        print()
        continue

           
    #Program 5.d) - To accept two integers and display the greatest common divisor and terminate the process when the user enters zero

    elif choice == "d" or choice == "D":

        num1 = int(input("Enter  the first number: "))
        num2 = int(input("Enter the second number: "))

        if (num1 == ord("e")) or (num2 == ord("e")):
            print("The program is being terminated cause you entered 'e' or '101'!")
            

        rem = 0
        if num1 > num2:
            while(num2 != 0):
                rem = num1 % num2
                num1 = num2
                num2 = rem
            print("The greatest common divisor of the two numbers is",num1)

        elif num2 > num1:
            while(num1 != 0):
                rem = num2 % num1
                num2 = num1
                num1 = rem
            print("The greatest common divisor of the two numbers is",num2,"!")

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
A : You can see all the Harshad numbers between 150 and 1000! 
B : You can see all the Palindromic Prime numbers in the range 200 to 400! 
C : You can see the binary equivalents of all decimal numbers from 20 to 40! 
D : Upon the input of two integers, you can see their greatest common divisor! 
Exit: You may exit the program!

Enter your choice - a/b/c/d/Exit: a

The Harshad numbers between 150 and 1000 are:
150 152 153 156
162 171 180 190
192 195 198 200
201 204 207 209
210 216 220 222
224 225 228 230
234 240 243 247
252 261 264 266
270 280 285 288
300 306 308 312
315 320 322 324
330 333 336 342
351 360 364 370
372 375 378 392
396 399 400 402
405 407 408 410
414 420 423 432
440 441 444 448
450 460 465 468
476 480 481 486
500 504 506 510
511 512 513 516
518 522 531 540
550 552 555 558
576 588 592 594
600 603 605 612
621 624 629 630
640 644 645 648
660 666 684 690
700 702 704 711
715 720 730 732
735 736 738 756
770 774 777 780
782 792 800 801
803 804 810 820
825 828 832 840
846 864 870 874
880 882 888 900
902 910 912 915
918 935 936 954
960 966 972 990
999 1000 

You have the following options to choose from:
A : You can see all the Harshad numbers between 150 and 1000! 
B : You can see all the Palindromic Prime numbers in the range 200 to 400! 
C : You can see the binary equivalents of all decimal numbers from 20 to 40! 
D : Upon the input of two integers, you can see their greatest common divisor! 
Exit: You may exit the program!

Enter your choice - a/b/c/d/Exit: b

The Paindromic Prime numbers between 200 and 400 are:
313 353 373 383 

You have the following options to choose from:
A : You can see all the Harshad numbers between 150 and 1000! 
B : You can see all the Palindromic Prime numbers in the range 200 to 400! 
C : You can see the binary equivalents of all decimal numbers from 20 to 40! 
D : Upon the input of two integers, you can see their greatest common divisor! 
Exit: You may exit the program!

Enter your choice - a/b/c/d/Exit: c

The binary equivalents of numbers from 20 to 40 are: 
10100 10101 10110
10111 11000 11001
11010 11011 11100
11101 11110 11111
100000 100001 100010
100011 100100 100101
100110 100111 101000

You have the following options to choose from:
A : You can see all the Harshad numbers between 150 and 1000! 
B : You can see all the Palindromic Prime numbers in the range 200 to 400! 
C : You can see the binary equivalents of all decimal numbers from 20 to 40! 
D : Upon the input of two integers, you can see their greatest common divisor! 
Exit: You may exit the program!

Enter your choice - a/b/c/d/Exit: d

Enter  the first number: 17
Enter the second number: 31
The greatest common divisor of the two numbers is 1 !

You have the following options to choose from:
A : You can see all the Harshad numbers between 150 and 1000! 
B : You can see all the Palindromic Prime numbers in the range 200 to 400! 
C : You can see the binary equivalents of all decimal numbers from 20 to 40! 
D : Upon the input of two integers, you can see their greatest common divisor! 
Exit: You may exit the program!

Enter your choice - a/b/c/d/Exit: e

Invalid choice!Please choose again!

You have the following options to choose from:
A : You can see all the Harshad numbers between 150 and 1000! 
B : You can see all the Palindromic Prime numbers in the range 200 to 400! 
C : You can see the binary equivalents of all decimal numbers from 20 to 40! 
D : Upon the input of two integers, you can see their greatest common divisor! 
Exit: You may exit the program!

Enter your choice - a/b/c/d/Exit: EXIT


The program will end now!
Thank you!
"""

  
