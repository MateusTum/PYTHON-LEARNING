#==========================VARIABLES===============================

#======================STRINGS A SERIES OF CARC=================

#firt_name = "Bro"
#second_name =
#last_name =
#nickname = 
#fullname = first_name+" "+second_name+" "+last_name
#print(type(name))
#print("Hello"+name)

#=========================INTS==================================

#age = 21
#BIRTHDAY EXAMPLE
#age += 1
#print(age)
#print(type(age))
#print ("Your age is: "+str(age))  #if you need to display a string with a data you have to type the +str(age) thing


#=======================FLOAT DATA TYPE================

#height = 250.5 
#print("Your height is: "+str(height)+"cm")
#print(type(height))

#====================BOOLEAN DATA TYPE ONLY STORE TRUE OR FALSE===============
#good use to see if something is true

#human = False
#print("Are you a human: "+str(human))
#print(type(human))


#MULTIPLE ASSIGNMENT = ALLOWS US TO ASSIGN MULTIPLE VARIABLES AT THE SAME TIME IN ONE LINE OF CODE

#name = "Matt"
#age = 22
#attractive = True

#name, age, attractive = "Matt", 21, True

#print(name), print(age), print(attractive)

#============== STRING METHODS ====================

#name = "bro code"

#print(len(name))
#print(name.find("B"))
#print(name.capitalize())
#print(name.upper())
#print(name.lower())
#print(name.isdigit())
#print(name.isalpha())   #CHECK TO SEE IF STRING CONTAINS ONLY ALPHABETIC LETTERS
#print(name.count("o"))
#print(name.replace("o" , "a"))
#print(name*3)

#=============TYPE CASTING = CONVERT THE DATA TYPE OF A VALUE TO ANOTHER DATA TYPE

#x = 1         #int
#y = 2.0       #float
#z = "3"       #str

#print(x)
#print(int(y))   #display Y as an integer
#print(z)

#print(int(z)+x+int(+12))


#z = int(z)   #makes the x an integer

#HERE WE START THE USER INTERFACE /// THE LOGIN AREA OF THE PROGRAM

def loginarea():
    print("Choose an username for your character")
    username = input("What is your username?")

    print("Choose a password for your character")
    password = input("What is your password?")

    print("Please, repeat your password to confirm:")
    password2 = input("Password:")

    if password == password2:
        print("Success")

    if not password == password2:
        print("Wrong password, returning to login")
        return loginarea()

loginarea()





print("Now you have to choose a vocation")
print("The vocations available are")

#THIS PART I COPIED FROM SOMEWHERE ELSE IN THE INTERNET

#Import the required library
from tkinter import*

#Create an instance of tkinter frame
win= Tk()

#Define geometry of the window
win.geometry("750x250")

#Define a function to close the popup window
def close_win(top):
   top.destroy()
def insert_val(e):
   e.insert(0, "Hello World!")

#Define a function to open the Popup Dialogue

def popupwin():
   #Create a Toplevel window
   top= Toplevel(win)
   top.geometry("750x250")

   #Create an Entry Widget in the Toplevel window
   entry= Entry(top, width= 25)
   entry.pack()

   #Create a Button to print something in the Entry widget
   Button(top,text= "Insert", command= lambda:insert_val(entry)).pack(pady= 5,side=TOP)
   #Create a Button Widget in the Toplevel Window
   button= Button(top, text="Ok", command=lambda:close_win(top))
   button.pack(pady=5, side= TOP)
#Create a Label
label= Label(win, text="Hello! Click the Button to Open the Popup Dialogue", font= ('Helvetica 15 bold'))
label.pack(pady=20)

#Create a Button
button= Button(win, text= "Click Me!", command= popupwin, font= ('Helvetica 14 bold'))
button.pack(pady=20)
win.mainloop()



#x = float(x)   #makes the z a float 

#if you need to print a variable along a string





