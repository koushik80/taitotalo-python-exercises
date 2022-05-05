#The exercise comes first(with a few extras if you want the extra challenge or want to spend more time), 
#followed by a discussion. Enjoy!

#Ask the user for a number.
#Depending on whether the number is even or odd,
#print out an appropriate message to the user.
#Hint: how does an even / odd number react differently when divided by 2?

#Extras:

#If the number is a multiple of 4, print out a different message.
#Ask the user for two numbers:
#one number to check(call it num) and one number to divide by(check). 
#If check divides evenly into num, tell that to the user.
#If not, print a different appropriate message.


while True:
    try:
        number = int(input('Please, write a number (-1 to exit): '))
    except:
        print('Error: That is not a valid number!')
        continue
    if number == -1:
        break

    if number % 4 == 0:
        print('Number is multiple of 4')
    elif number % 2 == 0:
        print('Number is even')
    else:
        print('Number is odd')
print('Thanks!')
