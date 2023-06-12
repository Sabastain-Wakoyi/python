
import random

# function to generate question
def generateQuestion():
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    operator = random.choice(['+', '-'])

    if operator == '+':
        question = f"What is {num1} + {num2}?"
        answer = num1 + num2
        points = 5
    else:
        question = f"What is {num1} - {num2}?"
        answer = num1 - num2
        points = 10

    return question, answer, points


# letter to grade function
def numberGradeToLetterGrade(grade):
    if grade >= 90:
        return 'A'
    elif grade >= 80:
        return 'B'
    elif grade >= 70:
        return 'C'
    elif grade >= 60:
        return 'D'
    else:
        return 'E'


# calculation function
def deoAiCal():
    correct_count = 0
    total_points = 0
    questions = []

    for _ in range(5):
        question, answer, points = generateQuestion()
        questions.append((question, answer, points))
        print(question, end=" ")
        user_answer = int(input())
        if user_answer == answer:
            print("Great Answer")
            correct_count += 1
            total_points += points
            result = "Correct"
        else:
            print("Poor  answer")
            result = "Incorrect"
        questions[-1] += (result,)

    grade = total_points / 25 * 100
    letter_grade = numberGradeToLetterGrade(grade)

    print("\nNumber of correct questions: ", correct_count)
    print("Grade:", letter_grade)
    print("All Questions")

    for question, answer, points, result in questions:
        print(question, result)


deoAiCal()
