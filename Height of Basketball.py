#Program to find height attained by basketball thrown by basketball player
print("This is a program to find the height attained by basketball thrown by basketball player")

#declare value of acceleration due to gravity in feet/second
a = -32

#read velocity from user
velocity = float(input("Enter the velocity : "))

#read player height from user
height_player = float(input("Enter player height : "))

#calculate time of travel of ball using formula time = velocity/acceleration
time = float(-velocity/a)

#calculate the height attained by ball using formula s = vt + 0.5at^2
height_ball = ((0.5*a)*(time**2)) + (velocity*time)

#add the player height with ball height
height_ball += height_player
print("The total height attained by ball is:",height_ball," feet")

"""OUTPUT:
This is a program to find the height attained by basketball thrown by basketball player
Enter the velocity : 32
Enter player height : 5
The total height attained by ball is: 21.0  feet
"""
