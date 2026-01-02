import random
import python_questions
import C_questions
import java_questions
import javascript_questions


print("How do you want to be quizzed? Write the number of your choice.")
print("1. Only Python")
print("2. Only Java")
print("3. Only C")
print("4. Only JavaScript")
print("5. All Languages")
quiz_choice = input()

if int(quiz_choice) == 1:
    questions = python_questions.send_questions()
    random.shuffle(questions)
    for question in questions:
        question()

if int(quiz_choice) == 2:
    questions = java_questions.send_questions()
    random.shuffle(questions)
    for question in questions:
        question()


if int(quiz_choice) == 3:
    questions = C_questions.send_questions()
    random.shuffle(questions)
    for question in questions:
        question()


if int(quiz_choice) == 4:
    questions = javascript_questions.send_questions()
    random.shuffle(questions)
    for question in questions:
        question()

if int(quiz_choice) == 5:
    questions = python_questions.send_questions() + javascript_questions.send_questions() + C_questions.send_questions() + java_questions.send_questions()
    random.shuffle(questions)
    for question in questions:
        question()

