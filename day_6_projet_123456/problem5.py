"""Content from 5 Problem and Solution with Algorithm.pptx:
Problem Statement
Write A Program That Performs All Arithmetic Operations On Two Variables.
"""

number_1 = input("Enter your first number: ")
number_2 = input("Enter your second number: ")

if number_1.isdigit() and number_2.isdigit():
    number_2 = int(number_2)
    number_1 = int(number_1)

    print(f"{number_1} + {number_2} = {number_1 + number_2}")
    print(f"{number_1} - {number_2} = {number_1 - number_2}")
    print(f"{number_1} / {number_2} = {number_1 / number_2}")
    print(f"{number_1} // {number_2} = {number_1 // number_2}")
    print(f"{number_1} x {number_2} = {number_1 * number_2}")