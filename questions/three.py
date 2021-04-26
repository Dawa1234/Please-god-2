"""If the tempreture is greater than 30,it's a hot otherwise if it's less than 10 then cold day,
otherwise it is neither hot nor cold."""

temperature = int(input("Enter the temperature: "))

if temperature >= 30:
    print("It is a hot day")
elif temperature <= 10:
    print("It is a cold day")
else:
    print("It is neither cold nor hot day")
