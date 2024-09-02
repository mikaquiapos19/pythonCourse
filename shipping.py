# Program Description:  This program determines the cheapest way to ship a package for a shipping company
#                       There are several different options for a customer to ship their package:
#                       1. Ground Shipping = small flat charge + rate based on weight of package
#                       2. Ground Shipping Premium = much higher flat charge but no charge on weight
#                       3. Drone Shipping = no flat charge, but the rate based on weight is three times that of ground shipping
# Author: Mika Quiapos
# Date: 02/09/24

# Initializing variables
weight = float(input("Weight: ")) # "define a weight variable and set it equal to any number" (weight in pounds)
cost = 0
premium_cost = 125 # Flat charge for GSP


# Ground Shipping - "create an if/elif/else statement"
if weight <= 2:
    cost = (weight * 1.50) + 20
    print("GS: Price = $" + f"{cost:.2f}") # using an f string to format the price to always have two decimal points
elif weight <= 6:
    cost = (weight * 3.00) + 20
    print("GS: Price = $" + f"{cost:.2f}")
elif weight <= 10:
    cost = (weight * 4.00) + 20
    print("GS: Price = $" + f"{cost:.2f}")
else:
    cost = (weight * 4.75) + 20
    print("GS: Price = $" + f"{cost:.2f}")


# Ground Shipping Premium
print("GSP: Price = $" + f"{premium_cost:.2f}")


# Drone Shipping
if weight <= 2:
    cost = weight * 4.50
    print("DS: Price = $" + f"{cost:.2f}")
elif weight <= 6:
    cost = weight * 9.00
    print("DS: Price = $" + f"{cost:.2f}")
elif weight <= 10:
    cost = weight * 12.00
    print("DS: Price = $" + f"{cost:.2f}")
else:
    cost = weight * 14.25
    print("DS: Price = $" + f"{cost:.2f}")