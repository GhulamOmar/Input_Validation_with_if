"""
Program: validation_with_if.py
Author: Ghulam Omar


Last date modified: 09/17/19
This program allows the user to enter first name, last name, age , and 3 scores.
and print the average of 3 scores. with validation if
"""


def average():  # Function definition.

    # user inputs
    score_1 = int(input(" Enter the first score"))
    if score_1 < 0:
        score_2 = int(input(" Enter the second score"))
        if score_2 < 0:
            score_3 = int(input("Please enter third score: "))
            if score_3 < 0:
                total_score = int(3)  # variable declaration.
                total_average = float(score_1 + score_2 + score_3) / total_score  # average calculation
                print(total_average)  # output the result
                return total_average  # return statement.






if __name__ == '__main__':
    average() # calling the function.
