#Take two lists, say for example these two:

#  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#and write a program that returns a list that contains only the elements that are common between the lists(without duplicates).
#Make sure your program works on two lists of different sizes.

#Extras:

#Randomly generate two lists to test this
#Write this in one line of Python(don’t worry if you can’t figure this out at this point - we’ll get to it soon)

#Solution:
import random

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

#main soln:
# print(list(set(a).intersection(b)))

#Extra1 soln:
#V1
#def get_list(max_length):
#    length = random.randint(1, max_length)
#    temp = []
#    for elem in range(length):
#        temp.append(random.randint(0, 100))


# V2
# def get_list(max_length):
#     temp = []
#     for _ in range(random.randint(1, max_length)):
#         temp.append(random.randint(0, 100))
#     return temp

#V3
def get_list(max_length):
    return [random.randint(0, 100) for _ in range(random.randint(1, max_length))]

a = get_list(20)
b = get_list(20)

print(f'list a={a}')
print(f'list b={b}')

print(f'Common elements = {list(set(a).intersection(b))}')

#Extra2 soln:

