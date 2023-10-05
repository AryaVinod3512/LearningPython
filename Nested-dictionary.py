MegaBasket = {56 : {'Product_desc' : 'Washing Machine' , 'Quantity' : 10 , 'Unit_Price' : 43000}, 32: {'Product_desc' : 'Dish Washer' , 'Quantity' : 20 , 'Unit_Price' : 22500}, 29 : 
              {'Product_desc' : 'Television' , 'Quantity' : 25 , 'Unit_Price' : 23000}, 45 : {'Product_desc' : 'Refrigerator' , 'Quantity' : 12 , 'Unit_Price' : 47500}}

while True:
    print("You have the following options to choose from:")
    print("A : You can see a database with the details of items for sale on Mega Basket! ")
    print("B : You can see a database with items and discounted prices for sale at Mega Basket! ")
    print("C : You can input a new item on sale and see the updated database! ")
    print("D : You can edit the details of an item on sale and see the updated database! ")
    print("E : You can see the details of the lowest-priced product! ")
    print("Exit: You may exit the program!")
    choice = input("\nEnter your choice(A/B/C/D/E/F/Exit): ")
    temp = MegaBasket.copy()
    
#Q1.(A) - Printing the details in a tabular format
    if choice == "a" or choice == "A":

        print()
        print(" "*30, "MEGA BASKET", " "*30)
        print("_"*80)
        print("CODE\t    PRODUCT_NAME\tQUANTITY\tUNIT_PRICE")
        print("_"*80)

        for i in MegaBasket:
            if i == 29:
                print(i,"\t   ", MegaBasket[i]['Product_desc'],"\t\t", MegaBasket[i]['Quantity'],"\t\t", MegaBasket[i]['Unit_Price'])
            else:
                print(i,"\t   ", MegaBasket[i]['Product_desc'],"\t", MegaBasket[i]['Quantity'],"\t\t", MegaBasket[i]['Unit_Price'])
                
        print()
        continue

#Q1.(B) - Compute the total prive of all the products. Display the information in the tabular format along with th total price
    elif choice == "b" or choice == "B":

        Total_Price = 0

        for key in MegaBasket:

            if MegaBasket[key]['Unit_Price'] > 40000:
                new_price = MegaBasket[key]['Unit_Price'] * (5/100)
                total =  MegaBasket[key]['Unit_Price'] - new_price
                Total_Price += (MegaBasket[key]['Quantity']) * total
               
            elif MegaBasket[key]['Unit_Price'] <= 25000:
                new_price = MegaBasket[key]['Unit_Price'] * (3/100)
                total =  MegaBasket[key]['Unit_Price'] - new_price
                Total_Price += (MegaBasket[key]['Quantity']) * total

            MegaBasket[key]['Total_Price'] = Total_Price
            
        print()  
        print(" "*30, "MEGA BASKET", " "*30)
        print("_"*80)
        print("CODE\t    PRODUCT_NAME\tQUANTITY\tUNIT_PRICE\tTOTAL_PRICE")
        print("_"*80)

        for i in MegaBasket:
            if i == 29:
                print(i,"\t   ", MegaBasket[i]['Product_desc'],"\t\t", MegaBasket[i]['Quantity'],"\t\t", MegaBasket[i]['Unit_Price'], "\t\t", MegaBasket[i]['Total_Price'])
            else:
                print(i,"\t   ", MegaBasket[i]['Product_desc'],"\t", MegaBasket[i]['Quantity'],"\t\t", MegaBasket[i]['Unit_Price'], "\t\t", MegaBasket[i]['Total_Price'])
           

        print()
        continue        


#Q1.(C) - Accept the details of a new item and display the updated database
    elif choice == "c" or choice == "C":

        print()
        print(input("Please fill in the details of a new item you would like to add to the database!"))
        new_code = int(input("Enter the code of the new item: "))
        new_item = input("Enter the name of the new item: ")
        new_quantity = int(input("Enter the quantity of the new item: "))
        new_unit_price = int(input("Enter the price of the new item: "))

        MegaBasket[new_code] = temp[new_code] = {'Product_desc' : new_item , 'Quantity' : new_quantity , 'Unit_Price' : new_unit_price}

        print()
        print(" "*30, "MEGA BASKET", " "*30)
        print("_"*80)
        print("CODE\t    PRODUCT_NAME\tQUANTITY\tUNIT_PRICE")
        print("_"*80)

        for i in temp:
            if i == 29:
                print(i,"\t   ", temp[i]['Product_desc'],"\t\t", temp[i]['Quantity'],"\t\t", temp[i]['Unit_Price'])
            else:
                print(i,"\t   ", temp[i]['Product_desc'],"\t", temp[i]['Quantity'],"\t\t", temp[i]['Unit_Price'])

      
        print()
        continue        

#Q1.(D) - To change the quantity of an existing item by accepting the code of that item and display the modified database
    elif choice == "d" or choice == "D":

        code = int(input("Enter the code of an item whose details you want to modify: "))
        while code not in temp.keys():
            print("The code does not exist!")
            code = int(input("Enter the code of an item whose details you wnt to modify: "))
        
        if code in temp.keys():
            quantity2 = int(input("Enter the new quantity of the item: "))
            key = code
            temp[key]['Quantity'] = quantity2

        
        print()
        print(" "*30, "MEGA BASKET", " "*30)
        print("_"*80)
        print("CODE\t    PRODUCT_NAME\tQUANTITY\tUNIT_PRICE")
        print("_"*80)

        for i in temp:
            if i == 29:
                print(i,"\t   ", temp[i]['Product_desc'],"\t\t", temp[i]['Quantity'],"\t\t", temp[i]['Unit_Price'])
            else:
                print(i,"\t   ", temp[i]['Product_desc'],"\t", temp[i]['Quantity'],"\t\t", temp[i]['Unit_Price'])
                
        print()
        continue

#Q1.(E) - To display the details of the product which costs the least
    elif choice == "e" or choice == "E":

        print()
        print("The item that costs the least is - ")
        List1 = []

        for key in temp:
            tester = temp[key]['Unit_Price']
            List1.append(tester)

        min = List1[0]
        for i in List1:
            if i < min:
                min = i

        for i in temp:
            if temp[i]['Unit_Price'] == min:
                print("CODE\t    PRODUCT_NAME\tQUANTITY\tUNIT_PRICE")
                print("_"*80)
                print()
                print(i,"\t   ", temp[i]['Product_desc'],"\t", temp[i]['Quantity'],"\t\t", temp[i]['Unit_Price'])
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

            
