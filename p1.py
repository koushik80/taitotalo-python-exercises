#Exercise:

#Exercise 1 (and Solution)
#Create a program that asks the user to enter their name and their age.
#Print out a message addressed to them that tells them the year that they will turn 100 years old.
#Note: for this exercise, the expectation is that you explicitly write out the year (and therefore be out of date the next year). 
#If you want to do this in a generic way, see exercise 39.

#Extras:

#1. Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. 
#(Hint: order of operations exists in Python)
#2. Print out that many copies of the previous message on separate lines. 
#(Hint: the string "\n is the same as pressing the ENTER button) 

#Solution:

import datetime

name = input("What\'s your name: ")
age = int(input("How old are you: "))
#today = datetime.date.today()
current_year = datetime.date.today().year
#year = current_year + (100 - age)
year = datetime.date.today().year + (100 - age)

#year = 2022 - age + 100
if age <= 0 or age > 130:
   print('It\'s impossible')
elif year > current_year:
   print(name + ", you will be 100 years old in the year" + str(year))
elif year == current_year:
   print(name + ", you will be 100 years old" + str(year))
else:
   print(name + ", you will be over 100 years old" + str(year))


#if name == str("Tero"):
   #print("King of no island")
#else:
   #print("You can choose to go to the hell!")
