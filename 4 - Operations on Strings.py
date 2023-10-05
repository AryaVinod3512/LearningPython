#Program to perform operations on an input string
print("This is a program to perform certain operations on an input string")

inp_list = input("Enter a sentence or a phrase: ").split()

while True:
    print("\nA: Count number of words in input string")
    print("B: Display frequency of each appearing word")
    print("C: Search for a particular word")
    print("E: Exit the program")
    choice = input("\nEnter a choice(A/B/C/E): ")

    if choice.upper() == "A":
        
        print("The para has",len(inp_list),"words")

    elif choice.upper() == "B":
        
        count = 0
        for i in inp_list:
            count = inp_list.count(i)
            print(i,count,sep = "\t",end = "\n")

    elif choice.upper() == "C":

        x = input("Enter a word: ")
        if x in inp_list:
            print("The word",x,"has been found at index",(inp_list.index(x)) + 1)
        elif x not in inp_list:
            print("The word",x,"was not found in the para.")

    elif choice.upper() == "E":

        print("The Program will end now! Thank you!")
        break

    else:
        print("Enter a correct choice!")
        continue

"""OUTPUT:
This is a program to perform certain operations on an input string
Enter a sentence or a phrase: I love igpay atinlay

A: Count number of words in input string
B: Display frequency of each appearing word
C: Search for a particular word
E: Exit the program

Enter a choice(A/B/C/E): a
The para has 4 words

A: Count number of words in input string
B: Display frequency of each appearing word
C: Search for a particular word
E: Exit the program

Enter a choice(A/B/C/E): b
I	1
love	1
igpay	1
atinlay	1

A: Count number of words in input string
B: Display frequency of each appearing word
C: Search for a particular word
E: Exit the program

Enter a choice(A/B/C/E): c
Enter a word: love
The word love has been found at index 2

A: Count number of words in input string
B: Display frequency of each appearing word
C: Search for a particular word
E: Exit the program

Enter a choice(A/B/C/E): d
Enter a correct choice!

A: Count number of words in input string
B: Display frequency of each appearing word
C: Search for a particular word
E: Exit the program

Enter a choice(A/B/C/E): e
The Program will end now! Thank you!
"""
