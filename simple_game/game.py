"""
Author: Siddhi Sawant
Title: Operator — Easy Games in Python
Code Version: Python3
Type: Code example
Link: https://www.askpython.com/python/examples/easy-games-in-python
"""

print("Welcome to the game")


def wrong_answers(score):
    return score - 1


def display_score(score, goal):
    print("Your score:", score)
    if score >= goal:
        print("Congratulations! You achieved the goal.")
    else:
        print("Sorry, you did not achieve the goal.")


answer = input("Are you ready to play (yes/no): ")
score = 0
total_questions = 3
goal = 3

if answer.lower() == "yes":
    for i in range(total_questions):
        if i == 0:
            question = "Question 1: What is your favorite programming language? "
            correct_answer = "python"
        elif i == 1:
            question = "Question 2: What year was Python created? "
            correct_answer = "1991"
        elif i == 2:
            question = "When Does this semester end (ddmm)? "
            correct_answer = "1901"

        answer = input(question)
        if answer.lower() == correct_answer:
            score += 1
            print("Correct!")
        else:
            print("Wrong Answer :(")
            score = wrong_answers(score)

    display_score(score, goal)
else:
    print("Okay, maybe next time!")
