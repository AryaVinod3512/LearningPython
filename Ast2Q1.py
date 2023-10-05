#Q1. Doing 5 different sets of operations on a list input by the user
#Code segment to get 10 integer numbers from the user and assign them to a single list
List1 = []
n = print("Enter 10 integer numbers of your choice") 
for l in range(1,11):
    num = int(input("Enter integer: "))
    List1.append(num)
print(List1)




#Code segment to drive the program based on choice input by user
while True:
    print("The following sets of functions can take place in this program:")
    print("A : Displays the maximum and minimum elements along with their posititons")
    print("B : Displays the elements in the reverse order")
    print("C : Displays the mean of even elements and the median of odd elements")
    print("D : Customising the input list just for you!")
    print("E : 2 new lists with the prime and composite numbers from the input list")
    print("Exit: You may exit the program!")
    print()
    choice = input("Enter your choice(A/B/C/D/E): ")
    print()
    
    #Q1.a. - Finding the maximum and minimum element in an input list and dislplaying it with their respective indices
    if choice == "A" or choice == "a":

        print("\nFinding the maximum and minimum element of your list along with their positions!")
        mini,maxi = List1[0],List1[0]
        mini_index,maxi_index = 1,1

        for i in range(0,10): 
            if List1[i] < mini: 
                mini = List1[i]
                mini_index = i
            if List1[i] > maxi: 
                maxi = List1[i]
                maxi_index = i + 1
                
        print('Minimum Element in the list' , List1 , 'is' , mini , "at", mini_index) 
        print('Maximum Element in the list' , List1 , 'is' , maxi , "at", maxi_index)
        print()
        continue

    
    #Q1.b. - Displaying the elements of the input list in reverse order
    if choice == "B" or choice == "b":

        print("\nDisplaying your list in reverse order!")

        List2 = []
        m = 9
        while m >= 0:
            List2.append(List1[m])
            m -= 1
        print("The reverse of the original list is: " , List2)
        print()
        continue

   
    #Q1.c. - Finding the mean of even elements and the median of odd elements
    if choice == "C" or choice == "c":

        import math
        sum = 0
        count = 0
        List3 = []
        
        List6 = List1
        
        for i in range(0,10):
            if List6[i] % 2 == 0:
                count += 1
                sum += List6[i]
            
            elif List6[i] % 2 == 1:
                List3.append(List6[i])
                

        mean_List1 = sum/count

        List3.sort() 
        n = len(List3)
        if n % 2 == 0:
            index1 = math.ceil(n/2)
            median_List3 = (List3[index1-1] + List3[index1])/2
            
        elif n % 2 == 1:
            index = math.ceil(n/2)
            median_List3 = List3[index-1]

        print("\nCheck this Out!")
        print("The mean of the even elements of your list" , List6 , "is" , mean_List1)
        print("The median of the odd elements of your list" , List6 , "is" , median_List3)
        print()
        continue

   

    #Q1.d. - Customising the input list using slicing
    if choice == "D" or choice == "d":

        List7 = List1.copy()
        print(List1)
        print("\nCustomising your list with new elements!")
        initial,final = 0,10

        while initial < 0 or final > 9 :
            initial = int(input("Enter the start position for slice: "))
            final = int(input("Enter the final position for slice: "))
            

            if initial < 0 or final > 9:
                print("Sorry! Index out of Range!")
                continue

        new_number = int(input("Enter a number you want to replace the original slice of the list: "))

        List7[(initial-1):(final)] = [new_number]

        print("The new list with the customised values is: " , List7)
        print()
        continue

    

    #Q1.e. - Creating 2 new lists with the prime and composite numbers from the input list respectively
    if choice == "E" or choice == "e":

        print("\nSorting the elements of your list into prime and composite numbers!")

        
        List4 = []
        List5 = []
        List8 = List1
        print(List1)
        print(List8)
        
        for number in List8:
            isPrime = True
            if number > 1:
                for k in range(2,number):
                    if number % k == 0:
                        isPrime = False
                        break
                if not isPrime:
                    List5.append(number)
                        
                elif isPrime:
                    List4.append(number)

        List4.sort()
        List5.sort()

        print("The list containing the prime numbers from your list is",List4)
        print("The list containing the composite numbers from your list is",List5)
        print()
        continue

    if choice == "Exit" or choice == "exit" or choice == "EXIT":
        print()
        print("The program will end now!")
        print("Thank you!")
        break


    else:
        print("Invalid choice!Please choose again!\n")
        continue

"""OUTPUT OF INPUT:
Enter 10 integer numbers of your choice
Enter integer: 1
Enter integer: 2
Enter integer: 3
Enter integer: 4
Enter integer: 5
Enter integer: 6
Enter integer: 5
Enter integer: 5
Enter integer: 7
Enter integer: 8
[1, 2, 3, 4, 5, 6, 5, 5, 7, 8]

The following sets of functions can take place in this program:
A : Displays the maximum and minimum elements along with their posititons
B : Displays the elements in the reverse order
C : Displays the mean of even elements and the median of odd elements
D : Customising the input list just for you!
E : 2 new lists with the prime and composite numbers from the input list
Exit: You may exit the program!

Enter your choice(A/B/C/D/E): a


Finding the maximum and minimum element of your list along with their positions!
Minimum Element in the list [1, 2, 3, 4, 5, 6, 5, 5, 7, 8] is 1 at 1
Maximum Element in the list [1, 2, 3, 4, 5, 6, 5, 5, 7, 8] is 8 at 10

The following sets of functions can take place in this program:
A : Displays the maximum and minimum elements along with their posititons
B : Displays the elements in the reverse order
C : Displays the mean of even elements and the median of odd elements
D : Customising the input list just for you!
E : 2 new lists with the prime and composite numbers from the input list
Exit: You may exit the program!

Enter your choice(A/B/C/D/E): b


Displaying your list in reverse order!
The reverse of the original list is:  [8, 7, 5, 5, 6, 5, 4, 3, 2, 1]

The following sets of functions can take place in this program:
A : Displays the maximum and minimum elements along with their posititons
B : Displays the elements in the reverse order
C : Displays the mean of even elements and the median of odd elements
D : Customising the input list just for you!
E : 2 new lists with the prime and composite numbers from the input list
Exit: You may exit the program!

Enter your choice(A/B/C/D/E): c


Check this Out!
The mean of the even elements of your list [1, 2, 3, 4, 5, 6, 5, 5, 7, 8] is 5.0
The median of the odd elements of your list [1, 2, 3, 4, 5, 6, 5, 5, 7, 8] is 5.0

The following sets of functions can take place in this program:
A : Displays the maximum and minimum elements along with their posititons
B : Displays the elements in the reverse order
C : Displays the mean of even elements and the median of odd elements
D : Customising the input list just for you!
E : 2 new lists with the prime and composite numbers from the input list
Exit: You may exit the program!

Enter your choice(A/B/C/D/E): d

[1, 2, 3, 4, 5, 6, 5, 5, 7, 8]

Customising your list with new elements!
Enter the start position for slice: 2
Enter the final position for slice: 6
Enter a number you want to replace the original slice of the list: 3
The new list with the customised values is:  [1, 3, 5, 5, 7, 8]

The following sets of functions can take place in this program:
A : Displays the maximum and minimum elements along with their posititons
B : Displays the elements in the reverse order
C : Displays the mean of even elements and the median of odd elements
D : Customising the input list just for you!
E : 2 new lists with the prime and composite numbers from the input list
Exit: You may exit the program!

Enter your choice(A/B/C/D/E): e


Sorting the elements of your list into prime and composite numbers!
[1, 2, 3, 4, 5, 6, 5, 5, 7, 8]
[1, 2, 3, 4, 5, 6, 5, 5, 7, 8]
The list containing the prime numbers from your list is [2, 3, 5, 5, 5, 7]
The list containing the composite numbers from your list is [4, 6, 8]

The following sets of functions can take place in this program:
A : Displays the maximum and minimum elements along with their posititons
B : Displays the elements in the reverse order
C : Displays the mean of even elements and the median of odd elements
D : Customising the input list just for you!
E : 2 new lists with the prime and composite numbers from the input list
Exit: You may exit the program!

Enter your choice(A/B/C/D/E): f

Invalid choice!Please choose again!

The following sets of functions can take place in this program:
A : Displays the maximum and minimum elements along with their posititons
B : Displays the elements in the reverse order
C : Displays the mean of even elements and the median of odd elements
D : Customising the input list just for you!
E : 2 new lists with the prime and composite numbers from the input list
Exit: You may exit the program!

Enter your choice(A/B/C/D/E): exit


The program will end now!
Thank you!"""


