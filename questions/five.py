'''If name is less than 3 characters name must be at least 3 character otherwise if it is more than 50 cahracters
name must be less than 50 characters so it looks good. '''

name = input("Enter you name: ")

if len(name) < 3:
    print("Your is too short, name must be at least more than 3 characters")
elif len(name) > 50:
    print("Your is too long, name must be less than 50 characters")
else:
    print("Your name looks good.")



