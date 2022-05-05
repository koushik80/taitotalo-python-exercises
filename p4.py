#Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
#(If you don’t know what a divisor is, it is a number that divides evenly into another number.
#For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)


num = int(input("Give a number: "))
candidates = list(range(1, num+1))
for candidate in candidates:
    if num % candidate == 0:
       print(candidate)

#in one line
# print ([candidate for candidates in range(1, num+1) if num % candidate == 0])
