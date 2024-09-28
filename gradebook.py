# Program Description:  This program creates a gradebook for students to organise subjects and grades
#                       This program is for practising lists
# Author: Mika Quiapos
# Date: September 28/09/24

# Recording data from last semester's gradebook
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Creating a list of the current semester's subjects
subjects = ["physics", "calculus", "poetry", "history"]

# Creating a list called grades and filling it with current scores
grades = [98, 97, 85, 88]

# Manually (without any methods) creating a 2-D list to combine subjects and grades
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

# Displaying the gradebook in its current state
print(gradebook)

# Adding grade for computer science class with a perfect score of 100
gradebook.append(["computer science", 100])
# print(gradebook)

# Adding grade for visual arts with a score of 93
gradebook.append(["visual arts", 93])
# print(gradebook)

# Modifying the gradebook - rewarding an extra 5 points for visual arts
gradebook[5][1] = 98

# Student decides to switch from a numerical grade value to a Pass/Fail option in poetry class
# Removing the grade value in gradebook for poetry
gradebook[2].remove(85)
# print(gradebook)

# Adding "Pass" value for poetry
gradebook[2].append("Pass")
# print(gradebook)

# Storing last semester and current semester gradebook into one full gradebook
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)