# WAP to sum of three given integers. However , if two values are equal sum will be zero.

num = int(input("Enter three or more than three digit no. :"))
add = 0
a = 0
while num > 0:
    rem = num % 10
    if a == rem:
        print("The sum is 0")
        break
    else:
        add += rem
        print(add)
    a = rem
    num = num // 10

