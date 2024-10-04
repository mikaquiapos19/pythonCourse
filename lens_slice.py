# Program Description:  This program organises sales data for a pizza joint called "Len's Slice".
#                       This program is for practicing lists
# Author: Mika Quiapos
# Date: 04/10/24

# Keeping track of the toppings available using a list
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

# Creating a list called prices to keep track of how much each kind of pizza slice costs
prices = [2, 6, 1, 3, 2, 7, 2]

# Our boss wants us to do some research on $2 slices
# Keeping track of the number of $2 slices
num_two_dollar_slices = prices.count(2)
print("Number of two dollar slices:", num_two_dollar_slices)

# Finding the amount of toppings we have for pizzas
num_pizzas = len(toppings)

# Displaying the amount of different types of pizza we sell
print("We sell", num_pizzas, "different kinds of pizza!")

# Storing and displaying pizza and slices in a single two-dimensional list
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]
print(pizza_and_prices)

# Sorting pizza and prices list into order of increasing price
pizza_and_prices.sort()
print("Ascending order (price):", pizza_and_prices)

# Storing and displaying the cheapest pizza
cheapest_pizza = pizza_and_prices[0]
print("Cheapest pizza:", cheapest_pizza)

# Storing and displaying the most expensive pizza
priciest_pizza = pizza_and_prices[-1]
print("Priciest pizza:", priciest_pizza)

# A person bought the last anchovies slice. Time to remove it from the list!
pizza_and_prices.pop()
print(pizza_and_prices)

# Time to add a new topping called "peppers" that costs $2.5, keeping the ascending order of prices
pizza_and_prices.insert(4, [2.5, "peppers"])
print("Updated toppings:", pizza_and_prices)

# Apparently three mice walk into the store, are broke, and are requesting for the three lowest cost pizzas!
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)