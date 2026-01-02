import random

def java_question_1():
    print("Question ID: 0002")
    print("Programming Language: Java")
    print("Tries Allowed: 3\n")

    print("How to print Hello World!")

    for i in range(3):
        answer = input()
        if answer == 'System.out.println("Hello World!");':
            print("Success!")
            break
        else:
            if i == 2:
                print("Failure!")
                print("Do you want to know the correct answer? Input yes or no.")
                truth = input()
                if truth == "Yes" or truth == "yes":
                    print("Correct Answer:")
                    print('System.out.println("Hello World!");')
            elif i == 1:
                print("You only have 1 try left.")
            else:
                print("You only have 2 tries left.")


def java_question_2():
    print("Question ID: 0005")
    print("Programming Language: Java")
    print("Tries Allowed: 3")

    print("What does the void keyword mean for a method?")
    firstQuestion = "A non-access modifier. Used for classes and methods.\n" \
                    "A void class cannot be used to create objects(to access it, it must be inherited from another class).\n" \
                    "A void method can only be used in a void class, and it does not have a body.\n" \
                    "The body is provided by the subclass(inherited from)."
    secondQuestion = "Used to declare a special type of class that only contains abstract methods."
    thirdQuestion = "An access modifier used for attributes, methods and constructors, making them only accessible within the declared class."
    fourthQuestion = "Specifies that a method should not have a return value."

    choices = [firstQuestion, secondQuestion, thirdQuestion, fourthQuestion]
    random.shuffle(choices)
    print("\n1. " + choices[0] + "\n")
    print("2. " + choices[1]  +  "\n")
    print("3. " + choices[2] +  "\n")
    print("4. " + choices[3])

    foundIndex = 0

    for i in range(len(choices)):
        currAnswer = choices[i]
        if (currAnswer == "Specifies that a method should not have a return value."):
            foundIndex = i + 1


    for i in range(3):
        answer = input()
        if int(answer) == foundIndex:
            print("Success!")
            break
        else:
            if i == 2:
                print("Failure!")
                print("Do you want to know the correct answer? Input yes or no.")
                truth = input()
                if truth == "Yes" or truth == "yes":
                    print("Correct Answer:")
                    print('Specifies that a method should not have a return value.')
            elif i == 1:
                print("You only have 1 try left.")
            else:
                print("You only have 2 tries left.")


def java_question_3():
    print("Question ID: 0006")
    print("Programming Language: Java")
    print("Tries Allowed: 3")

    print("What does the static keyword mean for a method?")
    firstQuestion = "A non-access modifier. Used for classes and methods.\n" \
                    "A static class cannot be used to create objects(to access it, it must be inherited from another class).\n" \
                    "A static method can only be used in a static class, and it does not have a body.\n" \
                    "The body is provided by the subclass(inherited from)."
    secondQuestion = "A non-access modifier used for methods and attributes.\n" \
                    "Static methods/attributes can be accessed without creating an object of a class."
    thirdQuestion = "An access modifier used for attributes, methods and constructors, making them only accessible within the declared class."
    fourthQuestion = "An access modifier used for classes, attributes, methods and constructors, making them accessible by any other class."

    choices = [firstQuestion, secondQuestion, thirdQuestion, fourthQuestion]
    random.shuffle(choices)
    print("\n1. " + choices[0] + "\n")
    print("2. " + choices[1]  +  "\n")
    print("3. " + choices[2] +  "\n")
    print("4. " + choices[3])

    foundIndex = 0

    for i in range(len(choices)):
        currAnswer = choices[i]
        if (currAnswer == "A non-access modifier used for methods and attributes.\n" \
                    "Static methods/attributes can be accessed without creating an object of a class."):
            foundIndex = i + 1


    for i in range(3):
        answer = input()
        if int(answer) == foundIndex:
            print("Success!")
            break
        else:
            if i == 2:
                print("Failure!")
                print("Do you want to know the correct answer? Input yes or no.")
                truth = input()
                if truth == "Yes" or truth == "yes":
                    print("Correct Answer:")
                    print('A non-access modifier used for methods and attributes.\n" \
                    "Static methods/attributes can be accessed without creating an object of a class.')
            elif i == 1:
                print("You only have 1 try left.")
            else:
                print("You only have 2 tries left.")

def send_questions():
    return [java_question_1, java_question_2, java_question_3]