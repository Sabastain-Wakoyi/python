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
#
#
#
#
#
#



import random

# function to generate question
def generateQuestion():
    num1 = random.randint(0, 10)  # Generate a random integer between 0 and 10 (inclusive) for num1
    num2 = random.randint(0, 10)  # Generate a random integer between 0 and 10 (inclusive) for num2
    operator = random.choice(['+', '-'])  # Randomly choose either '+' or '-' for the operator

    if operator == '+':
        question = f"What is {num1} + {num2}?"  # Create a question string for addition
        answer = num1 + num2  # Calculate the answer for addition
        points = 5  # Assign 5 points for a correct answer to an addition question
    else:
        question = f"What is {num1} - {num2}?"  # Create a question string for subtraction
        answer = num1 - num2  # Calculate the answer for subtraction
        points = 10  # Assign 10 points for a correct answer to a subtraction question

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
    correct_count = 0  # Variable to track the number of correct answers
    total_points = 0  # Variable to track the total points earned
    questions = []  # List to store the questions, answers, points, and results

    for _ in range(5):
        question, answer, points = generateQuestion()  # Generate a question, answer, and points using the generateQuestion function
        questions.append((question, answer, points))  # Add the question, answer, and points to the list of questions
        print(question, end=" ")  # Print the question
        user_answer = int(input())  # Get the user's answer from the input
        if user_answer == answer:
            print("Great Answer")  # Print a message for a correct answer
            correct_count += 1  # Increment the correct_count variable
            total_points += points  # Add the points to the total_points variable
            result = "Correct"  # Set the result as "Correct" for this question
        else:
            print("Poor answer")  # Print a message for an incorrect answer
            result = "Incorrect"  # Set the result as "Incorrect" for this question
        questions[-1] += (result,)  # Add the result to the last question in the list

    grade = total_points / 25 * 100  # Calculate the grade as a percentage
    letter_grade = numberGradeToLetterGrade(grade)  # Convert the grade to a letter grade

    print("\nNumber of correct questions:", correct_count)
    print("Grade:", letter_grade)
    print("All Questions")

    for question, answer, points, result in questions:
        print(question, result)  # Print each question and its result


deoAiCal()  # Call the deoAiCal function to start the calculation
