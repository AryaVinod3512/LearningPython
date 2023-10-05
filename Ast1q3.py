#Program 3 - The smart working of a computerised bus fare generator

total_fare = passenger_count = bus_fare =  0

passenger = input("Is the last passenger in?(Yes/No): ")                                #Question for the conductor

while passenger == "No":                                                                #Question for the passenger

    distance = float(input("Enter the distance you intend to travel (in km): "))

    if distance <= 10 and distance > 0:                                                                  #for distance between 1 and 10 both included
        bus_fare = 50
        print("Yor bus fare for the journey is Rs.50")
        

    elif distance <= 25 and distance > 0:
        bus_fare = 50 + ((distance - 10)*4.5)                                           #for distance between 11 and 25 both included
        print("Yor bus fare for the journey is Rs.",bus_fare)
        

    elif distance > 25 and distance > 0:
        bus_fare = 117.5 + ((distance-25)*4)                                            #117.5 = (15*4.5) + 50 = 67.5 + 50 ; for distance between 26 and +ve infinity both included
        print("Yor bus fare for the journey is Rs.",bus_fare)

    
    print("Thank you for riding on Greyhound Lines!Have a great day!")
    passenger = input("\nWas that the last passenger?(Yes/No): ")                       #Question for the conductor

    total_fare += bus_fare
    passenger_count += 1

print("\nThe total number of passengers that travelled today is ",passenger_count)
print("The total fare earned today is ",total_fare)


'''OUTPUT:
Is the last passenger in?(Yes/No): No
Enter the distance you intend to travel (in km): 4
Yor bus fare for the journey is Rs.50
Thank you for riding on Greyhound Lines!Have a great day!

Was that the last passenger?(Yes/No): No
Enter the distance you intend to travel (in km): 12
Yor bus fare for the journey is Rs. 59.0
Thank you for riding on Greyhound Lines!Have a great day!

Was that the last passenger?(Yes/No): No
Enter the distance you intend to travel (in km): 45
Yor bus fare for the journey is Rs. 197.5
Thank you for riding on Greyhound Lines!Have a great day!

Was that the last passenger?(Yes/No): Yes

The total number of passengers that travelled today is  3
The total fare earned today is  306.5 '''
