#Q5.To accept two square matrices of same odd dimensions and perform various processes on them
mat1=[]
mat2=[]
matsum=[]

row_mat1 = int(input('Number of rows for first matrix: '))
col_mat1 = int(input('Number of columns for first matrix: '))
row_mat2 = int(input('Number of rows for second matrix: '))
col_mat2 = int(input('Number of columns for second matrix: '))


while (row_mat1 % 2 != 1) and (row_mat2 % 2 != 1) and (col_mat1 % 2 != 1) and (col_mat2 % 2 != 1):
    print("Please enter odd dimensions for the input matrices!")
    row_mat1 = int(input('Number of rows for first matrix: '))
    col_mat1 = int(input('Number of columns for first matrix: '))
    row_mat2 = int(input('Number of rows for second matrix: '))
    col_mat2 = int(input('Number of columns for second matrix: '))

if (row_mat1 != row_mat2) or (col_mat1 != col_mat2):
    print("The matrices are not of the same order! Cannot compute sum of matrices!")
    exit

elif (row_mat1 == row_mat2) and (col_mat1 == col_mat2) and (row_mat1 % 2 == 1) and (row_mat2 % 2 == 1) and (col_mat1 % 2 == 1) and (col_mat2 % 2 == 1):
    
    
    for i in range(row_mat1):
        print("Row",(i+1))
        m1=[]
        for j in range(col_mat1):
            term = int(input("Enter a number:"))
            m1.append(term)
        mat1.append(m1)
    print()
    print("Matrix 1")
    for i in range(row_mat1):
        for  j in range(col_mat1):
            print(mat1[i][j],end = " ")
        print()


    print()
    for k in range(row_mat2):
        print("Row",(k+1))
        m2=[]
        for l in range(col_mat2):
            term = int(input("Enter a number:"))
            m2.append(term)
        mat2.append(m2)
    print()
    print("Matrix 2")
    for i in range(row_mat2):
        for  j in range(col_mat2):
            print(mat2[i][j],end = " ")
        print()
    print()
    print()

while True:
    print("You have the following options to choose from:")
    print("A : You can see the sum of both input matrices! ")
    print("B : You can see another matrix of same dimensions with alternate rows picked from the 2 input matrices! ")
    print("C : You can see a matrix with principlal diagonal elements as 1 and secondary diagonal elements as 0 from your 1st input matrix! ")
    print("D : You can see the sum of the elements of every row and column of the 2nd input matrix! ")
    print("E : You can see a 2 x 2 matrix with the corner elements of the 1st input matrix! ")
    print("Exit: You may exit the program!")
    choice = input("\nEnter your choice(A/B/C/D/E/Exit): ")

#Q5.(a) - Computing sum of 2 input matrices
    if choice == "a" or choice == "A":
        
        for i in range(row_mat1):
            m = []
            for j in range(col_mat1):
                term = mat1[i][j] + mat2[i][j]
                m.append(term)
            matsum.append(m)
        print()

        print("The matrix that gives the sum of the input matrices is: ")
        for i in range(row_mat1):
            for j in range(col_mat1):
                print(matsum[i][j],end = ' ')
            print()
        print()
        continue


#Q5.(b) - Creating another matrix of same dimensions with alternate rows picked from the 2 input matrices
    elif choice == "b" or choice == "B":

        for i in range(row_mat1):
            for j in range(col_mat1):
                if (i == 0) or (i % 2 == 0):
                  print(mat1[i][j],end = ' ')
                else:
                    print(mat2[i][j],end = ' ')
            print()
        print()
        continue
        
#Q5.(c) - Formatting a matrix with principlal diagonal elements as 1 and secondary diagonal elements as 0 from your 1st input matrix
    elif choice == "c" or choice == "C":

        diag = []
        for i in range(row_mat1):
            m=[]
            for j in range(row_mat1):
                if i == j:                               
                    m.append(1)
                elif (i+j == (row_mat1 - 1)):
                    m.append(0)                         
                else:
                    m.append(mat1[i][j])               
            diag.append(m)

        for i in range(row_mat1):
            for j in range(row_mat1):
                print(diag[i][j], end = ' ')
            print()
        print()
        continue            

                    
#Q5.(d) - Computing and display the sum of the elements of every row and column of the 2nd input matrix
    if choice == "d" or choice == "D":

         
        Lsum=[]
        for i in range(row_mat1):
            sum_row = 0
            for j in range(row_mat1):
                sum_row += mat2[i][j]                                  

            Lsum.append(sum_row)
            print("Sum of " + str(i+1) +" row: " + str(sum_row));

        for i in range(row_mat1):
            sum_col = 0
            for j in range(row_mat1):
                sum_col += mat2[j][i]                                   

            Lsum.append(sum_col)
            print("Sum of " + str(i+1) +" column: " + str(sum_col));

        print("List of all the sums is : ",Lsum)
        print()
        continue

        
#Q5.(e) - Creating a 2 x 2 matrix with the corner elements of the 1st input matrix
    elif choice == "e" or choice == "E":
        
        L_corner = []
        for i in range(row_mat1):
            for j in range(row_mat1):
                if (i == 0 or i == (row_mat1 - 1)) and (j == 0 or j == (row_mat1-1)):        
                    L_corner.append(mat1[i][j])
        
        print()
        print("Matrix with corner elements of 2nd input matrix: ")

        for i in range (len(L_corner)):                              
            if i%2==0:
                print(L_corner[i],end = ' ')
            else:
                print(L_corner[i])
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
Number of rows for first matrix: 3
Number of columns for first matrix: 3
Number of rows for second matrix: 3
Number of columns for second matrix: 3
Row 1
Enter a number:1
Enter a number:2
Enter a number:1
Row 2
Enter a number:3
Enter a number:4
Enter a number:3
Row 3
Enter a number:5
Enter a number:6
Enter a number:5

Matrix 1
1 2 1 
3 4 3 
5 6 5 

Row 1
Enter a number:7
Enter a number:8
Enter a number:7
Row 2
Enter a number:8
Enter a number:9
Enter a number:8
Row 3
Enter a number:9
Enter a number:2
Enter a number:9

Matrix 2
7 8 7 
8 9 8 
9 2 9 


You have the following options to choose from:
A : You can see the sum of both input matrices! 
B : You can see another matrix of same dimensions with alternate rows picked from the 2 input matrices! 
C : You can see a matrix with principlal diagonal elements as 1 and secondary diagonal elements as 0 from your 1st input matrix! 
D : You can see the sum of the elements of every row and column of the 2nd input matrix! 
E : You can see a 2 x 2 matrix with the corner elements of the 1st input matrix! 
Exit: You may exit the program!

Enter your choice(A/B/C/D/E/Exit): a

The matrix that gives the sum of the input matrices is: 
8 10 8 
11 13 11 
14 8 14 

You have the following options to choose from:
A : You can see the sum of both input matrices! 
B : You can see another matrix of same dimensions with alternate rows picked from the 2 input matrices! 
C : You can see a matrix with principlal diagonal elements as 1 and secondary diagonal elements as 0 from your 1st input matrix! 
D : You can see the sum of the elements of every row and column of the 2nd input matrix! 
E : You can see a 2 x 2 matrix with the corner elements of the 1st input matrix! 
Exit: You may exit the program!

Enter your choice(A/B/C/D/E/Exit): b
1 2 1 
8 9 8 
5 6 5 

You have the following options to choose from:
A : You can see the sum of both input matrices! 
B : You can see another matrix of same dimensions with alternate rows picked from the 2 input matrices! 
C : You can see a matrix with principlal diagonal elements as 1 and secondary diagonal elements as 0 from your 1st input matrix! 
D : You can see the sum of the elements of every row and column of the 2nd input matrix! 
E : You can see a 2 x 2 matrix with the corner elements of the 1st input matrix! 
Exit: You may exit the program!

Enter your choice(A/B/C/D/E/Exit): c
1 2 0 
3 1 3 
0 6 1

You have the following options to choose from:
A : You can see the sum of both input matrices! 
B : You can see another matrix of same dimensions with alternate rows picked from the 2 input matrices! 
C : You can see a matrix with principlal diagonal elements as 1 and secondary diagonal elements as 0 from your 1st input matrix! 
D : You can see the sum of the elements of every row and column of the 2nd input matrix! 
E : You can see a 2 x 2 matrix with the corner elements of the 1st input matrix! 
Exit: You may exit the program!

Enter your choice(A/B/C/D/E/Exit): d
Sum of 1 row: 22
Sum of 2 row: 25
Sum of 3 row: 20
Sum of 1 column: 24
Sum of 2 column: 19
Sum of 3 column: 24
List of all the sums is :  [22, 25, 20, 24, 19, 24]

You have the following options to choose from:
A : You can see the sum of both input matrices! 
B : You can see another matrix of same dimensions with alternate rows picked from the 2 input matrices! 
C : You can see a matrix with principlal diagonal elements as 1 and secondary diagonal elements as 0 from your 1st input matrix! 
D : You can see the sum of the elements of every row and column of the 2nd input matrix! 
E : You can see a 2 x 2 matrix with the corner elements of the 1st input matrix! 
Exit: You may exit the program!

Enter your choice(A/B/C/D/E/Exit): e

Matrix with corner elements of 2nd input matrix: 
1 1
5 5

You have the following options to choose from:
A : You can see the sum of both input matrices! 
B : You can see another matrix of same dimensions with alternate rows picked from the 2 input matrices! 
C : You can see a matrix with principlal diagonal elements as 1 and secondary diagonal elements as 0 from your 1st input matrix! 
D : You can see the sum of the elements of every row and column of the 2nd input matrix! 
E : You can see a 2 x 2 matrix with the corner elements of the 1st input matrix! 
Exit: You may exit the program!

Enter your choice(A/B/C/D/E/Exit): f
Invalid choice!Please choose again!

You have the following options to choose from:
A : You can see the sum of both input matrices! 
B : You can see another matrix of same dimensions with alternate rows picked from the 2 input matrices! 
C : You can see a matrix with principlal diagonal elements as 1 and secondary diagonal elements as 0 from your 1st input matrix! 
D : You can see the sum of the elements of every row and column of the 2nd input matrix! 
E : You can see a 2 x 2 matrix with the corner elements of the 1st input matrix! 
Exit: You may exit the program!

Enter your choice(A/B/C/D/E/Exit): Exit

The program will end now!
Thank you!
"""
