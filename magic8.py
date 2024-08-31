# Program Description:  This program simulates a Magic 8-Ball. It can answer "Yes" or "No" with a different fortune each time it executes.
#                       This program is for practising if-elif-else statements
# Author: Mika Quiapos
# Date: 31/08/24

# Imported modules
import random 

# Initialising Variables
name = input('What is your name?: ')
question = input('Ask me a "Yes" or "No" question: ')
answer = ""
random_number = random.randint(1, 10) #generates random int between 1 and 10 inclusive
# print(random_number)


# List of 8-Ball answers
if random_number == 1:
    answer = "Yes - definitely"
elif random_number == 2:
    answer = "It is decidedly so"
elif random_number == 3:
    answer = "Without a doubt"
elif random_number == 4:
    answer = "Reply hazy, try again"
elif random_number == 5:
    answer = "Ask again later"
elif random_number == 6:
    answer = "Better not tell you now"
elif random_number == 7:
    answer = "My sources say no"
elif random_number == 8:
    answer = "Outlook not so good"
elif random_number == 9:
    answer = "Very doubtful"
elif random_number == 10:
    answer = "The outcome is what you believe"
else:
    answer = "Error" # If number outside of 1-10 accidentally gets assigned


# Outputs result to user
if question == "": # if the user does not ask a question
    print("You did not provide a question! I simply cannot answer an unasked question")
elif name == "": # if name is left blank, only print question
    print("Question: " + question)
    print("\nMagic 8-Ball's answer: " + answer)
else: # if name is filled in, print both name and question
    print(name + " asks: " + question)
    print("\nMagic 8-Ball's answer: " + answer)


