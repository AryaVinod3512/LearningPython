String1 = input("Enter a string: ")

while True:
    print("\nYou have the following options to choose from:")
    print("A : You can get a count of all the upper-case and lower-case alphabets, vowels, words and sentences in your input! ")
    print("B : You can see the last letters of all the words of your input! ")
    print("C : You will get a count of the lower-case ts present in your input! ")
    print("D : You will get a count of the occurences of the word 'an' in your input! ")
    print("E : You will get a record of all the palindromic words in your input! ")
    print("F : You will get a copy of your input with all the occurences of the word 'an' deleted! ")
    print("Exit: You may exit the program!")
    choice = input("\nEnter your choice(A/B/C/D/E/F/Exit): ")

    UCvowels = "AEIOU"
    LCvowels = "aeiou"
    UCalphabet = "BCDFGHJKLMNPQRSTVWXYZ"
    LCalphabet = "bcdfghjklmnpqrstvwxyz"

#Q6.(a) - Find and display the number of upper-case and lower-case alphabets, vowels, words and sentences and their counts in a neat format with suitable message.
    if choice == "a" or choice == "A":
        
        
        words = space = sent = UCA = LCA = vowels = 0
        
        for alp in String1:

            if alp == " ":
                space += 1

            elif alp == ".":
                sent += 1

            elif alp in UCvowels or alp in LCvowels:
                vowels += 1

            elif alp in UCalphabet: 
                UCA += 1

            elif alp in LCalphabet:
                LCA += 1

        words = space + 1

        print()
        print("*************************** OUTPUT OPTION A ***************************")
        print(" FEATURE\t\t COUNT","\n Words", "\t\t\t", words, "\n", "Sentences\t\t",  sent, "\n" ,  "Uppercase Consonants\t",UCA, "\n" ,  "Lowercase Consonants\t",LCA, "\n" ,  "Vowels\t\t\t",vowels)
        continue


#Q6.(b) - Print only the last character of every word(should not be full stop or comma or any other special character).
    elif choice == "b" or choice == "B":

        print()
        print("*************************** OUTPUT OPTION B ***************************")
        print("The last letter of every word in your input is:")
        String2 = String1 + " "
        for ch in range(len(String2)):
            if String2[ch] == " " and ((String2[ch-1] in UCvowels) or (String2[ch-1] in LCvowels) or (String2[ch-1] in UCalphabet) or (String2[ch-1] in LCalphabet)):
                print(String2[ch - 1], end = " ")
        print()
        continue

#Q6.(c) - Count the number of lower case ‘t’ in the given string.
    elif choice == "c" or choice == "C":

        print()
        print("*************************** OUTPUT OPTION C ***************************")
        count = 0
        for ch in String1:
            if ch == "t":
                count += 1
        print("The letter 't' is present",count,"times in the given string!")
        continue


#Q6.(d) - Count and display the number of occurrences of the word ‘an’ in the given string.
    elif choice == "d" or choice == "D":

        
        String_split = String1.split(" ")
        count = 0
        for ch in String_split:
            if ch == "an":
                count += 1

        print()
        print("*************************** OUTPUT OPTION D ***************************")
        print("The word 'an' occurs",count,"times in the input statement!")
        continue
    
       
#Q6.(e) - Display and count all the palindromic words in the input string.
    elif choice == "e" or choice == "E":
        
        String2 = String1.lower()
        String_split = String2.split(" ") 

        print()
        print("*************************** OUTPUT OPTION E ***************************")
        print("The palindromic words in your sentence are:")
        s1 = ""
        count = 0
        for word in String_split:
            for ch in word:
                if ch == "," or ch == ".":
                    word = word.replace(ch,"")
            for i in range(len(word)-1,-1,-1):
                s1 += word[i]
                if word == s1:
                    print(word)
                    count += 1
            s1 = ""
        print("Thus, there are",count,"palindromic words in your sentence!")
        continue
    

#Q6.(f) - Display the original sring without all the occurences of the word 'an'.
    elif choice == "f" or choice == "F":

        word = " an "
        if word in String1:
            String1 = String1.replace(word," ")

        print()
        print("*************************** OUTPUT OPTION F ***************************")
        print("Your sentence without the word 'an' is:")
        print(String1)
        continue

    
    elif choice == "Exit" or choice == "exit" or choice == "EXIT":
        print()
        print("The program will end now!")
        print("Thank you!")
        break


    else:
        print("Invalid choice!Please choose again!\n")
        continue
   
            
    
