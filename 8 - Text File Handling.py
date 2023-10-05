print("This program performs operations on a text file called 'my_file.txt'")

#Creating text file

def Create_file():
    
    f = open("my_file.txt",'w')
    print("\nThe text file 'my_file.txt' has been successfully created!")

    string = input("Enter a para: ")
    f.write(string)
    print("Content has been successfully added to the file")
    
    f.close()
    
#Reading the text file

def Read_file():
    
    f = open("my_file.txt",'r')
    
    print("\nThe content of 'my_file.txt' is:")
    content = f.read()
    print(content)
    
    f.close()
    
#Capitalize the first letter of every word and print the word

def Caps_file():

    f = open("my_file.txt",'r')

    para = f.read()
    
    list1 = para.split()
    new_string = ""
    
    for i in list1:
        new_string = new_string + (i.capitalize()) + " "

    print(new_string)
    
    f.close()        
    

#Print the content of the file in reverse order

def Reverse_file():

    f = open("my_file.txt",'r')

    para = f.read()

    new_string = ""
    for i in range(-1,-(len(para))-1,-1):
        new_string += para[i]

    print(new_string)
    
    f.close()  

while True:
    
    print("\nA: Create a text file to old the content")
    print("B: Read the text file created and print its content")
    print("C: Capitalize the first letter of every word of the content")
    print("D: Reverse the entire string")
    print("E: Exit the program")

    choice = input("\nEnter your choice(A/B/C/D/E): ")

    if choice.upper() == "A":

        Create_file()

    elif choice.upper() == "B":

        Read_file()

    elif choice.upper() == "C":

        Caps_file()

    elif choice.upper() == "D":

        Reverse_file()

    elif choice.upper() == "E":

        print("The program will end now! Thank you!")
        break

    else:
        print("\nEnter a correct choice!")
        continue

"""OUTPUT:
This program performs operations on a text file called 'my_file.txt'

A: Create a text file to old the content
B: Read the text file created and print its content
C: Capitalize the first letter of every word of the content
D: Reverse the entire string
E: Exit the program

Enter your choice(A/B/C/D/E): a

The text file 'my_file.txt' has been successfully created!
Enter a para: I love pig latin
Content has been successfully added to the file

A: Create a text file to old the content
B: Read the text file created and print its content
C: Capitalize the first letter of every word of the content
D: Reverse the entire string
E: Exit the program

Enter your choice(A/B/C/D/E): b

The content of 'my_file.txt' is:
I love pig latin

A: Create a text file to old the content
B: Read the text file created and print its content
C: Capitalize the first letter of every word of the content
D: Reverse the entire string
E: Exit the program

Enter your choice(A/B/C/D/E): c
I Love Pig Latin 

A: Create a text file to old the content
B: Read the text file created and print its content
C: Capitalize the first letter of every word of the content
D: Reverse the entire string
E: Exit the program

Enter your choice(A/B/C/D/E): d
nital gip evol I

A: Create a text file to old the content
B: Read the text file created and print its content
C: Capitalize the first letter of every word of the content
D: Reverse the entire string
E: Exit the program

Enter your choice(A/B/C/D/E): e
The program will end now! Thank you!
"""
    
