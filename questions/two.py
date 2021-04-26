# WAP which accepts mark of four subject and display the total mark ,percentage and grade.

physics = float(input("Enter the marks of physics here--> "))
chemistry = float(input("Enter the marks of chemistry here--> "))
math = float(input("Enter the marks of math here--> "))
english = float(input("Enter the marks of english here--> "))

total_marks = physics + chemistry + math + english

percentage = (total_marks / 400) * 100

print(f"{percentage} %")

grade = percentage / 25

if percentage >= 70:
    print("Distinction")

elif percentage <= 70 and percentage >= 60:
    print("First division")

elif percentage <= 60 and percentage >= 50:
    print("Second division")

elif percentage <= 40:
    print("Failed")
