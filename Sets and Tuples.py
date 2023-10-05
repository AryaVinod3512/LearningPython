print("This program performs operations on sets and tuples")

setdata = set()
tupledata = tuple()

#run infinite loop for menu
while True:
    print("\nS : Set Operation \nT : Tuple Operations \nE : Exit Program\n")
    choice = input("Enter your choice(S/T/E): ")
    
    if choice.lower() == "s":
        
        while True:
            print("\nChoose the Set operation")
            print("1 : Add/Insert")
            print("2 : Remove/Delete")
            print("3 : Update/Append")
            print("4 : Display/View")
            print("0 : Exit")
            
            ops = input("\nEnter your choice of set operation(0/1/2/3/4/5): ")
                           
            if ops == "1":

                n = int(input("Enter how many elements you want to add to set: "))
                
                for i in range(n):
                    data = input("Enter the element to add : ")#read the data from the user
                    setdata.add(data)#adds data to set
                        
                print(setdata)
                      
            elif ops == "2":
                
                data = input("Enter the element to delete : ")        #read the data from the user
                setdata.discard(data)#delets perticular data from the set
                
                print(setdata)
                
            elif ops == "3":
                
                data = set(input("Enter an element to add to the existing set: "))#read the data from the user
                setdata.update(data)#Update data
                
                print(setdata)
                
            elif ops == "4":
                print(setdata)#print set
                
            elif ops == "0":
                print("The set operations will end now! Thank you!")
                break
                continue
            
            else:
                print("Invalid Choice")
                continue
                
    elif choice.lower() == "t":
        
        while True:
            print("\nChoose the Tuple operation you want to perform")
            print("1 : Add/Insert")
            print("2 : Display/View")
            print("3 : Delete Tuple")
            print("0 : Exit\n")
            
            ops = input("\nEnter your choice of tuple operation(0/1/2/3): ")
            
            if ops == "1":
                
                data = input("Enter the tuple elements to add : ")#read the data from the user
                tupledata += (data,)#New data is appended to the tuple

                print(tupledata)

            elif ops == "2":

                try:
                    print(tupledata)#prints the tuple data
                except NameError:
                    print("The tuple does not exist or has been deleted")
                
            elif ops == "3":
                
                del tupledata #delets entire tuple
                print("Tuple has been deleted!")
           
            elif ops == "0":
                print("The tuple operations will end now! Thank you!")
                break
                continue
            
            else:
                print("Invalid Choice")
                continue
                
    elif choice.lower() == "e":
        print("The program will end now! Thank you!")
        break
        
                
"""OUTPUT:
This program performs operations on sets and tuples

S : Set Operation 
T : Tuple Operations 
E : Exit Program

Enter your choice(S/T/E): s

Choose the Set operation
1 : Add/Insert
2 : Remove/Delete
3 : Update/Append
4 : Display/View
0 : Exit

Enter your choice of set operation(0/1/2/3/4/5): 1
Enter how many elements you want to add to set: 4
Enter the element to add : 1
Enter the element to add : 2
Enter the element to add : 2
Enter the element to add : Jam
{'1', 'Jam', '2'}

Choose the Set operation
1 : Add/Insert
2 : Remove/Delete
3 : Update/Append
4 : Display/View
0 : Exit

Enter your choice of set operation(0/1/2/3/4/5): 2
Enter the element to delete : 2
{'1', 'Jam'}

Choose the Set operation
1 : Add/Insert
2 : Remove/Delete
3 : Update/Append
4 : Display/View
0 : Exit

Enter your choice of set operation(0/1/2/3/4/5): 3
Enter an element to add to the existing set: 6
{'1', '6', 'Jam'}

Choose the Set operation
1 : Add/Insert
2 : Remove/Delete
3 : Update/Append
4 : Display/View
0 : Exit

Enter your choice of set operation(0/1/2/3/4/5): 4
{'1', '6', 'Jam'}

Choose the Set operation
1 : Add/Insert
2 : Remove/Delete
3 : Update/Append
4 : Display/View
0 : Exit

Enter your choice of set operation(0/1/2/3/4/5): 0
The set operations will end now! Thank you!

S : Set Operation 
T : Tuple Operations 
E : Exit Program

Enter your choice(S/T/E): t

Choose the Tuple operation you want to perform
1 : Add/Insert
2 : Display/View
3 : Delete Tuple
0 : Exit


Enter your choice of tuple operation(0/1/2/3): 1
Enter the tuple elements to add : 1 2 3
('1 2 3',)

Choose the Tuple operation you want to perform
1 : Add/Insert
2 : Display/View
3 : Delete Tuple
0 : Exit


Enter your choice of tuple operation(0/1/2/3): 2
('1 2 3',)

Choose the Tuple operation you want to perform
1 : Add/Insert
2 : Display/View
3 : Delete Tuple
0 : Exit


Enter your choice of tuple operation(0/1/2/3): 3
Tuple has been deleted!

Choose the Tuple operation you want to perform
1 : Add/Insert
2 : Display/View
3 : Delete Tuple
0 : Exit


Enter your choice of tuple operation(0/1/2/3): 2
The tuple does not exist or has been deleted

Choose the Tuple operation you want to perform
1 : Add/Insert
2 : Display/View
3 : Delete Tuple
0 : Exit

Enter your choice of tuple operation(0/1/2/3): 0
The tuple operations will end now! Thank you!

S : Set Operation 
T : Tuple Operations 
E : Exit Program

Enter your choice(S/T/E): e
The program will end now! Thank you!
"""
