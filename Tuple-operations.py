#Q2. Doing 3 different sets of operations on a tuple input by the user
#Code segment to get 5 string inputs from user and store in a tuple
print("Creating a tuple with 5 elements!")
tuple1 = ()
List1 = []
for i in range(0,5):
    element = input("Enter an element: ")
    List1.append(element)
    tuple1 = tuple(List1)

print(tuple1)
print()


#Code segment to drive the program based on choice input by user
while True:
    print("The following sets of functions can take place in this program:")
    print("A : The words of the tuple are reversed")
    print("B : The uppercase consonants and the lowercase vowels of each word will be displayed with ther count")
    print("C : The alternate letter in each word will be displayed as a new word of another tuple")
    print("Exit: You may exit the program!")
    print()
    choice = input("Enter your choice - A/B/C/Exit: ")
    print()

    #Code segment for the first function (A)
    if choice == "A" or choice == "a":

        reverse = []
        for issue in tuple1:
            string_org = issue
            string_rv = string_org[::-1]
            reverse.append(string_rv)
        print("The reverse of each word in your tuple is: ",reverse)
        print()
        continue
    
    #Code segment for the second function (B)
    elif choice == "B" or choice == "b":

        print("The tabular format holding the count of uppercase consonants and lowercase vowels is given below:")
        UC_count, LV_count = 0,0
        UC = []
        LV = []

        for word in tuple1:
            temp = word
            for ch in range(0,len(temp)):
                if temp[ch] in "aeiou":
                  LV.append(temp[ch])
                  LV_count += 1
                elif (temp[ch] not in "AEIOU") and (ord(temp[ch])>65 and ord(temp[ch])<= 90):
                    UC.append(temp[ch])
                    UC_count += 1   

            print(word,"\t",UC,"\t",UC_count,"\t",LV,"\t",LV_count)
            UC_count, LV_count = 0,0
            UC = []
            LV = []
        print()
        continue 
   


    #Code segment for the third function (C)
    elif choice == "C" or choice == "c":

        Alternate = ()
        List2 = []
        string_final = ""
        for string in tuple1:
            string_var = string
            for ch2 in range(0,len(string_var)):
                if ch2 % 2 == 0:
                    string_final += string_var[ch2]
                else:
                    pass

            List2.append(string_final)
            string_final = ""

        Alternate = tuple(List2)

        print("The alternate letters of each word in your tuple are: ")
        print(Alternate)
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
Creating a tuple with 5 elements!
Enter an element: Cat
Enter an element: BAt
Enter an element: TaR
Enter an element: MoM
Enter an element: DaD
('Cat', 'BAt', 'TaR', 'MoM', 'DaD')

The following sets of functions can take place in this program:
A : The words of the tuple are reversed
B : The uppercase consonants and the lowercase vowels of each word will be displayed with ther count
C : The alternate letter in each word will be displayed as a new word of another tuple
Exit: You may exit the program!

Enter your choice - A/B/C/Exit: a

The reverse of each word in your tuple is:  ['taC', 'tAB', 'RaT', 'MoM', 'DaD']

The following sets of functions can take place in this program:
A : The words of the tuple are reversed
B : The uppercase consonants and the lowercase vowels of each word will be displayed with ther count
C : The alternate letter in each word will be displayed as a new word of another tuple
Exit: You may exit the program!

Enter your choice - A/B/C/Exit: b

The tabular format holding the count of uppercase consonants and lowercase vowels is given below:
Cat 	 ['C'] 	         1 	 ['a'] 	 1
BAt 	 ['B'] 	         1 	 [] 	 0
TaR 	 ['T', 'R'] 	 2 	 ['a'] 	 1
MoM 	 ['M', 'M'] 	 2 	 ['o'] 	 1
DaD 	 ['D', 'D'] 	 2 	 ['a'] 	 1

The following sets of functions can take place in this program:
A : The words of the tuple are reversed
B : The uppercase consonants and the lowercase vowels of each word will be displayed with ther count
C : The alternate letter in each word will be displayed as a new word of another tuple
Exit: You may exit the program!

Enter your choice - A/B/C/Exit: c

The alternate letters of each word in your tuple are: 
('Ct', 'Bt', 'TR', 'MM', 'DD')

The following sets of functions can take place in this program:
A : The words of the tuple are reversed
B : The uppercase consonants and the lowercase vowels of each word will be displayed with ther count
C : The alternate letter in each word will be displayed as a new word of another tuple
Exit: You may exit the program!

Enter your choice - A/B/C/Exit: d

Invalid choice!Please choose again!

The following sets of functions can take place in this program:
A : The words of the tuple are reversed
B : The uppercase consonants and the lowercase vowels of each word will be displayed with ther count
C : The alternate letter in each word will be displayed as a new word of another tuple
Exit: You may exit the program!

Enter your choice - A/B/C/Exit: EXIT


The program will end now!
Thank you!
"""
