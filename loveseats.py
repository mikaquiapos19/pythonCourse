# Program Description: This program creates receipts for customers buying loveseats, settees, and lamps
# Author: Mika Quiapos
# Date: 30/08/24


# initialising variables
lovely_loveseat_description = """
Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white. """
lovely_loveseat_price = 254.00

stylish_settee_description = """
Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black. """
stylish_settee_price = 180.50

luxurious_lamp_description = """
Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade. """
luxurious_lamp_price = 52.15

sales_tax = 0.088

# < Our First Customer - Variables >
customer_one_total = 0 # Running tally of customer's expenses
customer_one_itemization = "" # list of descriptions of purchases
customer_one_tax = 0


# Customer purchased Lovely Loveseat
customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description 

# Customer purchased Luxurious Lamp
customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description


# Calculating sales tax to add to total cost
customer_one_tax = customer_one_total * sales_tax 
customer_one_total += customer_one_tax


# Printing receipt
print("Customer One Items:")
print(customer_one_itemization)

print("\nCustomer One Total:")
customer_one_total = format(customer_one_total, ".2f")
print(customer_one_total)
