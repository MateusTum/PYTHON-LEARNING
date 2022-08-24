#logical operator (and, or, not) = used to check if two or more condiitonal statements are true
#not can check one or more insted of two or more conditional statements

temp = int(input("What is the temperature outside?: "))

if temp >= 0 and temp <= 30:
    print("the temperature is good today")
    print("go outside!")
elif temp < 0 or temp >30:
    print("the temperature is bad today!")
    print("stay inside!")

#it will invert the values in this example >>

if not(temp >= 0 and temp <= 30):
    print("the temperature is good today")
    print("go outside!")
elif not(temp < 0 or temp >30):
    print("the temperature is bad today!")
    print("stay inside!")