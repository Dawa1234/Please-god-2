"""Given a positive real no. print its fractional part."""

realNumber = int(input("Enter any positive real number: "))

division = int(input("Enter the division no.:  "))

divide = realNumber / division

divided = realNumber // division

fracitional_part = divide - divided

print(f"The fratcional part of the real number is {fracitional_part}")
