from tkinter import *
from tkinter import ttk

root = Tk()

#Creating grid to space widgets
root.geometry("500x500+600+200")

#Create a title label
input1 = Label(root, text = "Name of User")
input1.pack(padx = 10, pady = 10)

#Create title entry box
inputbox1 = Entry(root, width = 25)
inputbox1.pack(padx = 10, pady = 10)

#Create a text label
input2 = Label(root, text = "Enter content to hold in text file")
input2.pack(padx = 10, pady = 10)

#Create text entry box
inputbox2 = Text(root, width = 40, height = 5, border = 15, relief = RAISED)
inputbox2.pack(padx = 10, pady = 10)

#Create save function to save entered data into text file
def save():
    file_title = inputbox1.get()
    file_contents = inputbox2.get(0.0, END)
    with open(file_title + ".txt", "w") as file:
        file.write(file_contents)
        output1 = Label(root, text = "Text file successfully created!", font = ("Calibri",10))
        output1.pack(padx = 10, pady = 10)
        file.close()

#Create Save button to call the Save function from user-end
button1 = Button(root, text = "Save", command = save, font = ("Calibri",10))
button1.pack(padx = 10, pady = 10)

#Create function to read content of text file
def Read_file():
    file_title = inputbox1.get()
    file_contents = inputbox2.get(0.0, END)
    with open(file_title + ".txt", "w+") as file:
        file.write(file_contents)
        output2 = Label(root, text = "The content of " + file_title + ".txt is: " + file_contents, font = ("Calibri",10))
        output2.pack(padx = 10, pady = 10)
        file.close()

#Create Read button to view the content of the text file
button2 = Button(root, text = "Read Text File", command = Read_file, font = ("Calibri",10))
button2.pack(padx = 10, pady = 10)

#Create function to capitalize the first letter of every word and print the word
def Caps_file():
    file_title = inputbox1.get()
    file_contents = inputbox2.get(0.0, END)
    
    with open(file_title + ".txt", "w+") as file:
        file.write(file_contents)
        file.close()
        
    with open(file_title + ".txt", "r") as file:
        para = file.read()
        
        list1 = para.split()
        new_string = ""
        for i in list1:
            new_string = new_string + (i.capitalize()) + " "
            
        output3 = Label(root, text = "The content of " + file_title + ".txt with the first letter of every word capitalized is: \n" + new_string, font = ("Calibri",10))
        output3.pack(padx = 10, pady = 10)
        file.close()

#Create Capitalize button to capitalize the first letter of every word from user-end
button3 = Button(root, text = "Capitalize the first letter of every word of the Text File", command = Caps_file, font = ("Calibri",10))
button3.pack(padx = 10, pady = 10)

#Create function to reverse the content of the text file
def Reverse_file():
    file_title = inputbox1.get()
    file_contents = inputbox2.get(0.0, END)
    
    with open(file_title + ".txt", "w+") as file:
        file.write(file_contents)
        file.close()
        
    with open(file_title + ".txt", "r") as file:
        para = file.read()

        new_string = ""
        for i in range(-1,-(len(para))-1,-1):
            new_string += para[i]
            
        output4 = Label(root, text = "The content of " + file_title + ".txt reversed is: \n" + new_string, font = ("Calibri",10))
        output4.pack(padx = 10, pady = 10)
        file.close()

#Create Reverse button to reverse the content of the text file from user-end
button4 = Button(root, text = "Reverse text of the Text File", command = Reverse_file, font = ("Calibri",10))
button4.pack(padx = 10, pady = 10)

#Function to clear the previous input as well as the previous output
def Clear():
    inputbox1.delete("0", END)
    inputbox2.delete("0.0", END)


#Create a Clear button to clear the previous input as well as the previous output
button5 = Button(root, text = "Clear", font = ("Calibri",10), command = Clear)
button5.pack(padx = 10, pady = 10)

#Function to close the window and terminate the program from user-end
def Close():
    end_label = Label(root, text = "This window will close now! Thank you!", font = ("Calibri",10))
    end_label.pack(padx = 10, pady = 10)
    root.after(2000,lambda:root.destroy())

#Create the Exit Window button to terminate the program rather than operating the Close Button
button6 = Button(root, text = "Exit Program", font = ("Calibri",10), command = Close)
button6.pack(padx = 10, pady = 10)

root.mainloop()
