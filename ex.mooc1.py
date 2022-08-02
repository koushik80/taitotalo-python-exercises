#Problem:

#In this exercise you will write a program for printing out grade statistics for a university course.
#The program asks the user for results from different students on the course.
#These include exam points and numbers of exercises completed. The program then prints out statistics based on the results.
#Exam points are integers between 0 and 20.
#The number of exercises completed is an integer between 0 and 100.
#The program kees asking for input until the user types in an empty line.
#You may assume all lines contain valid input, which means that there are two integers on each line, or the line is empty.
#And example of how the data is typed in:

                #Exam points and exercises completed: 15 87
                #Exam points and exercises completed: 10 55
                #Exam points and exercises completed: 11 40
                #Exam points and exercises completed: 4 17
                #Exam points and exercises completed:
                #Statistics:

#Solution:


points = []
grades = [0] * 6

def exam_and_exercise_completed(input):
    space = inpt.find(" ")
    exam = int(input[:space])
    exercise = int(input[space+1:])
    return [exam, exercise]

def exercise_points(amount):
    return amount // 10

def grade(points):
    raja_arvo = [0, 15, 18, 24, 28 ]
    for i in range(5, -1, -1):
        if points >= raja_arvo[i]:
            return i

while True:
    inpt = input("Exam points and exercises completed: ")
    if len(inpt) == 0:
        break
    exam_exercises = exam_and_exercise_completed(input)
    print(exam_exercises)
