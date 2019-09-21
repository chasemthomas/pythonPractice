# Exercise 1
# Character Input
# https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

import datetime

# Current datetime
now = datetime.datetime.now()
thisYear = now.year


'''
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
'''

# Get the user's name and save to a variable
name = str(input("\nName: "))

# Get the user's age and save to a variable
age = int(input("Age: "))

# Calculate how long until they are 100 years old

# 100 - age = years until they are 100
yearsUntil = 100 - age

# yearsUntil + current year = 100Year
targetYear = thisYear + yearsUntil

string = f"{name}, you will be 100 years old in {targetYear}."

print(string)

'''
Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
'''
repeatNum = int(input("\nFavorite number: "))

print(repeatNum * string)

print("")

'''
Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
'''
print((string + "\n") * repeatNum)
