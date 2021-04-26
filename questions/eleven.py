def addition(num):
    add = 0

    while num > 0:
        rem = num % 10
        add = add + rem
        num = num // 10
    return add


add = addition(int(input("Enter any number: ")))
print(add)
