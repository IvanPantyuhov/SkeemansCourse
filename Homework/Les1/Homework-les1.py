# Task1 - vers1
a, b = 1, 2
print(a, b)
a, b = b, a
print(a, b)

# Task1 - vers2
a = int(input("Write the number"))
b = int(input("Write the second number"))
print(a, b)
a, b = b, a
print(a, b)

# Task2
#       0123456789
title = str(input("Creat your secret code"))
print(title[::-1])

# Task 3
word = "Python is great"

num = int(input("Enter a number"))
if (num % 2) == 0:
    print(word[::-1])
else:
    print(word.upper())

# Task 4
# Test 1.0
point = 0
print("Welcome to Quiz")
print("Test 1 - collect the word")
#         012345678
question = "education"
print(question[3])
print(question[0])
print(question[6])
print(question[5])
print(question[7])
print(question[1])
print(question[8])
print(question[2])
print(question[4])

answer = str(input("Write you answer"))
if answer == "education":
    print("Great, go to next")
    point = point + 1
else:
    print("Try again")

# Test 2
print("Test 2 - task")
print("x ^ 2 = 16")
x = int(input())
if x == 4 or -4:
    print("Great, go to next")
    point = point + 1
if x == "-4":
    print("Great, go to next")
    point = point + 1
else:
    print("Try again")

# Test 3
print("Test 3 - task")
print("87 / 12 = y")
y = float(input())
if y == 7.25:
    print("You are best")
    point = point + 1
else:
    print("Try again")

#Result
print(f'Correct answers = {point}')
wrong_answers = 3 - point
print(f'Wrong answers = {wrong_answers}')

