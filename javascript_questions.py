import random

def javascript_question_1():
    print("Question ID: 0004")
    print("Programming Language: Javascript")
    print("Tries Allowed: 3\n")

    print("How to print Hello World! to console")

    for i in range(3):
        answer = input()
        if answer == 'console.log("Hello World!")':
            print("Success!")
            break
        else:
            if i == 2:
                print("Failure!")
                print("Do you want to know the correct answer? Input yes or no.")
                truth = input()
                if truth == "Yes" or truth == "yes":
                    print("Correct Answer:")
                    print('console.log("Hello World!")')
            elif i == 1:
                print("You only have 1 try left.")
            else:
                print("You only have 2 tries left.")

def send_questions():
    return [javascript_question_1]