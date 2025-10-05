"""
Problem Statement
Write A Program To Get Name And Age From The User And Display Name And Age On The Screen In This
Format:

Expected Result if name is “Faisal Zamir” and age is 25 then:
Hi Faisal Zamir! Your age is 2
"""

user_name = input("Enter your Fullname: ")

user_age = input("Enter Your age: ")

if user_name and user_age.isdigit():
    print(f"Hi {user_name}! your age is {user_age}")



