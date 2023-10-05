from tkinter import *

root = Tk()

root.title("Program1 - Python Lab EL")

heading = Label(root, text='''This interface can compute the height of a basketball thrown by basketball player!''', font=("Calibri",18))
heading.pack()

#Take input from the user of the height of the basketball player
input1 = Label(root, text = "Enter the height of the basketball player in feet", font = ("Calibri",14))
input1.pack(padx = 10, pady = 10)

inputbox1 = Entry(root, width=30, font = ("Calibri",14), borderwidth=5)
inputbox1.pack(padx=10, pady=10)


#Take input from the user of the initial velocity of ball
input2 = Label(root, text = "Enter the initial velocity of the ball", font = ("Calibri",14))
input2.pack(padx = 10, pady = 10)

inputbox2 = Entry(root, width = 30, font = ("Calibri",14), borderwidth=5)
inputbox2.pack(padx = 10, pady = 10)

#Function to compute the height of the ball thrown by the basketball player
def Calculate():
    a = -32
    height_player = float(inputbox1.get())
    velocity = float(inputbox2.get())
    time = float(-velocity/a)
    height_ball = ((0.5*a)*(time**2)) + (velocity*time)
    height_ball += height_player
    height_ball = '%0.3f'%(height_ball)
    output = "The total height attained by ball is: " + str(height_ball) + "  feet!"
    view_output = Label(root, text = output, font=("Calibri",14))
    view_output.pack()
    
#Create the Calculate button once the inputs are taken from the user
button1 = Button(root, text = "Calculate", font = ("Calibri",14), command = Calculate)
button1.pack(padx = 10, pady = 10)


#Function to clear the previous input as well as the previous output
def Clear():
    inputbox1.delete("0", END)
    inputbox2.delete("0", END)

#Create a Clear button to clear the previous input as well as the previous output
button2 = Button(root, text = "Clear", font = ("Calibri",14), command = Clear)
button2.pack(padx = 10, pady = 10)


#Function to close the window and terminate the program from user-end
def Close():
    end_label = Label(root, text = "This window will close now! Thank you!", font = ("Calibri",14))
    end_label.pack(padx = 10, pady = 10)
    root.after(2000,lambda:root.destroy())

#Create the Exit Window button to terminate the program rather than operating the Close Button
button3 = Button(root, text = "Exit Program", font = ("Calibri",14), command = Close)
button3.pack(padx = 10, pady = 10)

root.mainloop()
