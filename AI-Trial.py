# import random
#
#
# def generateQuestion():
#     num1 = random.randint(1, 20)
#     num2 = random.randint(1, 20)
#     operator = random.choice(['+', '-'])
#
#     if operator == '+':
#         answer = num1 + num2
#     else:
#         # Ensure that the result is a positive number
#         num1, num2 = max(num1, num2), min(num1, num2)
#         answer = num1 - num2
#
#     question = f"What is {num1} {operator} {num2}? "
#
#     return question, answer
#
#
# def numberGradeToLetterGrade(grade):
#     if grade >= 90:
#         return 'A'
#     elif grade >= 80:
#         return 'B'
#     elif grade >= 70:
#         return 'C'
#     elif grade >= 60:
#         return 'D'
#     else:
#         return 'E'
#
#
# def runMathQuiz():
#     score = 0
#
#     print("Welcome to the Math Quiz!")
#
#     for i in range(5):
#         question, answer = generateQuestion()
#         user_answer = int(input(question))
#
#         if user_answer == answer:
#             print("Correct!")
#             if '+' in question:
#                 score += 5
#             else:
#                 score += 10
#         else:
#             print(f"Incorrect! The correct answer is {answer}.")
#
#     grade = numberGradeToLetterGrade((score / 50) * 100)
#
#     print(f"\nNumber of correct answers: {score // 5}")
#     print(f"Letter grade: {grade}")
#
#
# runMathQuiz()





import random

#function to generate random questions
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


#grades conversion function
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
    score = 0
    question_list = []

    print("Welcome to AI By Dr Tony")

    for i in range(5):
        question, answer = generateQuestion()
        user_answer = int(input(question))

        if user_answer == answer:
            print("Good job")
            if '+' in question:
                score += 5
            else:
                score += 10
            question_list.append(f"{question}   Correct")
        else:
            print("Wrong Answer")
            question_list.append(f"{question}   Incorrect")

    grade = numberGradeToLetterGrade(score)

    print("\nNumber of correct questions:", score)
    print("Grade:", grade)

    print("\nAll Questions")
    for question in question_list:
        print(question)


runAiQuiz()









# import random
#
#
# def generateQuestion():
#     num1 = random.randint(1, 20)
#     num2 = random.randint(1, 20)
#     operator = random.choice(['+', '-'])
#
#     if operator == '+':
#         answer = num1 + num2
#     else:
#         # Ensure that the result is a positive number
#         num1, num2 = max(num1, num2), min(num1, num2)
#         answer = num1 - num2
#
#     question = f"What is {num1} {operator} {num2}? "
#
#     return question, answer
#
#
# def numberGradeToLetterGrade(grade):
#     if grade >= 90:
#         return 'A'
#     elif grade >= 80:
#         return 'B'
#     elif grade >= 70:
#         return 'C'
#     elif grade >= 60:
#         return 'D'
#     else:
#         return 'E'
#
#
# def runMathQuiz():
#     score = 0
#     question_list = []
#     correct_list = []
#
#     print("Welcome to the Math Quiz!")
#
#     for i in range(5):
#         question, answer = generateQuestion()
#         user_answer = int(input(question))
#
#         if user_answer == answer:
#             print("Good job")
#             if '+' in question:
#                 score += 5
#             else:
#                 score += 10
#             correct_list.append("Correct")
#         else:
#             print("Wrong Answer")
#             correct_list.append("Incorrect")
#
#         question_list.append(f"{question}          {correct_list[-1]}")
#
#     grade = numberGradeToLetterGrade((score / 50) * 100)
#
#     print("\nNumber of correct questions:", score // 5)
#     print("Grade:", grade)
#
#     print("\nAll Questions")
#     for i in range(5):
#         print(question_list[i])
#
#
# runMathQuiz()
