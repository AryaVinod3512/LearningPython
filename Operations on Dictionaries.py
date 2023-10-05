#Perform operations on a dictionary
print("This program performs certain operations on an employee database records")

n = int(input("Enter how many records you want to store: "))

Microsoft = {}

for i in range(n):
    emp_details = {}
    emp_id = int(input("\nEnter employee id: "))
    emp_name = input("Enter employee name: ")
    emp_dob = input("Enter employee DOB: ")
    emp_des = input("Enter employee designation: ")

    emp_details['Employee_Name'] = emp_name
    emp_details['DOB'] = emp_dob
    emp_details['Designation'] = emp_des
    Microsoft[emp_id] = emp_details
    
#Microsoft = {100 : {'Employee_Name' : 'Harsh' , 'DOB' : 10-09-08 , 'Designation' : Architect},101 : {'Employee_Name' : 'Chirag' , 'DOB' : 11-09-08 , 'Designation' : HR}, 102 : {'Employee_Name' : 'Manasa' , 'DOB' : 12-09-08 , 'Designation' : Manager}}

while True:
    
    print("\nA : Display the database")
    print("B : Search for a particular record in the database")
    print("C : Insert new record into the database")
    print("D : Delete a record from the database")
    print("E : Exit the program ")
    
    choice = input("\nEnter your choice(A/B/C/D/E): ")
    
#Display the database in tabular format
    if choice.upper() == "A":
        
        Status = bool(Microsoft)
        if  Status == False:
            print("\n No Employee Database found to print \n")
            
        else:

            print()
            print(" "*30, "EMPLOYEE DATABASE")
            print("_"*80)
            print("Employee_Id\tEmployee_Name\tDOB\t\tDesignation")
            print("_"*80)

            for i in Microsoft:
                print(i,"\t\t", Microsoft[i]['Employee_Name'],"\t", Microsoft[i]['DOB'],"\t\t", Microsoft[i]['Designation'])
                    
            print()

        continue

    
#Search for a particular record in a database
    elif choice.upper() == "B":

        sr_name = input("Enter name of employee whose record is to be retrieved: ")

        flag = 0
        for i in Microsoft:
            if Microsoft[i]['Employee_Name'] == sr_name:
                print("_"*80)
                print("Employee_Id\tEmployee_Name\tDOB\t\tDesignation")
                print("_"*80)

                print(i,"\t\t", Microsoft[i]['Employee_Name'],"\t", Microsoft[i]['DOB'],"\t\t", Microsoft[i]['Designation'])
                flag = 1

        if flag == 0:
                print("The record of",sr_name,"was not found!")

        continue

#Insert new records into a database
    elif choice.upper() == "C":

        new_emp_id = int(input("\nEnter employee id: "))
        new_emp_name = input("Enter employee name: ")
        new_emp_dob = input("Enter employee DOB: ")
        new_emp_des = input("Enter employee designation: ")

        Microsoft[new_emp_id] = {'Employee_Name' : new_emp_name , 'DOB' : new_emp_dob , 'Designation' : new_emp_des}

        print()
        print(" "*30, "EMPLOYEE DATABASE")
        print("_"*80)
        print("Employee_Id\tEmployee_Name\tDOB\tDesignation")
        print("_"*80)

        for i in Microsoft:
            print(i,"\t\t", Microsoft[i]['Employee_Name'],"\t", Microsoft[i]['DOB'],"\t\t", Microsoft[i]['Designation'])
                
        continue   

#Delete a record from the database
    elif choice.upper() == "D":

        sr_id = int(input("Enter id of the employee whose record is to be deleted: "))

        flag = 0
        for i in Microsoft.copy():
            if i == sr_id:
                Microsoft.pop(i)
                flag = 1

        if flag == 0:
                print("The record of employeeId",sr_id,"was not found!")

        elif flag == 1:
            print("The record of employeeId",sr_id,"was found!\n")

            print("_"*80)
            print("Employee_Id\tEmployee_Name\tDOB\t\tDesignation")
            print("_"*80)

            for i in Microsoft:
                print(i,"\t\t", Microsoft[i]['Employee_Name'],"\t", Microsoft[i]['DOB'],"\t\t", Microsoft[i]['Designation'])

        continue


    elif choice.upper() == "E":
        
        print("The program will end now!Thank you!")
        break


    else:
        print("Invalid choice!Please choose again!\n")
        continue

"""OUTPUT:
This program performs certain operations on an employee database records
Enter how many records you want to store: 3

Enter employee id: 100
Enter employee name: Harsh
Enter employee DOB: 10-09-08
Enter employee designation: Architect

Enter employee id: 101
Enter employee name: Chirag
Enter employee DOB: 11-09-08
Enter employee designation: HR

Enter employee id: 102
Enter employee name: Manasa
Enter employee DOB: 12-09-08
Enter employee designation: Manager

A : Display the database
B : Search for a particular record in the database
C : Insert new record into the database
D : Delete a record from the database
E : Exit the program 

Enter your choice(A/B/C/D/E): a

                               EMPLOYEE DATABASE
________________________________________________________________________________
Employee_Id	Employee_Name	    DOB		         Designation
________________________________________________________________________________
100 		 Harsh 	         10-09-08 		 Architect
101 		 Chirag 	 11-09-08 		 HR
102 		 Manasa 	 12-09-08 		 Manager


A : Display the database
B : Search for a particular record in the database
C : Insert new record into the database
D : Delete a record from the database
E : Exit the program 

Enter your choice(A/B/C/D/E): b
Enter name of employee whose record is to be retrieved: Manasa
________________________________________________________________________________
Employee_Id	Employee_Name	   DOB		         Designation
________________________________________________________________________________
102 		 Manasa 	 12-09-08 		 Manager

A : Display the database
B : Search for a particular record in the database
C : Insert new record into the database
D : Delete a record from the database
E : Exit the program 

Enter your choice(A/B/C/D/E): c

Enter employee id: 103
Enter employee name: Hamsini
Enter employee DOB: 13-09-08
Enter employee designation: Senior Manager

                               EMPLOYEE DATABASE
________________________________________________________________________________
Employee_Id	Employee_Name	    DOB	                 Designation
________________________________________________________________________________
100 		 Harsh 	         10-09-08 		 Architect
101 		 Chirag 	 11-09-08 		 HR
102 		 Manasa 	 12-09-08 		 Manager
103 		 Hamsini 	 13-09-08 		 Senior Manager

A : Display the database
B : Search for a particular record in the database
C : Insert new record into the database
D : Delete a record from the database
E : Exit the program 

Enter your choice(A/B/C/D/E): d
Enter id of the employee whose record is to be deleted: 101
The record of employeeId 101 was found!

________________________________________________________________________________
Employee_Id	Employee_Name	   DOB		         Designation
________________________________________________________________________________
100 		 Harsh 	         10-09-08 		 Architect
102 		 Manasa 	 12-09-08 		 Manager
103 		 Hamsini 	 13-09-08 		 Senior Manager

A : Display the database
B : Search for a particular record in the database
C : Insert new record into the database
D : Delete a record from the database
E : Exit the program 

Enter your choice(A/B/C/D/E): e
The program will end now!Thank you!
"""
