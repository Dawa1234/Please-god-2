''' Price of a house is $1M. If buyer has good credit, they need to put 10$ otherwise they need to put down 20%.
Print the down payment. '''

price_house = float(1000000)

buyer = input("Enter good credit or not:")
if buyer == "Good Credit " or buyer == "good credit" or buyer =="GOOD CREDIT":
    print("Buyers got good credit and is discounted by 10%")
    downpayment = price_house - 0.1 * price_house
    print("Discounted price is %s"%(downpayment))
else:
    print("Buyers doesn't have good credit and so discounted by 20%")
    downpayment = price_house - 0.2 * price_house
    print("Discounted price is %s"%(downpayment))
