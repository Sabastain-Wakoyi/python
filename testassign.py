import random


def generateQuestion():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operator = random.choice(['+', '-'])

    if operator == '+':
        answer = num1 + num2
    else:
        # Ensure that the result is a positive number
        num1, num2 = max(num1, num2), min(num1, num2)
        answer = num1 - num2

    question = f"What is {num1} {operator} {num2}? "

    return question, answer


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


def runMathQuiz():
    score = 0

    print("Welcome to the Math Quiz!")

    for i in range(5):
        question, answer = generateQuestion()
        user_answer = int(input(question))

        if user_answer == answer:
            print("Correct!")
            if '+' in question:
                score += 5
            else:
                score += 10
        else:
            print(f"Incorrect! The correct answer is {answer}.")

    grade = numberGradeToLetterGrade((score / 50) * 100)

    print(f"\nNumber of correct answers: {score // 5}")
    print(f"Letter grade: {grade}")


runMathQuiz()