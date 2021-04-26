"""Give a three digit number and find the sum of those digits"""

n = int(input("Enter any three digit number: "))

add = sum(int(digits) for digits in str(n))

print(add)
