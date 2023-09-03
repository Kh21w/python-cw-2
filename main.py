

#Part 1


My_name = input ("My name: ")
My_age = input ("My age: ")

print (f"My name Is {My_name}. I'm {My_age} years old.")


#Part 2


First_Number = int (input ("Enter The 1st number: "))
Second_Number = int (input ("Enter The 2nd number: "))
operation =  input ("Enter your operation type: ")

if operation == "+":
    print (First_Number + Second_Number)
elif operation == "-":
    print (First_Number - Second_Number)
elif operation == "*":
    print (First_Number * Second_Number)
elif operation == "/":
    print (First_Number / Second_Number)
else:
    print ("ERROR 404 (The operation is not valid)")


#Part 3


Bus_caacity = 30
Passengers = int (input ("People inside the bus: "))
People = int (input ("People outside the bus: "))

Empty_seats = Bus_caacity - Passengers

if Empty_seats >= People:
    print ("There's room inside. Welcome!")
else:
    print ("There's no room inside. Sorry.")

#room == مساحة