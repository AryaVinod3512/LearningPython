Student = ()
n = int(input("Enter the number of students whose details you want to record: "))

for i in range(1,(n+1)):
    list1  = []
    tuple1 = ()
    admno = input("Enter Admission Number of student: ")
    name  = input("Enter Name of student: ")
    cls   = input("Enter Class of student: ")
    sec   = input("Enter Section of student: ")
    fee   = input("Enter Fee of student: ")
    print()
    list1.append(cls)
    list1.append(sec)
    list1.append(fee)
    tuple1 = ((admno,name,list1))
    Student = Student + (tuple1,)

print()
print(" "*30, "STUDENT DETAILS", " "*30)
print("_"*80)
print("Admin No.\tStudent Name\t\tClass, Section, Fees")
print("_"*80)

for i in Student:
    for j in i:
        print(j,end = "\t\t   ")        
    print()

new_admno = input("Enter Admission Number of the student whose details are to be edited: ")
new_cls   = input("Enter new Class of student: ")
new_sec   = input("Enter new Section of student: ")
new_fee   = input("Enter new Fee of student: ")
print()

for j in Student:
    if j[0] == new_admno:
        j[2][0] = new_cls
        j[2][1] = new_sec
        j[2][2] = new_fee
       
        
print()
print(" "*30, "STUDENT DETAILS", " "*30)
print("_"*80)
print("Admin No.\tStudent Name\t\tClass, Section, Fees")
print("_"*80)

for i in Student:
    for j in i:
        print(j,end = "\t\t   ")        
    print()
print()

"""OUTPUT:
Enter the number of students whose details you want to record: 3
Enter Admission Number of student: 123
Enter Name of student: Abhi
Enter Class of student: 09
Enter Section of student: B
Enter Fee of student: 90000

Enter Admission Number of student: 456
Enter Name of student: Anna
Enter Class of student: 10
Enter Section of student: B
Enter Fee of student: 100000

Enter Admission Number of student: 789
Enter Name of student: Adya
Enter Class of student: 11
Enter Section of student: B
Enter Fee of student: 110000


                               STUDENT DETAILS                               
________________________________________________________________________________
Admin No.	Student Name		Class, Section, Fees
________________________________________________________________________________
123		   Abhi		   ['09', 'B', '90000']		   
456		   Anna		   ['10', 'B', '100000']		   
789		   Adya		   ['11', 'B', '110000']

Enter Admission Number of the student whose details are to be edited: 789
Enter new Class of student: 12
Enter new Section of student: A
Enter new Fee of student: 120000


                               STUDENT DETAILS                               
________________________________________________________________________________
Admin No.	Student Name		Class, Section, Fees
________________________________________________________________________________
123		   Abhi		   ['09', 'B', '90000']		   
456		   Anna		   ['10', 'B', '100000']		   
789		   Adya		   ['12', 'A', '120000']			   
"""
