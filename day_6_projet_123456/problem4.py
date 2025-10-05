"""

Content from 4 Problem and Solution with Algorithm.pptx:
Problem Statement 
Write A Python Program To Take Age From The User To Check Whether User Able To Participate In
Voting Or Not. If Age Is Less Than 18 Then It Don’t Allow To Participation. And Show, After How Much
Year A Person Will Be Able To Participate: 

Expected Result if user input 10 year then:
Sorry! You cannot participate in voting, you will be able to participate after 8 years

"""

user_age = input("Enter your age: ")
remaining_age = 0

if user_age.isdigit():
    age = int(user_age)

    if age >= 18:
        print("You able To Participate In Voting!")
    else:
        print("You are not able To Participate In Voting!")
        remaining_age = 18 - age
        print(f"Sorry! You cannot participate in voting, you will be able to participate after {remaining_age} years!")
