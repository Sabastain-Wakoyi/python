import random

def generateQuestion():
    num1 = random.randint(1, 15)
    num2 = random.randint(1, 15)
    operator = random.choice(['+', '-'])

    if operator == '+':
        answer = num1 + num2
    else:
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


def runAiQuiz():
    total_questions = 5
    score = 0
    question_list = []

    print("Welcome to AI By Dr Tony")

    for i in range(total_questions):
        question, answer = generateQuestion()
        user_answer = int(input(question))

        if user_answer == answer:
            print("Good job")
            if '+' in question:
                score += 5
            else:
                score += 10
            question_list.append(f"{question}\tCorrect")
        else:
            print("Wrong Answer")
            question_list.append(f"{question}\tIncorrect")

    percentage_correct = (score / total_questions) * 100
    grade = numberGradeToLetterGrade(percentage_correct)

    print("\nNumber of correct questions:", score)
    print("Grade:", grade)

    print("\nAll Questions")
    for question in question_list:
        print(question)


runAiQuiz()






