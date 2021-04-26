# Print weather the YEAR is LEAP YEAR or A COMMON YEAR.

year = int(input("Enter the number of days in the year: "))

if year % 4 == 0:
    print("It is a Leap Year")

else:
    print("It is a Common Year.")
