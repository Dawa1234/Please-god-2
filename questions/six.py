"""Input the weight of the a person in either kg or lbs. If the person provides his/her.
Convert kg into lbs and lbs into kg"""

weight = float(input("Enter your weight: "))

kg_Or_lbs = input("Enter kg or lbs: ")

if kg_Or_lbs == "KG" or kg_Or_lbs == "kg":
    weight_in_lbs = weight * 2.20462
    print("Your weight into lbs is %s" % weight_in_lbs)


elif kg_Or_lbs == "lbs" or kg_Or_lbs == "LBS":
    weight_in_kg = weight / 2.20462
    print("Your wight into kg is {}".format(weight_in_kg))

else:
    print("Your weight is not identified !!")
