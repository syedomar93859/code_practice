import random
import python_questions
import C_questions
import java_questions
import javascript_questions


print("How do you want to be quizzed? Write the number of your choice:")
print("1. Only Python")
print("2. Only Java")
print("3. Only C")
print("4. Only JavaScript")
print("5. All Programming Languages")
quiz_choice = input()
print("")

print("How many tries for each question. Enter a number:")
num_of_tries = int(input())
print("")

if int(quiz_choice) == 1:
    questions = python_questions.send_questions()
    random.shuffle(questions)

    for question in questions:
        question(num_of_tries)

    print("\nYou got " + str(python_questions.total_correct()) + "/" + str(len(questions)) + " for this quiz.")

if int(quiz_choice) == 2:
    questions = java_questions.send_questions()
    random.shuffle(questions)

    for question in questions:
        question(num_of_tries)

    print("\nYou got " + str(java_questions.total_correct()) + "/" + str(len(questions)) + " for this quiz.")



if int(quiz_choice) == 3:
    questions = C_questions.send_questions()
    random.shuffle(questions)

    for question in questions:
        question(num_of_tries)

    print("\nYou got " + str(C_questions.total_correct()) + "/" + str(len(questions)) + " for this quiz.")



if int(quiz_choice) == 4:
    questions = javascript_questions.send_questions()
    random.shuffle(questions)

    for question in questions:
        question(num_of_tries)
    
    print("\nYou got " + str(javascript_questions.total_correct()) + "/" + str(len(questions)) + " for this quiz.")

if int(quiz_choice) == 5:
    questions = python_questions.send_questions() + javascript_questions.send_questions() + C_questions.send_questions() + java_questions.send_questions()
    random.shuffle(questions)
    

    for question in questions:
        question(num_of_tries)

    correct_count = javascript_questions.total_correct() + C_questions.total_correct() + java_questions.total_correct() + python_questions.total_correct()
    print("\nYou got " + str(correct_count) + "/" + str(len(questions)) + " for this quiz.")

# print(correct_answers)
# questions = [q1,q2,q3,q4,q5,q6]
# random.shuffle(questions)
# count = 0;
# for func in questions:
#         count += 1
#         if (count == 1):
#             print("Question 1")
#         else:
#             print("Question " + str(count))
#         func()
#         print("\n")